#!/usr/bin/env python3
"""Call every capability in the catalog once with a SandBase key and record whether it works.

    export SANDBASE_API_KEY=sk-...
    python scripts/smoke_test.py --estimate                      # cost of a full pass, no calls
    python scripts/smoke_test.py --type llm --type embedding     # cheap first
    python scripts/smoke_test.py --type api --max-usd 30
    python scripts/smoke_test.py --platform                      # sandbox + agent checks
    python scripts/smoke_test.py --report                        # summary of all results so far

Inputs: the catalog example (or required fields filled from the schema), with the
cheapest priced parameters applied. Results append to .cache/smoke/results.jsonl, so a
run can be resumed; passed capabilities are skipped unless --retest is given.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
import threading
import time
import uuid
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "sdk" / "python"))
from sandbase import SandBase, SandBaseError  # noqa: E402

OUT = ROOT / ".cache" / "smoke"
RESULTS = OUT / "results.jsonl"
TIMEOUTS = {"video": 1200, "image": 600, "audio": 600, "api": 300}
WORKERS = {"api": 6, "llm": 6, "embedding": 2, "image": 4, "audio": 3, "video": 3}
_lock = threading.Lock()


# --------------------------------------------------------------------------- inputs

def load_records(types: list[str] | None, names: list[str] | None) -> list[dict]:
    recs = [json.loads(p.read_text()) for p in (ROOT / "catalog" / "models").glob("**/*.json")]
    if types:
        recs = [r for r in recs if r["type"] in types]
    if names:
        recs = [r for r in recs if r["name"] in set(names)]
    return sorted(recs, key=lambda r: (r["type"], r["name"]))


def cheapest(rec: dict) -> tuple[dict, float]:
    p = rec["pricing"]
    if rec["type"] == "llm":
        return {}, 0.002
    if rec["type"] == "embedding":
        return {}, 0.0001
    if "per_call" in p:
        return {}, p["per_call"]
    rows = [r for r in p.get("price_examples", []) if r.get("usd") is not None]
    if rows:
        row = min(rows, key=lambda r: r["usd"])
        return dict(row["params"]), row["usd"]
    return {}, p.get("reference_price") or 0.0


def fill_from_schema(schema: dict) -> dict | None:
    body = {}
    props = schema.get("properties") or {}
    for key in schema.get("required") or []:
        prop = props.get(key) or {}
        for k in ("example", "default"):
            if k in prop:
                body[key] = prop[k]
                break
        else:
            if isinstance(prop.get("examples"), list) and prop["examples"]:
                body[key] = prop["examples"][0]
            elif isinstance(prop.get("enum"), list) and prop["enum"]:
                body[key] = prop["enum"][0]
            else:
                return None
    for alt in schema.get("anyOf") or []:            # e.g. anyOf: [{required: [prompt]}, {required: [draft_id]}]
        if all(k in body for k in alt.get("required", [])):
            break
    else:
        if schema.get("anyOf"):
            first = schema["anyOf"][0].get("required", [])
            for key in first:
                prop = props.get(key) or {}
                val = prop.get("example", prop.get("default", (prop.get("examples") or [None])[0]))
                if val is None:
                    return None
                body[key] = val
    return body


CURL_BODY = re.compile(r"-d\s+'(\{.*?\})'", re.S)


def readme_body(rec: dict) -> dict | None:
    """The request body of the first curl example in the model's documentation."""
    for m in CURL_BODY.finditer(rec.get("readme") or ""):
        try:
            body = json.loads(m.group(1))
        except ValueError:
            continue
        if isinstance(body, dict):
            body.pop("model", None)
            return body
    return None


PLACEHOLDER = re.compile(r"^<[^<>]+>$")


def has_placeholder(body) -> bool:
    if isinstance(body, dict):
        return any(has_placeholder(v) for v in body.values())
    if isinstance(body, list):
        return any(has_placeholder(v) for v in body)
    return isinstance(body, str) and bool(PLACEHOLDER.match(body))


def resolve_placeholders(body: dict, schema: dict) -> dict | None:
    """Replace "<field>" placeholders from documentation with schema examples/defaults."""
    props = schema.get("properties") or {}
    out = {}
    for k, v in body.items():
        if isinstance(v, str) and PLACEHOLDER.match(v):
            prop = props.get(k) or {}
            for key in ("example", "default"):
                if key in prop:
                    out[k] = prop[key]
                    break
            else:
                if prop.get("examples"):
                    out[k] = prop["examples"][0]
                elif prop.get("enum"):
                    out[k] = prop["enum"][0]
                elif prop.get("type") in ("integer", "number"):
                    out[k] = prop.get("minimum", 1) or 1
                elif k not in (schema.get("required") or []):
                    continue
                else:
                    return None
        else:
            out[k] = v
    return out


def build_input(rec: dict) -> dict | None:
    schema = rec.get("input_schema") or {"type": "object"}
    example = next((e["input"] for e in rec.get("examples") or [] if e.get("input") and not has_placeholder(e["input"])), None)
    filled = fill_from_schema(schema)
    documented = readme_body(rec)
    if documented is not None and has_placeholder(documented):
        documented = resolve_placeholders(documented, schema)
    if example is not None:
        body = dict(example)
    elif documented and (not filled or not schema.get("properties")):
        body = documented
    elif filled is not None and (filled or not schema.get("required")):
        body = filled if filled or not documented else documented
    else:
        return None
    overrides, _ = cheapest(rec)
    body.update(overrides)
    return body


# --------------------------------------------------------------------------- calls

def classify(err: Exception) -> str:
    status = getattr(err, "status", None)
    text = str(err).lower()
    if status == 400:
        return "invalid_input"
    if status == 402:
        return "insufficient_balance"
    if status == 429:
        return "rate_limited"
    if status in (401, 403):
        return "auth"
    if status == 404:
        return "not_found"
    if "timeout" in text or "still" in text:
        return "timeout"
    if "failed" in text:
        return "run_failed"
    return f"http_{status}" if status else "error"


def call_one(sb: SandBase, rec: dict) -> dict:
    t0 = time.time()
    res = {"name": rec["name"], "type": rec["type"], "at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    try:
        if rec["type"] == "llm":
            out = sb.chat(rec["name"], [{"role": "user", "content": "Reply with the single word: ok"}], max_tokens=64)
            text = ((out.get("choices") or [{}])[0].get("message") or {}).get("content") or ""
            res.update(ok=bool(out.get("choices")), sample=str(text)[:80], run_id=out.get("id"))
        elif rec["type"] == "embedding":
            out = sb.request("POST", "/v1/embeddings", {"model": rec["name"], "input": "hello"})
            res.update(ok=bool(out.get("data")), run_id=out.get("id"))
        else:
            body = build_input(rec)
            if body is None:
                res.update(ok=False, category="needs_input", error="no example and required fields have no example/default")
                return res
            res["input"] = body
            run = sb.run(rec["name"], body, timeout=TIMEOUTS.get(rec["type"], 600), raise_on_failure=False)
            res["run_id"] = run.get("id")
            if run.get("status") in ("completed", "succeeded"):
                outputs = run.get("outputs") or []
                res.update(ok=bool(outputs) or run.get("output") is not None,
                           sample=json.dumps(outputs[:1] or run.get("output"), ensure_ascii=False)[:200])
                if not res["ok"]:
                    res["category"] = "empty_output"
            else:
                res.update(ok=False, category="run_failed", error=json.dumps(run.get("error"), ensure_ascii=False)[:500])
    except SandBaseError as exc:
        res.update(ok=False, category=classify(exc), error=str(exc)[:500])
    except Exception as exc:  # noqa: BLE001
        res.update(ok=False, category="client_error", error=repr(exc)[:500])
    res["seconds"] = round(time.time() - t0, 1)
    if res.get("run_id") and rec["type"] not in ("llm", "embedding"):
        try:
            res["cost"] = float(sb.cost(res["run_id"]).get("cost") or 0)
        except Exception:  # noqa: BLE001
            pass
    return res


def save(res: dict) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    with _lock, RESULTS.open("a") as fh:
        fh.write(json.dumps(res, ensure_ascii=False) + "\n")


def latest_results() -> dict[str, dict]:
    out: dict[str, dict] = {}
    if RESULTS.exists():
        for line in RESULTS.read_text().splitlines():
            r = json.loads(line)
            out[r["name"]] = r
    return out


# --------------------------------------------------------------------------- platform

def platform_checks(sb: SandBase) -> list[dict]:
    results = []

    def record(name, fn):
        t0 = time.time()
        try:
            detail = fn()
            results.append({"name": name, "type": "platform", "ok": True, "detail": detail, "seconds": round(time.time() - t0, 1)})
        except Exception as exc:  # noqa: BLE001
            results.append({"name": name, "type": "platform", "ok": False, "category": "error", "error": str(exc)[:500]})

    # Sandbox: every public template boots, runs a command and round-trips a file
    os.environ.setdefault("E2B_API_KEY", sb.api_key)
    os.environ.setdefault("E2B_API_URL", "https://sandbox.sandbase.ai")
    os.environ.setdefault("E2B_DOMAIN", "sandbox.sandbase.ai")
    try:
        from e2b import Sandbox
    except ImportError:
        results.append({"name": "sandbox", "type": "platform", "ok": False, "category": "skipped", "error": "pip install e2b"})
        Sandbox = None
    templates = json.loads((ROOT / "catalog" / "sandbox.json").read_text())["public_templates"]
    for tpl in templates if Sandbox else []:
        def sandbox_check(tid=tpl["id"]):
            sbx = Sandbox.create(tid, timeout=120)
            try:
                r = sbx.commands.run("python3 -c 'print(6*7)'")
                sbx.files.write("/tmp/smoke.txt", "ok")
                assert r.stdout.strip() == "42" and sbx.files.read("/tmp/smoke.txt") == "ok", (r.stdout, r.stderr)
                return sbx.sandbox_id
            finally:
                sbx.kill()
        record(f"sandbox/{(tpl['names'] or [tpl['id']])[0]}", sandbox_check)

    # Agents: create -> session -> follow-up -> service -> archive
    state = {}

    def agent_check():
        a = sb.create_agent("deepseek/deepseek-v4-flash", "Answer with just the number.", name="smoke-test")
        state["agent"] = a["id"]
        r = sb.run_agent(a["id"], "What is 2+3?")
        assert "5" in r["output"], r["output"]
        r2 = sb.send(r["session_id"], "Times 2?")
        assert "10" in r2["output"], r2["output"]
        return r["session_id"]

    def service_check():
        svc = sb.request("POST", "/v1/services", {"agent_id": state["agent"], "name": "smoke-test", "input": "What is 4+4?"},
                         {"Idempotency-Key": f"smoke-{uuid.uuid4()}"})
        state["service"] = svc
        run = sb.invoke_service(svc["id"])
        assert run["status"] == "succeeded" and "8" in (run.get("output") or ""), run
        return run["id"]

    record("agent/session", agent_check)
    if state.get("agent"):
        record("agent/service", service_check)
        if state.get("service"):
            sb.request("POST", f"/v1/services/{state['service']['id']}/archive", {"row_version": state["service"].get("row_version", 1)},
                       {"Idempotency-Key": f"smoke-{uuid.uuid4()}"})
        sb.request("DELETE", f"/v1/agents/{state['agent']}")
    return results


# --------------------------------------------------------------------------- report

def report() -> str:
    res = latest_results()
    by_type: dict[str, Counter] = defaultdict(Counter)
    fails: dict[str, list] = defaultdict(list)
    spent = 0.0
    for r in res.values():
        by_type[r["type"]]["ok" if r.get("ok") else "fail"] += 1
        spent += r.get("cost") or 0
        if not r.get("ok"):
            fails[r.get("category", "error")].append(r)
    lines = ["# Smoke test report", "", f"Updated {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}. Billed so far: ${spent:.2f}", "",
             "| type | ok | failed |", "|---|---|---|"]
    for t, c in sorted(by_type.items()):
        lines.append(f"| {t} | {c['ok']} | {c['fail']} |")
    for cat, items in sorted(fails.items(), key=lambda kv: -len(kv[1])):
        lines += ["", f"## {cat} ({len(items)})", ""]
        lines += [f"- `{r['name']}` ({r['type']}): {(r.get('error') or '')[:220]}" for r in sorted(items, key=lambda r: r["name"])]
    text = "\n".join(lines) + "\n"
    (OUT / "report.md").write_text(text)
    return text


# --------------------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--type", action="append", help="llm, embedding, api, image, video, audio (repeatable)")
    ap.add_argument("--name", action="append")
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--max-usd", type=float, default=0, help="stop scheduling once the estimated spend exceeds this")
    ap.add_argument("--retest", action="store_true", help="also re-run capabilities that already passed")
    ap.add_argument("--failed-only", action="store_true", help="only re-run capabilities whose last result failed")
    ap.add_argument("--estimate", action="store_true")
    ap.add_argument("--platform", action="store_true")
    ap.add_argument("--report", action="store_true")
    a = ap.parse_args()

    OUT.mkdir(parents=True, exist_ok=True)
    if a.report:
        print(report())
        return 0
    recs = load_records(a.type, a.name)
    if a.estimate:
        est = Counter()
        for r in recs:
            est[r["type"]] += cheapest(r)[1]
        for t, v in est.items():
            print(f"{t:10} {sum(1 for r in recs if r['type'] == t):5}  ~${v:.2f}")
        print(f"total ~${sum(est.values()):.2f}")
        return 0

    sb = SandBase()
    if a.platform:
        for r in platform_checks(sb):
            save(r)
            print(("ok  " if r["ok"] else "FAIL") + f" {r['name']}  {r.get('detail') or r.get('error', '')}")
        print(report().split("\n## ")[0])
        return 0

    prev = latest_results()
    if a.failed_only:
        recs = [r for r in recs if r["name"] in prev and not prev[r["name"]].get("ok")]
    elif not a.retest:
        recs = [r for r in recs if not prev.get(r["name"], {}).get("ok")]
    if a.limit:
        recs = recs[: a.limit]

    budget = a.max_usd or float("inf")
    planned, scheduled = 0.0, []
    for r in recs:
        c = cheapest(r)[1]
        if planned + c > budget:
            print(f"budget reached: scheduling stops before {r['name']} (~${planned:.2f} planned)")
            break
        planned += c
        scheduled.append(r)
    print(f"running {len(scheduled)} capabilities, estimated ~${planned:.2f}")

    by_type = defaultdict(list)
    for r in scheduled:
        by_type[r["type"]].append(r)
    done = Counter()
    for t, items in by_type.items():
        with ThreadPoolExecutor(max_workers=WORKERS.get(t, 3)) as pool:
            futs = {pool.submit(call_one, sb, r): r for r in items}
            for i, fut in enumerate(as_completed(futs), 1):
                res = fut.result()
                save(res)
                done["ok" if res.get("ok") else "fail"] += 1
                if not res.get("ok"):
                    print(f"FAIL {res['name']} [{res.get('category')}] {(res.get('error') or '')[:160]}")
                if i % 50 == 0:
                    print(f"  {t}: {i}/{len(items)}  ok={done['ok']} fail={done['fail']}")
    print(report().split("\n## ")[0])
    return 0


if __name__ == "__main__":
    sys.exit(main())

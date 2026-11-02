#!/usr/bin/env python3
"""Build the public SandBase API catalog from .cache/raw (see fetch_catalog.py).

Outputs (all whitelisted, no channel / cost / internal fields):
  catalog/index.json                 compact list of every capability
  catalog/models/<name>.json         full record: description, schemas, modes, pricing, examples
  docs/models/<name>.md              human-readable page per capability
  docs/INDEX.md                      browsable index grouped by type
  openapi/sandbase.openapi.json      OpenAPI 3.1 for /v1/run, /v1/run/{id}, /v1/api/<name>
  .cache/review.md                   internal publishing review (never published)
"""
from __future__ import annotations

import argparse
import copy
import itertools
import json
import os
import re
import shutil
import subprocess
import sys
from collections import Counter, defaultdict
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / ".cache" / "raw"
CONFIG = json.loads((ROOT / "config" / "publish.json").read_text())
BASE_URL = "https://api.sandbase.ai"
PAGE_URL = "https://www.sandbase.ai/model/{name}"
MEDIA_TYPES = {"image", "video", "audio"}
CATALOG_VERSION = "1"
# Everything generated is written to OUT first and swapped into the repository at the
# end (publish_outputs), so a half-finished build never shows up in the working tree.
OUT = ROOT / ".cache" / "build"
GENERATED = ["catalog", "docs/models", "docs/platforms", "docs/INDEX.md", "docs/SKILLS.md", "openapi", "exports", "llms.txt"]


def publish_outputs() -> None:
    for rel in GENERATED:
        src, dst = OUT / rel, ROOT / rel
        if not src.exists():
            continue
        dst.parent.mkdir(parents=True, exist_ok=True)
        old = ROOT / ".cache" / "build-old" / rel
        shutil.rmtree(old, ignore_errors=True) if old.is_dir() else old.unlink(missing_ok=True)
        old.parent.mkdir(parents=True, exist_ok=True)
        if dst.exists():
            dst.rename(old)
        src.rename(dst)
    shutil.rmtree(ROOT / ".cache" / "build-old", ignore_errors=True)
    shutil.rmtree(OUT, ignore_errors=True)


# --------------------------------------------------------------------------- helpers

def marker_regex(markers: list[str]) -> re.Pattern:
    parts = []
    for m in markers:
        esc = re.escape(m)
        parts.append(rf"\b{esc}\b" if re.fullmatch(r"[a-z0-9 ]+", m) else esc)
    return re.compile("|".join(parts), re.I)


def load_markers() -> list[str]:
    """Private upstream markers come from the environment, never from the repository."""
    raw = os.environ.get("SANDBASE_UPSTREAM_MARKERS")
    path = os.environ.get("SANDBASE_UPSTREAM_MARKERS_FILE") or str(ROOT / ".cache" / "private" / "upstream_markers.json")
    if raw:
        return json.loads(raw)
    if os.path.exists(path):
        return json.loads(Path(path).read_text())
    return []


MARKER_LIST = load_markers()
MARKERS = marker_regex(MARKER_LIST) if MARKER_LIST else re.compile(r"(?!x)x")


def num(v):
    if v in (None, ""):
        return None
    try:
        f = float(v)
    except (TypeError, ValueError):
        return None
    return int(f) if f.is_integer() and abs(f) < 1e15 and "." not in str(v) else f


def resolve_refs(node, components: dict, stack: tuple = ()):
    """Inline local #/components/schemas/* refs (non-recursive schemas only)."""
    if isinstance(node, dict):
        ref = node.get("$ref")
        if isinstance(ref, str) and ref.startswith("#/components/schemas/"):
            key = ref.rsplit("/", 1)[-1]
            if key in stack or key not in components:
                return {"type": "object", "description": f"(recursive or missing schema {key})"}
            merged = resolve_refs(copy.deepcopy(components[key]), components, stack + (key,))
            extra = {k: v for k, v in node.items() if k != "$ref"}
            if extra:
                merged = {**merged, **resolve_refs(extra, components, stack)}
            return merged
        return {k: resolve_refs(v, components, stack) for k, v in node.items()}
    if isinstance(node, list):
        return [resolve_refs(v, components, stack) for v in node]
    return node


def clean_schema(node):
    """Drop vendor-extension keys and examples that point at upstream hosts."""
    if isinstance(node, dict):
        out = {}
        for k, v in node.items():
            if k.startswith("x-"):
                continue
            if k in ("example", "examples") and MARKERS.search(json.dumps(v, ensure_ascii=False)):
                continue
            out[k] = clean_schema(v)
        # a default that violates its own schema breaks strict OpenAPI validators
        if "default" in out:
            d = out["default"]
            if (isinstance(d, str) and len(d) < (out.get("minLength") or 0)) or \
               (isinstance(out.get("enum"), list) and d not in out["enum"] and d is not None):
                del out["default"]
        return out
    if isinstance(node, list):
        return [clean_schema(v) for v in node]
    return node


def urls_in(node, acc: set):
    if isinstance(node, dict):
        for v in node.values():
            urls_in(v, acc)
    elif isinstance(node, list):
        for v in node:
            urls_in(v, acc)
    elif isinstance(node, str) and node.startswith(("http://", "https://")):
        acc.add(urlparse(node).netloc)
    return acc


PROVENANCE_KEYS = {"source", "source_url"}


def strip_provenance(node):
    """Example outputs carry internal provenance notes (source / source_url); drop them."""
    if isinstance(node, dict):
        return {k: strip_provenance(v) for k, v in node.items() if k not in PROVENANCE_KEYS}
    if isinstance(node, list):
        return [strip_provenance(v) for v in node]
    return node


def modes_of(raw: dict) -> list[str]:
    modes = raw.get("supported_modes")
    if isinstance(modes, list) and modes:
        return [m for m in modes if m in ("sync", "async", "stream")]
    return [raw.get("execution_mode") or "sync"]


def safe_component(name: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_")


def short(text: str, n: int = 280) -> str:
    text = re.sub(r"\s+", " ", (text or "")).strip()
    return text if len(text) <= n else text[: n - 1].rsplit(" ", 1)[0] + "…"


# --------------------------------------------------------------------------- pricing

LLM_SIMPLE = re.compile(
    r"\s*usage\.prompt_tokens\s*\*\s*[\d.]+\s*/\s*1000000\s*\+\s*usage\.completion_tokens\s*\*\s*[\d.]+\s*/\s*1000000\s*"
)


# Measured-usage variables whose meaning is public. A formula that uses anything else is
# billed from metered usage we do not publish, so only its reference price is shown.
PUBLIC_USAGE_VARS = {
    "prompt_tokens", "completion_tokens", "cached_tokens", "cache_creation_tokens", "reasoning_tokens",
    "input_image_tokens", "output_image_tokens", "input_text_tokens", "output_text_tokens",
    "cache_creation_1h_tokens", "reference_tokens", "duration", "input_video_seconds", "total_seconds",
    "width", "height", "num_frames", "fps", "seconds", "characters", "pages", "results",
}


def formula_vars(formula: str) -> list[str]:
    return sorted(set(f"{a}.{b}" for a, b in re.findall(r"\b(params|usage)\.([A-Za-z_]\w*)", formula)))


def build_price_cases(formula: str, schema: dict, base_params: dict) -> list[dict]:
    """Parameter combinations worth pricing: enums/booleans expanded, numbers at default/min/max."""
    props = (schema or {}).get("properties") or {}
    variables = [v.split(".", 1)[1] for v in formula_vars(formula) if v.startswith("params.")]
    usage_vars = [v.split(".", 1)[1] for v in formula_vars(formula) if v.startswith("usage.")]
    if any(u != "duration" for u in usage_vars) or "media_duration" in formula:
        return []
    axes: dict[str, list] = {}
    for var in variables:
        p = props.get(var) or {}
        if isinstance(p.get("enum"), list) and p["enum"]:
            axes[var] = p["enum"][:6]
        elif p.get("type") == "boolean":
            axes[var] = [False, True]
        elif p.get("type") in ("integer", "number"):
            vals = [p.get("default"), p.get("minimum"), p.get("maximum")]
            vals = [v for v in vals if isinstance(v, (int, float))]
            if vals:
                axes[var] = sorted(set(vals))[:3]
    names = list(axes)
    combos: list[dict] = []
    total = 1
    for n in names:
        total *= len(axes[n])
    if names and total <= 48:
        for values in itertools.product(*(axes[n] for n in names)):
            combos.append(dict(zip(names, values)))
    else:
        combos.append({})
        for n in names:
            for v in axes[n]:
                combos.append({n: v})
    cases = []
    for c in combos:
        params = {**base_params, **c}
        usage = {}
        if "duration" in usage_vars:
            d = params.get("duration")
            try:
                usage["duration"] = float(str(d).rstrip("s")) if d is not None else None
            except ValueError:
                usage["duration"] = None
            if usage["duration"] is None:
                continue
        cases.append({"params": params, "usage": usage, "varied": c, "estimate": bool(usage)})
    return cases


def eval_prices(jobs: list[dict]) -> dict[str, list]:
    if not jobs:
        return {}
    proc = subprocess.run(
        ["node", str(ROOT / "scripts" / "eval_prices.mjs")],
        input=json.dumps(jobs), capture_output=True, text=True, check=True,
    )
    return {r["name"]: r["results"] for r in json.loads(proc.stdout)}


def pricing_of(raw: dict) -> tuple[dict, list[str]]:
    card = raw.get("model_card") or {}
    flags: list[str] = []
    formula = (card.get("price_formula") or "").strip()
    base = num(card.get("base_price"))
    p: dict = {"currency": "USD"}
    if raw["type"] in ("llm", "embedding") or card.get("prompt_token_price") not in (None, ""):
        tokens = {
            "input": num(card.get("prompt_token_price")),
            "output": num(card.get("completion_token_price")),
            "reasoning": num(card.get("reasoning_price")),
            "cache_read_multiplier": num(card.get("cache_read_multiplier")),
            "cache_write_multiplier": num(card.get("cache_write_multiplier")),
            "cache_write_1h_multiplier": num(card.get("cache_write_1h_multiplier")),
        }
        tokens = {k: v for k, v in tokens.items() if v is not None}
        if tokens:
            p["model"] = "per_token"
            p["per_million_tokens"] = tokens
    private_usage = set(re.findall(r"\busage\.([A-Za-z_]\w*)", formula)) - PUBLIC_USAGE_VARS
    if private_usage:
        if p.get("model") != "per_token":
            p["model"] = "usage_based"
            p["note"] = "Billed per call from metered usage; the reference price is typical."
        if base is not None:
            p["reference_price"] = base
        flags.append("info: pricing usage_based (formula not published)")
        formula = ""
    elif formula and not LLM_SIMPLE.fullmatch(formula):
        p.setdefault("model", "formula")
        p["formula"] = formula
        p["formula_variables"] = formula_vars(formula)
        if base is not None:
            p["reference_price"] = base
    elif "model" not in p:
        if base == 0:
            p["model"] = "free"
            p["per_call"] = 0
        elif base is not None:
            p["model"] = "per_call"
            p["per_call"] = base
        else:
            p["model"] = "unknown"
            flags.append("info: no price published")
    if card.get("free_quota_eligible"):
        p["free_quota"] = {"eligible": True, "daily_calls_per_org": card.get("free_quota_daily_limit"),
                           "note": "Shared across all free-quota APIs, resets 00:00 UTC."}
    return p, flags


# --------------------------------------------------------------------------- build

def build_record(raw: dict, review: dict) -> dict:
    name = raw["name"]
    flags: list[str] = []
    card = raw.get("model_card") or {}
    schema = raw.get("unified_schema") or {}
    components = ((schema.get("components") or {}).get("schemas")) or {}
    req = components.get("GenerationRequest")
    resp = components.get("GenerationResponse")
    input_schema = clean_schema(resolve_refs(req, components)) if req else None
    resp_schema = clean_schema(resolve_refs(resp, components)) if resp else None
    if input_schema is not None and not (input_schema.get("properties") or input_schema.get("anyOf") or input_schema.get("oneOf")):
        input_schema = {"type": "object", "properties": {}, **{k: v for k, v in input_schema.items() if k != "properties"}}

    description = CONFIG["description_overrides"].get(name, raw.get("description") or "")
    readme = CONFIG["readme_overrides"].get(name, card.get("readme") or "")
    cover = card.get("cover_url") or None
    if cover and MARKERS.search(urlparse(cover).netloc):
        cover = None

    modes = modes_of(raw)
    t = raw["type"]
    if t == "llm":
        endpoints = {"chat_completions": "POST /v1/chat/completions", "responses": "POST /v1/responses",
                     "messages": "POST /v1/messages"}
    elif t == "embedding":
        endpoints = {"embeddings": "POST /v1/embeddings"}
    else:
        endpoints = {"run": "POST /v1/run"}
        if "async" in modes:
            endpoints["get_run"] = "GET /v1/run/{id}"
        if t == "api":
            endpoints["passthrough"] = f"POST /v1/api/{name}"

    examples = []
    public_hosts = set(CONFIG["public_media_hosts"])
    dropped_outputs = 0
    for ex in raw.get("examples") or []:
        item = {"input": ex.get("input_snapshot") or {}}
        if MARKERS.search(json.dumps(item["input"], ensure_ascii=False)):
            flags.append("info: example input mentions an upstream marker (dropped)")
            continue
        out = strip_provenance(ex.get("output_snapshot"))
        if t in MEDIA_TYPES and out and urls_in(out, set()) <= public_hosts and not MARKERS.search(json.dumps(out)):
            item["output"] = out
        elif out:
            dropped_outputs += 1
        if ex.get("is_default"):
            item["default"] = True
        examples.append(item)
    examples.sort(key=lambda e: not e.get("default"))

    pricing, pflags = pricing_of(raw)
    flags += pflags

    rec = {
        "name": name,
        "display_name": raw.get("display_name") or name,
        "type": t,
        "vendor": raw.get("vendor"),
        "vendor_slug": raw.get("vendor_slug"),
        "description": description,
        "tags": raw.get("capability_tags") or [],
        "capabilities": raw.get("skills") or [],
        "modes": modes,
        "default_mode": raw.get("execution_mode") or modes[0],
        "endpoints": endpoints,
        "input_schema": input_schema,
        ("response_schema" if resp_schema and {"id", "status"} <= set((resp_schema.get("properties") or {}).keys())
         else "output_schema"): resp_schema,
        "pricing": pricing,
        "examples": examples[:3],
        "readme": readme or None,
        "cover_url": cover,
        "page_url": PAGE_URL.format(name=name),
        "published_at": raw.get("published_at"),
        "created_at": raw.get("created_at"),
    }
    if "coming-soon" in (raw.get("capability_tags") or []):
        rec["status"] = "coming_soon"           # listed, but not callable yet
    rec = {k: v for k, v in rec.items() if v not in (None, [], {})}

    # final leak scan on everything we are about to publish
    published = json.dumps(rec, ensure_ascii=False)
    for m in sorted(set(x.lower() for x in MARKERS.findall(published))):
        where = [f for f in ("description", "readme", "input_schema", "output_schema", "response_schema", "examples")
                 if f in rec and MARKERS.search(json.dumps(rec[f], ensure_ascii=False)) and m in json.dumps(rec[f], ensure_ascii=False).lower()]
        flags.append(f"mentions '{m}' in {', '.join(where) or 'record'}")
    if dropped_outputs:
        review["dropped_outputs"] += dropped_outputs
    if flags:
        review["flags"][name] = flags
    return rec


def attach_price_examples(records: dict[str, dict]):
    jobs, meta = [], {}
    for name, rec in records.items():
        f = rec["pricing"].get("formula")
        if not f:
            continue
        base = {}
        props = (rec.get("input_schema") or {}).get("properties") or {}
        for k, p in props.items():
            if isinstance(p, dict) and "default" in p:
                base[k] = p["default"]
        if rec.get("examples"):
            base.update(rec["examples"][0]["input"])
        cases = build_price_cases(f, rec.get("input_schema") or {}, base)
        if not cases:
            continue
        jobs.append({"name": name, "formula": f, "cases": [{"params": c["params"], "usage": c["usage"]} for c in cases]})
        meta[name] = cases
    results = eval_prices(jobs)
    for name, vals in results.items():
        seen, rows = set(), []
        for case, usd in zip(meta[name], vals):
            if usd is None:
                continue
            key = json.dumps(case["varied"], sort_keys=True)
            if key in seen:
                continue
            seen.add(key)
            row = {"params": case["varied"], "usd": usd}
            if case["estimate"]:
                row["estimate"] = "assumes output duration equals requested duration"
            rows.append(row)
        if rows:
            records[name]["pricing"]["price_examples"] = rows[:48]


def price_summary(p: dict) -> dict:
    s = {"model": p.get("model")}
    if "per_call" in p:
        s["usd_per_call"] = p["per_call"]
    if "per_million_tokens" in p:
        t = p["per_million_tokens"]
        s["usd_per_million_tokens"] = {k: t[k] for k in ("input", "output") if k in t}
    ex = [r["usd"] for r in p.get("price_examples", []) if r.get("usd") is not None]
    if ex:
        s["usd_from"], s["usd_to"] = min(ex), max(ex)
    elif "reference_price" in p:
        s["usd_reference"] = p["reference_price"]
    if p.get("free_quota"):
        s["free_quota"] = True
    return s


# --------------------------------------------------------------------------- markdown

def md_escape(text) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def param_rows(schema: dict) -> list[str]:
    props = (schema or {}).get("properties") or {}
    required = set((schema or {}).get("required") or [])
    rows = []
    for k, p in props.items():
        if not isinstance(p, dict):
            continue
        typ = p.get("type") or ("enum" if "enum" in p else "")
        if isinstance(typ, list):
            typ = " \\| ".join(map(str, typ))
        extra = []
        if "enum" in p:
            extra.append("one of: " + ", ".join(f"`{e}`" for e in p["enum"][:12]) + (" …" if len(p["enum"]) > 12 else ""))
        if "default" in p:
            extra.append(f"default `{json.dumps(p['default'], ensure_ascii=False)}`")
        if "minimum" in p or "maximum" in p:
            extra.append(f"range {p.get('minimum', '')}–{p.get('maximum', '')}")
        desc = short(p.get("description") or p.get("title") or "", 220)
        rows.append(f"| `{k}` | {md_escape(typ)} | {'yes' if k in required else ''} | {md_escape(desc)} {md_escape('; '.join(extra))} |")
    return rows


def sample_body(rec: dict) -> dict:
    if rec.get("examples"):
        body = dict(rec["examples"][0]["input"])
    else:
        body = {}
        schema = rec.get("input_schema") or {}
        for k in schema.get("required") or []:
            p = (schema.get("properties") or {}).get(k) or {}
            if "example" in p:
                body[k] = p["example"]
            elif "default" in p:
                body[k] = p["default"]
            elif "enum" in p:
                body[k] = p["enum"][0]
            else:
                body[k] = "<" + k + ">"
    return body


def go_literal(v, indent: int = 1) -> str:
    pad = "\t" * indent
    if isinstance(v, dict):
        if not v:
            return "map[string]any{}"
        items = ",\n".join(f"{pad}\t{json.dumps(k)}: {go_literal(x, indent + 1)}" for k, x in v.items())
        return "map[string]any{\n" + items + ",\n" + pad + "}"
    if isinstance(v, list):
        return "[]any{" + ", ".join(go_literal(x, indent) for x in v) + "}"
    if v is None:
        return "nil"
    if isinstance(v, bool):
        return "true" if v else "false"
    return json.dumps(v, ensure_ascii=False)


def snippets_run(name: str, body: dict) -> list[str]:
    params = {k: v for k, v in body.items() if k != "model"}
    payload = json.dumps(body, ensure_ascii=False).replace("'", "'\\''")
    py_params = repr(params)
    ts_params = json.dumps(params, ensure_ascii=False, indent=2)
    go_params = go_literal(params, 0).replace("map[string]any{", "sandbase.Params{", 1)
    return [
        "**curl**", "", "```bash",
        "curl https://api.sandbase.ai/v1/run \\",
        "  -H \"Authorization: Bearer $SANDBASE_API_KEY\" -H 'Content-Type: application/json' \\",
        f"  -d '{payload}'", "```", "",
        "**Python** ([sdk/python](../../sdk/python))", "", "```python",
        "from sandbase import SandBase", "",
        f"result = SandBase().run({name!r}, {py_params})", "print(result[\"outputs\"])", "```", "",
        "**TypeScript** ([sdk/typescript](../../sdk/typescript))", "", "```ts",
        "import { SandBase } from \"@sandbaseai/sdk\";", "",
        f"const result = await new SandBase().run({json.dumps(name)}, {ts_params});", "console.log(result.outputs);", "```", "",
        "**Go** ([sdk/go](../../sdk/go))", "", "```go",
        "c, _ := sandbase.NewClient(\"\")",
        f"run, err := c.Run(ctx, {json.dumps(name)}, {go_params})", "```", "",
    ]


def snippets_llm(name: str) -> list[str]:
    msg = [{"role": "user", "content": "Hello"}]
    return [
        "OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. "
        "Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.", "",
        "**curl**", "", "```bash", "curl https://api.sandbase.ai/v1/chat/completions \\",
        "  -H \"Authorization: Bearer $SANDBASE_API_KEY\" -H 'Content-Type: application/json' \\",
        f"  -d '{json.dumps({'model': name, 'messages': msg})}'", "```", "",
        "**Python**", "", "```python", "from openai import OpenAI", "",
        "client = OpenAI(base_url=\"https://api.sandbase.ai/v1\", api_key=os.environ[\"SANDBASE_API_KEY\"])",
        f"resp = client.chat.completions.create(model={name!r}, messages=[{{\"role\": \"user\", \"content\": \"Hello\"}}])",
        "```", "",
        "**TypeScript**", "", "```ts", "import OpenAI from \"openai\";", "",
        "const client = new OpenAI({ baseURL: \"https://api.sandbase.ai/v1\", apiKey: process.env.SANDBASE_API_KEY });",
        f"const resp = await client.chat.completions.create({{ model: {json.dumps(name)}, messages: [{{ role: \"user\", content: \"Hello\" }}] }});",
        "```", "",
        "**Go** ([sdk/go](../../sdk/go))", "", "```go",
        f"resp, err := c.Chat(ctx, {json.dumps(name)}, []map[string]any{{{{\"role\": \"user\", \"content\": \"Hello\"}}}}, nil)",
        "```", "",
    ]


TYPE_NOUN = {"llm": "LLM", "image": "image generation model", "video": "video generation model",
             "audio": "audio model", "embedding": "embedding model", "api": "data API"}


def price_line(p: dict) -> str:
    m = p.get("model")
    if m == "per_call":
        return f"${p['per_call']} per call" + (" (free daily quota)" if p.get("free_quota") else "")
    if m == "free":
        return "free"
    if m == "per_token":
        t = p.get("per_million_tokens", {})
        return f"${t.get('input')} input / ${t.get('output')} output per 1M tokens"
    rows = [r["usd"] for r in p.get("price_examples", []) if r.get("usd") is not None]
    if rows:
        lo, hi = min(rows), max(rows)
        return f"from ${lo}" + (f" to ${hi}" if hi != lo else "") + " per run, depending on parameters"
    if p.get("reference_price") is not None:
        return f"about ${p['reference_price']} per call"
    return ""


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (text or "").lower()).strip("-") or "other"


def write_platform_pages(records: dict[str, dict], generated_at: str) -> int:
    """One landing page per vendor/platform, e.g. docs/platforms/tiktok.md (long-tail search: "TikTok API")."""
    groups: dict[str, list[dict]] = defaultdict(list)
    for r in records.values():
        groups[r.get("vendor") or "Other"].append(r)
    base = OUT / "docs" / "platforms"
    shutil.rmtree(base, ignore_errors=True)
    base.mkdir(parents=True)
    index = ["# Platforms", "", f"{len(groups)} platforms and model makers, each reachable with one SandBase API key.", "",
             "| Platform | Capabilities | Types |", "|---|---|---|"]
    for vendor, recs in sorted(groups.items(), key=lambda kv: (-len(kv[1]), kv[0].lower())):
        recs.sort(key=lambda r: r["name"])
        types = sorted({TYPE_NOUN.get(r["type"], r["type"]) for r in recs})
        is_data = all(r["type"] == "api" for r in recs)
        heading = f"{vendor} API" if is_data else f"{vendor} models API"
        lines = [f"# {heading}: {len(recs)} endpoints with pricing and code examples", "",
                 f"Call {len(recs)} {vendor} {'endpoints' if is_data else 'models'} through SandBase with one API key: "
                 "no separate account, one balance, the same request format for every endpoint. "
                 "Each page has the input schema, the price and curl / Python / TypeScript / Go examples.", "",
                 "| Endpoint | What it does | Price |", "|---|---|---|"]
        for r in recs:
            lines.append(f"| [`{r['name']}`](../models/{r['name']}.md) | {md_escape(short(r.get('description', ''), 140))} | "
                         f"{md_escape(price_line(r['pricing']))} |")
        lines += ["", "## Quick start", "", "```bash", "curl https://api.sandbase.ai/v1/run \\",
                  "  -H \"Authorization: Bearer $SANDBASE_API_KEY\" -H 'Content-Type: application/json' \\",
                  f"  -d '{json.dumps({'model': recs[0]['name'], **sample_body(recs[0])}, ensure_ascii=False)[:600]}'", "```", "",
                  "Get a key at [sandbase.ai](https://www.sandbase.ai/console). Back to [all platforms](README.md).", ""]
        (base / f"{slug(vendor)}.md").write_text("\n".join(lines))
        index.append(f"| [{md_escape(vendor)}]({slug(vendor)}.md) | {len(recs)} | {', '.join(types)} |")
    (base / "README.md").write_text("\n".join(index) + "\n")
    return len(groups)


def render_md(rec: dict) -> str:
    n = rec["name"]
    p = rec["pricing"]
    kind = TYPE_NOUN.get(rec["type"], "API")
    title = rec["display_name"] if rec["display_name"].lower().endswith(" api") else f"{rec['display_name']} API"
    lines = [f"# {title}: pricing, parameters and code examples", "",
             f"`{n}` · {kind} · {rec.get('vendor') or ''} · callable with one SandBase API key "
             f"from curl, Python, TypeScript and Go.", ""]
    summary = price_line(rec["pricing"])
    if summary:
        lines += [f"**Price:** {summary} · **Modes:** {', '.join(rec.get('modes') or ['sync'])}", ""]
    if rec.get("description"):
        lines += [rec["description"], ""]
    lines += ["## Pricing", ""]
    m = p.get("model")
    if m == "per_call":
        lines.append(f"- **${p['per_call']} per call** (USD)")
    elif m == "free":
        lines.append("- **Free**")
    elif m == "per_token":
        t = p["per_million_tokens"]
        lines.append(f"- Input **${t.get('input')}** / output **${t.get('output')}** per 1M tokens (USD)")
        for k in ("reasoning", "cache_read_multiplier", "cache_write_multiplier", "cache_write_1h_multiplier"):
            if k in t:
                lines.append(f"- {k.replace('_', ' ')}: {t[k]}")
    elif m == "usage_based":
        lines.append(f"- Usage-based. {p.get('note', '')} Reference: **${p.get('reference_price')}**")
    elif m == "formula":
        lines.append(f"- Depends on parameters ({', '.join(f'`{v}`' for v in p.get('formula_variables', []))}).")
        if p.get("price_examples"):
            lines += ["", "| parameters | USD |", "|---|---|"]
            for r in p["price_examples"][:24]:
                ps = ", ".join(f"{k}={json.dumps(v, ensure_ascii=False)}" for k, v in r["params"].items()) or "defaults"
                lines.append(f"| {md_escape(ps)} | {r['usd']}{' *' if r.get('estimate') else ''} |")
            if any(r.get("estimate") for r in p["price_examples"]):
                lines += ["", "\\* estimate: assumes output duration equals requested duration."]
        lines += ["", f"Formula: `{p['formula']}`" if len(p["formula"]) < 400 else "Formula: see the JSON record."]
    else:
        lines.append("- Price not published.")
    if p.get("free_quota"):
        lines.append(f"- Free quota: {p['free_quota'].get('daily_calls_per_org')} calls/day per organization (shared across free-quota APIs).")
    lines += ["", "## Call it", ""]
    if rec["type"] == "llm":
        lines += snippets_llm(n)
        if rec.get("capabilities"):
            lines += ["", "Capabilities: " + ", ".join(f"`{c}`" for c in rec["capabilities"])]
    elif rec["type"] == "embedding":
        lines += ["```bash", "curl https://api.sandbase.ai/v1/embeddings \\",
                  "  -H \"Authorization: Bearer $SANDBASE_API_KEY\" -H 'Content-Type: application/json' \\",
                  f"  -d '{json.dumps({'model': n, 'input': 'hello'})}'", "```"]
    else:
        body = {"model": n, **sample_body(rec)}
        lines += [f"Modes: {', '.join(rec['modes'])} (default `{rec['default_mode']}`). Only pass `mode` values listed here. "
                  "The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.", ""]
        lines += snippets_run(n, body)
        if "async" in rec["modes"]:
            lines += ["With plain HTTP, async runs return `{\"id\", \"status\": \"pending\"}`. Poll until `completed` or `failed`:", "",
                      "```bash", "curl https://api.sandbase.ai/v1/run/$RUN_ID -H \"Authorization: Bearer $SANDBASE_API_KEY\"", "```", ""]
        if rec["type"] == "api":
            lines += [f"Same call via the path form: `POST /v1/api/{n}` with the body above minus `model`.", ""]
        rows = param_rows(rec.get("input_schema") or {})
        if rows:
            lines += ["## Parameters", "", "| name | type | required | description |", "|---|---|---|---|", *rows, ""]
    if rec.get("readme"):
        body = re.sub(r"^# .*\n+", "", rec["readme"].strip(), count=1)
        lines += ["## Details", "", re.sub(r"^(#{1,5}) ", r"#\1 ", body, flags=re.M), ""]
    lines += ["---", f"Machine-readable: [`catalog/models/{n}.json`](../../catalog/models/{n}.json) · Store page: {rec['page_url']}", ""]
    return "\n".join(lines)


# --------------------------------------------------------------------------- openapi

RUN_RESPONSE = {
    "type": "object",
    "required": ["id", "status", "model"],
    "properties": {
        "id": {"type": "string"},
        "model": {"type": "string"},
        "status": {"type": "string", "enum": ["pending", "processing", "completed", "failed", "cancelled"]},
        "output": {"description": "Primary structured result (sync responses)."},
        "outputs": {"type": "array", "items": {"type": "object"},
                    "description": "Result items: media items carry `url`; data APIs carry `data`."},
        "error": {"description": "Present when status is failed.", "oneOf": [
            {"type": "string"},
            {"type": "object", "properties": {"type": {"type": "string"}, "message": {"type": "string"}}},
        ]},
    },
}


def build_openapi(records: dict[str, dict], generated_at: str) -> dict:
    schemas: dict = {"RunResponse": RUN_RESPONSE,
                     "Error": {"type": "object", "properties": {"error": {"type": "object"}}}}
    one_of, mapping, paths = [], {}, {}
    for name, rec in sorted(records.items()):
        if rec["type"] in ("llm", "embedding"):
            continue
        comp = safe_component(name)
        inp = copy.deepcopy(rec.get("input_schema") or {"type": "object"})
        run_schema = {"allOf": [{"type": "object", "required": ["model"], "properties": {
            "model": {"type": "string", "const": name},
            "mode": {"type": "string", "enum": rec["modes"]},
            **({"webhook_url": {"type": "string", "format": "uri"}} if "async" in rec["modes"] and rec["type"] in MEDIA_TYPES else {}),
        }}, inp], "title": rec["display_name"], "description": short(rec.get("description", ""), 500)}
        schemas[f"{comp}__Run"] = run_schema
        one_of.append({"$ref": f"#/components/schemas/{comp}__Run"})
        mapping[name] = f"#/components/schemas/{comp}__Run"
        if rec["type"] == "api":
            schemas[f"{comp}__Input"] = inp
            paths[f"/v1/api/{name}"] = {"post": {
                "operationId": comp, "summary": rec["display_name"], "tags": [rec.get("vendor") or "api"],
                "description": short(rec.get("description", ""), 1000) + f"\n\nPrice: {json.dumps(price_summary(rec['pricing']))}",
                "requestBody": {"required": True, "content": {"application/json": {"schema": {"$ref": f"#/components/schemas/{comp}__Input"}}}},
                "responses": {"200": {"description": "Completed", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/RunResponse"}}}},
                              "202": {"description": "Accepted (async)", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/RunResponse"}}}}},
                "x-sandbase-pricing": rec["pricing"],
            }}
    schemas["RunRequest"] = {"oneOf": one_of, "discriminator": {"propertyName": "model", "mapping": mapping}}
    paths = {
        "/v1/run": {"post": {
            "operationId": "run", "summary": "Run any model or API capability", "tags": ["run"],
            "description": "Body fields depend on `model`; see each RunRequest variant. Sync capabilities return 200 with the result; async ones return 202 with an id to poll.",
            "requestBody": {"required": True, "content": {"application/json": {"schema": {"$ref": "#/components/schemas/RunRequest"}}}},
            "responses": {"200": {"description": "Completed", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/RunResponse"}}}},
                          "202": {"description": "Accepted", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/RunResponse"}}}},
                          "400": {"description": "Invalid input"}, "401": {"description": "Missing or invalid key"},
                          "402": {"description": "Insufficient balance"}, "429": {"description": "Rate or free-quota limit"}},
        }},
        "/v1/run/{id}": {"get": {
            "operationId": "getRun", "summary": "Get a run", "tags": ["run"],
            "parameters": [{"name": "id", "in": "path", "required": True, "schema": {"type": "string"}}],
            "responses": {"200": {"description": "Run status", "content": {"application/json": {"schema": {"$ref": "#/components/schemas/RunResponse"}}}}},
        }},
        **paths,
    }
    return {
        "openapi": "3.1.0",
        "info": {"title": "SandBase API catalog", "version": generated_at[:10],
                 "description": "Every enabled SandBase model and API capability. LLMs use the OpenAI-compatible /v1/chat/completions; see catalog/index.json."},
        "servers": [{"url": BASE_URL}],
        "security": [{"bearer": []}],
        "components": {"securitySchemes": {"bearer": {"type": "http", "scheme": "bearer"}}, "schemas": schemas},
        "paths": paths,
    }


def nice(n: int, headline: bool = False) -> str:
    """Round down for marketing copy so numbers stay true as the catalog changes: 2,130 -> 2,000+, 176 -> 150+."""
    if headline and n >= 2000:
        step = 1000
    elif n >= 1000:
        step = 100
    elif n >= 100:
        step = 50
    else:
        step = 10
    return f"{max(step, n // step * step):,}+"


def update_readme_counts(index: dict):
    cfg = json.loads((ROOT / "config" / "categories.json").read_text())
    models = index["models"]
    by_type = Counter(m["type"] for m in models)
    ai = {t: by_type.get(t, 0) for t in ("llm", "video", "image", "audio")}
    n_ai = sum(n for t, n in by_type.items() if t != "api")
    apis = [m for m in models if m["type"] == "api"]
    vendors = Counter(m["vendor"] for m in apis)
    fq = index.get("free_quota") or {}

    en = (f"<b>{nice(index['count'], True)} models &amp; APIs</b> · {nice(n_ai)} AI models · {nice(len(apis))} data APIs "
          f"from {nice(len(vendors))} platforms<br><b>{fq.get('daily_calls_per_org', 100)} free API calls / day</b>"
          " · <b>Free sandboxes</b> · <b>Free agents</b>")
    zh = (f"<b>{nice(index['count'], True)} 个模型和 API</b> · {nice(n_ai)} 个 AI 模型 · {nice(len(apis))} 个数据 API，"
          f"来自 {nice(len(vendors))} 个平台<br><b>每天 {fq.get('daily_calls_per_org', 100)} 次免费 API 调用</b>"
          " · <b>沙箱免费</b> · <b>Agent 免费</b>")

    # What's inside: AI models by type, data APIs by category with the busiest platforms as examples
    media_vendors = Counter(m["vendor"] for m in models if m["type"] in ai)
    alias = cfg.get("display", {})
    top_media = ", ".join(alias.get(v, v) for v, _ in media_vendors.most_common(8))
    owner = {v: cat for cat, vs in cfg["vendors"].items() for v in vs}
    cats: dict[str, Counter] = {c: Counter() for c in cfg["order"]}
    for v, n in vendors.items():
        cats[owner.get(v, "more")][v] += n
    rows_en = [f"| **AI models** | {nice(n_ai)} | {nice(ai['llm'])} LLMs, {nice(ai['video'])} video, {nice(ai['image'])} image, "
               f"{nice(ai['audio'])} audio: {top_media}, … |"]
    rows_zh = [f"| **AI 模型** | {nice(n_ai)} | LLM {nice(ai['llm'])}、视频 {nice(ai['video'])}、图像 {nice(ai['image'])}、"
               f"音频 {nice(ai['audio'])}：{top_media} 等 |"]
    for c in cfg["order"]:
        cnt = cats[c]
        if not cnt:
            continue
        examples = ", ".join(alias.get(v, v) for v, _ in cnt.most_common(10))
        en_label, zh_label = cfg["labels"][c]
        rows_en.append(f"| {en_label} | {nice(sum(cnt.values()))} | {examples}, … |")
        rows_zh.append(f"| {zh_label} | {nice(sum(cnt.values()))} | {examples} 等 |")
    table_en = "\n".join(["| | Count | Includes |", "|---|---|---|", *rows_en])
    table_zh = "\n".join(["| | 数量 | 包括 |", "|---|---|---|", *rows_zh])

    for fname, tag, text, table in (("README.md", "en", en, table_en), ("README.zh-CN.md", "zh", zh, table_zh)):
        path = ROOT / fname
        if not path.exists():
            continue
        body = path.read_text()
        body = re.sub(rf"<!-- counts:{tag} -->.*?<!-- /counts:{tag} -->", lambda _: f"<!-- counts:{tag} -->{text}<!-- /counts:{tag} -->", body, flags=re.S)
        body = re.sub(rf"<!-- inside:{tag} -->.*?<!-- /inside:{tag} -->", lambda _: f"<!-- inside:{tag} -->\n{table}\n<!-- /inside:{tag} -->", body, flags=re.S)
        path.write_text(body)


def write_llms_txt(index: dict) -> None:
    """llms.txt (https://llmstxt.org): a map of this repository for AI assistants and agents."""
    raw = "https://raw.githubusercontent.com/sandbaseai/sandbase/main"
    by_type = Counter(m["type"] for m in index["models"])
    vendors = Counter(m["vendor"] for m in index["models"])
    lines = [
        "# SandBase",
        "",
        "> One API key to build your personal agent: AI models, data APIs, sandboxes and agents, pay as you go. "
        f"{nice(index['count'], True)} capabilities ({nice(by_type.get('api', 0))} data APIs, "
        f"{nice(sum(n for t, n in by_type.items() if t != 'api'))} AI models), 100 free data-API calls a day, "
        "free sandboxes (E2B-compatible) and free Agents (OpenAI Agents API-compatible).",
        "",
        "Base URL: https://api.sandbase.ai. Auth: `Authorization: Bearer $SANDBASE_API_KEY`. "
        "Every non-LLM capability: `POST /v1/run` with `{\"model\": \"<name>\", ...fields}`; async runs return an id to poll "
        "with `GET /v1/run/{id}`. LLMs: OpenAI-compatible `/v1/chat/completions` and `/v1/responses`, Anthropic `/v1/messages`.",
        "",
        "## Catalog",
        f"- [catalog/index.json]({raw}/catalog/index.json): every capability with type, modes, endpoint and price summary",
        f"- catalog/models/<name>.json ({raw}/catalog/models/openai/gpt-image-2.5-flare.json): input JSON Schema, output, modes, pricing, examples",
        f"- [openapi/sandbase.openapi.json]({raw}/openapi/sandbase.openapi.json): OpenAPI 3.1",
        f"- [docs/platforms/README.md]({raw}/docs/platforms/README.md): capabilities grouped by platform",
        f"- [exports/]({raw}/exports/README.md): price files for new-api / one-api, LiteLLM, OpenRouter-format tools and CSV",
        f"- [docs/guides/relay-platforms.md]({raw}/docs/guides/relay-platforms.md): using SandBase as an upstream for gateways and relays",
        "",
        "## Clients",
        f"- [Python]({raw}/sdk/python/README.md), [TypeScript]({raw}/sdk/typescript/README.md), [Go]({raw}/sdk/go/README.md): `run()` waits for sync and async results; Agents helpers",
        f"- [Sandboxes with the E2B SDK]({raw}/examples/sandbox/python/hello_sandbox.py)",
        f"- [Agents with the OpenAI SDK]({raw}/examples/agents/python/openai_agents.py)",
        "",
        "## Top platforms",
        "- " + ", ".join(v for v, _ in vendors.most_common(40)),
        "",
        "## Optional",
        "- [SandBase CLI / MCP for coding agents](https://github.com/sandbaseai/cli)",
        "- [Documentation](https://www.sandbase.ai/docs/)",
    ]
    (OUT / "llms.txt").write_text("\n".join(lines) + "\n")



# --------------------------------------------------------------------------- exports for other platforms

def write_exports(records: dict[str, dict], generated_at: str) -> None:
    """Price and model files in the formats that gateways, relay platforms and tools import."""
    out = OUT / "exports"
    (out / "new-api").mkdir(parents=True, exist_ok=True)
    (out / "litellm").mkdir(parents=True, exist_ok=True)
    records = {n: r for n, r in records.items() if r.get("status") != "coming_soon"}
    token_models = {n: r for n, r in sorted(records.items())
                    if r["type"] in ("llm", "embedding") and r["pricing"].get("per_million_tokens", {}).get("input") is not None}

    # CSV: one row per capability
    import csv
    with (out / "pricing.csv").open("w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["name", "type", "vendor", "pricing_model", "usd_per_call", "usd_per_1m_input_tokens",
                    "usd_per_1m_output_tokens", "usd_from", "usd_to", "free_daily_quota", "modes", "endpoint"])
        for n, r in sorted(records.items()):
            p, t = r["pricing"], r["pricing"].get("per_million_tokens", {})
            rows = [x["usd"] for x in p.get("price_examples", []) if x.get("usd") is not None]
            w.writerow([n, r["type"], r.get("vendor") or "", p.get("model") or "", p.get("per_call", ""),
                        t.get("input", ""), t.get("output", ""), min(rows) if rows else p.get("reference_price", ""),
                        max(rows) if rows else p.get("reference_price", ""), "yes" if p.get("free_quota") else "",
                        " ".join(r["modes"]), next(iter(r["endpoints"].values()))])

    # OpenAI /v1/models list
    (out / "openai-models.json").write_text(json.dumps({"object": "list", "data": [
        {"id": n, "object": "model", "created": 0, "owned_by": r.get("vendor_slug") or "sandbase"}
        for n, r in sorted(records.items()) if r["type"] == "llm"]}, indent=1) + "\n")

    # OpenRouter-style model list (used by many chat clients and routers)
    def per_token(v):
        return "0" if v in (None, 0) else f"{v / 1_000_000:.12f}".rstrip("0").rstrip(".")
    (out / "openrouter-models.json").write_text(json.dumps({"data": [{
        "id": n, "name": r["display_name"], "description": short(r.get("description", ""), 500),
        "context_length": r.get("context_length"),
        "pricing": {"prompt": per_token(r["pricing"]["per_million_tokens"].get("input")),
                    "completion": per_token(r["pricing"]["per_million_tokens"].get("output")), "request": "0", "image": "0"},
    } for n, r in token_models.items() if r["type"] == "llm"]}, indent=1) + "\n")

    # LiteLLM: custom pricing map and a proxy config
    litellm_prices = {}
    config = ["# LiteLLM proxy: export SANDBASE_API_KEY=... LITELLM_MASTER_KEY=sk-...; litellm --config config.yaml",
              "general_settings:", "  master_key: os.environ/LITELLM_MASTER_KEY", "model_list:"]
    for n, r in token_models.items():
        t = r["pricing"]["per_million_tokens"]
        entry = {"litellm_provider": "openai", "mode": "chat" if r["type"] == "llm" else "embedding",
                 "input_cost_per_token": (t.get("input") or 0) / 1_000_000,
                 "output_cost_per_token": (t.get("output") or 0) / 1_000_000}
        if r.get("context_length"):
            entry["max_input_tokens"] = r["context_length"]
        litellm_prices[f"sandbase/{n}"] = entry
        config += [f"  - model_name: {n}", "    litellm_params:", f"      model: openai/{n}",
                   "      api_base: https://api.sandbase.ai/v1", "      api_key: os.environ/SANDBASE_API_KEY",
                   "    model_info:", f"      input_cost_per_token: {entry['input_cost_per_token']:.12g}",
                   f"      output_cost_per_token: {entry['output_cost_per_token']:.12g}"]
    (out / "litellm" / "model_prices.json").write_text(json.dumps(litellm_prices, indent=1) + "\n")
    (out / "litellm" / "config.yaml").write_text("\n".join(config) + "\n")

    # new-api / one-api ratio settings. Ratio 1 = $0.002 per 1K tokens = $2 per 1M tokens.
    model_ratio, completion_ratio, cache_ratio = {}, {}, {}
    for n, r in token_models.items():
        t = r["pricing"]["per_million_tokens"]
        inp, outp = t.get("input") or 0, t.get("output")
        model_ratio[n] = round(inp / 2, 6)
        if inp and outp is not None:
            completion_ratio[n] = round(outp / inp, 6)
        if t.get("cache_read_multiplier") is not None:
            cache_ratio[n] = t["cache_read_multiplier"]
    for fname, data in (("model_ratio.json", model_ratio), ("completion_ratio.json", completion_ratio),
                        ("cache_ratio.json", cache_ratio)):
        (out / "new-api" / fname).write_text(json.dumps(data, indent=1, sort_keys=True) + "\n")
    (out / "new-api" / "models.txt").write_text(",".join(n for n, r in token_models.items() if r["type"] == "llm") + "\n")
    (out / "README.md").write_text(f"""# Exports

Generated from the catalog on {generated_at}. Do not edit by hand.

| File | Use it for |
|---|---|
| `pricing.csv` | Spreadsheets and BI: one row per capability with its price |
| `openai-models.json` | The OpenAI `/v1/models` list of SandBase LLMs |
| `openrouter-models.json` | Tools that read the OpenRouter model list format (per-token USD prices as strings) |
| `litellm/config.yaml`, `litellm/model_prices.json` | A LiteLLM proxy with every SandBase LLM and its price |
| `new-api/*` | new-api / one-api channel model list and ratio settings |

See [docs/guides/relay-platforms.md](../docs/guides/relay-platforms.md) for setup steps.
""")


# --------------------------------------------------------------------------- agents / skills / sandbox

def build_platform(generated_at: str) -> dict:
    """Whitelisted public Agent catalog, Skill catalog and Sandbox templates (from fetch_catalog.py)."""
    path = RAW / "platform.json"
    if not path.exists():
        return {}
    raw = json.loads(path.read_text())
    skills = [{"id": s["id"], "name": s.get("name"), "description": s.get("description"),
               "version": s.get("latest_version") or s.get("default_version")} for s in raw.get("skills", [])]
    templates = [{"id": t.get("templateID"), "names": t.get("names") or t.get("aliases") or [], "cpu_count": t.get("cpuCount"),
                  "memory_mb": t.get("memoryMB"), "disk_mb": t.get("diskSizeMB")}
                 for t in raw.get("sandbox_templates", []) if t.get("public") and t.get("buildStatus") == "ready"]
    platform = {
        "generated_at": generated_at,
        "skills": sorted(skills, key=lambda s: (s["name"] or "").lower()),
        "sandbox": {"protocol": "E2B", "api_url": "https://sandbox.sandbase.ai", "domain": "sandbox.sandbase.ai",
                    "sdk": {"python": "e2b", "javascript": "e2b"},
                    "pricing": {"model": "free", "usd": 0, "note": "Sandboxes are free."},
                    "public_templates": templates},
    }
    for leak in MARKERS.findall(json.dumps(platform, ensure_ascii=False)):
        print(f"WARNING: platform catalog mentions upstream marker '{leak}'", file=sys.stderr)
    (OUT / "catalog" / "skills.json").write_text(json.dumps(platform["skills"], ensure_ascii=False, indent=2) + "\n")
    (OUT / "catalog" / "sandbox.json").write_text(json.dumps(platform["sandbox"], ensure_ascii=False, indent=2) + "\n")

    lines = ["# Skills", "", f"{len(skills)} public Skills · generated {generated_at}. Attach them to an Agent with "
             "`skills: [{\"skill_id\": \"skl_…\"}]`.", "", "| Skill | Description |", "|---|---|"]
    lines += [f"| **{md_escape(s['name'])}**<br>`{s['id']}` | {md_escape(short(s['description'] or '', 200))} |" for s in platform["skills"]]
    (OUT / "docs" / "SKILLS.md").write_text("\n".join(lines) + "\n")
    return {"skills": len(skills), "sandbox_templates": len(templates)}


# --------------------------------------------------------------------------- main

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--strict", action="store_true", help="fail if any record still has review flags")
    args = ap.parse_args()
    if args.strict and not MARKER_LIST:
        print("strict: no upstream marker list (set SANDBASE_UPSTREAM_MARKERS or SANDBASE_UPSTREAM_MARKERS_FILE)", file=sys.stderr)
        return 2

    meta = json.loads((RAW / "meta.json").read_text())
    listing = json.loads((RAW / "list.json").read_text())
    exclude = set(CONFIG["exclude_models"])
    review = {"flags": {}, "dropped_outputs": 0, "excluded": sorted(exclude)}

    records: dict[str, dict] = {}
    for item in listing:
        if item["name"] in exclude or not item.get("enabled", True):
            continue
        raw = json.loads((RAW / "models" / f"{item['id']}.json").read_text())
        if not raw.get("enabled", True):
            continue
        rec = build_record(raw, review)
        if raw["type"] in ("llm", "embedding") and (item.get("context_length") or 0) > 0:
            rec["context_length"] = item["context_length"]
        records[raw["name"]] = rec
    attach_price_examples(records)

    shutil.rmtree(OUT, ignore_errors=True)
    OUT.mkdir(parents=True)

    generated_at = meta["fetched_at"]
    for name, rec in records.items():
        path = OUT / "catalog" / "models" / f"{name}.json"
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n")
        doc = OUT / "docs" / "models" / f"{name}.md"
        doc.parent.mkdir(parents=True, exist_ok=True)
        depth = name.count("/")
        # render_md writes repo-root links as ../../<path>; rebase them for the page's depth
        doc.write_text(render_md(rec).replace("](../../", "](" + "../" * (depth + 2)))

    index = {
        "catalog_version": CATALOG_VERSION,
        "generated_at": generated_at,
        "base_url": BASE_URL,
        "count": len(records),
        "counts_by_type": dict(Counter(r["type"] for r in records.values()).most_common()),
        "models": [{
            "name": r["name"], "display_name": r["display_name"], "type": r["type"], "vendor": r.get("vendor"),
            "description": short(r.get("description", "")), "tags": r.get("tags", []), "modes": r["modes"],
            "endpoint": next(iter(r["endpoints"].values())), "price": price_summary(r["pricing"]),
            **({"status": r["status"]} if r.get("status") else {}),
            "record": f"catalog/models/{r['name']}.json",
        } for r in sorted(records.values(), key=lambda r: (r["type"], r["name"]))],
    }
    fq = [r["pricing"]["free_quota"] for r in records.values() if r["pricing"].get("free_quota")]
    if fq:
        index["free_quota"] = {"apis": len(fq), "daily_calls_per_org": max(x.get("daily_calls_per_org") or 0 for x in fq),
                               "note": "Shared across all free-quota APIs per organization; resets 00:00 UTC."}
    platform_counts = build_platform(generated_at)
    if platform_counts:
        index["platform"] = {**platform_counts, "files": ["catalog/skills.json", "catalog/sandbox.json"]}
    (OUT / "catalog" / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=1) + "\n")

    by_type = defaultdict(list)
    for r in index["models"]:
        by_type[r["type"]].append(r)
    lines = ["# SandBase capability index", "", f"{len(records)} capabilities · generated {generated_at}", ""]
    lines += [f"- [{t}](#{t}) ({len(v)})" for t, v in by_type.items()]
    for t, items in by_type.items():
        lines += ["", f"## {t}", "", "| name | price (USD) | modes | description |", "|---|---|---|---|"]
        for r in items:
            pr = r["price"]
            if "usd_per_call" in pr:
                ps = f"{pr['usd_per_call']} / call"
            elif "usd_per_million_tokens" in pr:
                ps = f"{pr['usd_per_million_tokens'].get('input')} / {pr['usd_per_million_tokens'].get('output')} per 1M tok"
            elif "usd_from" in pr:
                ps = f"{pr['usd_from']}–{pr['usd_to']}" if pr["usd_from"] != pr["usd_to"] else f"{pr['usd_from']}"
            elif "usd_reference" in pr:
                ps = f"~{pr['usd_reference']}"
            else:
                ps = pr.get("model") or ""
            if pr.get("free_quota"):
                ps += " (free quota)"
            lines.append(f"| [`{r['name']}`](models/{r['name']}.md) | {ps} | {', '.join(r['modes'])} | {md_escape(short(r['description'], 120))} |")
    (OUT / "docs" / "INDEX.md").write_text("\n".join(lines) + "\n")

    write_platform_pages(records, generated_at)
    write_exports(records, generated_at)
    oa = build_openapi(records, generated_at)
    (OUT / "openapi").mkdir(exist_ok=True)
    (OUT / "openapi" / "sandbase.openapi.json").write_text(json.dumps(oa, ensure_ascii=False) + "\n")

    # internal review report
    rv = ["# Publishing review (internal, not published)", "", f"Generated {generated_at}. Records: {len(records)}.",
          f"Example outputs dropped (third-party content or non-SandBase media hosts): {review['dropped_outputs']}.", "",
          "Resolve each item via config/publish.json (exclude_models / description_overrides / readme_overrides).", ""]
    groups = defaultdict(list)
    for name, fl in sorted(review["flags"].items()):
        for f in fl:
            groups[re.sub(r" in .*", "", f)].append((name, f))
    for g, items in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        rv += [f"## {g} ({len(items)})", ""]
        rv += [f"- `{n}`: {f}" for n, f in items[:200]]
        rv.append("")
    (ROOT / ".cache" / "review.md").write_text("\n".join(rv))

    update_readme_counts(index)
    write_llms_txt(index)
    size = (OUT / "openapi" / "sandbase.openapi.json").stat().st_size
    print(f"records: {len(records)}  flagged: {len(review['flags'])}  openapi: {size/1e6:.1f} MB")
    print("by type:", index["counts_by_type"])
    print("pricing models:", dict(Counter(r["pricing"].get("model") for r in records.values())))
    print("with price_examples:", sum(1 for r in records.values() if r["pricing"].get("price_examples")))
    blocking = {n: [f for f in fl if not f.startswith("info:")] for n, fl in review["flags"].items()}
    blocking = {n: fl for n, fl in blocking.items() if fl}
    print("blocking review items:", len(blocking))
    if args.strict and blocking:
        print("strict: unresolved review flags, see .cache/review.md (nothing published)", file=sys.stderr)
        return 2
    publish_outputs()
    return 0


if __name__ == "__main__":
    sys.exit(main())

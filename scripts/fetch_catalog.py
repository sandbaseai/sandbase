#!/usr/bin/env python3
"""Fetch the public SandBase model catalog (list + per-model detail) into .cache/raw.

Only public, unauthenticated endpoints are used. Raw responses stay in .cache/
(git-ignored); build_catalog.py turns them into the published, whitelisted files.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
RAW = ROOT / ".cache" / "raw"
DEFAULT_BASE = "https://api.sandbase.ai"
HEADERS = {
    "User-Agent": "sandbase-catalog/0.1 (+https://github.com/sandbaseai/sandbase)",
    "Accept": "application/json",
}


def get_json(url: str, retries: int = 4) -> dict:
    last: Exception | None = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers=HEADERS)
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.load(resp)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as exc:
            last = exc
            if isinstance(exc, urllib.error.HTTPError) and exc.code == 404:
                raise
            time.sleep(1.5 * (attempt + 1))
    raise RuntimeError(f"GET {url} failed after {retries} attempts: {last}")


def unwrap(payload: dict):
    if isinstance(payload, dict) and "data" in payload and "code" in payload:
        if payload.get("code") not in (0, None):
            raise RuntimeError(f"API error: {payload.get('message')}")
        return payload["data"]
    return payload


def get_authed(url: str, key: str, header: str = "Authorization") -> dict | list:
    value = f"Bearer {key}" if header == "Authorization" else key
    req = urllib.request.Request(url, headers={**HEADERS, header: value})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.load(resp)


def fetch_platform(base: str, failures: list[str]) -> None:
    """The Skill catalog and Sandbox templates need a key (any SandBase key works).
    Without SANDBASE_API_KEY they are skipped and the previous snapshot is kept."""
    key = os.environ.get("SANDBASE_API_KEY")
    if not key:
        print("SANDBASE_API_KEY not set: skipping agents, skills and sandbox templates")
        return
    out = {}
    try:
        skills, after = [], ""
        for _ in range(50):
            page = get_authed(f"{base}/v1/skills/catalog?limit=100" + (f"&after={after}" if after else ""), key)
            skills += page.get("data", [])
            if not page.get("has_more"):
                break
            after = page.get("last_id") or ""
        out["skills"] = skills
        out["sandbox_templates"] = get_authed("https://sandbox.sandbase.ai/v2/templates?limit=100", key, "X-API-Key")
    except Exception as exc:  # noqa: BLE001
        failures.append(f"platform catalog: {exc}")
        return
    (RAW / "platform.json").write_text(json.dumps(out, ensure_ascii=False))
    print(f"platform: {len(out['skills'])} skills, {len(out['sandbox_templates'])} templates")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default=DEFAULT_BASE)
    ap.add_argument("--workers", type=int, default=6)
    ap.add_argument("--limit", type=int, default=0, help="only fetch N models (debug)")
    args = ap.parse_args()

    RAW.mkdir(parents=True, exist_ok=True)
    (RAW / "models").mkdir(exist_ok=True)

    listing = unwrap(get_json(f"{args.base}/api/models?limit=10000"))
    if not isinstance(listing, list) or not listing:
        print("empty model list", file=sys.stderr)
        return 1
    if args.limit:
        listing = listing[: args.limit]
    (RAW / "list.json").write_text(json.dumps(listing, ensure_ascii=False))
    print(f"list: {len(listing)} models")

    failures: list[str] = []

    def fetch(item: dict) -> str:
        detail = unwrap(get_json(f"{args.base}/api/models/{item['id']}"))
        (RAW / "models" / f"{item['id']}.json").write_text(json.dumps(detail, ensure_ascii=False))
        return item["name"]

    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(fetch, m): m["name"] for m in listing}
        for i, fut in enumerate(as_completed(futures), 1):
            try:
                fut.result()
            except Exception as exc:  # noqa: BLE001 - report and continue
                failures.append(f"{futures[fut]}: {exc}")
            if i % 200 == 0:
                print(f"  {i}/{len(listing)}")

    fetch_platform(args.base, failures)

    meta = {"fetched_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()), "base": args.base,
            "count": len(listing), "failures": failures}
    (RAW / "meta.json").write_text(json.dumps(meta, indent=2))
    print(f"details done, failures: {len(failures)}")
    for f in failures[:20]:
        print("  FAIL", f)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())

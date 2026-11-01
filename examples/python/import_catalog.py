#!/usr/bin/env python3
"""Load the catalog the way an integrating platform would: list, filter, read schema and price.

    python import_catalog.py --type video
    python import_catalog.py --search "web search" --limit 5
    python import_catalog.py --show exa/search
"""
from __future__ import annotations

import argparse
import json
import urllib.request
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
RAW_BASE = "https://raw.githubusercontent.com/sandbaseai/sandbase/main/"


def load(path: str, remote: bool):
    if remote:
        req = urllib.request.Request(RAW_BASE + path, headers={"User-Agent": "sandbase-example/0.1"})
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.load(resp)
    return json.loads((REPO / path).read_text())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--type")
    ap.add_argument("--search")
    ap.add_argument("--show")
    ap.add_argument("--limit", type=int, default=20)
    ap.add_argument("--remote", action="store_true", help="read from GitHub instead of this checkout")
    a = ap.parse_args()

    if a.show:
        rec = load(f"catalog/models/{a.show}.json", a.remote)
        print(json.dumps({k: rec[k] for k in ("name", "type", "modes", "endpoints", "pricing") if k in rec}, indent=2))
        props = (rec.get("input_schema") or {}).get("properties", {})
        print("parameters:", ", ".join(f"{k}{'*' if k in (rec['input_schema'].get('required') or []) else ''}" for k in props))
        return

    index = load("catalog/index.json", a.remote)
    rows = index["models"]
    if a.type:
        rows = [r for r in rows if r["type"] == a.type]
    if a.search:
        q = a.search.lower()
        rows = [r for r in rows if q in (r["name"] + " " + r["description"] + " " + " ".join(r["tags"])).lower()]
    print(f"{len(rows)} of {index['count']} capabilities (catalog {index['generated_at']})")
    for r in rows[: a.limit]:
        print(f"  {r['name']:<60} {r['type']:<6} {json.dumps(r['price'])}")


if __name__ == "__main__":
    main()

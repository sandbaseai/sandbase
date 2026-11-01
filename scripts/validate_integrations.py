#!/usr/bin/env python3
"""Validate integration proposals under integrations/<vendor>/<capability>/integration.yaml.

    pip install pyyaml jsonschema
    python scripts/validate_integrations.py                 # all proposals
    python scripts/validate_integrations.py path/to/integration.yaml ...

Checks: JSON Schema, folder/id consistency, no clash with an existing catalog name,
no credentials, async fields present, input_schema is valid JSON Schema, example size.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parent.parent
SCHEMA = json.loads((ROOT / "integrations" / "schema" / "integration.schema.json").read_text())
SECRET_PATTERNS = [
    re.compile(r"\b(sk|pk|rk)[-_][A-Za-z0-9]{16,}"),
    re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}"),
    re.compile(r"\bey[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}"),  # JWT
    re.compile(r"(?i)(api[_-]?key|secret|token|password)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
]
MAX_EXAMPLE_BYTES = 32 * 1024


def existing_names() -> set[str]:
    index = ROOT / "catalog" / "index.json"
    if not index.exists():
        return set()
    return {m["name"] for m in json.loads(index.read_text())["models"]}


def check(path: Path, catalog: set[str]) -> list[str]:
    errors: list[str] = []
    raw = path.read_text(encoding="utf-8")
    for pat in SECRET_PATTERNS:
        if pat.search(raw):
            errors.append("looks like it contains a credential; remove it (maintainers arrange access)")
            break
    try:
        doc = yaml.safe_load(raw)
    except yaml.YAMLError as exc:
        return [f"invalid YAML: {exc}"]
    if not isinstance(doc, dict):
        return ["top level must be a mapping"]

    for err in sorted(Draft202012Validator(SCHEMA).iter_errors(doc), key=lambda e: list(e.path)):
        where = "/".join(str(p) for p in err.path) or "(root)"
        errors.append(f"{where}: {err.message}")
    if errors:
        return errors

    rel = path.parent.relative_to(ROOT / "integrations").as_posix()
    if rel != doc["id"]:
        errors.append(f"folder integrations/{rel}/ must match id '{doc['id']}'")
    if doc["id"] in catalog:
        errors.append(f"'{doc['id']}' already exists in the catalog; pick another id or open an issue to update it")

    auth = doc["request"]["auth"]
    if auth["type"] in ("header", "query") and not auth.get("name"):
        errors.append("request.auth.name is required for header/query auth")
    ex = doc["execution"]
    if ex["mode"] == "async":
        for field in ("poll_path", "task_id_field", "status_field", "status_map"):
            if field not in ex:
                errors.append(f"execution.{field} is required for async APIs")
    pricing = doc["pricing"]
    if pricing["model"] != "free" and "usd" not in pricing:
        errors.append("pricing.usd is required unless pricing.model is free")
    if pricing["model"] == "per_unit" and not (pricing.get("unit") and pricing.get("unit_field")):
        errors.append("pricing.unit and pricing.unit_field are required for per_unit")

    try:
        Draft202012Validator.check_schema(doc["input_schema"])
    except Exception as exc:  # noqa: BLE001
        errors.append(f"input_schema is not valid JSON Schema: {str(exc).splitlines()[0]}")
    if "output_example" in doc and len(json.dumps(doc["output_example"])) > MAX_EXAMPLE_BYTES:
        errors.append("output_example is larger than 32 KiB; trim it")
    return errors


def main(argv: list[str]) -> int:
    paths = [Path(p).resolve() for p in argv] or sorted((ROOT / "integrations").glob("**/integration.yaml"))
    paths = [p for p in paths if "_template" not in p.parts]
    catalog = existing_names()
    failed = 0
    for p in paths:
        errs = check(p, catalog)
        rel = p.relative_to(ROOT)
        if errs:
            failed += 1
            print(f"FAIL {rel}")
            for e in errs:
                print(f"  - {e}")
        else:
            print(f"ok   {rel}")
    if not paths:
        print("no integration proposals found")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

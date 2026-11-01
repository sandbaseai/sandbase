#!/usr/bin/env python3
"""Run code in a SandBase sandbox with the official E2B SDK (pip install e2b).

    export SANDBASE_API_KEY=sk-...
    python hello_sandbox.py              # uses the first ready public template

SandBase speaks the E2B protocol: point the SDK at sandbox.sandbase.ai and use your SandBase key.
"""
import json
import os
import urllib.request

os.environ.setdefault("E2B_API_KEY", os.environ["SANDBASE_API_KEY"])
os.environ.setdefault("E2B_API_URL", "https://sandbox.sandbase.ai")
os.environ.setdefault("E2B_DOMAIN", "sandbox.sandbase.ai")
os.environ.pop("E2B_SANDBOX_URL", None)

from e2b import Sandbox  # noqa: E402  (import after the environment is configured)


def first_ready_template() -> str:
    req = urllib.request.Request(
        "https://sandbox.sandbase.ai/v2/templates?limit=100",
        headers={"X-API-Key": os.environ["E2B_API_KEY"], "User-Agent": "sandbase-example/0.1"},
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        templates = json.load(resp)
    ready = [t for t in templates if t.get("buildStatus") == "ready"]
    if not ready:
        raise SystemExit("no ready sandbox template is visible to this key")
    return ready[0]["templateID"]


template = os.environ.get("SANDBASE_TEMPLATE_ID") or first_ready_template()
sandbox = Sandbox.create(template, timeout=120)   # seconds; deleted below either way
try:
    print("sandbox:", sandbox.sandbox_id)
    result = sandbox.commands.run("python3 -c 'print(sum(range(10)))'")
    print("stdout:", result.stdout.strip(), "exit:", result.exit_code)
    sandbox.files.write("/tmp/hello.txt", "hello from SandBase")
    print("file:", sandbox.files.read("/tmp/hello.txt"))
finally:
    sandbox.kill()
    print("deleted")

"""SandBase Python client. Standard library only.

    from sandbase import SandBase

    sb = SandBase()                                    # reads SANDBASE_API_KEY
    out = sb.run("exa/search", query="AI agents")      # sync or async: waits for the result
    run = sb.submit("bytedance/seedance/2.5/text-to-video", prompt="a cat surfing", duration=4)
    done = sb.wait(run["id"])
    print(sb.cost(done["id"]))
"""
from __future__ import annotations

import json
import os
import time
import urllib.error
import urllib.request
from typing import Any

__all__ = ["SandBase", "SandBaseError", "TERMINAL_STATUSES"]
__version__ = "0.1.0"

DEFAULT_BASE_URL = "https://api.sandbase.ai"
TERMINAL_STATUSES = frozenset({"completed", "succeeded", "failed", "cancelled", "canceled"})


class SandBaseError(RuntimeError):
    """Raised for HTTP errors, failed runs and timeouts."""

    def __init__(self, message: str, status: int | None = None, body: Any = None):
        super().__init__(message)
        self.status = status
        self.body = body


class SandBase:
    def __init__(self, api_key: str | None = None, base_url: str | None = None, timeout: float = 300):
        self.api_key = api_key or os.environ.get("SANDBASE_API_KEY")
        if not self.api_key:
            raise SandBaseError("missing API key: pass api_key or set SANDBASE_API_KEY")
        self.base_url = (base_url or os.environ.get("SANDBASE_BASE_URL") or DEFAULT_BASE_URL).rstrip("/")
        self.timeout = timeout

    # ------------------------------------------------------------------ HTTP

    def request(self, method: str, path: str, body: Any = None, headers: dict | None = None) -> Any:
        """Call any SandBase endpoint, e.g. request("POST", "/v1/chat/completions", {...})."""
        req = urllib.request.Request(
            self.base_url + path,
            method=method,
            data=None if body is None else json.dumps(body).encode(),
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
                # the edge rejects urllib's default "Python-urllib/x.y" User-Agent
                "User-Agent": f"sandbase-python/{__version__}",
                **(headers or {}),
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                raw = resp.read()
        except urllib.error.HTTPError as exc:
            raw = exc.read()
            try:
                parsed = json.loads(raw)
            except ValueError:
                parsed = raw.decode(errors="replace")
            raise SandBaseError(f"HTTP {exc.code}: {str(parsed)[:500]}", exc.code, parsed) from None
        return json.loads(raw) if raw else None

    # ------------------------------------------------------------------ runs

    def submit(self, model: str, params: dict | None = None, *, mode: str | None = None,
               webhook_url: str | None = None, **fields: Any) -> dict:
        """POST /v1/run. Sync capabilities return the finished run; async ones return {id, status: pending}."""
        body = {"model": model, **(params or {}), **fields}
        if mode:
            body["mode"] = mode
        if webhook_url:
            body["webhook_url"] = webhook_url
        return self.request("POST", "/v1/run", body)

    def get(self, run_id: str) -> dict:
        return self.request("GET", f"/v1/run/{run_id}")

    def wait(self, run_id: str, timeout: float = 900, interval: float = 2.0, max_interval: float = 15.0) -> dict:
        """Poll GET /v1/run/{id} with backoff until the run reaches a terminal status."""
        deadline = time.monotonic() + timeout
        while True:
            run = self.get(run_id)
            if run.get("status") in TERMINAL_STATUSES:
                return run
            if time.monotonic() > deadline:
                raise SandBaseError(f"run {run_id} still {run.get('status')} after {timeout:.0f}s", body=run)
            time.sleep(interval)
            interval = min(interval * 1.5, max_interval)

    def run(self, model: str, params: dict | None = None, *, timeout: float = 900, raise_on_failure: bool = True,
            **fields: Any) -> dict:
        """Run any capability and return the finished run, whether it is sync or async."""
        result = self.submit(model, params, **fields)
        if result.get("status") not in TERMINAL_STATUSES:
            result = self.wait(result["id"], timeout=timeout)
        if raise_on_failure and result.get("status") == "failed":
            raise SandBaseError(f"run {result.get('id')} failed: {result.get('error')}", body=result)
        return result

    def cost(self, run_id: str) -> dict:
        """What a run was billed: GET /v1/tasks/{id}/cost."""
        return self.request("GET", f"/v1/tasks/{run_id}/cost")

    # ------------------------------------------------------------------ LLM

    def chat(self, model: str, messages: list[dict], **fields: Any) -> dict:
        """OpenAI-compatible chat completion. For streaming, use the official openai SDK with base_url."""
        return self.request("POST", "/v1/chat/completions", {"model": model, "messages": messages, **fields})

    # ------------------------------------------------------------------ Agents

    def create_agent(self, model: str, instructions: str | None = None, name: str | None = None,
                     idempotency_key: str | None = None, wait_ready: bool = True, **fields: Any) -> dict:
        """POST /v1/agents. Waits until the new version can start Sessions."""
        body = {"model": model, **({"instructions": instructions} if instructions else {}),
                **({"name": name} if name else {}), **fields}
        agent = self.request("POST", "/v1/agents", body, {"Idempotency-Key": idempotency_key or _key()})
        return self._wait_agent_ready(agent) if wait_ready else agent

    def run_agent(self, agent_id: str, input: str, timeout: float = 900, **fields: Any) -> dict:
        """Start a Session with `input` and wait for the turn. Returns {session_id, status, output, turn}."""
        session = self.request("POST", "/v1/agents/sessions", {"agent_id": agent_id, "input": input, **fields},
                               {"Idempotency-Key": _key()})
        return self._finish_turn(session["id"], previous_turns=0, timeout=timeout)

    def send(self, session_id: str, input: str, timeout: float = 900) -> dict:
        """Send a follow-up message to a Session and wait for its turn."""
        previous = len(self._turns(session_id))
        self.request("POST", f"/v1/agents/sessions/{session_id}/events", {"input": input}, {"Idempotency-Key": _key()})
        return self._finish_turn(session_id, previous_turns=previous, timeout=timeout)

    def session_items(self, session_id: str, limit: int = 100) -> list[dict]:
        return self.request("GET", f"/v1/agents/sessions/{session_id}/items?order=asc&limit={limit}").get("data", [])

    def invoke_service(self, service_id: str, input: str | None = None, wait: bool = True, timeout: float = 900,
                       idempotency_key: str | None = None) -> dict:
        """POST /v1/services/{id}/invoke; with wait=True, polls the Run and adds the Session's final `output`."""
        run = self.request("POST", f"/v1/services/{service_id}/invoke", {"input": input} if input else {},
                           {"Idempotency-Key": idempotency_key or _key()})
        if not wait:
            return run
        deadline = time.monotonic() + timeout
        interval = 2.0
        while run.get("status") not in ("succeeded", "failed", "cancelled", "canceled"):
            if time.monotonic() > deadline:
                raise SandBaseError(f"service run {run['id']} still {run.get('status')}", body=run)
            time.sleep(interval)
            interval = min(interval * 1.5, 15.0)
            run = self.request("GET", f"/v1/services/{service_id}/runs/{run['id']}")
        if run.get("session_id"):
            run["output"] = self._latest_output(run["session_id"])
        return run

    # internals

    def _wait_agent_ready(self, agent: dict, timeout: float = 120) -> dict:
        deadline = time.monotonic() + timeout
        while agent.get("projection_status") not in (None, "ready"):
            if agent.get("projection_status") == "failed" or time.monotonic() > deadline:
                raise SandBaseError(f"agent {agent.get('id')} projection {agent.get('projection_status')}", body=agent)
            time.sleep(2)
            agent = self.request("GET", f"/v1/agents/{agent['id']}")
        return agent

    def _latest_output(self, session_id: str) -> str:
        newest_first = self.request("GET", f"/v1/agents/sessions/{session_id}/items?order=desc&limit=50").get("data", [])
        tail = []
        for item in newest_first:
            if item.get("type") == "message" and item.get("role") == "user":
                break
            tail.append(item)
        return _last_assistant_text(list(reversed(tail)))

    def _turns(self, session_id: str) -> list[dict]:
        return self.request("GET", f"/v1/agents/sessions/{session_id}/turns").get("data", [])  # newest first

    def _finish_turn(self, session_id: str, previous_turns: int, timeout: float) -> dict:
        deadline = time.monotonic() + timeout
        interval = 2.0
        while True:
            turns = self._turns(session_id)
            if len(turns) > previous_turns and turns[0].get("status") in TURN_TERMINAL:
                turn = turns[0]
                break
            session = self.request("GET", f"/v1/agents/sessions/{session_id}")
            if session.get("status") == "failed":
                raise SandBaseError(f"session {session_id} failed: {session.get('failure')}", body=session)
            if time.monotonic() > deadline:
                raise SandBaseError(f"session {session_id} turn not finished after {timeout:.0f}s", body=session)
            time.sleep(interval)
            interval = min(interval * 1.5, 10.0)
        if turn.get("status") != "completed":
            raise SandBaseError(f"turn {turn.get('id')} {turn.get('status')}: {turn.get('error')}", body=turn)
        return {"session_id": session_id, "status": turn["status"],
                "output": self._latest_output(session_id), "turn": turn}


TURN_TERMINAL = frozenset({"completed", "failed", "cancelled", "canceled", "incomplete", "expired"})


def _key() -> str:
    import uuid
    return f"sdk-{uuid.uuid4()}"


def _last_assistant_text(items: list[dict]) -> str:
    """Text of the assistant messages after the last user message."""
    out: list[str] = []
    for item in items:
        if item.get("type") == "message" and item.get("role") == "user":
            out = []
        elif item.get("type") == "message" and item.get("role") == "assistant":
            for part in item.get("content") or []:
                if part.get("type") == "output_text":
                    out.append(part.get("text", ""))
    return "\n".join(out)

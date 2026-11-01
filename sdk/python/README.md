# sandbase (Python)

Standard library only, Python 3.9+.

```bash
pip install "git+https://github.com/sandbaseai/sandbase#subdirectory=sdk/python"
export SANDBASE_API_KEY=sk-...
```

```python
from sandbase import SandBase

sb = SandBase()

# Any capability, sync or async: run() returns the finished result
r = sb.run("exa/search", query="AI agents", numResults=3)
print(r["outputs"][0]["data"]["results"][0]["url"])

# Async without blocking
job = sb.submit("bytedance/seedance/2.5/text-to-video", prompt="a cat surfing", duration=4)
video = sb.wait(job["id"], timeout=900)
print(video["outputs"][0]["url"], sb.cost(job["id"])["cost"])

# LLM (OpenAI-compatible)
print(sb.chat("openai/gpt-6.1-sol", [{"role": "user", "content": "Hi"}])["choices"][0]["message"]["content"])
```

Every model's fields and price: [`catalog/models/<name>.json`](../../catalog/) or [`docs/INDEX.md`](../../docs/INDEX.md).

## Agents

```python
agent = sb.create_agent("deepseek/deepseek-v4-flash", "Answer in one short sentence.")
r = sb.run_agent(agent["id"], "What is 2+2?")      # {"session_id", "status", "output", "turn"}
r2 = sb.send(r["session_id"], "And times 10?")       # follow-up in the same Session
run = sb.invoke_service("svc_...", "What is 7+7?")   # Service Run; run["output"] is the final answer
```

## Sandboxes

Use the official E2B SDK (`pip install e2b`) with `E2B_API_URL=https://sandbox.sandbase.ai`, `E2B_DOMAIN=sandbox.sandbase.ai` and your SandBase key as `E2B_API_KEY`. See [`examples/sandbox/python`](../../examples/sandbox/python/hello_sandbox.py).

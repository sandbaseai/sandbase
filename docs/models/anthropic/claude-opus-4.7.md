# Anthropic: Claude Opus 4.7 API: pricing, parameters and code examples

`anthropic/claude-opus-4.7` · LLM · Anthropic · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $5 input / $25 output per 1M tokens · **Modes:** sync

Opus 4.7 is the next generation of Anthropic's Opus family, built for long-running, asynchronous agents. Building on the coding and agentic strengths of Opus 4.6, it delivers stronger performance on complex, multi-step tasks and more reliable agentic execution across extended workflows. It is especially effective for asynchronous agent pipelines where tasks unfold over time - large codebases, multi-stage debugging, and end-to-end project orchestration.

Beyond coding, Opus 4.7 brings improved knowledge work capabilities - from drafting documents and building presentations to analyzing data. It maintains coherence across very long outputs and extended sessions, making it a strong default for tasks that require persistence, judgment, and follow-through.

## Pricing

- Input **$5** / output **$25** per 1M tokens (USD)
- cache read multiplier: 0.1
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "anthropic/claude-opus-4.7", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='anthropic/claude-opus-4.7', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "anthropic/claude-opus-4.7", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "anthropic/claude-opus-4.7", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/anthropic/claude-opus-4.7.json`](../../../catalog/models/anthropic/claude-opus-4.7.json) · Store page: https://www.sandbase.ai/model/anthropic/claude-opus-4.7

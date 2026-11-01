# OpenAI: GPT-5.1-Codex

`openai/gpt-5.1-codex` · llm · OpenAI

GPT-5.1-Codex is a version of OpenAI's GPT-5.1 optimized for agentic coding in Codex and similar environments, released in November 2025 with text and image input and text output. It targets autonomous, long-running software engineering work inside coding agents and tools, and OpenAI notes its underlying snapshot is updated over time. Pick it over general GPT-5.1 when building coding agents; OpenAI serves it through the Responses API only.

## Pricing

- Input **$1.25** / output **$10** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-5.1-codex", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-5.1-codex', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-5.1-codex", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-5.1-codex", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-5.1-codex.json`](../../../catalog/models/openai/gpt-5.1-codex.json) · Store page: https://www.sandbase.ai/model/openai/gpt-5.1-codex

# OpenAI: GPT-6.1 Sol API: pricing, parameters and code examples

`openai/gpt-6.1-sol` · LLM · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $2 input / $10 output per 1M tokens · **Modes:** sync

GPT-6.1 Sol is OpenAI's upgrade to GPT-6 Sol, introduced at DevDay 2026 and positioned between GPT-6 Astra and GPT-6 Luna, with text and image input. OpenAI says it delivers near-Astra performance for complex coding, computer use and professional work, and recommends comparing it with Astra on your own tasks. Pick it for demanding agentic work at scale when Astra's full depth is not required; it always reasons at least at a low level and has no reasoning-off option.

## Pricing

- Input **$2** / output **$10** per 1M tokens (USD)
- cache read multiplier: 0.05
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-6.1-sol", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-6.1-sol', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-6.1-sol", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-6.1-sol", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-6.1-sol.json`](../../../catalog/models/openai/gpt-6.1-sol.json) · Store page: https://www.sandbase.ai/model/openai/gpt-6.1-sol

# Qwen: Qwen3.8 Max Prime API: pricing, parameters and code examples

`alibaba/qwen3.8-max-prime` · LLM · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $4 input / $12 output per 1M tokens · **Modes:** sync

Qwen3.8 Max Prime is the Fast mode (Prime) serving option for Alibaba's Qwen3.8 Max: the same model with the same vision input and reasoning, delivered at higher output speed. Alibaba states Fast mode raises tokens per second to about 1.5 to 2 times the standard API, aimed at latency-sensitive uses such as AI coding assistants, multi-step agent reasoning and real-time conversation. Pick it over standard Qwen3.8 Max when response speed matters; it adds no new capabilities.

## Pricing

- Input **$4** / output **$12** per 1M tokens (USD)
- cache read multiplier: 0.125
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen3.8-max-prime", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='alibaba/qwen3.8-max-prime', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "alibaba/qwen3.8-max-prime", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "alibaba/qwen3.8-max-prime", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/alibaba/qwen3.8-max-prime.json`](../../../catalog/models/alibaba/qwen3.8-max-prime.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen3.8-max-prime

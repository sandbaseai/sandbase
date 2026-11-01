# OpenAI: GPT-5.6 Sol Pro

`openai/gpt-5.6-sol-pro` · llm · OpenAI

GPT-5.6 Sol Pro is the same GPT-5.6 Sol model, the flagship of OpenAI's GPT-5.6 family, served in OpenAI's pro reasoning mode rather than as a separate model. Pro mode spends more model work on each request before returning one final answer, which OpenAI recommends for complex optimization, high-value coding or review, and deep analysis. It brings higher latency and token usage, so standard Sol remains the better choice for routine or latency-sensitive work.

## Pricing

- Input **$4** / output **$20** per 1M tokens (USD)
- cache read multiplier: 0.1
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-5.6-sol-pro", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-5.6-sol-pro', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-5.6-sol-pro", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-5.6-sol-pro", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-5.6-sol-pro.json`](../../../catalog/models/openai/gpt-5.6-sol-pro.json) · Store page: https://www.sandbase.ai/model/openai/gpt-5.6-sol-pro

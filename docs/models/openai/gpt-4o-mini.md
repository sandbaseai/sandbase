# OpenAI: GPT-4o-mini

`openai/gpt-4o-mini` · llm · OpenAI

GPT-4o mini is OpenAI's small, fast model from the GPT-4o family, released in July 2024 with text and image input and text output, including Structured Outputs. OpenAI positions it for focused tasks such as intent classification, keyword extraction, translation and tagging, and calls it ideal for fine-tuning, including distilling outputs from a larger model like GPT-4o. Pick it over GPT-4o when latency and throughput matter more than peak capability.

## Pricing

- Input **$0.15** / output **$0.6** per 1M tokens (USD)
- cache read multiplier: 0.5

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-4o-mini", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-4o-mini', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-4o-mini", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-4o-mini", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-4o-mini.json`](../../../catalog/models/openai/gpt-4o-mini.json) · Store page: https://www.sandbase.ai/model/openai/gpt-4o-mini

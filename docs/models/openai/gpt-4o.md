# OpenAI: GPT-4o

`openai/gpt-4o` · llm · OpenAI

GPT-4o ("o" for "omni") is OpenAI's versatile, high-intelligence GPT model released in May 2024, accepting text and image input and producing text output, including Structured Outputs. OpenAI describes it as fast and flexible, suited to general-purpose chat, image understanding, function calling and non-English language tasks. This entry tracks OpenAI's default GPT-4o alias; use one of the dated GPT-4o snapshots when a workload needs fixed behavior.

## Pricing

- Input **$2.5** / output **$10** per 1M tokens (USD)
- cache read multiplier: 0.5

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-4o", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-4o', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-4o", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-4o", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-4o.json`](../../../catalog/models/openai/gpt-4o.json) · Store page: https://www.sandbase.ai/model/openai/gpt-4o

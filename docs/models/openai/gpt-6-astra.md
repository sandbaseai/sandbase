# OpenAI: GPT-6 Astra

`openai/gpt-6-astra` · llm · OpenAI

GPT-6 Astra is OpenAI's flagship GPT-6 reasoning model, described by OpenAI as its most capable model for the most demanding work, with text and image input. OpenAI recommends it for complex reasoning, coding, computer use, research and document creation, including multi-step workflows across code, browsers and professional software. It is the top tier above GPT-6.1 Sol and GPT-6 Luna; choose it when quality matters most, or the Astra Pro variant for the hardest requests.

## Pricing

- Input **$10** / output **$50** per 1M tokens (USD)
- cache read multiplier: 0.1
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-6-astra", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-6-astra', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-6-astra", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-6-astra", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-6-astra.json`](../../../catalog/models/openai/gpt-6-astra.json) · Store page: https://www.sandbase.ai/model/openai/gpt-6-astra

# OpenAI: GPT-6 Sol

`openai/gpt-6-sol` · llm · OpenAI

GPT-6 Sol is the middle tier of OpenAI's GPT-6 reasoning family, released in September 2026 alongside GPT-6 Luna and built, according to OpenAI, for complex coding and agentic workflows, with text and image input. It was trained with methods similar to GPT-6 Astra to bring much of Astra's capability to a faster tier. OpenAI's docs now point to GPT-6.1 Sol as the updated Sol model, so this entry mainly suits workloads already validated on GPT-6 Sol.

## Pricing

- Input **$2** / output **$10** per 1M tokens (USD)
- cache read multiplier: 0.1
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-6-sol", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-6-sol', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-6-sol", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-6-sol", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-6-sol.json`](../../../catalog/models/openai/gpt-6-sol.json) · Store page: https://www.sandbase.ai/model/openai/gpt-6-sol

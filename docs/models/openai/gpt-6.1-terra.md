# OpenAI: GPT-6.1 Terra API: pricing, parameters and code examples

`openai/gpt-6.1-terra` · LLM · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1 input / $5 output per 1M tokens · **Modes:** sync

GPT-6.1 Terra is the middle tier of OpenAI's GPT-6.1 family and the replacement for GPT-5.6 Terra, with text and image input. OpenAI positions it for everyday agentic, coding and writing work, with particular gains in visual reasoning over screenshots and documents and in computer use, at half the price of GPT-6.1 Sol. Reasoning effort ranges from none to max with medium as the default; choose GPT-6.1 Sol for harder work or GPT-6 Luna for the highest-volume tasks.

## Pricing

- Input **$1** / output **$5** per 1M tokens (USD)
- cache read multiplier: 0.05
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-6.1-terra", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-6.1-terra', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-6.1-terra", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-6.1-terra", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-6.1-terra.json`](../../../catalog/models/openai/gpt-6.1-terra.json) · Store page: https://www.sandbase.ai/model/openai/gpt-6.1-terra

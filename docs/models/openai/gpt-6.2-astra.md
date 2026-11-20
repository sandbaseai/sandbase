# OpenAI: GPT-6.2 Astra API: pricing, parameters and code examples

`openai/gpt-6.2-astra` · LLM · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $8 input / $40 output per 1M tokens · **Modes:** sync

GPT-6.2 Astra is the flagship model of OpenAI's GPT-6.2 series, built for the hardest projects, with text, image and file input and a context window of about 1M tokens. It suits real-world engineering, professional work and scientific research that need deep multi-step reasoning, coding and tool use. It sits above GPT-6.2 Sol; choose the Astra Pro variant for the most demanding single requests.

## Pricing

- Input **$8** / output **$40** per 1M tokens (USD)
- cache read multiplier: 0.05
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-6.2-astra", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-6.2-astra', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-6.2-astra", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-6.2-astra", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-6.2-astra.json`](../../../catalog/models/openai/gpt-6.2-astra.json) · Store page: https://www.sandbase.ai/model/openai/gpt-6.2-astra

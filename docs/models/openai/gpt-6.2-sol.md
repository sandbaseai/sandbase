# OpenAI: GPT-6.2 Sol API: pricing, parameters and code examples

`openai/gpt-6.2-sol` · LLM · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $2 input / $10 output per 1M tokens · **Modes:** sync

GPT-6.2 Sol is OpenAI's upgrade to GPT-6.1 Sol, positioned below the flagship GPT-6.2 Astra in the GPT-6.2 series, with text, image and file input and a context window of about 1M tokens. It is an efficient, versatile reasoning model for everyday professional work, coding and agentic tasks at scale. Choose GPT-6.2 Astra when a task needs the deepest reasoning, or the Sol Pro variant for harder single requests.

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
  -d '{"model": "openai/gpt-6.2-sol", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-6.2-sol', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-6.2-sol", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-6.2-sol", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-6.2-sol.json`](../../../catalog/models/openai/gpt-6.2-sol.json) · Store page: https://www.sandbase.ai/model/openai/gpt-6.2-sol

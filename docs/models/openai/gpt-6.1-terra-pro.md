# OpenAI: GPT-6.1 Terra Pro API: pricing, parameters and code examples

`openai/gpt-6.1-terra-pro` · LLM · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1 input / $5 output per 1M tokens · **Modes:** sync

GPT-6.1 Terra Pro is the same GPT-6.1 Terra model, the balanced middle tier of OpenAI's GPT-6.1 family, served in OpenAI's pro reasoning mode instead of standard mode. Pro mode applies more model work to each request and returns a single final answer, which OpenAI says can improve reliability on difficult problems while increasing latency and token usage. It fits harder coding, review or analysis tasks where Terra's tier is preferred but extra quality on a single answer matters.

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
  -d '{"model": "openai/gpt-6.1-terra-pro", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-6.1-terra-pro', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-6.1-terra-pro", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-6.1-terra-pro", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-6.1-terra-pro.json`](../../../catalog/models/openai/gpt-6.1-terra-pro.json) · Store page: https://www.sandbase.ai/model/openai/gpt-6.1-terra-pro

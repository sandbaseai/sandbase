# OpenAI: GPT-5.5 Pro API: pricing, parameters and code examples

`openai/gpt-5.5-pro` · LLM · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $30 input / $180 output per 1M tokens · **Modes:** sync

GPT-5.5 Pro is a separate OpenAI model in the GPT-5.5 family that uses more compute to think harder and give consistently better answers, according to OpenAI. It is intended for tough, high-stakes problems where answer quality matters more than speed, and some requests can take several minutes to finish. Choose it over standard GPT-5.5 when reliability on difficult reasoning, coding or analysis justifies the extra latency; OpenAI serves it for multi-turn and batch API requests.

## Pricing

- Input **$30** / output **$180** per 1M tokens (USD)

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-5.5-pro", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-5.5-pro', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-5.5-pro", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-5.5-pro", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-5.5-pro.json`](../../../catalog/models/openai/gpt-5.5-pro.json) · Store page: https://www.sandbase.ai/model/openai/gpt-5.5-pro

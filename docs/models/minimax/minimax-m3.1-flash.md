# MiniMax: MiniMax M3.1 Flash

`minimax/minimax-m3.1-flash` · llm · Minimax

MiniMax-M3.1-Flash is the fast, cost-efficient tier of MiniMax's M3.1 generation, which MiniMax describes as an ultra-efficient open-weight model for everyday work. It is a multimodal coding model that accepts text, image and video input and supports a context window of up to 1M tokens. Thinking is always on, and its depth can be tuned with reasoning effort levels from low to max, making it suited to agentic coding, tool use and routine software development at lower latency and cost than MiniMax-M3.

## Pricing

- Input **$0.15** / output **$0.6** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/minimax-m3.1-flash", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='minimax/minimax-m3.1-flash', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "minimax/minimax-m3.1-flash", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "minimax/minimax-m3.1-flash", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/minimax/minimax-m3.1-flash.json`](../../../catalog/models/minimax/minimax-m3.1-flash.json) · Store page: https://www.sandbase.ai/model/minimax/minimax-m3.1-flash

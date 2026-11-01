# MoonshotAI: Kimi K2.6

`moonshotai/kimi-k2.6` · llm · Moonshotai

Kimi K2.6 is Moonshot AI's general-purpose multimodal model, taking text, image and video input with both thinking and non-thinking modes and a 256K-token context. Moonshot highlights more reliable long-horizon coding across languages such as Rust, Go and Python and tasks like frontend, DevOps and performance optimization, along with stronger instruction following, self-correction and autonomous agent execution. Choose Kimi K3 for flagship-level work with a 1M context.

## Pricing

- Input **$0.95** / output **$4** per 1M tokens (USD)
- cache read multiplier: 0.1684

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "moonshotai/kimi-k2.6", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='moonshotai/kimi-k2.6', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "moonshotai/kimi-k2.6", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "moonshotai/kimi-k2.6", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/moonshotai/kimi-k2.6.json`](../../../catalog/models/moonshotai/kimi-k2.6.json) · Store page: https://www.sandbase.ai/model/moonshotai/kimi-k2.6

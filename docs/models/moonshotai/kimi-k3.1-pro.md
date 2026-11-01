# MoonshotAI: Kimi K3.1 Pro

`moonshotai/kimi-k3.1-pro` · llm · Moonshotai

Kimi K3.1 Pro is Moonshot AI's flagship open-weight multimodal reasoning model, a post-trained successor to Kimi K3 with a 1M-token context window. It accepts text, image and video input and is built for long-horizon coding, agentic tool use and visual software work.

## Pricing

- Input **$2** / output **$10** per 1M tokens (USD)
- cache read multiplier: 0.1
- cache write multiplier: 1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "moonshotai/kimi-k3.1-pro", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='moonshotai/kimi-k3.1-pro', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "moonshotai/kimi-k3.1-pro", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "moonshotai/kimi-k3.1-pro", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/moonshotai/kimi-k3.1-pro.json`](../../../catalog/models/moonshotai/kimi-k3.1-pro.json) · Store page: https://www.sandbase.ai/model/moonshotai/kimi-k3.1-pro

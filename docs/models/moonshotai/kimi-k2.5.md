# MoonshotAI: Kimi K2.5 API: pricing, parameters and code examples

`moonshotai/kimi-k2.5` · LLM · Moonshotai · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.6 input / $3 output per 1M tokens · **Modes:** sync

Kimi K2.5 is Moonshot AI's open-source native multimodal agentic model, built by continuing pretraining of Kimi K2 on about 15 trillion mixed visual and text tokens. It is a 1T-parameter mixture-of-experts model with 32B active parameters and a 256K-token context, offering instant and thinking modes. Moonshot highlights coding from visual specifications such as UI designs and an agent swarm mode that splits complex tasks across parallel sub-agents; Kimi K2.6 later succeeded it.

## Pricing

- Input **$0.6** / output **$3** per 1M tokens (USD)
- cache read multiplier: 0.1667

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "moonshotai/kimi-k2.5", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='moonshotai/kimi-k2.5', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "moonshotai/kimi-k2.5", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "moonshotai/kimi-k2.5", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/moonshotai/kimi-k2.5.json`](../../../catalog/models/moonshotai/kimi-k2.5.json) · Store page: https://www.sandbase.ai/model/moonshotai/kimi-k2.5

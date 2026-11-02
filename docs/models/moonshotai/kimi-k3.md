# MoonshotAI: Kimi K3 API: pricing, parameters and code examples

`moonshotai/kimi-k3` · LLM · Moonshotai · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $3 input / $15 output per 1M tokens · **Modes:** sync

Kimi K3 is Moonshot AI's flagship model, a 2.8-trillion-parameter open-weight mixture-of-experts model with native visual understanding and a 1M-token context. It is built on Kimi Delta Attention, a hybrid linear attention, plus Attention Residuals, and always runs in thinking mode with selectable effort. Moonshot positions it for long-horizon coding across large codebases and terminal tools, visual software tasks such as frontend and game work, and end-to-end knowledge work.

## Pricing

- Input **$3** / output **$15** per 1M tokens (USD)
- cache read multiplier: 0.1
- cache write multiplier: 1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "moonshotai/kimi-k3", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='moonshotai/kimi-k3', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "moonshotai/kimi-k3", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "moonshotai/kimi-k3", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/moonshotai/kimi-k3.json`](../../../catalog/models/moonshotai/kimi-k3.json) · Store page: https://www.sandbase.ai/model/moonshotai/kimi-k3

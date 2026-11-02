# Z.ai: GLM 5.3 Flash API: pricing, parameters and code examples

`z-ai/glm-5.3-flash` · LLM · Z-Ai · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.15 input / $0.5 output per 1M tokens · **Modes:** sync

GLM-5.3-Flash is the first native multimodal model in Z.ai's GLM-5 series, a 320B-parameter mixture-of-experts model with 18B active parameters that combines sparse and linear attention to cut long-context compute and KV cache. Vision is built into its coding loop, letting it inspect rendered interfaces and GUI feedback for frontend, game and computer-use work, and it also handles office documents and financial research. Z.ai reports it outperforms GLM-5.2; GLM-5.3-FlashX serves it at higher speed.

## Pricing

- Input **$0.15** / output **$0.5** per 1M tokens (USD)
- cache read multiplier: 0.2

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "z-ai/glm-5.3-flash", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='z-ai/glm-5.3-flash', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "z-ai/glm-5.3-flash", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "z-ai/glm-5.3-flash", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/z-ai/glm-5.3-flash.json`](../../../catalog/models/z-ai/glm-5.3-flash.json) · Store page: https://www.sandbase.ai/model/z-ai/glm-5.3-flash

# Z.ai: GLM 4.5 Air API: pricing, parameters and code examples

`z-ai/glm-4.5-air` · LLM · Z-Ai · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.2 input / $1.1 output per 1M tokens · **Modes:** sync

GLM-4.5-Air is the lightweight member of Z.ai's GLM-4.5 family, a mixture-of-experts model with 106B total and 12B active parameters built as a foundation model for agent-oriented applications. It offers hybrid reasoning, with a thinking mode for complex reasoning and tool use and a non-thinking mode for instant replies, and is tuned for tool calling, web browsing, software engineering and front-end development. Choose GLM-4.5 for more capacity.

## Pricing

- Input **$0.2** / output **$1.1** per 1M tokens (USD)
- cache read multiplier: 0.15

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "z-ai/glm-4.5-air", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='z-ai/glm-4.5-air', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "z-ai/glm-4.5-air", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "z-ai/glm-4.5-air", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `reasoning`, `function_calling`
---
Machine-readable: [`catalog/models/z-ai/glm-4.5-air.json`](../../../catalog/models/z-ai/glm-4.5-air.json) · Store page: https://www.sandbase.ai/model/z-ai/glm-4.5-air

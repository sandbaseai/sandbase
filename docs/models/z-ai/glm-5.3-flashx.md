# Z.ai: GLM 5.3 FlashX

`z-ai/glm-5.3-flashx` · llm · Z-Ai

GLM-5.3-FlashX is the high-speed tier of Z.ai's GLM-5.3-Flash, documented together with Flash and delivering inference speeds of up to 200 tokens per second. It shares Flash's native multimodal design and hybrid sparse-plus-linear attention, with image, video and file input, always-on reasoning, tool calling and structured output. Pick it over standard Flash for latency-sensitive coding agents, GUI and browser tasks, and interactive chat.

## Pricing

- Input **$0.37** / output **$1.25** per 1M tokens (USD)
- cache read multiplier: 0.2432

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "z-ai/glm-5.3-flashx", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='z-ai/glm-5.3-flashx', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "z-ai/glm-5.3-flashx", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "z-ai/glm-5.3-flashx", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/z-ai/glm-5.3-flashx.json`](../../../catalog/models/z-ai/glm-5.3-flashx.json) · Store page: https://www.sandbase.ai/model/z-ai/glm-5.3-flashx

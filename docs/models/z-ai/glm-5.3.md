# Z.ai: GLM 5.3 API: pricing, parameters and code examples

`z-ai/glm-5.3` · LLM · Z-Ai · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1.4 input / $4.4 output per 1M tokens · **Modes:** sync

GLM-5.3 is Z.ai's flagship text model for complex software engineering and long-horizon agent work, built on the same base model as GLM-5.2 with all gains coming from expanded post-training. Z.ai highlights stronger agentic coding, terminal operation, and vulnerability discovery and exploitation analysis for security work. It always runs with reasoning enabled at selectable effort levels and accepts text only; choose GLM-5.3-Flash for image input or lighter, faster serving.

## Pricing

- Input **$1.4** / output **$4.4** per 1M tokens (USD)
- cache read multiplier: 0.1857

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "z-ai/glm-5.3", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='z-ai/glm-5.3', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "z-ai/glm-5.3", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "z-ai/glm-5.3", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/z-ai/glm-5.3.json`](../../../catalog/models/z-ai/glm-5.3.json) · Store page: https://www.sandbase.ai/model/z-ai/glm-5.3

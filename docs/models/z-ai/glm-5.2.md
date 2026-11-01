# Z.ai: GLM 5.2

`z-ai/glm-5.2` · llm · Z-Ai

GLM-5.2 is Z.ai's open-weight flagship text model released in June 2026 for long-horizon tasks, and the first GLM model to deliver that capability on a usable 1M-token context. Z.ai positions it for project-scale software engineering, deep debugging and full development workflows from requirements to deployable products, with steadier long-task execution and closer adherence to engineering standards. GLM-5.3 builds on the same base model with further post-training for coding.

## Pricing

- Input **$1.4** / output **$4.4** per 1M tokens (USD)
- cache read multiplier: 0.1857

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "z-ai/glm-5.2", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='z-ai/glm-5.2', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "z-ai/glm-5.2", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "z-ai/glm-5.2", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/z-ai/glm-5.2.json`](../../../catalog/models/z-ai/glm-5.2.json) · Store page: https://www.sandbase.ai/model/z-ai/glm-5.2

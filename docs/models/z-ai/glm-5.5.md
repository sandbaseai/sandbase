# Z.ai: GLM 5.5

`z-ai/glm-5.5` · llm · Z-Ai

GLM 5.5 is listed on SandBase as an upcoming model in Z.ai's GLM series and is not yet available on SandBase. As of early October 2026, Z.ai has not officially announced GLM 5.5 or published its capabilities, specifications or release date. Specifications and pricing will be confirmed at launch, once Z.ai publishes official details.

## Pricing

- Price not published.

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "z-ai/glm-5.5", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='z-ai/glm-5.5', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "z-ai/glm-5.5", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "z-ai/glm-5.5", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `reasoning`, `structured_output`, `function_calling`, `coming-soon`
---
Machine-readable: [`catalog/models/z-ai/glm-5.5.json`](../../../catalog/models/z-ai/glm-5.5.json) · Store page: https://www.sandbase.ai/model/z-ai/glm-5.5

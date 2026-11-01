# StepFun: Step 5 Preview

`stepfun/step-5-preview` · llm · Stepfun

Step 5 Preview is StepFun's flagship model for agentic work, built on a sparse Mixture-of-Experts architecture with 27B active and 600B total parameters. It accepts text, image, and video input with a 1M-token context window, and supports tool calling, structured outputs, and configurable reasoning.

It is designed for software engineering, long-horizon agent workflows, and professional knowledge tasks. As a preview release, its behavior may change before the stable version.

## Pricing

- Input **$1** / output **$2.7** per 1M tokens (USD)
- cache read multiplier: 0.05

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "stepfun/step-5-preview", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='stepfun/step-5-preview', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "stepfun/step-5-preview", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "stepfun/step-5-preview", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/stepfun/step-5-preview.json`](../../../catalog/models/stepfun/step-5-preview.json) · Store page: https://www.sandbase.ai/model/stepfun/step-5-preview

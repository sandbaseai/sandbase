# Tencent: Hy4 preview API: pricing, parameters and code examples

`tencent/hy4-preview` · LLM · Tencent · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.834 input / $2.501 output per 1M tokens · **Modes:** sync

Hy4 preview is Tencent Hunyuan's open-source preview of its Hy4 generation, a mixture-of-experts language model with 770B total and 49B active parameters and a context window exceeding 1M tokens. Tencent built it for real-world productivity: long-context software development and front-end work, office and financial analysis, game prototyping and scientific research. Tencent follows a preview-first approach, with official Hy4 releases to come after this model.

## Pricing

- Input **$0.834** / output **$2.501** per 1M tokens (USD)
- cache read multiplier: 0.0504

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent/hy4-preview", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='tencent/hy4-preview', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "tencent/hy4-preview", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "tencent/hy4-preview", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/tencent/hy4-preview.json`](../../../catalog/models/tencent/hy4-preview.json) · Store page: https://www.sandbase.ai/model/tencent/hy4-preview

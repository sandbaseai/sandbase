# Qwen: Qwen3.8 27B API: pricing, parameters and code examples

`alibaba/qwen3.8-27b` · LLM · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.5 input / $3 output per 1M tokens · **Modes:** sync

Qwen3.8 27B is the compact dense member of Alibaba's Qwen3.8 family, an open-weight native vision-language model that understands images and video, with thinking mode on by default. Compared with Qwen3.6 27B, Alibaba focuses the upgrade on coding and office tasks across text and visual inputs, aiming for more reliable end-to-end completion of complex multi-step work. It suits teams that want Qwen3.8-generation agent skills in a smaller, deployment-friendly model.

## Pricing

- Input **$0.5** / output **$3** per 1M tokens (USD)
- cache read multiplier: 0.2
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen3.8-27b", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='alibaba/qwen3.8-27b', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "alibaba/qwen3.8-27b", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "alibaba/qwen3.8-27b", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/alibaba/qwen3.8-27b.json`](../../../catalog/models/alibaba/qwen3.8-27b.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen3.8-27b

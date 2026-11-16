# Qwen: Qwen4 Max API: pricing, parameters and code examples

`alibaba/qwen4-max` · LLM · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1.666667 input / $5 output per 1M tokens · **Modes:** sync

Qwen4 Max is the flagship of Alibaba's Qwen 4 generation, released in November 2026. It is a multimodal reasoning model that takes text, images and video, with thinking on by default (reasoning_effort sets the depth), tool calling, web search and structured outputs, a 1M-token context and up to 393K output tokens shared by thinking and the answer. Alibaba positions it for coding, office work, frontend design and complex agent tasks, at a lower price than Qwen3.8 Max.

## Pricing

- Input **$1.666667** / output **$5** per 1M tokens (USD)
- cache read multiplier: 0.05
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen4-max", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='alibaba/qwen4-max', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "alibaba/qwen4-max", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "alibaba/qwen4-max", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/alibaba/qwen4-max.json`](../../../catalog/models/alibaba/qwen4-max.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen4-max

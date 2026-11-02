# Qwen: Qwen3.7 Flash API: pricing, parameters and code examples

`alibaba/qwen3.7-flash` · LLM · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 input / $0.13 output per 1M tokens · **Modes:** sync

Qwen3.7 Flash is the Flash tier of Alibaba's Qwen3.7 series, a native vision-language reasoning model that accepts text, images and video, released in July 2026. Alibaba describes it as an upgrade over Qwen3.6 Flash in multimodal understanding, object recognition, spatial perception and agent execution, with more stable search and multimodal coding agents. Choose it over Qwen3.7 Plus or Max when speed and high-volume throughput matter more than peak capability.

## Pricing

- Input **$0.03** / output **$0.13** per 1M tokens (USD)
- cache read multiplier: 0.2
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen3.7-flash", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='alibaba/qwen3.7-flash', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "alibaba/qwen3.7-flash", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "alibaba/qwen3.7-flash", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/alibaba/qwen3.7-flash.json`](../../../catalog/models/alibaba/qwen3.7-flash.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen3.7-flash

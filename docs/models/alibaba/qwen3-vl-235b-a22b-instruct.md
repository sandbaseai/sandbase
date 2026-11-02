# Qwen: Qwen3 VL 235B A22B Instruct API: pricing, parameters and code examples

`alibaba/qwen3-vl-235b-a22b-instruct` · LLM · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.4 input / $1.6 output per 1M tokens · **Modes:** sync

Qwen3-VL 235B A22B Instruct is the largest Mixture-of-Experts model in Alibaba's open-weight Qwen3-VL vision-language family, in its non-thinking Instruct edition, released in September 2025. Qwen positions it for visual agents that operate PC and mobile GUIs, generating HTML, CSS or diagrams from images and video, 2D and 3D grounding, long-video understanding and OCR in 32 languages. Choose it for direct answers; a separate Thinking edition targets multimodal STEM reasoning.

## Pricing

- Input **$0.4** / output **$1.6** per 1M tokens (USD)
- cache read multiplier: 1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen3-vl-235b-a22b-instruct", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='alibaba/qwen3-vl-235b-a22b-instruct', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "alibaba/qwen3-vl-235b-a22b-instruct", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "alibaba/qwen3-vl-235b-a22b-instruct", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/alibaba/qwen3-vl-235b-a22b-instruct.json`](../../../catalog/models/alibaba/qwen3-vl-235b-a22b-instruct.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen3-vl-235b-a22b-instruct

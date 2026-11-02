# Qwen: Qwen3 VL 30B A3B Instruct API: pricing, parameters and code examples

`alibaba/qwen3-vl-30b-a3b-instruct` · LLM · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.13 input / $0.52 output per 1M tokens · **Modes:** sync

Qwen3-VL 30B A3B Instruct is the mid-size Mixture-of-Experts, non-thinking edition of Alibaba's open-weight Qwen3-VL vision-language family, activating about 3 billion parameters per token. Alibaba positions it for fast responses with upgraded image and video understanding, long videos and documents, spatial awareness, object recognition, multilingual OCR and visual agents that operate GUIs. It sits between Qwen3-VL 8B and 235B A22B in size and capability.

## Pricing

- Input **$0.13** / output **$0.52** per 1M tokens (USD)

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen3-vl-30b-a3b-instruct", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='alibaba/qwen3-vl-30b-a3b-instruct', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "alibaba/qwen3-vl-30b-a3b-instruct", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "alibaba/qwen3-vl-30b-a3b-instruct", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/alibaba/qwen3-vl-30b-a3b-instruct.json`](../../../catalog/models/alibaba/qwen3-vl-30b-a3b-instruct.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen3-vl-30b-a3b-instruct

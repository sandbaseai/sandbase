# Qwen: Qwen3 VL 8B Instruct API: pricing, parameters and code examples

`alibaba/qwen3-vl-8b-instruct` · LLM · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.18 input / $0.7 output per 1M tokens · **Modes:** sync

Qwen3-VL 8B Instruct is the 8-billion-parameter dense, non-thinking edition of Alibaba's open-weight Qwen3-VL vision-language family. Alibaba notes it needs less GPU memory while keeping the series' upgraded image and video understanding, long-document and long-video handling, spatial awareness, object recognition, multilingual OCR and GUI agent abilities. Pick it for lighter multimodal deployments; the 30B A3B and 235B A22B models trade size for more capability.

## Pricing

- Input **$0.18** / output **$0.7** per 1M tokens (USD)

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen3-vl-8b-instruct", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='alibaba/qwen3-vl-8b-instruct', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "alibaba/qwen3-vl-8b-instruct", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "alibaba/qwen3-vl-8b-instruct", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/alibaba/qwen3-vl-8b-instruct.json`](../../../catalog/models/alibaba/qwen3-vl-8b-instruct.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen3-vl-8b-instruct

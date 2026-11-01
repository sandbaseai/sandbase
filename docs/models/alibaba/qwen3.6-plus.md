# Qwen: Qwen3.6 Plus

`alibaba/qwen3.6-plus` · llm · Alibaba

Qwen3.6 Plus is the Plus tier of Alibaba's Qwen3.6 series, a hosted native vision-language reasoning model released in April 2026. Alibaba reports marked gains over the Qwen3.5 series in agentic coding, front-end development and vibe coding, along with multimodal object recognition, OCR and object localization. Model Studio now lists it as a legacy model, with Qwen3.7 Plus as the recommended Plus-tier option, so it fits workloads already validated on this version.

## Pricing

- Input **$0.5** / output **$3** per 1M tokens (USD)
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen3.6-plus", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='alibaba/qwen3.6-plus', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "alibaba/qwen3.6-plus", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "alibaba/qwen3.6-plus", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/alibaba/qwen3.6-plus.json`](../../../catalog/models/alibaba/qwen3.6-plus.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen3.6-plus

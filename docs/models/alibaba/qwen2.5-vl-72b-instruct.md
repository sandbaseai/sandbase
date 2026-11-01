# Qwen: Qwen2.5 VL 72B Instruct

`alibaba/qwen2.5-vl-72b-instruct` · llm · Alibaba

Qwen2.5-VL 72B Instruct is the largest instruction-tuned model in Alibaba's open-weight Qwen2.5-VL vision-language family, released in early 2025. Qwen highlights recognition of common objects and analysis of text, charts, icons and layouts in images, visual localization with bounding boxes or points, structured extraction from invoices, forms and tables, visual agent use and understanding of videos over an hour long. It predates the Qwen3-VL line and suits workloads validated on it.

## Pricing

- Input **$0.25** / output **$0.75** per 1M tokens (USD)

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen2.5-vl-72b-instruct", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='alibaba/qwen2.5-vl-72b-instruct', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "alibaba/qwen2.5-vl-72b-instruct", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "alibaba/qwen2.5-vl-72b-instruct", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `structured_output`
---
Machine-readable: [`catalog/models/alibaba/qwen2.5-vl-72b-instruct.json`](../../../catalog/models/alibaba/qwen2.5-vl-72b-instruct.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen2.5-vl-72b-instruct

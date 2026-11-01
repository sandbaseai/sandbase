# Qwen: Qwen3.8 Max (0902)

`alibaba/qwen3.8-max-0902` · llm · Alibaba

Qwen3.8 Max (0902) is the pinned snapshot of Alibaba's Qwen3.8 Max dated September 2, 2026, intended for workloads that need a fixed version. Alibaba describes it as an upgraded snapshot with stronger engineering-scale coding and long-horizon autonomous development, steadier multi-tool orchestration and end-to-end task delivery, and refined chart reasoning, document parsing and multimodal perception. It keeps the flagship's vision input, thinking mode and full tool support.

## Pricing

- Input **$2** / output **$6** per 1M tokens (USD)
- cache read multiplier: 0.125
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen3.8-max-0902", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='alibaba/qwen3.8-max-0902', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "alibaba/qwen3.8-max-0902", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "alibaba/qwen3.8-max-0902", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/alibaba/qwen3.8-max-0902.json`](../../../catalog/models/alibaba/qwen3.8-max-0902.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen3.8-max-0902

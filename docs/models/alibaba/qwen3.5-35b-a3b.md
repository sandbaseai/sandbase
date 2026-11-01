# Qwen: Qwen3.5-35B-A3B

`alibaba/qwen3.5-35b-a3b` · llm · Alibaba

Qwen3.5 35B A3B is an open-weight native vision-language model from Alibaba's Qwen3.5 series, released in February 2026, pairing linear attention with a sparse Mixture-of-Experts design that activates about 3 billion of its 35 billion parameters. Alibaba describes its overall performance as comparable to Qwen3.5 27B with higher inference efficiency. It supports thinking mode, tool calling and image and video understanding, and is the open-weight counterpart of the hosted Qwen3.5 Flash.

## Pricing

- Input **$0.25** / output **$2** per 1M tokens (USD)
- cache read multiplier: 1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen3.5-35b-a3b", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='alibaba/qwen3.5-35b-a3b', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "alibaba/qwen3.5-35b-a3b", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "alibaba/qwen3.5-35b-a3b", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/alibaba/qwen3.5-35b-a3b.json`](../../../catalog/models/alibaba/qwen3.5-35b-a3b.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen3.5-35b-a3b

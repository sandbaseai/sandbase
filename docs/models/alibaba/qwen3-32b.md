# Qwen: Qwen3 32B

`alibaba/qwen3-32b` · llm · Alibaba

Qwen3 32B is the largest dense model in Alibaba's open-weight Qwen3 family, released in April 2025 with 32.8 billion parameters. One model switches between a thinking mode for complex logic, math and coding and a non-thinking mode for fast general dialogue. Qwen highlights tool integration in both modes, creative writing, role-play, multi-turn conversation and support for more than 100 languages and dialects. It suits text workloads that want a mid-size open model with optional reasoning.

## Pricing

- Input **$0.16** / output **$0.64** per 1M tokens (USD)

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen3-32b", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='alibaba/qwen3-32b', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "alibaba/qwen3-32b", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "alibaba/qwen3-32b", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/alibaba/qwen3-32b.json`](../../../catalog/models/alibaba/qwen3-32b.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen3-32b

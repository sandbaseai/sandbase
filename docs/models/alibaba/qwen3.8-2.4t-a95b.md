# Qwen: Qwen3.8 2.4T A95B API: pricing, parameters and code examples

`alibaba/qwen3.8-2.4t-a95b` · LLM · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $2 input / $6 output per 1M tokens · **Modes:** sync

Qwen3.8 2.4T A95B is the open-weight release of Alibaba's Qwen3.8 Max-class model, a sparse Mixture-of-Experts with 2.4 trillion total and about 95 billion active parameters, published in August 2026 as the first Qwen-Max-class open model. It targets coding, professional work, research and long-horizon agentic tasks, with tunable reasoning depth. Alibaba's hosted Qwen3.8 Max builds on it and adds vision input, a non-thinking mode and official built-in tools.

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
  -d '{"model": "alibaba/qwen3.8-2.4t-a95b", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='alibaba/qwen3.8-2.4t-a95b', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "alibaba/qwen3.8-2.4t-a95b", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "alibaba/qwen3.8-2.4t-a95b", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/alibaba/qwen3.8-2.4t-a95b.json`](../../../catalog/models/alibaba/qwen3.8-2.4t-a95b.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen3.8-2.4t-a95b

# Qwen: Qwen3.7 Max

`alibaba/qwen3.7-max` · llm · Alibaba

Qwen3.7 Max is the largest and most capable model in Alibaba's Qwen3.7 series as of its May 2026 release, a reasoning model built for agent-centric work and offered here with text input and output. Alibaba highlights its strengths in programming, office and productivity tasks, and long-running autonomous execution. Model Studio now lists the Qwen3.7 line as legacy and recommends Qwen3.8 Max for the strongest reasoning, so it fits workloads already validated on Qwen3.7 Max.

## Pricing

- Input **$2.5** / output **$7.5** per 1M tokens (USD)
- cache read multiplier: 0.2
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen3.7-max", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='alibaba/qwen3.7-max', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "alibaba/qwen3.7-max", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "alibaba/qwen3.7-max", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/alibaba/qwen3.7-max.json`](../../../catalog/models/alibaba/qwen3.7-max.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen3.7-max

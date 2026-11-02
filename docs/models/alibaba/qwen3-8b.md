# Qwen: Qwen3 8B API: pricing, parameters and code examples

`alibaba/qwen3-8b` · LLM · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.18 input / $0.7 output per 1M tokens · **Modes:** sync

Qwen3 8B is a compact dense model in Alibaba's open-weight Qwen3 family, released in April 2025 with 8.2 billion parameters. Like its siblings, it switches between a thinking mode for math, coding and logical reasoning and a non-thinking mode for efficient dialogue, with tool use in both modes and coverage of more than 100 languages and dialects. Choose it for lightweight text reasoning and chat where Qwen3 32B is more than the task needs.

## Pricing

- Input **$0.18** / output **$0.7** per 1M tokens (USD)
- cache read multiplier: 1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen3-8b", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='alibaba/qwen3-8b', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "alibaba/qwen3-8b", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "alibaba/qwen3-8b", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/alibaba/qwen3-8b.json`](../../../catalog/models/alibaba/qwen3-8b.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen3-8b

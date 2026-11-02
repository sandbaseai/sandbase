# Qwen: Qwen3.6 27B API: pricing, parameters and code examples

`alibaba/qwen3.6-27b` · LLM · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.6 input / $3.6 output per 1M tokens · **Modes:** sync

Qwen3.6 27B is an open-weight dense 27-billion-parameter vision-language model in Alibaba's Qwen3.6 family, released in April 2026 with thinking and non-thinking modes. Qwen positions it for agentic coding, including front-end workflows and repository-level reasoning, plus STEM reasoning, spatial understanding, object localization, document OCR and video understanding. Its dense design is simple to deploy, and it can retain reasoning context across turns for iterative development.

## Pricing

- Input **$0.6** / output **$3.6** per 1M tokens (USD)

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen3.6-27b", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='alibaba/qwen3.6-27b', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "alibaba/qwen3.6-27b", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "alibaba/qwen3.6-27b", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/alibaba/qwen3.6-27b.json`](../../../catalog/models/alibaba/qwen3.6-27b.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen3.6-27b

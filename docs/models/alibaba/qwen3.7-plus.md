# Qwen: Qwen3.7 Plus API: pricing, parameters and code examples

`alibaba/qwen3.7-plus` · LLM · Alibaba · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.4 input / $1.6 output per 1M tokens · **Modes:** sync

Qwen3.7 Plus is the balanced Plus tier of Alibaba's Qwen3.7 series, a reasoning model with text and image input released in June 2026. Alibaba highlights its multimodal hybrid agent abilities: perceiving real-world scenes, reading screens and operating GUIs, generating code from visual references and navigating mobile apps end to end, alongside coding, tool use and productivity work. Model Studio recommends it as its default for general and coding workloads, with Qwen3.8 Max for harder reasoning.

## Pricing

- Input **$0.4** / output **$1.6** per 1M tokens (USD)
- cache read multiplier: 0.2
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen3.7-plus", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='alibaba/qwen3.7-plus', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "alibaba/qwen3.7-plus", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "alibaba/qwen3.7-plus", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/alibaba/qwen3.7-plus.json`](../../../catalog/models/alibaba/qwen3.7-plus.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen3.7-plus

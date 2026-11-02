# DeepSeek: DeepSeek V4 Flash Vision Exp (Experimental) API: pricing, parameters and code examples

`deepseek/deepseek-v4-flash-vision-exp` · LLM · DeepSeek · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.3 input / $1.2 output per 1M tokens · **Modes:** sync

DeepSeek V4 Flash Vision Exp is an experimental multimodal understanding model that accepts mixed text and image input and produces text output. It supports OpenAI-compatible image URL and base64 data URL content parts while retaining the text, reasoning, tool-calling, and JSON-output capabilities of DeepSeek V4 Flash.

## Pricing

- Input **$0.3** / output **$1.2** per 1M tokens (USD)
- cache read multiplier: 0.02

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "deepseek/deepseek-v4-flash-vision-exp", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='deepseek/deepseek-v4-flash-vision-exp', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "deepseek/deepseek-v4-flash-vision-exp", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "deepseek/deepseek-v4-flash-vision-exp", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/deepseek/deepseek-v4-flash-vision-exp.json`](../../../catalog/models/deepseek/deepseek-v4-flash-vision-exp.json) · Store page: https://www.sandbase.ai/model/deepseek/deepseek-v4-flash-vision-exp

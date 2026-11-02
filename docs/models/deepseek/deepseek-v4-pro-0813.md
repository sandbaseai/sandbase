# DeepSeek: DeepSeek V4 Pro 0813 API: pricing, parameters and code examples

`deepseek/deepseek-v4-pro-0813` · LLM · DeepSeek · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1.32 input / $3.96 output per 1M tokens · **Modes:** sync

DeepSeek V4 Pro 0813 is the pinned GA release of DeepSeek V4 Pro from August 2026, for workloads that need a fixed version. It keeps V4 Pro's 1.6T-parameter mixture-of-experts design and 1M-token context, with thinking and non-thinking modes, tool calls and JSON output, and DeepSeek reports much stronger agent performance than the April preview, especially in production. DeepSeek has said it will keep serving V4 Pro alongside V4.1 Flash.

## Pricing

- Input **$1.32** / output **$3.96** per 1M tokens (USD)
- cache read multiplier: 0.0333

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "deepseek/deepseek-v4-pro-0813", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='deepseek/deepseek-v4-pro-0813', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "deepseek/deepseek-v4-pro-0813", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "deepseek/deepseek-v4-pro-0813", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/deepseek/deepseek-v4-pro-0813.json`](../../../catalog/models/deepseek/deepseek-v4-pro-0813.json) · Store page: https://www.sandbase.ai/model/deepseek/deepseek-v4-pro-0813

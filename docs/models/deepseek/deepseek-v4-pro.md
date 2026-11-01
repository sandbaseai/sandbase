# DeepSeek: DeepSeek V4 Pro

`deepseek/deepseek-v4-pro` · llm · DeepSeek

DeepSeek V4 Pro is the large tier of DeepSeek's V4 family, a 1.6T-parameter mixture-of-experts model with 49B active parameters, introduced as an open-weight preview in April 2026 with a 1M-token context. It combines token-wise compression with DeepSeek Sparse Attention and supports thinking and non-thinking modes, aimed at agentic coding, advanced reasoning and knowledge-heavy work. On DeepSeek's API this name now serves the August 2026 GA revision; use the 0813 entry to pin that version.

## Pricing

- Input **$1.32** / output **$3.96** per 1M tokens (USD)
- cache read multiplier: 0.0333

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "deepseek/deepseek-v4-pro", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='deepseek/deepseek-v4-pro', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "deepseek/deepseek-v4-pro", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "deepseek/deepseek-v4-pro", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/deepseek/deepseek-v4-pro.json`](../../../catalog/models/deepseek/deepseek-v4-pro.json) · Store page: https://www.sandbase.ai/model/deepseek/deepseek-v4-pro

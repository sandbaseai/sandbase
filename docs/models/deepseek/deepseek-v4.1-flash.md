# DeepSeek: DeepSeek V4.1 Flash

`deepseek/deepseek-v4.1-flash` · llm · DeepSeek

DeepSeek V4.1 Flash is the smallest model in DeepSeek's V4.1 architecture family, released in September 2026 with native visual understanding. It is a 552B-parameter mixture-of-experts model using a Causal Encoder-Decoder design that activates 8B parameters for input and 16B for output, with a KV cache about a quarter the size of the previous Flash generation. DeepSeek positions it for agentic coding and long-context work and reports it ahead of V4 Pro, replacing V4 Flash and V4 Flash Vision Exp on its API.

## Pricing

- Input **$0.3** / output **$1.2** per 1M tokens (USD)
- cache read multiplier: 0.02

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "deepseek/deepseek-v4.1-flash", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='deepseek/deepseek-v4.1-flash', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "deepseek/deepseek-v4.1-flash", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "deepseek/deepseek-v4.1-flash", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/deepseek/deepseek-v4.1-flash.json`](../../../catalog/models/deepseek/deepseek-v4.1-flash.json) · Store page: https://www.sandbase.ai/model/deepseek/deepseek-v4.1-flash

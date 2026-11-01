# DeepSeek: DeepSeek V4 Flash

`deepseek/deepseek-v4-flash` · llm · DeepSeek

DeepSeek V4 Flash is an efficiency-optimized Mixture-of-Experts model from DeepSeek with 284B total parameters and 13B activated parameters, supporting a 1M-token context window. It is designed for fast inference and high-throughput workloads, while maintaining strong reasoning and coding performance.

The model includes hybrid attention for efficient long-context processing. Reasoning efforts `high` and `xhigh` are supported; `xhigh` maps to max reasoning. It is well suited for applications such as coding assistants, chat systems, and agent workflows where responsiveness and cost efficiency are important.

## Pricing

- Input **$0.3** / output **$1.2** per 1M tokens (USD)
- cache read multiplier: 0.02

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "deepseek/deepseek-v4-flash", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='deepseek/deepseek-v4-flash', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "deepseek/deepseek-v4-flash", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "deepseek/deepseek-v4-flash", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/deepseek/deepseek-v4-flash.json`](../../../catalog/models/deepseek/deepseek-v4-flash.json) · Store page: https://www.sandbase.ai/model/deepseek/deepseek-v4-flash

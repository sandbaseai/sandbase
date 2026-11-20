# Tencent: Hy4 flash API: pricing, parameters and code examples

`tencent/hy4-flash` · LLM · Tencent · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.07 input / $0.281 output per 1M tokens · **Modes:** sync

Hy4 flash is the cost-efficient tier of Tencent Hunyuan's Hy4 family, with roughly a quarter of the flagship's parameters for lower latency and cost. It accepts text and image input, has a context window of about 1M tokens, and supports reasoning, tool calling and structured output. It targets code assistance, agent workflows and high-volume tasks where Hy4's full depth is not needed.

## Pricing

- Input **$0.07** / output **$0.281** per 1M tokens (USD)
- cache read multiplier: 0.0429

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent/hy4-flash", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='tencent/hy4-flash', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "tencent/hy4-flash", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "tencent/hy4-flash", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/tencent/hy4-flash.json`](../../../catalog/models/tencent/hy4-flash.json) · Store page: https://www.sandbase.ai/model/tencent/hy4-flash

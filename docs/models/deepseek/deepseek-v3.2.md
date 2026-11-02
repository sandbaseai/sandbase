# DeepSeek: DeepSeek V3.2 API: pricing, parameters and code examples

`deepseek/deepseek-v3.2` · LLM · DeepSeek · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.252 input / $0.378 output per 1M tokens · **Modes:** sync

DeepSeek-V3.2 is DeepSeek's open-weight, reasoning-first model released in December 2025 as the official successor to V3.2-Exp. It introduces DeepSeek Sparse Attention to reduce long-context training and inference compute and is DeepSeek's first model to integrate thinking directly into tool use, trained on agent data synthesized across more than 1,800 environments. It supports tool calling in both thinking and non-thinking modes, suiting agents and general reasoning.

## Pricing

- Input **$0.252** / output **$0.378** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "deepseek/deepseek-v3.2", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='deepseek/deepseek-v3.2', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "deepseek/deepseek-v3.2", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "deepseek/deepseek-v3.2", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/deepseek/deepseek-v3.2.json`](../../../catalog/models/deepseek/deepseek-v3.2.json) · Store page: https://www.sandbase.ai/model/deepseek/deepseek-v3.2

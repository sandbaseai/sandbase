# MiniMax: MiniMax M2.5

`minimax/minimax-m2.5` · llm · Minimax

MiniMax-M2.5 is a MiniMax M2-series language model released in February 2026 for real-world productivity, trained with reinforcement learning across hundreds of thousands of complex real-world environments. MiniMax highlights coding across more than ten languages and the full development lifecycle, planning projects like a software architect before writing code, plus agentic search, tool use and office work. MiniMax now lists it as a legacy model behind M2.7 and M3.

## Pricing

- Input **$0.3** / output **$1.2** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/minimax-m2.5", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='minimax/minimax-m2.5', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "minimax/minimax-m2.5", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "minimax/minimax-m2.5", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/minimax/minimax-m2.5.json`](../../../catalog/models/minimax/minimax-m2.5.json) · Store page: https://www.sandbase.ai/model/minimax/minimax-m2.5

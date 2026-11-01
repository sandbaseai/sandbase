# MiniMax: MiniMax M2.7

`minimax/minimax-m2.7` · llm · Minimax

MiniMax-M2.7 is a MiniMax M2-series language model that MiniMax describes as its first model to take part in its own development, building agent harnesses, skills and memory for reinforcement learning experiments. It is positioned for end-to-end software engineering including log analysis, bug troubleshooting and code security, high-fidelity editing in Excel, PowerPoint and Word, and character-consistent interaction. A faster highspeed variant exists, and MiniMax-M3 adds multimodality and longer context.

## Pricing

- Input **$0.3** / output **$1.2** per 1M tokens (USD)
- cache read multiplier: 0.2

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/minimax-m2.7", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='minimax/minimax-m2.7', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "minimax/minimax-m2.7", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "minimax/minimax-m2.7", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/minimax/minimax-m2.7.json`](../../../catalog/models/minimax/minimax-m2.7.json) · Store page: https://www.sandbase.ai/model/minimax/minimax-m2.7

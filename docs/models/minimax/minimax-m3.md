# MiniMax: MiniMax M3

`minimax/minimax-m3` · llm · Minimax

MiniMax-M3 is MiniMax's flagship multimodal foundation model, which MiniMax describes as open-weight. It is built on MiniMax Sparse Attention, which selects key-value blocks to cut long-context compute and supports up to a 1M-token context, and it was trained natively on text and visual data for image and video understanding. MiniMax positions it for long-horizon coding, agentic tool use and autonomous multi-step work such as research paper reproduction and GPU kernel optimization.

## Pricing

- Input **$0.3** / output **$1.2** per 1M tokens (USD)
- cache read multiplier: 0.2

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "minimax/minimax-m3", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='minimax/minimax-m3', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "minimax/minimax-m3", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "minimax/minimax-m3", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/minimax/minimax-m3.json`](../../../catalog/models/minimax/minimax-m3.json) · Store page: https://www.sandbase.ai/model/minimax/minimax-m3

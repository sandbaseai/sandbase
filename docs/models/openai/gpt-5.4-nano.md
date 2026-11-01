# OpenAI: GPT-5.4 Nano

`openai/gpt-5.4-nano` · llm · OpenAI

GPT-5.4 nano is the smallest and fastest tier of OpenAI's GPT-5.4 family, released in March 2026 with text and image input and text output. OpenAI recommends it for tasks where speed matters most, such as classification, data extraction, ranking and coding subagents that handle simpler supporting work. Choose it for high-volume pipelines; unlike GPT-5.4 mini, it does not support the computer use or tool search tools.

## Pricing

- Input **$0.2** / output **$1.25** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-5.4-nano", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-5.4-nano', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-5.4-nano", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-5.4-nano", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-5.4-nano.json`](../../../catalog/models/openai/gpt-5.4-nano.json) · Store page: https://www.sandbase.ai/model/openai/gpt-5.4-nano

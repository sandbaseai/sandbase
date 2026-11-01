# OpenAI: GPT-5.6 Terra

`openai/gpt-5.6-terra` · llm · OpenAI

GPT-5.6 Terra is the middle tier of OpenAI's GPT-5.6 reasoning family, with text and image input, and is described by OpenAI as a balanced model for everyday work; it roughly corresponds to the mini tier of earlier GPT-5 families. It suits day-to-day coding, analysis and agentic tasks that need solid reasoning without flagship-level depth. Choose GPT-5.6 Sol for the most demanding work, GPT-5.6 Luna for the highest-volume tasks, or Terra Pro for hard individual requests.

## Pricing

- Input **$2** / output **$12** per 1M tokens (USD)
- cache read multiplier: 0.1
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-5.6-terra", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-5.6-terra', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-5.6-terra", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-5.6-terra", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-5.6-terra.json`](../../../catalog/models/openai/gpt-5.6-terra.json) · Store page: https://www.sandbase.ai/model/openai/gpt-5.6-terra

# OpenAI: GPT-6 Luna

`openai/gpt-6-luna` · llm · OpenAI

GPT-6 Luna is the smallest, fastest tier of OpenAI's GPT-6 reasoning family, described by OpenAI as its most efficient model for focused, high-volume tasks, with text and image input. It was trained with methods similar to GPT-6 Astra to carry much of that model's strengths into a faster tier. Choose it for high-throughput chat, extraction and lightweight agent steps, and move to GPT-6.1 Sol or GPT-6 Astra when work needs deeper reasoning.

## Pricing

- Input **$0.1** / output **$0.5** per 1M tokens (USD)
- cache read multiplier: 0.1
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-6-luna", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-6-luna', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-6-luna", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-6-luna", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-6-luna.json`](../../../catalog/models/openai/gpt-6-luna.json) · Store page: https://www.sandbase.ai/model/openai/gpt-6-luna

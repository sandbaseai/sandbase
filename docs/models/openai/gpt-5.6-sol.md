# OpenAI: GPT-5.6 Sol API: pricing, parameters and code examples

`openai/gpt-5.6-sol` · LLM · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $4 input / $20 output per 1M tokens · **Modes:** sync

GPT-5.6 Sol is the flagship tier of OpenAI's GPT-5.6 reasoning family, accepting text and image input; OpenAI says it roughly corresponds to the unsuffixed tier of earlier GPT-5 families, and the plain GPT-5.6 name routes to it. OpenAI positions it for complex professional work, including coding, knowledge work, cybersecurity and science. Pick it over GPT-5.6 Terra or Luna when tasks need the most capability in this family, or the Sol Pro variant for the hardest requests.

## Pricing

- Input **$4** / output **$20** per 1M tokens (USD)
- cache read multiplier: 0.1
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-5.6-sol", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-5.6-sol', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-5.6-sol", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-5.6-sol", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-5.6-sol.json`](../../../catalog/models/openai/gpt-5.6-sol.json) · Store page: https://www.sandbase.ai/model/openai/gpt-5.6-sol

# OpenAI: GPT-5.4 Mini

`openai/gpt-5.4-mini` · llm · OpenAI

GPT-5.4 mini is the smaller, faster tier of OpenAI's GPT-5.4 family, released in March 2026 with text and image input and text output. OpenAI describes it as its strongest mini model at release for coding, computer use and subagents, bringing much of GPT-5.4's capability to high-volume workloads at more than twice the speed of GPT-5 mini. Pick it over full GPT-5.4 for responsive coding assistants and agent fleets, and over nano when tasks need computer use.

## Pricing

- Input **$0.75** / output **$4.5** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-5.4-mini", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-5.4-mini', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-5.4-mini", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-5.4-mini", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-5.4-mini.json`](../../../catalog/models/openai/gpt-5.4-mini.json) · Store page: https://www.sandbase.ai/model/openai/gpt-5.4-mini

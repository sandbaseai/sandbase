# OpenAI: GPT-5.2 API: pricing, parameters and code examples

`openai/gpt-5.2` · LLM · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1.75 input / $14 output per 1M tokens · **Modes:** sync

GPT-5.2 is OpenAI's GPT-5 series flagship released in December 2025, positioned by OpenAI for complex professional work and long-running agents, with text and image input and text output. It offers configurable reasoning effort from none up to an extra-high setting, and OpenAI highlights its performance on well-specified knowledge work across dozens of occupations alongside coding and tool use. OpenAI now calls it a previous flagship, with GPT-5.4 following it.

## Pricing

- Input **$1.75** / output **$14** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-5.2", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-5.2', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-5.2", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-5.2", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-5.2.json`](../../../catalog/models/openai/gpt-5.2.json) · Store page: https://www.sandbase.ai/model/openai/gpt-5.2

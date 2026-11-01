# OpenAI: GPT-5.4

`openai/gpt-5.4` · llm · OpenAI

GPT-5.4 is OpenAI's flagship GPT-5.4 reasoning model for complex professional work, released in March 2026 with text and image input, text output and a context window of about 1.05M tokens. OpenAI positions it for coding, professional knowledge work and multi-step agent workflows, with configurable reasoning effort and broad tool support including web search, code interpreter, computer use and MCP. Choose it over GPT-5.4 mini or nano when task depth matters more than speed.

## Pricing

- Input **$2.5** / output **$15** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-5.4", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-5.4', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-5.4", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-5.4", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-5.4.json`](../../../catalog/models/openai/gpt-5.4.json) · Store page: https://www.sandbase.ai/model/openai/gpt-5.4

# OpenAI: GPT-4.1

`openai/gpt-4.1` · llm · OpenAI

GPT-4.1 is OpenAI's flagship non-reasoning model in the GPT-4.1 series, released in April 2025 alongside GPT-4.1 mini and nano, with text and image input and text output. OpenAI positions it for instruction following, tool calling and coding, with improved long-context comprehension across its 1M-token window and low latency because it skips a separate reasoning step. Pick it over the mini and nano tiers when output quality matters more than speed; OpenAI suggests GPT-5-class models for the most complex tasks.

## Pricing

- Input **$2** / output **$8** per 1M tokens (USD)
- cache read multiplier: 0.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-4.1", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-4.1', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-4.1", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-4.1", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-4.1.json`](../../../catalog/models/openai/gpt-4.1.json) · Store page: https://www.sandbase.ai/model/openai/gpt-4.1

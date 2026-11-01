# OpenAI: GPT-4.1 Nano

`openai/gpt-4.1-nano` · llm · OpenAI

GPT-4.1 nano is the fastest and smallest tier of OpenAI's GPT-4.1 series, released in April 2025 as a non-reasoning model with text and image input and text output. It keeps the 1M-token context window and the instruction-following and tool-calling focus of its siblings, and OpenAI points to low-latency tasks such as classification and autocompletion. Choose it for high-volume, simple workloads; GPT-4.1 mini or GPT-4.1 handle harder prompts better.

## Pricing

- Input **$0.1** / output **$0.4** per 1M tokens (USD)
- cache read multiplier: 0.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-4.1-nano", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-4.1-nano', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-4.1-nano", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-4.1-nano", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-4.1-nano.json`](../../../catalog/models/openai/gpt-4.1-nano.json) · Store page: https://www.sandbase.ai/model/openai/gpt-4.1-nano

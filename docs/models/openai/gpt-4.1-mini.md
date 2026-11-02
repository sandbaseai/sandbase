# OpenAI: GPT-4.1 Mini API: pricing, parameters and code examples

`openai/gpt-4.1-mini` · LLM · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.4 input / $1.6 output per 1M tokens · **Modes:** sync

GPT-4.1 mini is the smaller, faster tier of OpenAI's GPT-4.1 series, released in April 2025 as a non-reasoning model that accepts text and images and returns text. OpenAI describes it as strong at instruction following and tool calling, with the same 1M-token context window as GPT-4.1 and lower latency. It suits interactive apps, chat and agent tool calls where responsiveness matters more than the extra depth of full GPT-4.1.

## Pricing

- Input **$0.4** / output **$1.6** per 1M tokens (USD)
- cache read multiplier: 0.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-4.1-mini", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-4.1-mini', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-4.1-mini", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-4.1-mini", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-4.1-mini.json`](../../../catalog/models/openai/gpt-4.1-mini.json) · Store page: https://www.sandbase.ai/model/openai/gpt-4.1-mini

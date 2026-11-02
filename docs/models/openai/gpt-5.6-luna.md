# OpenAI: GPT-5.6 Luna API: pricing, parameters and code examples

`openai/gpt-5.6-luna` · LLM · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.2 input / $1.2 output per 1M tokens · **Modes:** sync

GPT-5.6 Luna is the smallest, fastest tier of OpenAI's GPT-5.6 reasoning family, with text and image input; OpenAI says it roughly corresponds to the nano tier of earlier GPT-5 families. It is designed for high-volume workloads such as classification, extraction, routing, chat and lightweight agent steps where throughput and latency matter. Pick GPT-5.6 Terra or GPT-5.6 Sol when tasks need more capability, and the pro variant when a hard request needs more reasoning work.

## Pricing

- Input **$0.2** / output **$1.2** per 1M tokens (USD)
- cache read multiplier: 0.1
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-5.6-luna", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-5.6-luna', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-5.6-luna", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-5.6-luna", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-5.6-luna.json`](../../../catalog/models/openai/gpt-5.6-luna.json) · Store page: https://www.sandbase.ai/model/openai/gpt-5.6-luna

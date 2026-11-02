# OpenAI: GPT-5.5 API: pricing, parameters and code examples

`openai/gpt-5.5` · LLM · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $5 input / $30 output per 1M tokens · **Modes:** sync

GPT-5.5 is an OpenAI flagship reasoning model with text and image input, made available in the API in April 2026 and described by OpenAI as built for complex professional work. OpenAI positions it for writing and debugging code, online research, data analysis, creating documents and spreadsheets, and operating software across tools until a task is done. It succeeds GPT-5.4 at similar per-token latency, and a pinned snapshot dated 2026-04-23 is available for fixed-version workloads.

## Pricing

- Input **$5** / output **$30** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-5.5", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-5.5', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-5.5", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-5.5", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-5.5.json`](../../../catalog/models/openai/gpt-5.5.json) · Store page: https://www.sandbase.ai/model/openai/gpt-5.5

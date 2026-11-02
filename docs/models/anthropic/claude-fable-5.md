# Anthropic: Claude Fable 5 API: pricing, parameters and code examples

`anthropic/claude-fable-5` · LLM · Anthropic · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $10 input / $50 output per 1M tokens · **Modes:** sync

Claude Fable 5 is a Mythos-class model from Anthropic, built for autonomous knowledge work and coding. It supports text, image, and file inputs with text output, with reasoning support and a 1M-token context window. It is suited for long-running, complex, and asynchronous tasks that previously required frequent human check-ins.

It is particularly strong at end-to-end work that would otherwise take a person hours, days, or weeks - taking on problems that are long-running, ambiguous, or highly multi-step. It executes well-scoped tasks with few mistakes, automatically self-correcting through verification loops, and ships with robust safeguards.

## Pricing

- Input **$10** / output **$50** per 1M tokens (USD)
- cache read multiplier: 0.1
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "anthropic/claude-fable-5", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='anthropic/claude-fable-5', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "anthropic/claude-fable-5", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "anthropic/claude-fable-5", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/anthropic/claude-fable-5.json`](../../../catalog/models/anthropic/claude-fable-5.json) · Store page: https://www.sandbase.ai/model/anthropic/claude-fable-5

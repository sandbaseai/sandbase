# Anthropic: Claude Opus 4.6

`anthropic/claude-opus-4.6` · llm · Anthropic

Opus 4.6 is Anthropic’s strongest model for coding and long-running professional tasks. It is built for agents that operate across entire workflows rather than single prompts, making it especially effective for large codebases, complex refactors, and multi-step debugging that unfolds over time. The model shows deeper contextual understanding, stronger problem decomposition, and greater reliability on hard engineering tasks than prior generations.

Beyond coding, Opus 4.6 excels at sustained knowledge work. It produces near-production-ready documents, plans, and analyses in a single pass, and maintains coherence across very long outputs and extended sessions. This makes it a strong default for tasks that require persistence, judgment, and follow-through, such as technical design, migration planning, and end-to-end project execution.

## Pricing

- Input **$5** / output **$25** per 1M tokens (USD)
- cache read multiplier: 0.1
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "anthropic/claude-opus-4.6", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='anthropic/claude-opus-4.6', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "anthropic/claude-opus-4.6", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "anthropic/claude-opus-4.6", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/anthropic/claude-opus-4.6.json`](../../../catalog/models/anthropic/claude-opus-4.6.json) · Store page: https://www.sandbase.ai/model/anthropic/claude-opus-4.6

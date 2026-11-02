# Anthropic: Claude Haiku 5.5 API: pricing, parameters and code examples

`anthropic/claude-haiku-5.5` · LLM · Anthropic · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.1 input / $0.5 output per 1M tokens · **Modes:** sync

Claude Haiku 5.5 is Anthropic's small, fast model for high-volume, cost-sensitive work such as summarization, classification, compaction, subagents, and browser use. It succeeds Claude Haiku 4.5 with stronger coding, computer use, and knowledge work, adds an adjustable effort setting, and accepts text, image, and file input with a 1M-token context window.

## Pricing

- Input **$0.1** / output **$0.5** per 1M tokens (USD)
- cache read multiplier: 0.1
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "anthropic/claude-haiku-5.5", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='anthropic/claude-haiku-5.5', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "anthropic/claude-haiku-5.5", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "anthropic/claude-haiku-5.5", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/anthropic/claude-haiku-5.5.json`](../../../catalog/models/anthropic/claude-haiku-5.5.json) · Store page: https://www.sandbase.ai/model/anthropic/claude-haiku-5.5

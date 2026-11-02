# Anthropic: Claude Opus 5 API: pricing, parameters and code examples

`anthropic/claude-opus-5` · LLM · Anthropic · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $5 input / $25 output per 1M tokens · **Modes:** sync

Claude Opus 5 is the most powerful model in the Claude 5 family from Anthropic. It excels at complex reasoning, analysis, and creative tasks with superior accuracy and nuance. It supports text, image, and file inputs with text output, reasoning support and a 1M-token context window.

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
  -d '{"model": "anthropic/claude-opus-5", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='anthropic/claude-opus-5', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "anthropic/claude-opus-5", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "anthropic/claude-opus-5", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/anthropic/claude-opus-5.json`](../../../catalog/models/anthropic/claude-opus-5.json) · Store page: https://www.sandbase.ai/model/anthropic/claude-opus-5

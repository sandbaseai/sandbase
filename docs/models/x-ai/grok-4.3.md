# xAI: Grok 4.3 API: pricing, parameters and code examples

`x-ai/grok-4.3` · LLM · xAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1.25 input / $2.5 output per 1M tokens · **Modes:** sync

Grok 4.3 is an xAI reasoning model that xAI describes as fast and reliable, with strong tool calling and instruction following. It accepts text and image input with text output, offers a 1M-token context window, and supports configurable reasoning effort that can be switched off or raised, defaulting to low. It suits agentic workflows, long-document analysis and high-volume instruction-following tasks, while Grok 4.5 through 4.7 later took over as xAI's flagship for coding.

## Pricing

- Input **$1.25** / output **$2.5** per 1M tokens (USD)
- cache read multiplier: 0.16

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "x-ai/grok-4.3", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='x-ai/grok-4.3', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "x-ai/grok-4.3", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "x-ai/grok-4.3", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/x-ai/grok-4.3.json`](../../../catalog/models/x-ai/grok-4.3.json) · Store page: https://www.sandbase.ai/model/x-ai/grok-4.3

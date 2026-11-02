# Google: Gemini 3.1 Pro Preview API: pricing, parameters and code examples

`google/gemini-3.1-pro-preview` · LLM · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $2 input / $12 output per 1M tokens · **Modes:** sync

Gemini 3.1 Pro Preview is the Pro-tier reasoning model of Google's Gemini 3 series, released in February 2026 to refine Gemini 3 Pro with better thinking, improved token efficiency and more grounded, factually consistent answers. Google optimizes it for software engineering and for agentic workflows that need precise tool use and reliable multi-step execution across real-world domains. It accepts text, image, video, audio and PDF input, remains a preview model, and is Google's recommended replacement for the retired Gemini 3 Pro Preview.

## Pricing

- Input **$2** / output **$12** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-3.1-pro-preview", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='google/gemini-3.1-pro-preview', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "google/gemini-3.1-pro-preview", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "google/gemini-3.1-pro-preview", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `audio_input`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/google/gemini-3.1-pro-preview.json`](../../../catalog/models/google/gemini-3.1-pro-preview.json) · Store page: https://www.sandbase.ai/model/google/gemini-3.1-pro-preview

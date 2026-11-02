# Google: Gemini 3 Flash Preview API: pricing, parameters and code examples

`google/gemini-3-flash-preview` · LLM · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.5 input / $3 output per 1M tokens · **Modes:** sync

Gemini 3 Flash Preview is the preview release of the Flash tier in Google's Gemini 3 series, released in December 2025. Google described it at launch as its most powerful agentic and vibe-coding model to that point, built on Gemini 3 reasoning with multimodal understanding across text, image, video, audio and PDF input. It remains a preview endpoint with no announced shutdown date, and Google recommends Gemini 3.6 Flash as its replacement.

## Pricing

- Input **$0.5** / output **$3** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-3-flash-preview", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='google/gemini-3-flash-preview', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "google/gemini-3-flash-preview", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "google/gemini-3-flash-preview", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `audio_input`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/google/gemini-3-flash-preview.json`](../../../catalog/models/google/gemini-3-flash-preview.json) · Store page: https://www.sandbase.ai/model/google/gemini-3-flash-preview

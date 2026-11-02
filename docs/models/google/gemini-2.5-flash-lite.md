# Google: Gemini 2.5 Flash Lite API: pricing, parameters and code examples

`google/gemini-2.5-flash-lite` · LLM · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.1 input / $0.4 output per 1M tokens · **Modes:** sync

Gemini 2.5 Flash-Lite is the lightweight tier of Google's Gemini 2.5 family, released in July 2025 and described by Google as the fastest multimodal model in that family. It is aimed at high-volume classification, simple data extraction and very low-latency applications, with optional thinking and support for text, image, video, audio and PDF input. It remains a stable model with no announced shutdown date; pick Gemini 2.5 Flash for more capability within the same generation.

## Pricing

- Input **$0.1** / output **$0.4** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-2.5-flash-lite", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='google/gemini-2.5-flash-lite', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "google/gemini-2.5-flash-lite", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "google/gemini-2.5-flash-lite", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `audio_input`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/google/gemini-2.5-flash-lite.json`](../../../catalog/models/google/gemini-2.5-flash-lite.json) · Store page: https://www.sandbase.ai/model/google/gemini-2.5-flash-lite

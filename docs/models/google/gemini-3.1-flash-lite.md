# Google: Gemini 3.1 Flash Lite API: pricing, parameters and code examples

`google/gemini-3.1-flash-lite` · LLM · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.25 input / $1.5 output per 1M tokens · **Modes:** sync

Gemini 3.1 Flash-Lite is the generally available, low-latency Flash-Lite tier of Google's Gemini 3 series, released in May 2026 as the stable successor to the 3.1 Flash-Lite preview. Google targets it at high-frequency, lightweight tasks such as high-volume translation, transcription, entity extraction, document summarization and routing queries between larger models. Google has scheduled its shutdown for May 7, 2027 and recommends Gemini 3.5 Flash-Lite as the replacement.

## Pricing

- Input **$0.25** / output **$1.5** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-3.1-flash-lite", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='google/gemini-3.1-flash-lite', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "google/gemini-3.1-flash-lite", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "google/gemini-3.1-flash-lite", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `audio_input`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/google/gemini-3.1-flash-lite.json`](../../../catalog/models/google/gemini-3.1-flash-lite.json) · Store page: https://www.sandbase.ai/model/google/gemini-3.1-flash-lite

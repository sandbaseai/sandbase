# Google: Gemini 2.5 Flash

`google/gemini-2.5-flash` · llm · Google

Gemini 2.5 Flash is the workhorse model of Google's Gemini 2.5 family, a thinking model released as stable in June 2025. Google positions it for large-scale processing, low-latency and high-volume tasks that require reasoning, and agentic use cases, with text, image, video and audio input. It sits between 2.5 Flash-Lite and 2.5 Pro in the same generation and remains a stable model with no announced shutdown date.

## Pricing

- Input **$0.3** / output **$2.5** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-2.5-flash", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='google/gemini-2.5-flash', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "google/gemini-2.5-flash", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "google/gemini-2.5-flash", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `audio_input`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/google/gemini-2.5-flash.json`](../../../catalog/models/google/gemini-2.5-flash.json) · Store page: https://www.sandbase.ai/model/google/gemini-2.5-flash

# Google: Gemini 4 Argon

`google/gemini-4-argon` · llm · Google

Gemini 4 Argon is Google's flagship reasoning model and the first model of the Gemini 4 generation, generally available since October 13, 2026. Google trained it to keep context and precision across long, multi-step work such as complex software engineering, legal and financial research, and cybersecurity defense. It accepts text, image, video, audio and PDF input with a 1M-token context window, always reasons before answering with low, medium or high effort, and supports function calling and structured output.

## Pricing

- Input **$4** / output **$20** per 1M tokens (USD)
- cache read multiplier: 0.05

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-4-argon", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='google/gemini-4-argon', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "google/gemini-4-argon", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "google/gemini-4-argon", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `audio_input`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/google/gemini-4-argon.json`](../../../catalog/models/google/gemini-4-argon.json) · Store page: https://www.sandbase.ai/model/google/gemini-4-argon

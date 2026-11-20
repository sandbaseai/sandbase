# Google: Gemini 4 Neon API: pricing, parameters and code examples

`google/gemini-4-neon` · LLM · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $3 input / $15 output per 1M tokens · **Modes:** sync

Gemini 4 Neon is a fast, mid-priced model in Google's Gemini 4 family, released on November 18, 2026. Google built it for coding and agentic work, including repository and terminal coding and web development. It accepts text, image, video, audio and PDF input with a 1M-token context window, supports adjustable reasoning effort, and supports function calling and structured output.

## Pricing

- Input **$3** / output **$15** per 1M tokens (USD)
- cache read multiplier: 0.05

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-4-neon", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='google/gemini-4-neon', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "google/gemini-4-neon", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "google/gemini-4-neon", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `audio_input`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/google/gemini-4-neon.json`](../../../catalog/models/google/gemini-4-neon.json) · Store page: https://www.sandbase.ai/model/google/gemini-4-neon

# Google: Gemini 3.6 Flash

`google/gemini-3.6-flash` · llm · Google

Gemini 3.6 Flash is a multimodal reasoning model in Google's Gemini 3 Flash line, released in July 2026 alongside 3.5 Flash-Lite. Google describes it as delivering frontier-level intelligence at higher speed for real-world agentic work, excelling at code generation, agentic execution and spatial reasoning, and particularly effective in rapid agentic loops with repeated coding iterations. It is Google's recommended replacement for the Gemini 3 Flash preview; 3.7 Flash and 3.8 Flash followed it.

## Pricing

- Input **$0.75** / output **$3.75** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-3.6-flash", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='google/gemini-3.6-flash', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "google/gemini-3.6-flash", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "google/gemini-3.6-flash", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `audio_input`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/google/gemini-3.6-flash.json`](../../../catalog/models/google/gemini-3.6-flash.json) · Store page: https://www.sandbase.ai/model/google/gemini-3.6-flash

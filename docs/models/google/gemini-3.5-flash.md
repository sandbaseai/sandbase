# Google: Gemini 3.5 Flash

`google/gemini-3.5-flash` · llm · Google

Gemini 3.5 Flash is the Flash model of Google's Gemini 3.5 family, introduced at Google I/O in May 2026. Google positions it as delivering frontier-level intelligence at Flash speed, built for sub-agent deployment, multi-step workflows and long-horizon tasks at scale, and particularly effective in rapid agentic loops with complex coding iterations. It takes text, image, video, audio and PDF input with text output; Google's model list now labels it a legacy Flash model behind 3.6, 3.7 and 3.8 Flash.

## Pricing

- Input **$1.5** / output **$9** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-3.5-flash", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='google/gemini-3.5-flash', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "google/gemini-3.5-flash", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "google/gemini-3.5-flash", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `audio_input`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/google/gemini-3.5-flash.json`](../../../catalog/models/google/gemini-3.5-flash.json) · Store page: https://www.sandbase.ai/model/google/gemini-3.5-flash

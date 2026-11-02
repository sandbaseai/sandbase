# Google: Gemini 3.8 Flash API: pricing, parameters and code examples

`google/gemini-3.8-flash` · LLM · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1.5 input / $7.5 output per 1M tokens · **Modes:** sync

Gemini 3.8 Flash is a Flash-tier reasoning model in Google's Gemini 3 series, released in September 2026 and described by Google as its most intelligent Flash model as of release. Google positions it for long-horizon software engineering, autonomous agents and complex enterprise workflows, with significant gains over 3.7 Flash in coding, agentic tasks and multi-step reasoning in specialized domains. It accepts text, image, video, audio and PDF input with text output, and suits demanding agentic and coding work.

## Pricing

- Input **$1.5** / output **$7.5** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-3.8-flash", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='google/gemini-3.8-flash', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "google/gemini-3.8-flash", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "google/gemini-3.8-flash", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `audio_input`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/google/gemini-3.8-flash.json`](../../../catalog/models/google/gemini-3.8-flash.json) · Store page: https://www.sandbase.ai/model/google/gemini-3.8-flash

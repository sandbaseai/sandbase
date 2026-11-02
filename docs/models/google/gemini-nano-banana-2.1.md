# Google: Nano Banana 2.1 (Gemini Nano Banana 2.1) API: pricing, parameters and code examples

`google/gemini-nano-banana-2.1` · LLM · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1.5 input / $7.5 output per 1M tokens · **Modes:** sync

Nano Banana 2.1 (Gemini Nano Banana 2.1) is Google's Flash-tier image generation and editing model, succeeding Nano Banana 2 and producing images alongside text through the native Gemini generateContent API. It improves prompt adherence, text rendering, product recontextualization and multi-turn editing consistency, supports extreme aspect ratios and 1K to 4K output, and can ground generation with Google web and image search. Pick Nano Banana Pro instead for the most demanding professional design work.

## Pricing

- Input **$1.5** / output **$7.5** per 1M tokens (USD)
- cache read multiplier: 1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-nano-banana-2.1", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='google/gemini-nano-banana-2.1', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "google/gemini-nano-banana-2.1", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "google/gemini-nano-banana-2.1", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `image_output`
---
Machine-readable: [`catalog/models/google/gemini-nano-banana-2.1.json`](../../../catalog/models/google/gemini-nano-banana-2.1.json) · Store page: https://www.sandbase.ai/model/google/gemini-nano-banana-2.1

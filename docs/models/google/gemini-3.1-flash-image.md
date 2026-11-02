# Google: Nano Banana 2 (Gemini 3.1 Flash Image) API: pricing, parameters and code examples

`google/gemini-3.1-flash-image` · LLM · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.5 input / $3 output per 1M tokens · **Modes:** sync

Nano Banana 2 (Gemini 3.1 Flash Image) is Google's image generation and conversational image editing model in the Gemini 3 series, producing images alongside text from text, image, video and PDF input. Google positions it as the high-efficiency, low-latency counterpart to Nano Banana Pro for high-volume developer use, adding output resolutions from 0.5K to 4K, extra wide and tall aspect ratios, image search grounding and improved multilingual text rendering. Choose Nano Banana Pro for complex, precision design work.

## Pricing

- Input **$0.5** / output **$3** per 1M tokens (USD)

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-3.1-flash-image", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='google/gemini-3.1-flash-image', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "google/gemini-3.1-flash-image", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "google/gemini-3.1-flash-image", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `image_output`
---
Machine-readable: [`catalog/models/google/gemini-3.1-flash-image.json`](../../../catalog/models/google/gemini-3.1-flash-image.json) · Store page: https://www.sandbase.ai/model/google/gemini-3.1-flash-image

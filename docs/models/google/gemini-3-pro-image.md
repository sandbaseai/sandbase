# Google: Nano Banana Pro (Gemini 3 Pro Image)

`google/gemini-3-pro-image` · llm · Google

Nano Banana Pro (Gemini 3 Pro Image) is the Pro-tier image generation and editing model of Google's Gemini 3 line, using a reasoning core and producing images alongside text. Google positions it for professional work such as complex graphic design, high-fidelity product mockups and factual data visualizations that need accurate text rendering, with real-world grounding via Google Search and studio-quality visuals up to 4K. Pick Nano Banana 2 instead for faster, higher-volume generation.

## Pricing

- Input **$2** / output **$12** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-3-pro-image", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='google/gemini-3-pro-image', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "google/gemini-3-pro-image", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "google/gemini-3-pro-image", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `image_output`
---
Machine-readable: [`catalog/models/google/gemini-3-pro-image.json`](../../../catalog/models/google/gemini-3-pro-image.json) · Store page: https://www.sandbase.ai/model/google/gemini-3-pro-image

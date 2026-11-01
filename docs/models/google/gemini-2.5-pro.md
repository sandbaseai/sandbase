# Google: Gemini 2.5 Pro

`google/gemini-2.5-pro` · llm · Google

Gemini 2.5 Pro is the Pro-tier thinking model of Google's Gemini 2.5 family, released as stable in June 2025 and described by Google as its most advanced model in that family. It is built for reasoning over complex problems in code, math and STEM, and for analyzing large datasets, codebases and documents using long context. It accepts audio, image, video, text and PDF input; Gemini 3.1 Pro Preview is the Pro-tier successor in the Gemini 3 series.

## Pricing

- Input **$1.25** / output **$10** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-2.5-pro", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='google/gemini-2.5-pro', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "google/gemini-2.5-pro", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "google/gemini-2.5-pro", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `audio_input`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/google/gemini-2.5-pro.json`](../../../catalog/models/google/gemini-2.5-pro.json) · Store page: https://www.sandbase.ai/model/google/gemini-2.5-pro

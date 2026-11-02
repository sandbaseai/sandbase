# Google: Gemini 3.1 Pro Preview Custom Tools API: pricing, parameters and code examples

`google/gemini-3.1-pro-preview-customtools` · LLM · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $2 input / $12 output per 1M tokens · **Modes:** sync

Gemini 3.1 Pro Preview Custom Tools is a separate endpoint of Google's Gemini 3.1 Pro Preview, the Pro-tier reasoning model of the Gemini 3 series, tuned for agentic workflows that mix bash with custom tools. Google says it is better at prioritizing user-defined functions, such as file viewing or code search tools, over a general bash tool. Pick it for coding agents built on custom tools; Google notes quality may fluctuate in use cases that do not benefit from such tools, where the standard 3.1 Pro Preview fits better.

## Pricing

- Input **$2** / output **$12** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-3.1-pro-preview-customtools", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='google/gemini-3.1-pro-preview-customtools', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "google/gemini-3.1-pro-preview-customtools", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "google/gemini-3.1-pro-preview-customtools", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `audio_input`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/google/gemini-3.1-pro-preview-customtools.json`](../../../catalog/models/google/gemini-3.1-pro-preview-customtools.json) · Store page: https://www.sandbase.ai/model/google/gemini-3.1-pro-preview-customtools

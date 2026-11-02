# Xiaomi: MiMo-V2.6-Flash API: pricing, parameters and code examples

`xiaomi/mimo-v2.6-flash` · LLM · Xiaomi · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.14 input / $0.28 output per 1M tokens · **Modes:** sync

MiMo-V2.6-Flash is the efficiency tier of Xiaomi's open-source MiMo-V2.6 series, released in September 2026 as a natively omni-modal reasoning model that takes text, image, video and audio input and returns text. Xiaomi positions it as the balance of intelligence and efficiency for high-frequency calls and large-scale professional workflows, with a 1M-token context, tool calling and structured output. Xiaomi reports it surpasses MiMo-V2.5-Pro; choose MiMo-V2.6-Pro for the hardest tasks.

## Pricing

- Input **$0.14** / output **$0.28** per 1M tokens (USD)
- cache read multiplier: 0.02

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaomi/mimo-v2.6-flash", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='xiaomi/mimo-v2.6-flash', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "xiaomi/mimo-v2.6-flash", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "xiaomi/mimo-v2.6-flash", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `audio_input`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/xiaomi/mimo-v2.6-flash.json`](../../../catalog/models/xiaomi/mimo-v2.6-flash.json) · Store page: https://www.sandbase.ai/model/xiaomi/mimo-v2.6-flash

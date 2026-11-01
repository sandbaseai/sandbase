# Xiaomi: MiMo-V2.6-Pro

`xiaomi/mimo-v2.6-pro` · llm · Xiaomi

MiMo-V2.6-Pro is the flagship of Xiaomi's open-source MiMo-V2.6 series, a trillion-parameter, natively omni-modal reasoning model released in September 2026 that takes text, image, video and audio input. Xiaomi built it for complex projects, long-horizon agents, coding, office and design work, cybersecurity, computer operation and research, with a 1M-token context. Pick it over MiMo-V2.6-Flash when task difficulty matters more than speed and volume.

## Pricing

- Input **$0.435** / output **$0.87** per 1M tokens (USD)
- cache read multiplier: 0.0083

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaomi/mimo-v2.6-pro", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='xiaomi/mimo-v2.6-pro', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "xiaomi/mimo-v2.6-pro", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "xiaomi/mimo-v2.6-pro", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `audio_input`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/xiaomi/mimo-v2.6-pro.json`](../../../catalog/models/xiaomi/mimo-v2.6-pro.json) · Store page: https://www.sandbase.ai/model/xiaomi/mimo-v2.6-pro

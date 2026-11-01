# Qwen: Qwen3.8 Omni Flash

`alibaba/qwen3.8-omni-flash` · llm · Alibaba

Qwen3.8 Omni Flash is Alibaba's omni-modal reasoning model in the Qwen3.8 family, accepting text, image, audio and video input and returning text, with a 1M-token context window. Alibaba positions it for audio and video understanding and content analysis, including transcription-aware summarization, meeting and lecture review, and multimodal agent steps, with tool calling and adjustable reasoning effort. Pick Qwen3.8 Flash for text and image workloads that do not need audio or video input.

## Pricing

- Input **$0.15** / output **$0.47** per 1M tokens (USD)
- cache read multiplier: 0.1067
- cache write multiplier: 1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "alibaba/qwen3.8-omni-flash", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='alibaba/qwen3.8-omni-flash', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "alibaba/qwen3.8-omni-flash", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "alibaba/qwen3.8-omni-flash", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `audio_input`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/alibaba/qwen3.8-omni-flash.json`](../../../catalog/models/alibaba/qwen3.8-omni-flash.json) · Store page: https://www.sandbase.ai/model/alibaba/qwen3.8-omni-flash

# Meta: Llama 3.3 70B Instruct

`meta/llama-3.3-70b-instruct` · llm · Meta

Llama 3.3 70B Instruct is Meta's instruction-tuned, text-only multilingual model released on December 6, 2024, built on an optimized transformer with grouped-query attention and a 128K-token context. It is optimized for assistant-style multilingual dialogue in eight officially supported languages, including English, German, French, Spanish, Hindi and Thai. It is a static open-weight model with a December 2023 knowledge cutoff, and its license also permits synthetic data generation and distillation.

## Pricing

- Input **$0.1** / output **$0.32** per 1M tokens (USD)

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "meta/llama-3.3-70b-instruct", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='meta/llama-3.3-70b-instruct', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "meta/llama-3.3-70b-instruct", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "meta/llama-3.3-70b-instruct", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/meta/llama-3.3-70b-instruct.json`](../../../catalog/models/meta/llama-3.3-70b-instruct.json) · Store page: https://www.sandbase.ai/model/meta/llama-3.3-70b-instruct

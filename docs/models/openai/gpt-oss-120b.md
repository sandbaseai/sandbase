# OpenAI: gpt-oss-120b API: pricing, parameters and code examples

`openai/gpt-oss-120b` · LLM · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.039 input / $0.18 output per 1M tokens · **Modes:** sync

gpt-oss-120b is OpenAI's largest open-weight reasoning model, released in August 2025 under the Apache 2.0 license: a 117B-parameter mixture-of-experts model with 5.1B active parameters that fits on a single 80GB GPU. OpenAI positions it for production, general-purpose and high-reasoning use, with adjustable low, medium or high reasoning, full chain-of-thought access, and native function calling, browsing, Python execution and structured outputs. It is text-only and can be self-hosted or fine-tuned.

## Pricing

- Input **$0.039** / output **$0.18** per 1M tokens (USD)

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-oss-120b", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-oss-120b', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-oss-120b", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-oss-120b", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-oss-120b.json`](../../../catalog/models/openai/gpt-oss-120b.json) · Store page: https://www.sandbase.ai/model/openai/gpt-oss-120b

# OpenAI: GPT-5 API: pricing, parameters and code examples

`openai/gpt-5` · LLM · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1.25 input / $10 output per 1M tokens · **Modes:** sync

GPT-5 is OpenAI's reasoning model released in August 2025 for coding, reasoning and agentic tasks across domains, accepting text and image input and producing text. OpenAI describes it as a coding collaborator for fixing bugs, editing code and answering questions about complex codebases, with configurable reasoning effort that includes a minimal setting for quicker replies. OpenAI now labels it a previous model, and later GPT-5.x releases are its recommended successors for fresh work.

## Pricing

- Input **$1.25** / output **$10** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-5", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-5', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-5", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-5", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-5.json`](../../../catalog/models/openai/gpt-5.json) · Store page: https://www.sandbase.ai/model/openai/gpt-5

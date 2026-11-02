# OpenAI: GPT-5.3-Codex API: pricing, parameters and code examples

`openai/gpt-5.3-codex` · LLM · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1.75 input / $14 output per 1M tokens · **Modes:** sync

GPT-5.3-Codex is OpenAI's agentic coding model announced in February 2026, optimized for Codex and similar environments, with text and image input and text output. OpenAI called it its most capable agentic coding model at release and says it extends Codex from writing and reviewing code to most tasks developers and professionals do on a computer. It supports low to extra-high reasoning effort and suits long-running coding, debugging and computer-use agents.

## Pricing

- Input **$1.75** / output **$14** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-5.3-codex", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-5.3-codex', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-5.3-codex", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-5.3-codex", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-5.3-codex.json`](../../../catalog/models/openai/gpt-5.3-codex.json) · Store page: https://www.sandbase.ai/model/openai/gpt-5.3-codex

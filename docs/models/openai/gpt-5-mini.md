# OpenAI: GPT-5 Mini API: pricing, parameters and code examples

`openai/gpt-5-mini` · LLM · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.25 input / $2 output per 1M tokens · **Modes:** sync

GPT-5 mini is the faster, more efficient tier of OpenAI's GPT-5 reasoning family, released in August 2025 with text and image input and text output. OpenAI recommends it for well-defined tasks and precise prompts in low-latency, high-volume workloads, keeping GPT-5's configurable reasoning. Choose it over full GPT-5 when speed and throughput matter more than maximum depth; OpenAI's later small models are its suggested successors.

## Pricing

- Input **$0.25** / output **$2** per 1M tokens (USD)
- cache read multiplier: 0.1

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-5-mini", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-5-mini', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-5-mini", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-5-mini", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-5-mini.json`](../../../catalog/models/openai/gpt-5-mini.json) · Store page: https://www.sandbase.ai/model/openai/gpt-5-mini

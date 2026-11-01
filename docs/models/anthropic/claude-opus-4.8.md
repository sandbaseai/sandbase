# Anthropic: Claude Opus 4.8

`anthropic/claude-opus-4.8` · llm · Anthropic

Claude Opus 4.8 is Anthropic's most capable generally available model in the Opus family. It supports text, image, and file inputs with text output, with reasoning support and a 1M-token context window. It is suited for highly autonomous agents, long-horizon agentic work, knowledge work, and memory-driven tasks where coherence over extended sessions matters.

It is particularly strong on multi-step reasoning, complex coding, and end-to-end project orchestration - large codebases, multi-stage debugging, and long-running asynchronous agent pipelines. Beyond coding, it handles knowledge work such as drafting documents, building presentations, and analyzing data, maintaining quality across very long outputs.

## Pricing

- Input **$5** / output **$25** per 1M tokens (USD)
- cache read multiplier: 0.1
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "anthropic/claude-opus-4.8", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='anthropic/claude-opus-4.8', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "anthropic/claude-opus-4.8", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "anthropic/claude-opus-4.8", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/anthropic/claude-opus-4.8.json`](../../../catalog/models/anthropic/claude-opus-4.8.json) · Store page: https://www.sandbase.ai/model/anthropic/claude-opus-4.8

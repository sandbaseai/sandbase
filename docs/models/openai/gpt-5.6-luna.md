# OpenAI: GPT-5.6 Luna API: pricing, parameters and code examples

`openai/gpt-5.6-luna` · LLM · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.2 input / $1.2 output per 1M tokens · **Modes:** sync

GPT-5.6 Luna is the smallest, fastest tier of OpenAI's GPT-5.6 reasoning family, with text and image input; OpenAI says it roughly corresponds to the nano tier of earlier GPT-5 families. It is designed for high-volume workloads such as classification, extraction, routing, chat and lightweight agent steps where throughput and latency matter. Pick GPT-5.6 Terra or GPT-5.6 Sol when tasks need more capability, and the pro variant when a hard request needs more reasoning work.

## Pricing

- Input **$0.2** / output **$1.2** per 1M tokens (USD)
- cache read multiplier: 0.1
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-5.6-luna", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-5.6-luna', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-5.6-luna", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-5.6-luna", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
## Details

GPT-5.6 Luna is the smallest and fastest tier of OpenAI's GPT-5.6 reasoning family. OpenAI says it matches the nano tier of earlier GPT-5 families. It reads text and images, writes text, and has a 1.05M-token context window at $0.20 per 1M input tokens.

### When to use it

- Classification, extraction and routing at high volume.
- Lightweight agent steps that need tools and JSON, not deep reasoning.
- Long-context lookups where the price per token matters.

### Call it

The model works on Chat Completions (`/v1/chat/completions`) and on OpenAI's Responses API (`/v1/responses`).

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key="$SANDBASE_API_KEY")

resp = client.chat.completions.create(
    model="openai/gpt-5.6-luna",
    messages=[{"role": "user", "content": "Explain what an API gateway does."}],
    reasoning_effort="low",
    max_tokens=512,
)
print(resp.choices[0].message.content)
```

### What works on SandBase

Checked with real calls through SandBase on October 28, 2026.

| Feature | Works | Notes |
|---|---|---|
| Streaming | Yes | `stream: true`, with `usage` in the last chunk when `stream_options.include_usage` is set. |
| Tool calling | Yes | `tools` and `tool_choice`; returns `tool_calls`. |
| Structured output | Yes | `response_format: {"type": "json_schema", …}` returned valid JSON. |
| Image input | Yes | `image_url` parts with an https URL or a `data:` URI. |
| Reasoning | Adjustable | Set `reasoning_effort` on Chat Completions or `reasoning: {"effort": …}` on Responses. In our checks `"low"` used no reasoning tokens on a short question and `"high"` did. |

### Limits and parameters

- Context window: 1,050,000 tokens.
- Maximum output: 128,000 tokens per request (`max_tokens`).
- The request schema accepts `temperature` and `seed`; it has no `top_p` or `stop`.

### Example response

Real response to "In two sentences, explain what an API gateway does." through Chat Completions, trimmed.

```json
{
  "id": "e578284d-bf7…",
  "object": "chat.completion",
  "model": "openai/gpt-5.6-luna",
  "choices": [
    {
      "index": 0,
      "finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "An API gateway acts as a single entry point for client requests, routing them to the appropriate backend services. It can also handle cross-cutting concerns…"
      }
    }
  ],
  "usage": {
    "completion_tokens": 48,
    "completion_tokens_details": {
      "reasoning_tokens": 0
    },
    "prompt_tokens": 17,
    "prompt_tokens_details": {
      "cache_write_tokens": 0,
      "cached_tokens": 0
    },
    "total_tokens": 65
  }
}
```

### Pricing

| Tokens | Price per 1M |
|---|---|
| Input | $0.20 |
| Output | $1.20 |
| Cached input (read) | $0.02 |
| Cache write, 5-minute | $0.25 |

Requests with 272,000 or more prompt tokens are billed at $0.40 per 1M input and $1.80 per 1M output tokens.

Reasoning tokens are part of `completion_tokens` and are billed at the output price.

### Related models

- [GPT-5.6 Terra](/models/openai/gpt-5.6-terra): the middle tier of the same family.
- [GPT-5.6 Sol](/models/openai/gpt-5.6-sol): the most capable tier of the same family.
- [GPT-5.6 Luna Pro](/models/openai/gpt-5.6-luna-pro): Luna with more reasoning work per request.

---
Machine-readable: [`catalog/models/openai/gpt-5.6-luna.json`](../../../catalog/models/openai/gpt-5.6-luna.json) · Store page: https://www.sandbase.ai/model/openai/gpt-5.6-luna

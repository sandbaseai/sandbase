# OpenAI: GPT-4o-mini API: pricing, parameters and code examples

`openai/gpt-4o-mini` · LLM · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.15 input / $0.6 output per 1M tokens · **Modes:** sync

GPT-4o mini is OpenAI's small, fast model from the GPT-4o family, released in July 2024 with text and image input and text output, including Structured Outputs. OpenAI positions it for focused tasks such as intent classification, keyword extraction, translation and tagging, and calls it ideal for fine-tuning, including distilling outputs from a larger model like GPT-4o. Pick it over GPT-4o when latency and throughput matter more than peak capability.

## Pricing

- Input **$0.15** / output **$0.6** per 1M tokens (USD)
- cache read multiplier: 0.5

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-4o-mini", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-4o-mini', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-4o-mini", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-4o-mini", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `structured_output`, `function_calling`
## Details

GPT-4o mini is OpenAI's small, fast model from the GPT-4o family, released in July 2024. It reads text and images, writes text, and costs $0.15 per 1M input tokens, so it suits narrow, high-volume jobs where speed matters more than depth.

### When to use it

- Classification, tagging, routing and keyword extraction.
- Short translations and rewrites in a pipeline.
- Filling a JSON schema from free text or a screenshot.

### Call it

The model works on Chat Completions (`/v1/chat/completions`) and on OpenAI's Responses API (`/v1/responses`). Existing OpenAI SDK code only needs the SandBase base URL.

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key="$SANDBASE_API_KEY")

resp = client.chat.completions.create(
    model="openai/gpt-4o-mini",
    messages=[{"role": "user", "content": "Explain what an API gateway does."}],
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
| Structured output | Yes | `response_format: {"type": "json_schema", …}` with `strict: true` returned valid JSON. |
| Image input | Yes | `image_url` parts with an https URL or a `data:` URI. |
| Reasoning | No | It is not a reasoning model; `reasoning_tokens` is always 0. |

### Limits and parameters

- Context window: 128,000 tokens.
- Maximum output: 16,384 tokens per request (`max_tokens`).
- The request schema accepts `temperature`, `top_p`, `frequency_penalty`, `presence_penalty`, `seed` and `stop`.

### Example response

Real response to "In two sentences, explain what an API gateway does." through Chat Completions, trimmed.

```json
{
  "id": "fd15fbaa-130…",
  "object": "chat.completion",
  "model": "openai/gpt-4o-mini",
  "choices": [
    {
      "index": 0,
      "finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "An API gateway acts as a single entry point for client applications to access various microservices within a system, managing requests and directing them to…"
      }
    }
  ],
  "usage": {
    "completion_tokens": 54,
    "completion_tokens_details": {
      "reasoning_tokens": 0
    },
    "prompt_tokens": 18,
    "prompt_tokens_details": {
      "cache_write_tokens": 0,
      "cached_tokens": 0
    },
    "total_tokens": 72
  }
}
```

### Pricing

| Tokens | Price per 1M |
|---|---|
| Input | $0.15 |
| Output | $0.60 |
| Cached input (read) | $0.075 |

### Related models

- [GPT-4.1 Mini](/models/openai/gpt-4.1-mini): a newer small OpenAI model with a longer context window.
- [GPT-5.6 Luna](/models/openai/gpt-5.6-luna): OpenAI's current small reasoning tier.
- [GPT-4o](/models/openai/gpt-4o): the full GPT-4o model, when mini is not accurate enough.

---
Machine-readable: [`catalog/models/openai/gpt-4o-mini.json`](../../../catalog/models/openai/gpt-4o-mini.json) · Store page: https://www.sandbase.ai/model/openai/gpt-4o-mini

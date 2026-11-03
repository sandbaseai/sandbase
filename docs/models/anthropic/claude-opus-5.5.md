# Anthropic: Claude Opus 5.5 API: pricing, parameters and code examples

`anthropic/claude-opus-5.5` · LLM · Anthropic · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $4 input / $20 output per 1M tokens · **Modes:** sync

Claude Opus 5.5 is the most powerful model in the Claude 5 family from Anthropic. It excels at complex reasoning, analysis, and creative tasks with superior accuracy and nuance. It supports text, image, and file inputs with text output, reasoning support and a 1M-token context window.

## Pricing

- Input **$4** / output **$20** per 1M tokens (USD)
- cache read multiplier: 0.05
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "anthropic/claude-opus-5.5", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='anthropic/claude-opus-5.5', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "anthropic/claude-opus-5.5", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "anthropic/claude-opus-5.5", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
## Details

Claude Opus 5.5 is the largest model in Anthropic's Claude 5 family. It takes text and images, writes text, and has a 1M-token context window. Use it for the hard parts of a system: long-document analysis, multi-step agent work and code changes where a wrong answer costs more than the tokens.

### When to use it

- Agents that plan, call tools and recover from their own mistakes over many steps.
- Reading a whole codebase, contract set or research corpus in one request.
- Reviewing or rewriting work produced by cheaper models.

### Call it

The model works on Chat Completions (`/v1/chat/completions`), so the OpenAI SDK only needs a new base URL. It also works on Anthropic's Messages API (`/v1/messages`), which you need for Messages-only features such as `output_format`, `stop_sequences` and `cache_control`.

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key="$SANDBASE_API_KEY")

resp = client.chat.completions.create(
    model="anthropic/claude-opus-5.5",
    messages=[{"role": "user", "content": "Explain what an API gateway does."}],
    max_tokens=512,
)
print(resp.choices[0].message.content)
```

### What works on SandBase

Checked with real calls through SandBase on October 28, 2026.

| Feature | Works | Notes |
|---|---|---|
| Streaming | Yes | `stream: true`; the last chunk carries `usage` when `stream_options.include_usage` is set. |
| Tool calling | Yes | OpenAI-style `tools` and `tool_choice`; returns `tool_calls`. |
| Image input | Yes | `image_url` parts with an https URL or a `data:` URI. |
| Structured output | Messages API only | On Chat Completions `response_format` is ignored and the model answers in prose. On `/v1/messages`, `output_format: {"type": "json_schema", "schema": …}` returns JSON that matches the schema. |
| Stop sequences | Messages API only | Chat Completions rejects `stop` for this model with a 400. Use `stop_sequences` on `/v1/messages`. |

### Limits and parameters

- Context window: 1,000,000 tokens.
- Maximum output: 128,000 tokens per request (`max_tokens`).
- `top_p` is rejected with "`top_p` is deprecated for this model". Use `temperature` (0 to 2) instead.
- It counts more tokens for the same text than older Claude models: one 9,419-token system prompt on Claude Haiku 4.5 counted 13,320 input tokens on Opus 5.5. Budget cost and context from a real count, not an older estimate.

### Example response

Real response to "In two sentences, explain what an API gateway does." through Chat Completions, trimmed.

```json
{
  "id": "81ea378c-6a4…",
  "object": "chat.completion",
  "model": "anthropic/claude-opus-5.5",
  "choices": [
    {
      "index": 0,
      "finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "An API gateway is a server that sits between clients and a collection of backend services, acting as a single entry point that receives API requests and routes…"
      }
    }
  ],
  "usage": {
    "completion_tokens": 120,
    "completion_tokens_details": {
      "reasoning_tokens": 0
    },
    "prompt_tokens": 24,
    "prompt_tokens_details": {
      "cache_write_tokens": 0,
      "cached_tokens": 0
    },
    "total_tokens": 144
  }
}
```

### Pricing

| Tokens | Price per 1M |
|---|---|
| Input | $4.00 |
| Output | $20.00 |
| Cached input (read) | $0.20 |
| Cache write, 5-minute | $5.00 |
| Cache write, 1-hour | $8.00 |

Prompt caching works through `cache_control` blocks on `/v1/messages`: the first call reports `cache_creation_input_tokens`, a repeat within the cache lifetime reports the same count as `cache_read_input_tokens`. Reads cost 5% of the input price.

### Related models

- [Claude Sonnet 5.5](/models/anthropic/claude-sonnet-5.5): the Sonnet tier of the same family, at half the price per token.
- [Claude Haiku 5.5](/models/anthropic/claude-haiku-5.5): the smallest and cheapest Claude 5 tier, for high-volume steps.
- [Claude Opus 5](/models/anthropic/claude-opus-5): the previous Opus release.

---
Machine-readable: [`catalog/models/anthropic/claude-opus-5.5.json`](../../../catalog/models/anthropic/claude-opus-5.5.json) · Store page: https://www.sandbase.ai/model/anthropic/claude-opus-5.5

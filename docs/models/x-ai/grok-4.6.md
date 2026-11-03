# xAI: Grok 4.6 API: pricing, parameters and code examples

`x-ai/grok-4.6` · LLM · xAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $2 input / $6 output per 1M tokens · **Modes:** sync

Grok 4.6 is xAI's frontier reasoning model for coding, agentic tasks and knowledge work, released in August 2026 as the successor to Grok 4.5. xAI focused it on long-running agents and ambitious interactive and visual projects, such as turning a broad product idea into a working first version and refining it over several rounds. It accepts text and image input with text output and configurable reasoning effort; Grok 4.7 succeeded it in September 2026.

## Pricing

- Input **$2** / output **$6** per 1M tokens (USD)
- cache read multiplier: 0.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "x-ai/grok-4.6", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='x-ai/grok-4.6', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "x-ai/grok-4.6", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "x-ai/grok-4.6", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
## Details

Grok 4.6 is xAI's reasoning model for coding, agent tasks and knowledge work, released in August 2026. It takes text and images, writes text, and offers a 500K-token context window. It reasons before it answers by default, so expect reasoning tokens on every call. Grok 4.7 replaced it in September 2026.

### When to use it

- Agents that build a working first version of an app and refine it over several rounds.
- Coding and debugging tasks that benefit from step-by-step reasoning.
- Questions over long inputs, up to the 500K-token window.

### Call it

The model works on Chat Completions (`/v1/chat/completions`).

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key="$SANDBASE_API_KEY")

resp = client.chat.completions.create(
    model="x-ai/grok-4.6",
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
| Structured output | Yes | `response_format: {"type": "json_schema", …}` returned valid JSON. |
| Image input | Yes | `image_url` parts with an https URL or a `data:` URI. |
| Reasoning | By default | A two-sentence answer used 221 reasoning tokens. `reasoning_effort` is accepted. |

### Limits and parameters

- Context window: 500,000 tokens.
- Maximum output: 500,000 tokens per request (`max_tokens`).
- Leave room in `max_tokens` for reasoning. A small limit can be used up before the visible answer is written.

### Example response

Real response to "In two sentences, explain what an API gateway does." through Chat Completions, trimmed.

```json
{
  "id": "e8a8a919-29c…",
  "object": "chat.completion",
  "model": "x-ai/grok-4.6",
  "choices": [
    {
      "index": 0,
      "finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "An API gateway is a reverse-proxy layer that sits in front of backend services, receiving client API requests, applying cross-cutting concerns such as…"
      }
    }
  ],
  "usage": {
    "completion_tokens": 292,
    "completion_tokens_details": {
      "reasoning_tokens": 221
    },
    "prompt_tokens": 647,
    "prompt_tokens_details": {
      "cache_write_tokens": 0,
      "cached_tokens": 512
    },
    "total_tokens": 939
  }
}
```

### Pricing

| Tokens | Price per 1M |
|---|---|
| Input | $2.00 |
| Output | $6.00 |
| Cached input (read) | $0.50 |

Requests with 200,000 or more prompt tokens are billed at $4.00 per 1M input and $12.00 per 1M output tokens.

Reasoning tokens are part of `completion_tokens` and are billed at the output price.

### Related models

- [Grok 4.7](/models/x-ai/grok-4.7): the release that replaced 4.6.
- [Grok 4.5](/models/x-ai/grok-4.5): the previous release.

---
Machine-readable: [`catalog/models/x-ai/grok-4.6.json`](../../../catalog/models/x-ai/grok-4.6.json) · Store page: https://www.sandbase.ai/model/x-ai/grok-4.6

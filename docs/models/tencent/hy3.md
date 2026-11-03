# Tencent: Hy3 API: pricing, parameters and code examples

`tencent/hy3` · LLM · Tencent · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.132 input / $0.528 output per 1M tokens · **Modes:** sync

Hy3 is a 295B-parameter Mixture-of-Experts model from Tencent (21B active, 192 experts with top-8 routing) built for reasoning, agentic workflows, and real-world production use. It supports configurable reasoning effort.

## Pricing

- Input **$0.132** / output **$0.528** per 1M tokens (USD)
- cache read multiplier: 0.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tencent/hy3", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='tencent/hy3', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "tencent/hy3", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "tencent/hy3", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `reasoning`, `structured_output`, `function_calling`
## Details

Hy3 is a 295B-parameter mixture-of-experts model from Tencent, with 21B parameters active per token. It is text-only, reasons before it answers, and has a 262K-token context window. It costs $0.13 per 1M input tokens.

### When to use it

- Agent workflows that need tool calls and JSON output at low cost.
- Batch reasoning jobs, such as grading or extraction over many documents.
- Chinese and English text tasks.

### Call it

The model works on Chat Completions (`/v1/chat/completions`).

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key="$SANDBASE_API_KEY")

resp = client.chat.completions.create(
    model="tencent/hy3",
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
| Image input | No | Requests with `image_url` parts fail. Send text only. |
| Reasoning | By default | A two-sentence answer used 206 reasoning tokens. `reasoning_effort` is accepted. |

### Limits and parameters

- Context window: 262,144 tokens.
- Maximum output: 128,000 tokens per request (`max_tokens`).
- The request schema accepts `temperature`, `top_p`, `top_k`, `frequency_penalty`, `presence_penalty`, `seed` and `stop`.
- Leave room in `max_tokens` for reasoning tokens.

### Example response

Real response to "In two sentences, explain what an API gateway does." through Chat Completions, trimmed.

```json
{
  "id": "e9b4b1ff-f52…",
  "object": "chat.completion",
  "model": "tencent/hy3",
  "choices": [
    {
      "index": 0,
      "finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "An API gateway serves as a single entry point and reverse proxy that routes client requests to the appropriate backend services or microservices. It also…"
      }
    }
  ],
  "usage": {
    "completion_tokens": 258,
    "completion_tokens_details": {
      "reasoning_tokens": 206
    },
    "prompt_tokens": 23,
    "prompt_tokens_details": {
      "cache_write_tokens": 0,
      "cached_tokens": 0
    },
    "total_tokens": 281
  }
}
```

### Pricing

| Tokens | Price per 1M |
|---|---|
| Input | $0.132 |
| Output | $0.528 |
| Cached input (read) | $0.033 |

Reasoning tokens are part of `completion_tokens` and are billed at the output price.

### Related models

- [Hy4 preview](/models/tencent/hy4-preview): Tencent's next generation, in preview.
- [DeepSeek V4.1 Flash](/models/deepseek/deepseek-v4.1-flash): a low-cost reasoning model that also reads images.

---
Machine-readable: [`catalog/models/tencent/hy3.json`](../../../catalog/models/tencent/hy3.json) · Store page: https://www.sandbase.ai/model/tencent/hy3

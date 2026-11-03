# Anthropic: Claude Haiku 4.5 API: pricing, parameters and code examples

`anthropic/claude-haiku-4.5` · LLM · Anthropic · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1 input / $5 output per 1M tokens · **Modes:** sync

Claude Haiku 4.5 is Anthropic’s fastest and most efficient model, delivering near-frontier intelligence at a fraction of the cost and latency of larger Claude models. Matching Claude Sonnet 4’s performance across reasoning, coding, and computer-use tasks, Haiku 4.5 brings frontier-level capability to real-time and high-volume applications.

It introduces extended thinking to the Haiku line; enabling controllable reasoning depth, summarized or interleaved thought output, and tool-assisted workflows with full support for coding, bash, web search, and computer-use tools. Scoring >73% on SWE-bench Verified, Haiku 4.5 ranks among the world’s best coding models while maintaining exceptional responsiveness for sub-agents, parallelized execution, and scaled deployment.

## Pricing

- Input **$1** / output **$5** per 1M tokens (USD)
- cache read multiplier: 0.1
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "anthropic/claude-haiku-4.5", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='anthropic/claude-haiku-4.5', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "anthropic/claude-haiku-4.5", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "anthropic/claude-haiku-4.5", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
## Details

Claude Haiku 4.5 is the fast, low-cost tier of Anthropic's Claude 4.5 family. It reads text and images, writes text, and has a 200K-token context window. Anthropic added extended thinking to Haiku with this release; you turn it on per request through the Messages API.

### When to use it

- Real-time chat and support assistants where latency matters.
- Sub-agents that handle many small steps for a larger model.
- Coding help and code review at high volume.

### Call it

The model works on Chat Completions (`/v1/chat/completions`) and on Anthropic's Messages API (`/v1/messages`). Use Messages when you want extended thinking.

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key="$SANDBASE_API_KEY")

resp = client.chat.completions.create(
    model="anthropic/claude-haiku-4.5",
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
| Image input | Yes | `image_url` parts with an https URL or a `data:` URI. |
| Extended thinking | Messages API | Send `thinking: {"type": "enabled", "budget_tokens": 2000}` to `/v1/messages`; the reply starts with a `thinking` block. `reasoning_effort` on Chat Completions has no effect. |
| Structured output | No | `response_format` on Chat Completions and `output_format` on Messages are both ignored; the model answers in prose. Describe the JSON you want in the prompt, or define a tool whose input schema is the shape you need. |

### Limits and parameters

- Context window: 200,000 tokens.
- Maximum output: 64,000 tokens per request (`max_tokens`).
- Accepts `temperature`, `top_p` and `stop` on Chat Completions, and `stop_sequences` on Messages.

### Example response

Real response to "In two sentences, explain what an API gateway does." through Chat Completions, trimmed.

```json
{
  "id": "431cc58b-9b0…",
  "object": "chat.completion",
  "model": "anthropic/claude-haiku-4.5",
  "choices": [
    {
      "index": 0,
      "finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "An API gateway is the single entry point that sits in front of a set of backend services and routes each incoming client request to the service that handles…"
      }
    }
  ],
  "usage": {
    "completion_tokens": 98,
    "completion_tokens_details": {
      "reasoning_tokens": 0
    },
    "prompt_tokens": 18,
    "prompt_tokens_details": {
      "cache_write_tokens": 0,
      "cached_tokens": 0
    },
    "total_tokens": 116
  }
}
```

### Pricing

| Tokens | Price per 1M |
|---|---|
| Input | $1.00 |
| Output | $5.00 |
| Cached input (read) | $0.10 |
| Cache write, 5-minute | $1.25 |
| Cache write, 1-hour | $2.00 |

Prompt caching works through `cache_control` blocks on `/v1/messages`; a repeat call reports the cached prefix as `cache_read_input_tokens`. Reads cost 10% of the input price.

### Related models

- [Claude Haiku 5.5](/models/anthropic/claude-haiku-5.5): the current Haiku tier.
- [Claude Sonnet 4.5](/models/anthropic/claude-sonnet-4.5): the Sonnet model of the same generation, for harder tasks.

---
Machine-readable: [`catalog/models/anthropic/claude-haiku-4.5.json`](../../../catalog/models/anthropic/claude-haiku-4.5.json) · Store page: https://www.sandbase.ai/model/anthropic/claude-haiku-4.5

# DeepSeek: DeepSeek V4.1 Flash API: pricing, parameters and code examples

`deepseek/deepseek-v4.1-flash` · LLM · DeepSeek · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.3 input / $1.2 output per 1M tokens · **Modes:** sync

DeepSeek V4.1 Flash is the smallest model in DeepSeek's V4.1 architecture family, released in September 2026 with native visual understanding. It is a 552B-parameter mixture-of-experts model using a Causal Encoder-Decoder design that activates 8B parameters for input and 16B for output, with a KV cache about a quarter the size of the previous Flash generation. DeepSeek positions it for agentic coding and long-context work and reports it ahead of V4 Pro, replacing V4 Flash and V4 Flash Vision Exp on its API.

## Pricing

- Input **$0.3** / output **$1.2** per 1M tokens (USD)
- cache read multiplier: 0.02

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "deepseek/deepseek-v4.1-flash", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='deepseek/deepseek-v4.1-flash', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "deepseek/deepseek-v4.1-flash", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "deepseek/deepseek-v4.1-flash", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
## Details

DeepSeek V4.1 Flash is the smallest model in DeepSeek's V4.1 family, released in September 2026. It is a 552B-parameter mixture-of-experts model that reads text and images, reasons before it answers, and has a 1M-token context window with up to 384K output tokens. DeepSeek positions it for agentic coding and long-context work.

### When to use it

- Coding agents that read large parts of a repository.
- Long-document question answering and summarization.
- Screenshots and diagrams combined with text in one request.

### Call it

The model works on Chat Completions (`/v1/chat/completions`).

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key="$SANDBASE_API_KEY")

resp = client.chat.completions.create(
    model="deepseek/deepseek-v4.1-flash",
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
| Reasoning | By default | A two-sentence answer used 79 reasoning tokens. `reasoning_effort` is accepted. |

### Limits and parameters

- Context window: 1,048,576 tokens.
- Maximum output: 384,000 tokens per request (`max_tokens`).
- The request schema accepts `temperature`, `top_p`, `top_k`, `frequency_penalty`, `presence_penalty`, `seed` and `stop`.
- Leave room in `max_tokens` for reasoning tokens.

### Example response

Real response to "In two sentences, explain what an API gateway does." through Chat Completions, trimmed.

```json
{
  "id": "7466ca35-539…",
  "object": "chat.completion",
  "model": "deepseek/deepseek-v4.1-flash",
  "choices": [
    {
      "index": 0,
      "finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "An API gateway is a single entry point that receives client requests and routes them to the appropriate backend services. It also handles cross-cutting…"
      }
    }
  ],
  "usage": {
    "completion_tokens": 127,
    "completion_tokens_details": {
      "reasoning_tokens": 79
    },
    "prompt_tokens": 41,
    "prompt_tokens_details": {
      "cache_write_tokens": 0,
      "cached_tokens": 0
    },
    "total_tokens": 168
  }
}
```

### Pricing

| Tokens | Price per 1M |
|---|---|
| Input | $0.30 |
| Output | $1.20 |
| Cached input (read) | $0.006 |

Reasoning tokens are part of `completion_tokens` and are billed at the output price.

### Related models

- [DeepSeek V4 Pro](/models/deepseek/deepseek-v4-pro): DeepSeek's larger V4 model.
- [DeepSeek V4 Flash](/models/deepseek/deepseek-v4-flash): the previous Flash generation.
- [DeepSeek V3](/models/deepseek/deepseek-chat): DeepSeek V3, without reasoning or image input.

---
Machine-readable: [`catalog/models/deepseek/deepseek-v4.1-flash.json`](../../../catalog/models/deepseek/deepseek-v4.1-flash.json) · Store page: https://www.sandbase.ai/model/deepseek/deepseek-v4.1-flash

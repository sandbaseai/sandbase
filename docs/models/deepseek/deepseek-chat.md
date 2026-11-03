# DeepSeek: DeepSeek V3 API: pricing, parameters and code examples

`deepseek/deepseek-chat` · LLM · DeepSeek · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.32 input / $0.89 output per 1M tokens · **Modes:** sync

DeepSeek-V3 is the latest model from the DeepSeek team, building upon the instruction following and coding abilities of the previous versions. Pre-trained on nearly 15 trillion tokens, the reported evaluations reveal that the model outperforms other open-source models and rivals leading closed-source models.

For model details, please visit [the DeepSeek-V3 repo](https://github.com/deepseek-ai/DeepSeek-V3) for more information, or see the [launch announcement](https://api-docs.deepseek.com/news/news1226).

## Pricing

- Input **$0.32** / output **$0.89** per 1M tokens (USD)

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "deepseek/deepseek-chat", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='deepseek/deepseek-chat', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "deepseek/deepseek-chat", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "deepseek/deepseek-chat", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `structured_output`, `function_calling`
## Details

This is DeepSeek V3, the December 2024 DeepSeek chat model, served under the ID `deepseek/deepseek-chat`. It is text-only, does not reason before it answers, and has a 164K-token context window. Use it for general chat and coding when you do not need images or reasoning.

### When to use it

- General chat and writing assistants on a budget.
- Code generation and explanation.
- Tool-calling and JSON-output steps in a pipeline.

### Call it

The model works on Chat Completions (`/v1/chat/completions`).

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key="$SANDBASE_API_KEY")

resp = client.chat.completions.create(
    model="deepseek/deepseek-chat",
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
| Reasoning | No | `reasoning_tokens` is always 0. |

### Limits and parameters

- Context window: 163,840 tokens.
- Maximum output: 16,384 tokens per request (`max_tokens`).
- The request schema accepts `temperature`, `top_p`, `top_k`, `frequency_penalty`, `presence_penalty`, `seed` and `stop`.

### Example response

Real response to "In two sentences, explain what an API gateway does." through Chat Completions, trimmed.

```json
{
  "id": "a8233b6c-efe…",
  "object": "chat.completion",
  "model": "deepseek/deepseek-chat",
  "choices": [
    {
      "index": 0,
      "finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "An API gateway acts as a single entry point for managing and routing API requests between clients and backend services. It handles tasks such as…"
      }
    }
  ],
  "usage": {
    "completion_tokens": 45,
    "completion_tokens_details": {
      "reasoning_tokens": 0
    },
    "prompt_tokens": 14,
    "prompt_tokens_details": {
      "cache_write_tokens": 0,
      "cached_tokens": 0
    },
    "total_tokens": 59
  }
}
```

### Pricing

| Tokens | Price per 1M |
|---|---|
| Input | $0.32 |
| Output | $0.89 |

### Related models

- [DeepSeek V4.1 Flash](/models/deepseek/deepseek-v4.1-flash): DeepSeek's current fast model, with reasoning and image input.
- [DeepSeek V3.2](/models/deepseek/deepseek-v3.2): a later V3 release.
- [DeepSeek V4 Pro](/models/deepseek/deepseek-v4-pro): DeepSeek's larger V4 model.

---
Machine-readable: [`catalog/models/deepseek/deepseek-chat.json`](../../../catalog/models/deepseek/deepseek-chat.json) · Store page: https://www.sandbase.ai/model/deepseek/deepseek-chat

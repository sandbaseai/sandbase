# TypeSafe: Jev 1.14 API: pricing, parameters and code examples

`typesafe/jev-1.14` · LLM · TypeSafe · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.042 input / $0 output per 1M tokens · **Modes:** sync

Jev 1.14 is the latest version of Jev, TypeSafe AI's flagship and first public System One model, which makes structured decisions for software instead of generating text. Given a state and typed questions, it returns a chosen option, a rubric score or the probability that a statement is true, with confidence estimates that code can threshold. Compared with Jev 1.13 it brings small improvements across the board, with the largest gains in multilingual support. TypeSafe positions it for automated decision points that software can branch on, sort or route with, with complex judgments split into atomic questions combined in code.

## Pricing

- Input **$0.042** / output **$0** per 1M tokens (USD)

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "typesafe/jev-1.14", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='typesafe/jev-1.14', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "typesafe/jev-1.14", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "typesafe/jev-1.14", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `decisions`
---
Machine-readable: [`catalog/models/typesafe/jev-1.14.json`](../../../catalog/models/typesafe/jev-1.14.json) · Store page: https://www.sandbase.ai/model/typesafe/jev-1.14

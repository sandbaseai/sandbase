# OpenAI: GPT-6 Astra Pro API: pricing, parameters and code examples

`openai/gpt-6-astra-pro` · LLM · OpenAI · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $10 input / $50 output per 1M tokens · **Modes:** sync

GPT-6 Astra Pro is the same GPT-6 Astra model, OpenAI's most capable GPT-6 tier, served in OpenAI's pro reasoning mode rather than as different weights. In pro mode the model does more work on each request before returning one final answer, which OpenAI suggests for complex optimization, high-value coding or review, and deep analysis. Expect higher latency and token usage than standard Astra, so reserve it for problems where a marginal quality gain changes the outcome.

## Pricing

- Input **$10** / output **$50** per 1M tokens (USD)
- cache read multiplier: 0.1
- cache write multiplier: 1.25

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "openai/gpt-6-astra-pro", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='openai/gpt-6-astra-pro', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "openai/gpt-6-astra-pro", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "openai/gpt-6-astra-pro", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/openai/gpt-6-astra-pro.json`](../../../catalog/models/openai/gpt-6-astra-pro.json) · Store page: https://www.sandbase.ai/model/openai/gpt-6-astra-pro

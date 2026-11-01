# ByteDance: Seed-2.1-Pro

`bytedance/seed-2.1-pro` · llm · Bytedance

Seed 2.1 Pro is the larger of the two models in ByteDance Seed's Seed2.1 family, offered as Doubao-Seed-2.1-Pro through Doubao and Volcano Engine. ByteDance built Seed2.1 for real-world productivity: multi-step general agent work such as planning, document processing and tool use, end-to-end coding from requirement analysis to validation, and computer-use tasks. It also brings strong image, document and long-video understanding, and Seed 2.1 Turbo is the smaller sibling.

## Pricing

- Input **$0.890208** / output **$4.451039** per 1M tokens (USD)
- cache read multiplier: 0.2

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bytedance/seed-2.1-pro", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='bytedance/seed-2.1-pro', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "bytedance/seed-2.1-pro", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "bytedance/seed-2.1-pro", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`
---
Machine-readable: [`catalog/models/bytedance/seed-2.1-pro.json`](../../../catalog/models/bytedance/seed-2.1-pro.json) · Store page: https://www.sandbase.ai/model/bytedance/seed-2.1-pro

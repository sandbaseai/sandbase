# Anthropic: Claude Fable 5.5

`anthropic/claude-fable-5.5` · llm · Anthropic

Claude Fable 5.5 is the expected successor to Claude Fable 5.1, Anthropic's tier above Opus for repository-scale coding, long-running agents and high-stakes review. Anthropic has not officially released it yet; specifications, pricing and API availability will be confirmed at launch.

## Pricing

- Price not published.

## Call it

OpenAI-compatible: any OpenAI SDK works with `base_url=https://api.sandbase.ai/v1`. Anthropic (`/v1/messages`) and Gemini (`/v1beta/models/...`) formats are also accepted.

**curl**

```bash
curl https://api.sandbase.ai/v1/chat/completions \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "anthropic/claude-fable-5.5", "messages": [{"role": "user", "content": "Hello"}]}'
```

**Python**

```python
from openai import OpenAI

client = OpenAI(base_url="https://api.sandbase.ai/v1", api_key=os.environ["SANDBASE_API_KEY"])
resp = client.chat.completions.create(model='anthropic/claude-fable-5.5', messages=[{"role": "user", "content": "Hello"}])
```

**TypeScript**

```ts
import OpenAI from "openai";

const client = new OpenAI({ baseURL: "https://api.sandbase.ai/v1", apiKey: process.env.SANDBASE_API_KEY });
const resp = await client.chat.completions.create({ model: "anthropic/claude-fable-5.5", messages: [{ role: "user", content: "Hello" }] });
```

**Go** ([sdk/go](../../../sdk/go))

```go
resp, err := c.Chat(ctx, "anthropic/claude-fable-5.5", []map[string]any{{"role": "user", "content": "Hello"}}, nil)
```


Capabilities: `chat`, `vision`, `reasoning`, `structured_output`, `function_calling`, `coming-soon`
---
Machine-readable: [`catalog/models/anthropic/claude-fable-5.5.json`](../../../catalog/models/anthropic/claude-fable-5.5.json) · Store page: https://www.sandbase.ai/model/anthropic/claude-fable-5.5

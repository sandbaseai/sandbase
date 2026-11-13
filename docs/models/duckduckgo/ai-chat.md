# DuckDuckGo AI Chat Answer API: pricing, parameters and code examples

`duckduckgo/ai-chat` · data API · DuckDuckGo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get the answer DuckDuckGo's Duck.ai chat gives for a question with a chosen chat model, with answer text and a token for follow-up questions.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "duckduckgo/ai-chat", "q": "How does a heat pump work?"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('duckduckgo/ai-chat', {'q': 'How does a heat pump work?'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("duckduckgo/ai-chat", {
  "q": "How does a heat pump work?"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "duckduckgo/ai-chat", sandbase.Params{
	"q": "How does a heat pump work?",
})
```

Same call via the path form: `POST /v1/api/duckduckgo/ai-chat` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the prompt you want to send to Duck AI, DuckDuckGo's AI chat.  |
| `model` | string |  | Parameter defines the AI model that answers the prompt. It can be set to: `gpt-5.6-luna` - GPT-5.6 Luna `gpt-6-luna` - GPT-6 Luna `gpt-5.4-mini` - GPT-5.4 mini `claude-haiku-4-5` - Claude Haiku 4.5 `mistral-small-2603`…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `subsequent_request_token` | string |  | Parameter defines the token used to continue a Duck AI conversation. Pass this token with a new `q` to send a follow-up prompt that includes the previous prompts and answers as context (multi-turn). The token is…  |

## Details

Get the answer DuckDuckGo's Duck.ai chat gives for a question with a chosen chat model, with answer text and a token for follow-up questions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/duckduckgo/ai-chat" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "How does a heat pump work?"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the prompt you want to send to Duck AI, DuckDuckGo's AI chat. |
| `model` | string | No | Parameter defines the AI model that answers the prompt. It can be set to: `gpt-5.6-luna` - GPT-5.6 Luna `gpt-6-luna` - GPT-6 Luna `gpt-5.4-mini` - GPT-5.4 mini `claude-haiku-4-5` - Claude Haiku 4.5 `mistral-small-2603` - Mistral Small 4 `ti |
| `subsequent_request_token` | string | No | Parameter defines the token used to continue a Duck AI conversation. Pass this token with a new `q` to send a follow-up prompt that includes the previous prompts and answers as context (multi-turn). The token is returned by the API from you |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/duckduckgo/ai-chat.json`](../../../catalog/models/duckduckgo/ai-chat.json) · Store page: https://www.sandbase.ai/model/duckduckgo/ai-chat

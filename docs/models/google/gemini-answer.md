# Google Gemini Answer API: pricing, parameters and code examples

`google/gemini-answer` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get the answer Google Gemini gives for a question in the Gemini web app, with answer text, cited sources and a token for follow-up questions.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/gemini-answer", "q": "How does a heat pump work?"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/gemini-answer', {'q': 'How does a heat pump work?'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/gemini-answer", {
  "q": "How does a heat pump work?"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/gemini-answer", sandbase.Params{
	"q": "How does a heat pump work?",
})
```

Same call via the path form: `POST /v1/api/google/gemini-answer` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the prompt you want to send to Google Gemini.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `subsequent_request_token` | string |  | Parameter defines the token used to continue a Google Gemini conversation. Pass this token with a new `q` to send a follow-up prompt that includes the previous prompts and answers as context (multi-turn). The token is…  |

## Details

Get the answer Google Gemini gives for a question in the Gemini web app, with answer text, cited sources and a token for follow-up questions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/gemini-answer" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "How does a heat pump work?"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the prompt you want to send to Google Gemini. |
| `subsequent_request_token` | string | No | Parameter defines the token used to continue a Google Gemini conversation. Pass this token with a new `q` to send a follow-up prompt that includes the previous prompts and answers as context (multi-turn). The token is returned by the API fr |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/gemini-answer.json`](../../../catalog/models/google/gemini-answer.json) · Store page: https://www.sandbase.ai/model/google/gemini-answer

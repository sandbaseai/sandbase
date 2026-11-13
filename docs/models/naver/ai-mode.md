# Naver AI Mode API: pricing, parameters and code examples

`naver/ai-mode` · data API · Naver · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get Naver's AI-generated answer for a query with the answer text, cited sources and follow-up token for continuing the conversation.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "naver/ai-mode", "query": "서울 맛집 추천"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('naver/ai-mode', {'query': '서울 맛집 추천'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("naver/ai-mode", {
  "query": "서울 맛집 추천"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "naver/ai-mode", sandbase.Params{
	"query": "서울 맛집 추천",
})
```

Same call via the path form: `POST /v1/api/naver/ai-mode` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Parameter defines the query you want to search. You can use anything that you would use in a regular Naver AI Mode search.  |
| `continuable` | string |  | Set parameter to `true` to make the conversation continuable. It defaults to `false`. When set to `true`, the API will return a `subsequent_request_token` in the response which can be used to continue the conversation…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `subsequent_request_token` | string |  | Parameter defines the token used to continue a Naver AI Mode conversation. Pass this token to send a follow-up question that includes the prior exchange as context (multi-turn). The token is returned by the API from…  |

## Details

Get Naver's AI-generated answer for a query with the answer text, cited sources and follow-up token for continuing the conversation.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/naver/ai-mode" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "서울 맛집 추천"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Parameter defines the query you want to search. You can use anything that you would use in a regular Naver AI Mode search. |
| `continuable` | string | No | Set parameter to `true` to make the conversation continuable. It defaults to `false`. When set to `true`, the API will return a `subsequent_request_token` in the response which can be used to continue the conversation with a follow-up quest |
| `subsequent_request_token` | string | No | Parameter defines the token used to continue a Naver AI Mode conversation. Pass this token to send a follow-up question that includes the prior exchange as context (multi-turn). The token is returned by the API from your previous request us |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/naver/ai-mode.json`](../../../catalog/models/naver/ai-mode.json) · Store page: https://www.sandbase.ai/model/naver/ai-mode

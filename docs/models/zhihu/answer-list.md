# Zhihu Answer List API: pricing, parameters and code examples

`zhihu/answer-list` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Get answers for a Zhihu question with sorting and pagination controls. Use it to browse responses to a known question and continue through additional answer pages.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/answer-list", "questionId": "19550225"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/answer-list', {'questionId': '19550225'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/answer-list", {
  "questionId": "19550225"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/answer-list", sandbase.Params{
	"questionId": "19550225",
})
```

Same call via the path form: `POST /v1/api/zhihu/answer-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `order` | string |  | Sorting criteria for answers. one of: `_default`, `_updated`; default `"_updated"` |
| `cursor` | string |  | Pagination cursor from previous result.  |
| `offset` | integer |  | Start offset, begins with 0. default `0` |
| `sessionId` | string |  | Session ID from previous result.  |
| `questionId` | string | yes | Question ID  |

## Details

Get answers for a Zhihu question with sorting and pagination controls. Use it to browse responses to a known question and continue through additional answer pages.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/answer-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"questionId": "19550225"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `questionId` | string | Yes | Question ID |
| `cursor` | string | No | Pagination cursor from previous result. |
| `offset` | integer | No | Start offset, begins with 0. |
| `order` | string | No | Sorting criteria for answers. |
| `sessionId` | string | No | Session ID from previous result. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/zhihu/answer-list.json`](../../../catalog/models/zhihu/answer-list.json) · Store page: https://www.sandbase.ai/model/zhihu/answer-list

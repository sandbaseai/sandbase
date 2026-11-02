# 1688 Factory Search API: pricing, parameters and code examples

`1688/search/factories` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Search 1688 factories and manufacturers by keyword, sorted by default order or repurchase rate.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/search/factories", "keyword": "phone case"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/search/factories', {'keyword': 'phone case'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/search/factories", {
  "keyword": "phone case"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/search/factories", sandbase.Params{
	"keyword": "phone case",
})
```

Same call via the path form: `POST /v1/api/1688/search/factories` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starting at 1. default `1` |
| `sort` | string |  | Factory sort order. one of: `default`, `repurchase_rate`; default `"default"` |
| `keyword` | string | yes | Factory search keyword.  |
| `pageSize` | integer |  | Number of items requested per page. The returned count may differ. default `20` |

## Details

Search 1688 factories and manufacturers by keyword, sorted by default order or repurchase rate.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/search/factories" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "phone case"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Factory search keyword. |
| `page` | integer | No | Page number, starting at 1. |
| `pageSize` | integer | No | Number of items requested per page. The returned count may differ. |
| `sort` | string | No | Factory sort order. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/1688/search/factories.json`](../../../../catalog/models/1688/search/factories.json) · Store page: https://www.sandbase.ai/model/1688/search/factories

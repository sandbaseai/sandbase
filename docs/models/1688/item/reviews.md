# 1688 Product Reviews API: pricing, parameters and code examples

`1688/item/reviews` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Get buyer reviews for a 1688 product by item ID with pagination and default or latest sorting, for supplier and product quality research.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/item/reviews", "itemId": "1046925823679"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/item/reviews', {'itemId': '1046925823679'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/item/reviews", {
  "itemId": "1046925823679"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/item/reviews", sandbase.Params{
	"itemId": "1046925823679",
})
```

Same call via the path form: `POST /v1/api/1688/item/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starting at 1. default `1` |
| `itemId` | string | yes | 1688 product ID.  |
| `sortType` | string |  | Review sort order. one of: `default`, `latest`; default `"default"` |

## Details

Get buyer reviews for a 1688 product by item ID with pagination and default or latest sorting, for supplier and product quality research.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/item/reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "1046925823679"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | 1688 product ID. |
| `page` | integer | No | Page number, starting at 1. |
| `sortType` | string | No | Review sort order. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/1688/item/reviews.json`](../../../../catalog/models/1688/item/reviews.json) · Store page: https://www.sandbase.ai/model/1688/item/reviews

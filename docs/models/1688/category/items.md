# 1688 Category Products API: pricing, parameters and code examples

`1688/category/items` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

List 1688 wholesale products in a category with output language, sort, price, dropshipping and factory filters.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/category/items", "catId": "97"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/category/items', {'catId': '97'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/category/items", {
  "catId": "97"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/category/items", sandbase.Params{
	"catId": "97",
})
```

Same call via the path form: `POST /v1/api/1688/category/items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starting at 1. default `1` |
| `sort` | string |  | Product sort order. one of: `default`, `sales`, `price_up`, `price_down`; default `"default"` |
| `catId` | string | yes | 1688 platform category ID.  |
| `language` | string |  | Output language. one of: `en`, `zh`, `ru`, `vi`, `ja`, `ko`; default `"zh"` |
| `pageSize` | integer |  | Number of items requested per page. The returned count may differ. default `20` |
| `priceEnd` | string |  | Maximum price filter in CNY.  |
| `newArrival` | boolean |  | Filter for new products.  |
| `priceStart` | string |  | Minimum price filter in CNY.  |
| `freeShipping` | boolean |  | Filter for free shipping.  |
| `isSuperFactory` | boolean |  | Optional super-factory filter.  |
| `supportDropshipping` | boolean |  | Filter for support for dropshipping.  |

## Details

List 1688 wholesale products in a category with output language, sort, price, dropshipping and factory filters.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/category/items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"catId": "97", "language": "en"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `catId` | string | Yes | 1688 platform category ID. |
| `language` | string | No | Output language. |
| `page` | integer | No | Page number, starting at 1. |
| `pageSize` | integer | No | Number of items requested per page. The returned count may differ. |
| `sort` | string | No | Product sort order. |
| `priceStart` | string | No | Minimum price filter in CNY. |
| `priceEnd` | string | No | Maximum price filter in CNY. |
| `newArrival` | boolean | No | Filter for new products. |
| `supportDropshipping` | boolean | No | Filter for support for dropshipping. |
| `freeShipping` | boolean | No | Filter for free shipping. |
| `isSuperFactory` | boolean | No | Optional super-factory filter. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/1688/category/items.json`](../../../../catalog/models/1688/category/items.json) · Store page: https://www.sandbase.ai/model/1688/category/items

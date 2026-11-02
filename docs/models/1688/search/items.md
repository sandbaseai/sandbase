# 1688 Product Search API: pricing, parameters and code examples

`1688/search/items` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search 1688 wholesale products by keyword with price, minimum order quantity, tiered prices, sales, repurchase rate and delivery info. Sort and filter by price, MOQ, dropshipping, free shipping and factory.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/search/items", "keyword": "蓝牙耳机"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/search/items', {'keyword': '蓝牙耳机'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/search/items", {
  "keyword": "蓝牙耳机"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/search/items", sandbase.Params{
	"keyword": "蓝牙耳机",
})
```

Same call via the path form: `POST /v1/api/1688/search/items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `moq` | integer |  | Minimum order quantity filter.  |
| `page` | integer |  | Page number, starting at 1. default `1` |
| `sort` | string |  | Product sort order. one of: `default`, `sales`, `price_up`, `price_down`; default `"default"` |
| `keyword` | string | yes | Search keyword.  |
| `pageSize` | integer |  | Number of items requested per page. The returned count may differ. default `20` |
| `priceEnd` | string |  | Maximum price filter in CNY.  |
| `newArrival` | boolean |  | Filter for new products.  |
| `priceStart` | string |  | Minimum price filter in CNY.  |
| `freeShipping` | boolean |  | Filter for free shipping.  |
| `isSuperFactory` | boolean |  | Optional super-factory filter.  |
| `supportDropshipping` | boolean |  | Filter for support for dropshipping.  |

## Details

Search 1688 wholesale products by keyword with price, minimum order quantity, tiered prices, sales, repurchase rate and delivery info. Sort and filter by price, MOQ, dropshipping, free shipping and factory.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/search/items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "蓝牙耳机"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `page` | integer | No | Page number, starting at 1. |
| `pageSize` | integer | No | Number of items requested per page. The returned count may differ. |
| `sort` | string | No | Product sort order. |
| `moq` | integer | No | Minimum order quantity filter. |
| `priceStart` | string | No | Minimum price filter in CNY. |
| `priceEnd` | string | No | Maximum price filter in CNY. |
| `newArrival` | boolean | No | Filter for new products. |
| `supportDropshipping` | boolean | No | Filter for support for dropshipping. |
| `freeShipping` | boolean | No | Filter for free shipping. |
| `isSuperFactory` | boolean | No | Optional super-factory filter. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/1688/search/items.json`](../../../../catalog/models/1688/search/items.json) · Store page: https://www.sandbase.ai/model/1688/search/items

# Taobao Shop Products API: pricing, parameters and code examples

`taobao/shop/items` · data API · Taobao · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

List products in a Taobao or Tmall shop by seller ID and shop ID, with optional keyword search, shop-category filter, sorting and pagination.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "taobao/shop/items", "sellerId": "1659916565", "shopId": "103710607"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('taobao/shop/items', {'sellerId': '1659916565', 'shopId': '103710607'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("taobao/shop/items", {
  "sellerId": "1659916565",
  "shopId": "103710607"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "taobao/shop/items", sandbase.Params{
	"sellerId": "1659916565",
	"shopId": "103710607",
})
```

Same call via the path form: `POST /v1/api/taobao/shop/items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starting from 1. default `1` |
| `sort` | string |  | Product sort order. one of: `comprehensive`, `sales`, `new`, `price-asc`, `price-desc`; default `"comprehensive"` |
| `catId` | string |  | Shop category ID from Shop Detail. Omit to include all shop categories.  |
| `shopId` | string | yes | Taobao shop ID associated with the seller.  |
| `keyword` | string |  | Keyword to search for products within the shop. Omit to list products without a keyword filter.  |
| `sellerId` | string | yes | Taobao seller user ID associated with the shop.  |

## Details

List products in a Taobao or Tmall shop by seller ID and shop ID, with optional keyword search, shop-category filter, sorting and pagination.

The result is returned in `outputs[0].data` in the platform's original structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/taobao/shop/items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sellerId": "1659916565", "shopId": "103710607"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sellerId` | string | Yes | Taobao seller user ID associated with the shop. |
| `shopId` | string | Yes | Taobao shop ID associated with the seller. |
| `catId` | string | No | Shop category ID from Shop Detail. Omit to include all shop categories. |
| `keyword` | string | No | Keyword to search for products within the shop. Omit to list products without a keyword filter. |
| `sort` | string | No | Product sort order. |
| `page` | integer | No | Page number, starting from 1. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/taobao/shop/items.json`](../../../../catalog/models/taobao/shop/items.json) · Store page: https://www.sandbase.ai/model/taobao/shop/items

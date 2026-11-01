# 1688 Image Search

`1688/search/by-image` · api · 1688

Find 1688 wholesale products that match an image URL, with prices, minimum order quantity and supplier info. Sort and filter by price, MOQ, factory, verified supplier and shipping.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/search/by-image", "imgUrl": "https://cbu01.alicdn.com/img/ibank/O1CN01Z5b6Ax1Bs2nVv6E3n_!!2216226597326-0-cib.jpg"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/search/by-image', {'imgUrl': 'https://cbu01.alicdn.com/img/ibank/O1CN01Z5b6Ax1Bs2nVv6E3n_!!2216226597326-0-cib.jpg'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/search/by-image", {
  "imgUrl": "https://cbu01.alicdn.com/img/ibank/O1CN01Z5b6Ax1Bs2nVv6E3n_!!2216226597326-0-cib.jpg"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/search/by-image", sandbase.Params{
	"imgUrl": "https://cbu01.alicdn.com/img/ibank/O1CN01Z5b6Ax1Bs2nVv6E3n_!!2216226597326-0-cib.jpg",
})
```

Same call via the path form: `POST /v1/api/1688/search/by-image` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `moq` | integer |  | Minimum order quantity filter.  |
| `page` | integer |  | Page number, starting at 1. default `1` |
| `sort` | string |  | Product sort order. one of: `default`, `sales`, `price_up`, `price_down`; default `"default"` |
| `imgUrl` | string | yes | Image URL or image reference returned by Image Conversion. Convert external images for the selected search target before searching.  |
| `pageSize` | integer |  | Number of items requested per page. The returned count may differ. default `20` |
| `priceEnd` | string |  | Maximum price filter in CNY.  |
| `isFactory` | boolean |  | Filter by factory status.  |
| `newArrival` | boolean |  | Filter for new products.  |
| `priceStart` | string |  | Minimum price filter in CNY.  |
| `freeShipping` | boolean |  | Filter for free shipping.  |
| `verifiedSupplier` | boolean |  | Filter for verified sellers.  |
| `supportDropshipping` | boolean |  | Filter for support for dropshipping.  |

## Details

Find 1688 wholesale products that match an image URL, with prices, minimum order quantity and supplier info. Sort and filter by price, MOQ, factory, verified supplier and shipping.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/search/by-image" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"imgUrl": "https://cbu01.alicdn.com/img/ibank/O1CN01dVDdAa1g2z0YPmnXe_!!2218348464085-0-cib.jpg"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `imgUrl` | string | Yes | Image URL or image reference returned by Image Conversion. Convert external images for the selected search target before searching. |
| `page` | integer | No | Page number, starting at 1. |
| `pageSize` | integer | No | Number of items requested per page. The returned count may differ. |
| `sort` | string | No | Product sort order. |
| `moq` | integer | No | Minimum order quantity filter. |
| `priceStart` | string | No | Minimum price filter in CNY. |
| `priceEnd` | string | No | Maximum price filter in CNY. |
| `supportDropshipping` | boolean | No | Filter for support for dropshipping. |
| `isFactory` | boolean | No | Filter by factory status. |
| `verifiedSupplier` | boolean | No | Filter for verified sellers. |
| `freeShipping` | boolean | No | Filter for free shipping. |
| `newArrival` | boolean | No | Filter for new products. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/1688/search/by-image.json`](../../../../catalog/models/1688/search/by-image.json) · Store page: https://www.sandbase.ai/model/1688/search/by-image

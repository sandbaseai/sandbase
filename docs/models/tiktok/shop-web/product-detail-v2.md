# TikTok Shop Product Details (V2) API: pricing, parameters and code examples

`tiktok/shop-web/product-detail-v2` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns basic product details from TikTok Shop for a specified item. Query by product identifier with optional region and seller filters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/shop-web/product-detail-v2", "product_id": "1731581114818794403", "region": "GB"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/shop-web/product-detail-v2', {'product_id': '1731581114818794403', 'region': 'GB'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/shop-web/product-detail-v2", {
  "product_id": "1731581114818794403",
  "region": "GB"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/shop-web/product-detail-v2", sandbase.Params{
	"product_id": "1731581114818794403",
	"region": "GB",
})
```

Same call via the path form: `POST /v1/api/tiktok/shop-web/product-detail-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Region code (US/GB/SG/MY/PH/TH/VN/ID)  |
| `seller_id` | string |  | Seller ID (can be empty string)  |
| `product_id` | string | yes | Product ID (required)  |

## Details

Retrieve TikTok Shop product information by supplying a `product_id`. You can also narrow results by setting `region` and `seller_id`.

### Use cases

- Inspect basic product metadata on TikTok Shop.
- Monitor specific shop inventory across supported countries.
- Track individual TikTok Shop listings by product ID.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/product-detail-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "<product_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Product ID (required) |
| `region` | string | No | Region code (US/GB/SG/MY/PH/TH/VN/ID) |
| `seller_id` | string | No | Seller ID (can be empty string) |

### Notes

- Supported `region` codes include US, GB, SG, MY, PH, TH, VN, and ID.
- `seller_id` can be left as an empty string if unknown.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Shop Product Details](/apis/tiktok/shop-web/product-detail): Retrieves full product details and page component information from TikTok Shop by product ID.
- [TikTok Shop Product Detail (V3)](/apis/tiktok/shop-web/product-detail-v3): Returns comprehensive TikTok Shop product data including shop information, videos, and recommendations for a given product ID across supported regions.
- [TikTok Shop Product ID by Share Link](/apis/tiktok/shop-web/product-id-by-share-link): Returns the TikTok Shop product identifier extracted from a provided product share link.

---
Machine-readable: [`catalog/models/tiktok/shop-web/product-detail-v2.json`](../../../../catalog/models/tiktok/shop-web/product-detail-v2.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/product-detail-v2

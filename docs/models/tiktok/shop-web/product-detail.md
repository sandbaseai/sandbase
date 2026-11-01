# TikTok Shop Product Details

`tiktok/shop-web/product-detail` · api · TikTok

Retrieves full product details and page component information from TikTok Shop by product ID. Supports regional filtering across markets such as the US, UK, and Southeast Asia.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/shop-web/product-detail", "product_id": "1732108663255959373"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/shop-web/product-detail', {'product_id': '1732108663255959373'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/shop-web/product-detail", {
  "product_id": "1732108663255959373"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/shop-web/product-detail", sandbase.Params{
	"product_id": "1732108663255959373",
})
```

Same call via the path form: `POST /v1/api/tiktok/shop-web/product-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Region code (US/GB/SG/MY/PH/TH/VN/ID) default `"MY"` |
| `seller_id` | string |  | Seller ID (can be empty string) default `""` |
| `product_id` | string | yes | Product ID (required)  |

## Details

Retrieve comprehensive product information from TikTok Shop using `product_id`. Optionally filter by `region` and `seller_id` to inspect localized catalog entries.

### Use cases

- Inspect detailed TikTok Shop product page components and data.
- Monitor specific TikTok Shop listings across supported regional markets.
- Analyze product information by combining product and seller identifiers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/product-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "1732108663255959373"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Product ID (required) |
| `region` | string | No | Region code (US/GB/SG/MY/PH/TH/VN/ID) |
| `seller_id` | string | No | Seller ID (can be empty string) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "components_map": [
      {
        "component_name": "top_reviewed_products",
        "component_type": "top_reviewed_products"
      }
    ]
  }
}
```

### Notes

- `product_id` is required.
- Supported values for `region` include US, GB, SG, MY, PH, TH, VN, and ID.
- `seller_id` can be passed as an empty string.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Shop Product Details (V2)](/model/tiktok/shop-web/product-detail-v2): Returns basic product details from TikTok Shop for a specified item.
- [TikTok Shop Product Detail (V3)](/model/tiktok/shop-web/product-detail-v3): Returns comprehensive TikTok Shop product data including shop information, videos, and recommendations for a given product ID across supported regions.
- [TikTok Shop Product ID by Share Link](/model/tiktok/shop-web/product-id-by-share-link): Returns the TikTok Shop product identifier extracted from a provided product share link.

---
Machine-readable: [`catalog/models/tiktok/shop-web/product-detail.json`](../../../../catalog/models/tiktok/shop-web/product-detail.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/product-detail

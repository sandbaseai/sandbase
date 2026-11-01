# TikTok Shop Product Detail (V3)

`tiktok/shop-web/product-detail-v3` · api · TikTok

Returns comprehensive TikTok Shop product data including shop information, videos, and recommendations for a given product ID across supported regions.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/shop-web/product-detail-v3", "product_id": "1732108663255959373"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/shop-web/product-detail-v3', {'product_id': '1732108663255959373'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/shop-web/product-detail-v3", {
  "product_id": "1732108663255959373"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/shop-web/product-detail-v3", sandbase.Params{
	"product_id": "1732108663255959373",
})
```

Same call via the path form: `POST /v1/api/tiktok/shop-web/product-detail-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Region code (US/GB/SG/MY/PH/TH/VN/ID) default `"SG"` |
| `product_id` | string | yes | Product ID (required)  |

## Details

Retrieve detailed TikTok Shop product information by supplying a required `product_id`. An optional `region` parameter can also be supplied to target specific regional marketplaces.

### Use cases

- Retrieve complete product page components and metadata.
- Extract shop details and related video recommendations.
- Inspect regional product listings across supported territories.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/product-detail-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "1732108663255959373"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Product ID (required) |
| `region` | string | No | Region code (US/GB/SG/MY/PH/TH/VN/ID) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "product_data": {
    "page_config": {
      "components_map": [
        {
          "component_name": "user_info",
          "component_type": "user_info"
        }
      ]
    }
  }
}
```

### Notes

- Supported values for `region` include US, GB, SG, MY, PH, TH, VN, and ID.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Shop Product Details](/model/tiktok/shop-web/product-detail): Retrieves full product details and page component information from TikTok Shop by product ID.
- [TikTok Shop Product Details (V2)](/model/tiktok/shop-web/product-detail-v2): Returns basic product details from TikTok Shop for a specified item.
- [TikTok Shop Product ID by Share Link](/model/tiktok/shop-web/product-id-by-share-link): Returns the TikTok Shop product identifier extracted from a provided product share link.

---
Machine-readable: [`catalog/models/tiktok/shop-web/product-detail-v3.json`](../../../../catalog/models/tiktok/shop-web/product-detail-v3.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/product-detail-v3

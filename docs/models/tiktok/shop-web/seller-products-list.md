# TikTok Seller Products List API: pricing, parameters and code examples

`tiktok/shop-web/seller-products-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns product listings and SKU details for a designated TikTok Shop merchant. Filter items by seller ID, target region, and pagination parameters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/shop-web/seller-products-list", "seller_id": "7495150558072178725"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/shop-web/seller-products-list', {'seller_id': '7495150558072178725'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/shop-web/seller-products-list", {
  "seller_id": "7495150558072178725"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/shop-web/seller-products-list", sandbase.Params{
	"seller_id": "7495150558072178725",
})
```

Same call via the path form: `POST /v1/api/tiktok/shop-web/seller-products-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Region code (US/GB/SG/MY/PH/TH/VN/ID) default `"US"` |
| `seller_id` | string | yes | Seller ID (required)  |
| `search_params` | string |  | Search parameters for pagination (optional) default `""` |

## Details

Look up product listings from a TikTok Shop merchant by passing `seller_id`. You can also target a specific marketplace using `region` and navigate through pages using `search_params`.

### Use cases

- Retrieve product catalogs and SKU data for a TikTok Shop seller.
- Monitor merchandise offerings across supported regional storefronts.
- Collect merchant inventory data for competitive retail analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/seller-products-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"seller_id": "7495150558072178725"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `seller_id` | string | Yes | Seller ID (required) |
| `region` | string | No | Region code (US/GB/SG/MY/PH/TH/VN/ID) |
| `search_params` | string | No | Search parameters for pagination (optional) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "products": [
      {
        "sku_info": [
          {
            "PriceInfo": {
              "currency_name": "USD",
              "sale_price_decimal": "63.7",
              "sale_price_decimal_part_format": "70",
              "sale_price_format": "63.70",
              "sale_price_integer_part_format": "63",
              "single_product_price_decimal": "63.7"
            }
          }
        ]
      }
    ]
  }
}
```

### Notes

- Supported `region` values include US, GB, SG, MY, PH, TH, VN, and ID.
- Use `search_params` to paginate through product results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Shop Product Details](/model/tiktok/shop-web/product-detail): Retrieves full product details and page component information from TikTok Shop by product ID.
- [TikTok Shop Product Details (V2)](/model/tiktok/shop-web/product-detail-v2): Returns basic product details from TikTok Shop for a specified item.
- [TikTok Shop Product Detail (V3)](/model/tiktok/shop-web/product-detail-v3): Returns comprehensive TikTok Shop product data including shop information, videos, and recommendations for a given product ID across supported regions.

---
Machine-readable: [`catalog/models/tiktok/shop-web/seller-products-list.json`](../../../../catalog/models/tiktok/shop-web/seller-products-list.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/seller-products-list

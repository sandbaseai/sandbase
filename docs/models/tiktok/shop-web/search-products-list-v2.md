# TikTok Shop Product Search (V2) API: pricing, parameters and code examples

`tiktok/shop-web/search-products-list-v2` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns search results for items listed on TikTok Shop by keyword, including ratings, seller details, and sales volume across supported regions.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/shop-web/search-products-list-v2", "region": "US", "search_word": "coffee"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/shop-web/search-products-list-v2', {'region': 'US', 'search_word': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/shop-web/search-products-list-v2", {
  "region": "US",
  "search_word": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/shop-web/search-products-list-v2", sandbase.Params{
	"region": "US",
	"search_word": "coffee",
})
```

Same call via the path form: `POST /v1/api/tiktok/shop-web/search-products-list-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Offset (default 0) default `0` |
| `region` | string |  | Region code (US/GB/SG/MY/PH/TH/VN/ID) default `"US"` |
| `page_token` | string |  | Page token default `""` |
| `search_word` | string | yes | Search keyword (required)  |

## Details

Search for products on TikTok Shop using a required `search_word` keyword and optional regional filtering.

### Use cases

- Discover trending TikTok Shop merchandise for specific search queries.
- Compare regional product availability and seller information across markets.
- Monitor catalog listings and sales metrics for competitive research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/search-products-list-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_word": "coffee"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `search_word` | string | Yes | Search keyword (required) |
| `offset` | integer | No | Offset (default 0) |
| `region` | string | No | Region code (US/GB/SG/MY/PH/TH/VN/ID) |
| `page_token` | string | No | Page token |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "component_data": {
      "products": [
        {
          "product_id": "1732722489403216265",
          "title": "（Flash Sale 3 X）RYZE Mushroom Coffee USDA Organic with 6 Adaptogenic Mushrooms and MCT Oi…",
          "product_price_info": {
            "currency_name": "USD",
            "price_prefix": "From",
            "sale_price_decimal": "11.99",
            "sale_price_decimal_part_format": "99",
            "sale_price_format": "11.99",
            "sale_price_integer_part_format": "11"
          },
          "rate_info": {
            "review_count": "0",
            "score": 0
          },
          "seller_info": {
            "seller_id": "7494946156944000393",
            "shop_name": "Loud The Glass"
          },
          "seo_url": {
            "canonical_url": "https://shop.tiktok.com/us/pdp/1732722489403216265",
            "type": 1,
            "updated_at": "0"
          },
          "sold_info": {
            "sold_count": 1
          }
        }
      ]
    }
  }
}
```

### Notes

- Supported `region` codes include US, GB, SG, MY, PH, TH, VN, and ID.
- Pagination is handled via `offset` and `page_token` parameters.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Shop Product Details](/model/tiktok/shop-web/product-detail): Retrieves full product details and page component information from TikTok Shop by product ID.
- [TikTok Shop Product Details (V2)](/model/tiktok/shop-web/product-detail-v2): Returns basic product details from TikTok Shop for a specified item.
- [TikTok Shop Product Detail (V3)](/model/tiktok/shop-web/product-detail-v3): Returns comprehensive TikTok Shop product data including shop information, videos, and recommendations for a given product ID across supported regions.

---
Machine-readable: [`catalog/models/tiktok/shop-web/search-products-list-v2.json`](../../../../catalog/models/tiktok/shop-web/search-products-list-v2.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/search-products-list-v2

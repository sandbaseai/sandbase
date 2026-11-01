# TikTok Shop Product Search

`tiktok/shop-web/search-products-list` · api · TikTok

Searches TikTok Shop listings matching a keyword query and returns product details, seller profiles, ratings, and sales figures. Supports region filtering and pagination.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/shop-web/search-products-list", "offset": 0, "page_token": "", "region": "VN", "search_word": "áo khoác zip bé"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/shop-web/search-products-list', {'offset': 0, 'page_token': '', 'region': 'VN', 'search_word': 'áo khoác zip bé'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/shop-web/search-products-list", {
  "offset": 0,
  "page_token": "",
  "region": "VN",
  "search_word": "áo khoác zip bé"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/shop-web/search-products-list", sandbase.Params{
	"offset": 0,
	"page_token": "",
	"region": "VN",
	"search_word": "áo khoác zip bé",
})
```

Same call via the path form: `POST /v1/api/tiktok/shop-web/search-products-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Offset for pagination (default 0) default `0` |
| `region` | string |  | Region code (US/GB/SG/MY/PH/TH/VN/ID) default `"US"` |
| `page_token` | string |  | Page token for next page default `""` |
| `search_word` | string | yes | Search keyword (required)  |

## Details

Query TikTok Shop listings by specifying a keyword via `search_word` alongside optional region targeting and pagination parameters.

### Use cases

- Search TikTok Shop catalogs for relevant items by keyword.
- Monitor competitor sales volume and product performance within specific regions.
- Retrieve seller profiles and ratings associated with searched merchandise.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/search-products-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"search_word": "coffee"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `search_word` | string | Yes | Search keyword (required) |
| `offset` | integer | No | Offset for pagination (default 0) |
| `region` | string | No | Region code (US/GB/SG/MY/PH/TH/VN/ID) |
| `page_token` | string | No | Page token for next page |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "products": [
      {
        "product_id": "1732307512139747336",
        "title": "coffee cup",
        "product_price_info": {
          "currency_name": "USD",
          "sale_price_decimal": "1",
          "sale_price_decimal_part_format": "00",
          "sale_price_format": "1.00",
          "sale_price_integer_part_format": "1",
          "single_product_price_decimal": "1"
        },
        "rate_info": {
          "review_count": "0",
          "score": 0
        },
        "seller_info": {
          "seller_id": "7495365574818695176",
          "shop_name": "A&R things"
        },
        "seo_url": {
          "canonical_url": "https://shop.tiktok.com/us/pdp/coffee-cup-perfect-for-espresso-cappuccino-lovers…",
          "type": 2,
          "updated_at": "1775059203403"
        },
        "sold_info": {
          "sold_count": 2
        }
      }
    ]
  }
}
```

### Notes

- Supported `region` values include US, GB, SG, MY, PH, TH, VN, and ID.
- Pagination can be controlled using `offset` (default 0) or `page_token` for sequential pages.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Shop Product Details](/model/tiktok/shop-web/product-detail): Retrieves full product details and page component information from TikTok Shop by product ID.
- [TikTok Shop Product Details (V2)](/model/tiktok/shop-web/product-detail-v2): Returns basic product details from TikTok Shop for a specified item.
- [TikTok Shop Product Detail (V3)](/model/tiktok/shop-web/product-detail-v3): Returns comprehensive TikTok Shop product data including shop information, videos, and recommendations for a given product ID across supported regions.

---
Machine-readable: [`catalog/models/tiktok/shop-web/search-products-list.json`](../../../../catalog/models/tiktok/shop-web/search-products-list.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/search-products-list

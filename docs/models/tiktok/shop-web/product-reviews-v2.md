# TikTok Shop Product Reviews

`tiktok/shop-web/product-reviews-v2` · api · TikTok

Get TikTok Shop product reviews by product ID: rating, review text, SKU, reviewer country and time, with star filters, sorting and pagination across regions.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/shop-web/product-reviews-v2", "product_id": "1729408816995078528"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/shop-web/product-reviews-v2', {'product_id': '1729408816995078528'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/shop-web/product-reviews-v2", {
  "product_id": "1729408816995078528"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/shop-web/product-reviews-v2", sandbase.Params{
	"product_id": "1729408816995078528",
})
```

Same call via the path form: `POST /v1/api/tiktok/shop-web/product-reviews-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Region code, available regions are as follows: US: United States; SG: Singapore; MY: Malaysia; PH: Philippines; TH: Thailand; VN: Vietnam; ID: Indonesia; JP: Japan; MX: Mexico default `"US"` |
| `sort_rule` | integer |  | Sort rule, default 2 default `2` |
| `page_start` | integer |  | Starting page number, default 1 default `1` |
| `product_id` | string | yes | Product ID (required)  |
| `filter_type` | integer |  | Filter type default `1` |
| `filter_value` | integer |  | Star filter default `6` |

## Details

Pass a TikTok Shop product ID and get customer reviews with ratings and review text. Filter by stars and choose the region.

### Use cases

- Analyze customer feedback on products.
- Monitor competitor product reviews.
- Find product issues from low-star reviews.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/product-reviews-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "1729408816995078528"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Product ID (required) |
| `region` | string | No | Region code, available regions are as follows: US: United States; SG: Singapore; MY: Malaysia; PH: Philippines; TH: Tha… |
| `sort_rule` | integer | No | Sort rule, default 2 |
| `page_start` | integer | No | Starting page number, default 1 |
| `filter_type` | integer | No | Filter type |
| `filter_value` | integer | No | Star filter |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "total_reviews": "12035",
    "product_reviews": [
      {
        "review_id": "7693380094657398541",
        "product_id": "1729408816995078528",
        "review_rating": 5,
        "review_time": "1791254704159",
        "review_country": "US",
        "sku_specification": "90 Count (1 Month Supply)",
        "review_text": "Only been taking for a few weeks but I'm expecting great th…",
        "reviewer_name": "D**"
      }
    ]
  }
}
```

### Notes

- `region`: US, SG, MY, PH, TH, VN, ID and more.
- Paginate with `page_start`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Get product detail V1(Full data)](/model/tiktok/shop-web/product-detail): if so, try using `fetch_product_detail_v3`.
- [Get product detail V2 (Less Data)](/model/tiktok/shop-web/product-detail-v2): for more complete data, use `fetch_product_detail` or `fetch_product_detail_v3`.
- [Get product detail V3 (Full Data)](/model/tiktok/shop-web/product-detail-v3): Get TikTok Shop product details Provides the most complete product information including recommendations, videos, shop info, etc..

---
Machine-readable: [`catalog/models/tiktok/shop-web/product-reviews-v2.json`](../../../../catalog/models/tiktok/shop-web/product-reviews-v2.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/product-reviews-v2

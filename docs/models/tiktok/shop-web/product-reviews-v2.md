# TikTok Shop Product Reviews API: pricing, parameters and code examples

`tiktok/shop-web/product-reviews-v2` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get TikTok Shop product reviews by product ID: rating, review text, SKU, reviewer country and time, with star filters, sorting and pagination across regions.

## Pricing

- **$0.001 per call** (USD)
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

Returns customer reviews for a TikTok Shop product, with star rating, review text, purchased SKU, reviewer country and review time. It also returns the product's overall score and a count of reviews per star. The only required input is `product_id`.

### Use cases

- Read the newest reviews for a competitor product and track what buyers praise or complain about.
- Pull low-star reviews of your own product to find repeated problems.
- Compare the star breakdown of the same product across regions.
- Group reviews by `sku_specification` to see which variant gets the best ratings.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop-web/product-reviews-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "1729408816995078528"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Product ID (required) |
| `filter_type` | integer | No | Filter type |
| `filter_value` | integer | No | Star filter |
| `page_start` | integer | No | Starting page number, default 1 |
| `region` | string | No | Region code, available regions are as follows: US: United States; SG: Singapore; MY: Malaysia; PH: Philippines; TH: Thailand; VN: Vietnam; ID: Indonesia; JP: Japan; MX: Mexico |
| `sort_rule` | integer | No | Sort rule, default 2 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "has_more": true,
    "product_reviews": [
      {
        "display_image_url": "https://p16-oec-general-useast5.ttcdn-us.com/tos-useast5-i-omjb5zjo8w-tx/38ba06c…",
        "is_incentivized_review": false,
        "is_verified_purchase": true,
        "product_id": "1729408816995078528",
        "product_name": "Zoyava Collagen Supplement - Type I, II, III, V and X - with Biotin, Keratin, Hy…",
        "review_country": "US",
        "review_id": "7703793193254684429",
        "review_images": [],
        "review_rating": 5,
        "review_text": "",
        "review_time": "1793679163277",
        "reviewer_avatar_url": "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/9dee922b3d0d844…"
      }
    ],
    "review_ratings": {
      "overall_score": 4.5,
      "rating_result": {
        "1": "822",
        "2": "239",
        "3": "616",
        "4": "993",
        "5": "10170"
      },
      "review_count": "12840"
    },
    "total_reviews": "12840"
  },
  "message": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.product_reviews[].review_id` | ID of the review. |
| `data.product_reviews[].review_rating` | Star rating given in this review, from 1 to 5. |
| `data.product_reviews[].review_text` | Text written by the reviewer. It can be an empty string when the buyer left only a rating. |
| `data.product_reviews[].review_time` | Time the review was posted, as a millisecond timestamp in a string. |
| `data.product_reviews[].sku_id / data.product_reviews[].sku_specification` | ID and label of the variant the reviewer bought, such as a pack size. |
| `data.product_reviews[].is_verified_purchase / data.product_reviews[].is_incentivized_review` | Flags that show whether the review comes from a verified purchase and whether it was incentivized. |
| `data.product_reviews[].review_country / data.product_reviews[].reviewer_name` | Country code of the review and the masked name of the reviewer. |
| `data.product_reviews[].review_images` | List of images attached to the review. It is empty when the buyer added none. |
| `data.review_ratings.overall_score / data.review_ratings.rating_result` | Average score for the product and the number of reviews for each star level, keyed `1` to `5`. |
| `data.total_reviews / data.has_more` | Total number of reviews for the product, and whether more reviews are available on later pages. |

### Notes

- Counts such as `total_reviews`, `review_count` and the values in `rating_result` are strings, not numbers.
- Request the next page by raising `page_start`. Keep going while `has_more` is `true`.
- Use `region` to pick the market, for example `US`, `SG`, `MY`, `PH`, `TH`, `VN`, `ID`, `JP` or `MX`. Use `filter_value` for the star filter.
- If you only have a share link, call [TikTok Shop Product ID by Share Link](/apis/tiktok/shop-web/product-id-by-share-link) to get the `product_id`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Get product detail V1(Full data)](/apis/tiktok/shop-web/product-detail): if so, try using `fetch_product_detail_v3`.
- [Get product detail V2 (Less Data)](/apis/tiktok/shop-web/product-detail-v2): for more complete data, use `fetch_product_detail` or `fetch_product_detail_v3`.
- [Get product detail V3 (Full Data)](/apis/tiktok/shop-web/product-detail-v3): Get TikTok Shop product details Provides the most complete product information including recommendations, videos, shop info, etc..

---
Machine-readable: [`catalog/models/tiktok/shop-web/product-reviews-v2.json`](../../../../catalog/models/tiktok/shop-web/product-reviews-v2.json) · Store page: https://www.sandbase.ai/model/tiktok/shop-web/product-reviews-v2

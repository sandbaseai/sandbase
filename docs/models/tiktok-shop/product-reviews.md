# TikTok Shop Product Reviews API: pricing, parameters and code examples

`tiktok-shop/product-reviews` · data API · TikTok Shop · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00095 per call · **Modes:** sync

Fetch customer reviews for a TikTok Shop product by URL (rating, text, reviewer, country, and verified-buyer flag).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00095**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok-shop/product-reviews", "url": "https://www.tiktok.com/shop/pdp/cat-nail-clipper-by-potaroma-adjustable-sizes-built-in-file-safe-for-kittens-cats/1731578642912612516"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok-shop/product-reviews', {'url': 'https://www.tiktok.com/shop/pdp/cat-nail-clipper-by-potaroma-adjustable-sizes-built-in-file-safe-for-kittens-cats/1731578642912612516'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok-shop/product-reviews", {
  "url": "https://www.tiktok.com/shop/pdp/cat-nail-clipper-by-potaroma-adjustable-sizes-built-in-file-safe-for-kittens-cats/1731578642912612516"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok-shop/product-reviews", sandbase.Params{
	"url": "https://www.tiktok.com/shop/pdp/cat-nail-clipper-by-potaroma-adjustable-sizes-built-in-file-safe-for-kittens-cats/1731578642912612516",
})
```

Same call via the path form: `POST /v1/api/tiktok-shop/product-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | TikTok Shop product URL (e.g. https://www.tiktok.com/shop/pdp/.../1729385633899532161).  |
| `page` | integer |  | 1-based results page. Use with hasMore in the output to paginate. default `1`; range 1– |
| `region` | string |  | Two-letter country code of the product's shop region (e.g. US). Strongly recommended for correct results.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `images`, and it is served only by a source that returns every one…  |

## Details

Returns customer reviews for one TikTok Shop product, including the star rating, review text, reviewer name, country, and a verified-purchase flag. It needs a TikTok Shop product URL. The response also gives the product's overall rating and total review count.

### Use cases

- Collect review text for a product to run sentiment analysis on customer complaints and praise.
- Track the average `rating` and `totalReviews` of a competing product over time.
- Pull review photos from `images` to see how buyers use the product.
- Filter on `verifiedPurchase` to study only reviews from confirmed buyers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok-shop/product-reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/shop/pdp/cat-nail-clipper-by-potaroma-adjustable-sizes-built-in-file-safe-for-kittens-cats/1731578642912612516"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | TikTok Shop product URL (e.g. https://www.tiktok.com/shop/pdp/.../1729385633899532161). |
| `page` | integer | No | 1-based results page. Use with hasMore in the output to paginate. |
| `region` | string | No | Two-letter country code of the product's shop region (e.g. US). Strongly recommended for correct results. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `images`, and it is served only by a source that returns every one of  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "hasMore": true,
    "rating": 4.4,
    "reviews": [
      {
        "avatarUrl": "https://p16-common-sign.tiktokcdn-us.com/tos-useast5-avt-0068-tx/f2b26e61d48dad7…",
        "country": "United States",
        "createdUtc": 1789964716,
        "id": "7687839852292884237",
        "images": [],
        "productId": "1731578642912612516",
        "rating": 5,
        "reviewerName": "Jæ",
        "sku": "Item: Default",
        "text": "These are the best nail clippers I’ve found for cats. I was worried about hittin…",
        "verifiedPurchase": true
      }
    ],
    "totalReviews": 1452
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.rating` | Overall product rating, shown as 4.4 in this response. |
| `data.totalReviews` | Total number of reviews for the product across all pages. |
| `data.hasMore` | `true` when more review pages exist. Request the next `page` to continue. |
| `data.reviews[].id` | Unique ID of the review, as a string. |
| `data.reviews[].rating` | Star rating the reviewer gave, as a whole number such as 5. |
| `data.reviews[].text` | Written review text. It can be in any language, such as Spanish. |
| `data.reviews[].reviewerName / data.reviews[].avatarUrl` | Display name and profile picture URL of the reviewer. |
| `data.reviews[].country` | Country of the reviewer, written as a full name such as `United States`. |
| `data.reviews[].verifiedPurchase` | `true` when the review comes from a verified buyer. |
| `data.reviews[].images` | List of photo URLs attached to the review. The list is empty when the review has no photos. |
| `data.reviews[].sku` | Product variant the reviewer bought, such as `Item: Default`. |
| `data.reviews[].createdUtc` | Review creation time as a Unix timestamp. |

### Notes

- Copy the product URL from a TikTok Shop product page. The number at the end of the URL is the product ID, which also appears as `productId` in each review.
- To paginate, raise `page` from 1 and keep going while `data.hasMore` is `true`.
- Set `region` to the two-letter country code of the product's shop, for example `US`.
- Use [TikTok Shop Product](/apis/tiktok-shop/product) to get the product's own details, or [TikTok Shop Search](/apis/tiktok-shop/search) to find product URLs.

### Pricing

Billed at the actual cost of each call, about $0.00095 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok-shop/product-reviews.json`](../../../catalog/models/tiktok-shop/product-reviews.json) · Store page: https://www.sandbase.ai/model/tiktok-shop/product-reviews

# Amazon Best Sellers API: pricing, parameters and code examples

`amazon/best-sellers` · data API · Amazon · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get the Amazon Best Sellers list for a category path in a chosen marketplace country, with rank, title, price, rating and ASIN, page by page.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/best-sellers", "category": "electronics"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('amazon/best-sellers', {'category': 'electronics'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("amazon/best-sellers", {
  "category": "electronics"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "amazon/best-sellers", sandbase.Params{
	"category": "electronics",
})
```

Same call via the path form: `POST /v1/api/amazon/best-sellers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `country` | string |  | Country code for the Amazon product. one of: `US`, `AU`, `BR`, `CA`, `CN`, `FR`, `DE`, `IN`, `IT`, `MX`, `NL`, `SG` …; default `"US"` |
| `category` | string | yes | Best Sellers category path taken from an Amazon Best Sellers URL. It may be a category slug or a nested category path.  |

## Details

Returns the Amazon Best Sellers list for one category in one marketplace country. Each item has its rank, ASIN, title, star rating, rating count, photo and product URL. You send a `category` path and can set `country` and `page`.

### Use cases

- Track which products hold the top ranks in a category such as `electronics` over time.
- Build a list of ASINs from a category to feed into product research or catalog tracking.
- Compare top sellers in the same category across marketplaces by changing `country`.
- Check the rating and rating count of current best sellers before choosing products to stock.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/amazon/best-sellers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category": "electronics"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | Yes | Best Sellers category path taken from an Amazon Best Sellers URL. It may be a category slug or a nested category path. |
| `country` | string | No | Country code for the Amazon product. |
| `page` | integer | No | Page number for pagination. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "best_sellers": [
    {
      "asin": "B08JHCVHTY",
      "product_num_ratings": 281657,
      "product_photo": "https://images-na.ssl-images-amazon.com/images/I/31YHGbJsldL._AC_UL900_SR900,600…",
      "product_price": "$11.99",
      "product_star_rating": "4.4",
      "product_title": "blink plus plan with monthly auto-renewal",
      "product_url": "https://www.amazon.com/dp/B08JHCVHTY",
      "rank": 1,
      "rank_change_label": null
    }
  ],
  "category_name": "Electronics",
  "country": "US",
  "domain": "www.amazon.com"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `best_sellers[]` | One entry per product on the requested page of the Best Sellers list. |
| `best_sellers[].rank` | Position of the product in the list. `1` is the top seller. |
| `best_sellers[].asin` | Amazon product ID. Use it to look up the product in other APIs. |
| `best_sellers[].product_title` | Product title as shown in the list. |
| `best_sellers[].product_star_rating / best_sellers[].product_num_ratings` | Average star rating as a string, and the number of ratings as an integer. |
| `best_sellers[].product_url / best_sellers[].product_photo` | Link to the product page and link to the product image. |
| `best_sellers[].rank_change_label` | Label for a rank change. It is `null` in this response. |
| `category_name / country / domain` | The category name, country code and Amazon domain that the list came from. |

### Notes

- Copy the `category` value from an Amazon Best Sellers URL. It can be a slug like `electronics` or a nested path.
- Use `page` to move through the list. It defaults to `1`.
- `country` defaults to `US`. The response echoes it in `country` and gives the matching `domain`, such as `www.amazon.com`.
- Use the `asin` values with [Amazon Product Details](/apis/amazon/product-detail) to get more data on a single product.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/amazon/best-sellers.json`](../../../catalog/models/amazon/best-sellers.json) · Store page: https://www.sandbase.ai/model/amazon/best-sellers

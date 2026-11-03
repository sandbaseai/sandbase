# Amazon Products By Category API: pricing, parameters and code examples

`amazon/category-products` · data API · Amazon · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get paginated Amazon products for a numeric category node in a selected country marketplace, with configurable result sorting.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/category-products", "categoryId": "electronics"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('amazon/category-products', {'categoryId': 'electronics'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("amazon/category-products", {
  "categoryId": "electronics"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "amazon/category-products", sandbase.Params{
	"categoryId": "electronics",
})
```

Same call via the path form: `POST /v1/api/amazon/category-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `sortBy` | string |  | Sort by. one of: `RELEVANCE`, `LOWEST_PRICE`, `HIGHEST_PRICE`, `REVIEWS`, `NEWEST`, `BEST_SELLERS`; default `"RELEVANCE"` |
| `country` | string |  | Country code for the Amazon product. one of: `US`, `AU`, `BR`, `CA`, `CN`, `FR`, `DE`, `IN`, `IT`, `MX`, `NL`, `SG` …; default `"US"` |
| `categoryId` | string | yes | Numeric Amazon category node ID taken from the node query parameter of a category URL.  |

## Details

Returns a page of Amazon products listed under one category node in a chosen country marketplace. You send a numeric `categoryId` and can set `country`, `sortBy` and `page`. Each product includes its ASIN, title, rating, offer count and listing badges.

### Use cases

- Find discounted listings in one category by comparing `product_original_price` with the current listed amount.
- Rank a category with `sortBy` set to `BEST_SELLERS` or `REVIEWS` to find top items.
- Build a catalog of ASINs in a category, then fetch full details for each one.
- Compare the same category across country marketplaces by changing `country`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/amazon/category-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"categoryId": "electronics"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `categoryId` | string | Yes | Numeric Amazon category node ID taken from the node query parameter of a category URL. |
| `country` | string | No | Country code for the Amazon product. |
| `page` | integer | No | Page number for pagination. |
| `sortBy` | string | No | Sort by. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "country": "US",
  "domain": "www.amazon.com",
  "products": [
    {
      "asin": "B0FHJ7TKZM",
      "climate_pledge_friendly": true,
      "currency": "USD",
      "delivery": "Join Prime to get FREE delivery Tomorrow, Nov 4Or Non-members get FREE delivery …",
      "has_variations": true,
      "is_amazon_choice": false,
      "is_best_seller": false,
      "is_prime": true,
      "product_badge": "Limited Prime deal",
      "product_minimum_offer_price": "$39.99",
      "product_num_offers": 1,
      "product_num_ratings": 8292
    }
  ],
  "total_products": 917494
}
```

### Response fields

| Field | Meaning |
|---|---|
| `total_products` | Total number of products reported for the category. Use it to plan how many pages to request. |
| `country / domain` | The marketplace country code and the Amazon domain used for the results, such as `US` and `www.amazon.com`. |
| `products[].asin` | The Amazon product ID. Use it to look up the product in other APIs. |
| `products[].product_title` | The product title as shown in the listing. |
| `products[].product_price / products[].product_original_price / products[].product_minimum_offer_price` | The current listed amount, the original amount before a discount, and the lowest offer amount. All are strings that include the currency symbol. |
| `products[].currency` | The currency code for the amounts, such as `USD`. |
| `products[].product_star_rating / products[].product_num_ratings` | The average star rating as a string and the number of ratings. |
| `products[].product_num_offers` | The number of offers shown for the product. |
| `products[].is_prime / products[].is_best_seller / products[].is_amazon_choice / products[].climate_pledge_friendly` | Boolean flags for Prime eligibility and listing badges. |
| `products[].sales_volume` | Text such as `10K+ bought in past month`. |
| `products[].product_url / products[].product_photo` | The product page link and the main image link. |

### Notes

- Take `categoryId` from the `node` query parameter of an Amazon category URL.
- Set `page` to get more results. It starts at 1 by default.
- To get full data for one item, pass its `asin` to [Amazon Product Details](/apis/amazon/product-detail).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/amazon/category-products.json`](../../../catalog/models/amazon/category-products.json) · Store page: https://www.sandbase.ai/model/amazon/category-products

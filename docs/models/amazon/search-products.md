# Amazon Product Search API: pricing, parameters and code examples

`amazon/search-products` · data API · Amazon · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search Amazon marketplace products by keyword or ASIN with country, sort, condition, Prime-only, deals, and page controls.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/search-products", "keyword": "iphone"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('amazon/search-products', {'keyword': 'iphone'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("amazon/search-products", {
  "keyword": "iphone"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "amazon/search-products", sandbase.Params{
	"keyword": "iphone",
})
```

Same call via the path form: `POST /v1/api/amazon/search-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `sortBy` | string |  | Sort order for Amazon product search results. one of: `RELEVANCE`, `LOWEST_PRICE`, `HIGHEST_PRICE`, `REVIEWS`, `NEWEST`, `BEST_SELLERS`; default `"RELEVANCE"` |
| `country` | string |  | Country code for the Amazon marketplace. one of: `US`, `AU`, `BR`, `CA`, `CN`, `FR`, `DE`, `IN`, `IT`, `MX`, `NL`, `SG` …; default `"US"` |
| `isPrime` | boolean |  | Whether to return only Prime-eligible products. default `false` |
| `keyword` | string | yes | Search keyword or ASIN to find Amazon products.  |
| `productCondition` | string |  | Product condition filter for Amazon search results. one of: `ALL`, `NEW`, `USED`, `RENEWED`, `COLLECTIBLE`; default `"ALL"` |
| `dealsAndDiscounts` | string |  | Deals and discounts filter for Amazon search results. one of: `NONE`, `ALL_DISCOUNTS`, `TODAYS_DEALS`; default `"NONE"` |

## Details

Returns a page of Amazon search results for a keyword or ASIN. Each product has its ASIN, title, rating, offer count, badges, and delivery text. The only required input is `keyword`.

### Use cases

- Compare listings for the same keyword across Amazon marketplaces by changing `country`.
- Track which products carry the best seller or Amazon's Choice badge for a search term.
- Find listings that show a discount by setting `dealsAndDiscounts` to `ALL_DISCOUNTS` or `TODAYS_DEALS`.
- Build a list of ASINs for a keyword and pass them to a product detail lookup.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/amazon/search-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "iphone"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword or ASIN to find Amazon products. |
| `country` | string | No | Country code for the Amazon marketplace. |
| `dealsAndDiscounts` | string | No | Deals and discounts filter for Amazon search results. |
| `isPrime` | boolean | No | Whether to return only Prime-eligible products. |
| `page` | integer | No | Page number for pagination. |
| `productCondition` | string | No | Product condition filter for Amazon search results. |
| `sortBy` | string | No | Sort order for Amazon product search results. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "country": "US",
  "domain": "www.amazon.com",
  "products": [
    {
      "asin": "B0HJHXTRFN",
      "climate_pledge_friendly": false,
      "currency": "USD",
      "delivery": "FREE delivery Thu, Nov 5Or fastest delivery Tomorrow, Nov 4",
      "has_variations": true,
      "is_amazon_choice": false,
      "is_best_seller": false,
      "is_prime": false,
      "product_minimum_offer_price": "$1,549.00",
      "product_num_offers": 1,
      "product_num_ratings": 13,
      "product_original_price": null
    }
  ],
  "total_products": 259
}
```

### Response fields

| Field | Meaning |
|---|---|
| `total_products` | Number of products the search matched. |
| `country / domain` | Amazon marketplace country code and domain that served the search. |
| `products[].asin` | Amazon product ID. Use it to look up the product elsewhere. |
| `products[].product_title` | Listing title as shown in the search results. |
| `products[].product_price / products[].product_original_price` | Current listed amount and the earlier amount shown before a discount, both as formatted strings with a currency symbol. The original amount is `null` when no discount is shown. |
| `products[].product_minimum_offer_price / products[].product_num_offers` | Lowest amount among the offers for the product, and the number of offers listed. |
| `products[].currency` | Currency code for the amounts on the listing, for example `USD`. |
| `products[].product_star_rating / products[].product_num_ratings` | Average star rating as a string, and the count of ratings. |
| `products[].is_best_seller / products[].is_amazon_choice / products[].is_prime / products[].climate_pledge_friendly` | Boolean flags for the badges and Prime eligibility shown on the listing. |
| `products[].sales_volume` | Text such as `1K+ bought in past month`. |
| `products[].product_url / products[].product_photo` | Link to the product page and the main product image URL. |

### Notes

- Pass an ASIN such as `B0DHJ896RY` as `keyword` to search for a specific product.
- Use `page` to get more results. Each response holds one page of `products`, and `total_products` shows the overall match count.
- For full details on one ASIN, call [Amazon Product Details](/apis/amazon/product-detail).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/amazon/search-products.json`](../../../catalog/models/amazon/search-products.json) · Store page: https://www.sandbase.ai/model/amazon/search-products

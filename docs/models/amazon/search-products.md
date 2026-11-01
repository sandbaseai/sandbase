# Amazon Product Search

`amazon/search-products` · api · Amazon

Search Amazon marketplace products by keyword or ASIN with country, sort, condition, Prime-only, deals, and page controls.

## Pricing

- **$0.013889 per call** (USD)
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

Search Amazon marketplace products by keyword or ASIN with country, sort, condition, Prime-only, deals, and page controls.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/amazon/search-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "iphone"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword or ASIN to find Amazon products. |
| `country` | string | No | Country code for the Amazon marketplace. |
| `sortBy` | string | No | Sort order for Amazon product search results. |
| `productCondition` | string | No | Product condition filter for Amazon search results. |
| `isPrime` | boolean | No | Whether to return only Prime-eligible products. |
| `dealsAndDiscounts` | string | No | Deals and discounts filter for Amazon search results. |
| `page` | integer | No | Page number for pagination. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/amazon/search-products.json`](../../../catalog/models/amazon/search-products.json) · Store page: https://www.sandbase.ai/model/amazon/search-products

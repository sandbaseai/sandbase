# Amazon Products By Category API: pricing, parameters and code examples

`amazon/category-products` · data API · Amazon · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Get paginated Amazon products for a numeric category node in a selected country marketplace, with configurable result sorting.

## Pricing

- **$0.013889 per call** (USD)
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

Get paginated Amazon products for a numeric category node in a selected country marketplace, with configurable result sorting.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/amazon/category-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"categoryId": "electronics"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `categoryId` | string | Yes | Numeric Amazon category node ID taken from the node query parameter of a category URL. |
| `country` | string | No | Country code for the Amazon product. |
| `sortBy` | string | No | Sort by. |
| `page` | integer | No | Page number for pagination. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/amazon/category-products.json`](../../../catalog/models/amazon/category-products.json) · Store page: https://www.sandbase.ai/model/amazon/category-products

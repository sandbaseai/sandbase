# Shop Search Merchants By Category API: pricing, parameters and code examples

`shop-app/search-merchants-by-category` · data API · Shop · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Searches for merchants within a shop.app category page.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "shop-app/search-merchants-by-category", "category": "women"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('shop-app/search-merchants-by-category', {'category': 'women'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("shop-app/search-merchants-by-category", {
  "category": "women"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "shop-app/search-merchants-by-category", sandbase.Params{
	"category": "women",
})
```

Same call via the path form: `POST /v1/api/shop-app/search-merchants-by-category` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination (1-indexed). default `1` |
| `category` | string | yes | Category slug to search within. Known categories: women, men, beauty, home, fitness-nutrition, baby-toddler, food-drinks, sporting-goods, toys-games, pet-supplies, accessories, electronics, arts-crafts, luggage-bags.…  |
| `page_size` | integer |  | Number of merchants per page. default `20` |
| `max_rating` | number |  | Maximum average rating. Merchants above this rating are excluded.  |
| `min_rating` | number |  | Minimum average rating (e.g. 4.5). Merchants below this rating are excluded.  |
| `max_reviews` | integer |  | Maximum number of product reviews the merchant may have. Merchants with more reviews are excluded.  |
| `min_reviews` | integer |  | Minimum number of product reviews the merchant must have. Merchants with fewer reviews are excluded.  |

## Details

Searches for merchants within a shop.app category page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "shop-app/search-merchants-by-category", "page": 1, "category": "women", "page_size": 20, "max_rating": 5.0, "min_rating": 3.0, "max_reviews": 500000, "min_reviews": 100}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | Yes | Category slug to search within. Known categories: women, men, beauty, home, fitness-nutrition, baby-toddler, food-drinks, sporting-goods, toys-games, pet-supplies, accessories, electronics, arts-crafts, luggage-bags. Ali |
| `max_rating` | number | No | Maximum average rating. Merchants above this rating are excluded. |
| `max_reviews` | integer | No | Maximum number of product reviews the merchant may have. Merchants with more reviews are excluded. |
| `min_rating` | number | No | Minimum average rating (e.g. 4.5). Merchants below this rating are excluded. |
| `min_reviews` | integer | No | Minimum number of product reviews the merchant must have. Merchants with fewer reviews are excluded. |
| `page` | integer | No | Page number for pagination (1-indexed). |
| `page_size` | integer | No | Number of merchants per page. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/shop-app/search-merchants-by-category.json`](../../../catalog/models/shop-app/search-merchants-by-category.json) · Store page: https://www.sandbase.ai/model/shop-app/search-merchants-by-category

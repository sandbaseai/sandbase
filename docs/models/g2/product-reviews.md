# G2 Product Reviews API: pricing, parameters and code examples

`g2/product-reviews` · data API · G2 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.05 per call · **Modes:** async

Retrieve paginated user reviews for a given software product, 10 reviews per page, newest-first in G2's default order. Each review includes author, designation, segment, title, date (ISO YYYY-MM-DD), rating (0-5 on a.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "g2/product-reviews", "slug": "slack"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('g2/product-reviews', {'slug': 'slack'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("g2/product-reviews", {
  "slug": "slack"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "g2/product-reviews", sandbase.Params{
	"slug": "slack",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/g2/product-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination range -9007199254740991–9007199254740991 |
| `slug` | string | yes | Product slug (e.g. 'slack', 'hubspot-sales-hub')  |
| `star_rating` | integer |  | Filter by star rating (1-5) using G2's rating filter; reviews in the 1-star bucket display ratings between 0 and 1. Omit to return reviews of all ratings. range -9007199254740991–9007199254740991 |

## Details

Retrieve paginated user reviews for a given software product, 10 reviews per page, newest-first in G2's default order. Each review includes author, designation, segment, title, date (ISO YYYY-MM-DD), rating (0-5 on a.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/g2/product-reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "slack"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | Product slug (e.g. 'slack', 'hubspot-sales-hub') |
| `page` | integer | No | Page number for pagination |
| `star_rating` | integer | No | Filter by star rating (1-5) using G2's rating filter; reviews in the 1-star bucket display ratings between 0 and 1. Omit to return reviews of all ratings. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/g2/product-reviews.json`](../../../catalog/models/g2/product-reviews.json) · Store page: https://www.sandbase.ai/model/g2/product-reviews

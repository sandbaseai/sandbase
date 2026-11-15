# G2 Product Reviews API: pricing, parameters and code examples

`g2/product-reviews` · data API · G2 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0025 per call · **Modes:** sync

Pull G2 software reviews for any product: star rating, what reviewers like and dislike, problems solved, market segment, and G2's rating rubric as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0025**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "g2/product-reviews", "product": "hubspot-marketing-hub"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('g2/product-reviews', {'product': 'hubspot-marketing-hub'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("g2/product-reviews", {
  "product": "hubspot-marketing-hub"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "g2/product-reviews", sandbase.Params{
	"product": "hubspot-marketing-hub",
})
```

Same call via the path form: `POST /v1/api/g2/product-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of reviews to return. The minimum is 50 because G2 review sources will not serve a smaller page. You are billed per returned result, so a lower limit costs less. default `50`; range 50–100 |
| `sortBy` | string |  | Sort order for the returned reviews: newest first, most helpful first, highest or lowest rated first, or G2's own default ordering. one of: `recent`, `helpful`, `highest`, `lowest`, `default`; default `"recent"` |
| `product` | string | yes | G2 product slug, for example hubspot-marketing-hub. A full G2 product URL is also accepted and reduced to its slug.  |

## Details

Pull G2 software reviews for any product: star rating, what reviewers like and dislike, problems solved, market segment, and G2's rating rubric as clean JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "g2/product-reviews", "limit": 50, "sortBy": "recent", "product": "hubspot-marketing-hub"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product` | string | Yes | G2 product slug, for example hubspot-marketing-hub. A full G2 product URL is also accepted and reduced to its slug. |
| `limit` | integer | No | Maximum number of reviews to return. The minimum is 50 because G2 review sources will not serve a smaller page. You are billed per returned result, so a lower limit costs less. |
| `sortBy` | string | No | Sort order for the returned reviews: newest first, most helpful first, highest or lowest rated first, or G2's own default ordering. One of: `recent`, `helpful`, `highest`, `lowest`, `default`. |

### Pricing

Billed at the actual cost of each call: about $5e-05 per result returned (about $0.0025 for 50 results). A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/g2/product-reviews.json`](../../../catalog/models/g2/product-reviews.json) · Store page: https://www.sandbase.ai/model/g2/product-reviews

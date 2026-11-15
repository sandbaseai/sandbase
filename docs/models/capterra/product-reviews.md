# Capterra Product Reviews API: pricing, parameters and code examples

`capterra/product-reviews` · data API · Capterra · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0077 per call · **Modes:** sync

Pull Capterra software reviews for any product: overall and sub-ratings, pros and cons, reviewer job title, company size, and industry as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0077**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "capterra/product-reviews", "product": "https://www.capterra.com/p/135003/Slack/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('capterra/product-reviews', {'product': 'https://www.capterra.com/p/135003/Slack/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("capterra/product-reviews", {
  "product": "https://www.capterra.com/p/135003/Slack/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "capterra/product-reviews", sandbase.Params{
	"product": "https://www.capterra.com/p/135003/Slack/",
})
```

Same call via the path form: `POST /v1/api/capterra/product-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of reviews to return. The minimum is 10 because the cheapest Capterra review source will not serve a smaller page. You are billed per returned result, so a lower limit costs less. Default 10, max 50.… default `10`; range 10–50 |
| `sortBy` | string |  | Sort order for the returned reviews: newest first, most complete first, or highest or lowest rated first. one of: `recent`, `complete`, `highest`, `lowest`; default `"recent"` |
| `product` | string | yes | Capterra product URL, for example https://www.capterra.com/p/135003/Slack/. Capterra identifies a product by both its numeric id and its slug, so the full URL is required.  |

## Details

Pull Capterra software reviews for any product: overall and sub-ratings, pros and cons, reviewer job title, company size, and industry as clean JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "capterra/product-reviews", "limit": 25, "sortBy": "recent", "product": "https://www.capterra.com/p/135003/Slack/"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product` | string | Yes | Capterra product URL, for example https://www.capterra.com/p/135003/Slack/. Capterra identifies a product by both its numeric id and its slug, so the full URL is required. |
| `limit` | integer | No | Maximum number of reviews to return. The minimum is 10 because the cheapest Capterra review source will not serve a smaller page. You are billed per returned result, so a lower limit costs less. Default 10, max 50. Each  |
| `sortBy` | string | No | Sort order for the returned reviews: newest first, most complete first, or highest or lowest rated first. One of: `recent`, `complete`, `highest`, `lowest`. |

### Pricing

Billed at the actual cost of each call: about $0.00077 per result returned (about $0.0077 for 10 results). A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/capterra/product-reviews.json`](../../../catalog/models/capterra/product-reviews.json) · Store page: https://www.sandbase.ai/model/capterra/product-reviews

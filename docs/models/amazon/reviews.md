# Amazon Reviews API: pricing, parameters and code examples

`amazon/reviews` · data API · Amazon · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.016 per call · **Modes:** sync

Pull customer reviews for any Amazon product by ASIN or URL: rating, title, text, date, and verified-buyer badge.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.016**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/reviews", "product": "B07PXGQC1Q"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('amazon/reviews', {'product': 'B07PXGQC1Q'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("amazon/reviews", {
  "product": "B07PXGQC1Q"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "amazon/reviews", sandbase.Params{
	"product": "B07PXGQC1Q",
})
```

Same call via the path form: `POST /v1/api/amazon/reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Review sort order: most helpful first or most recent first (e.g. recent). one of: `helpful`, `recent` |
| `limit` | integer |  | Maximum number of results to return (1-50, default 50). default `50`; range 1–50 |
| `region` | string |  | Amazon marketplace domain the product ASIN belongs to (e.g. amazon.co.uk). one of: `amazon.com`, `amazon.ca`, `amazon.de`, `amazon.fr`, `amazon.co.uk`, `amazon.it`, `amazon.es`, `amazon.com.au`, `amazon.co.jp`, `amazon.com.br`, `amazon.com.mx`, `amazon.nl` … |
| `endDate` | string |  | Only return reviews on or before this date, inclusive, in YYYY-MM-DD format (e.g. 2026-06-30).  |
| `keyword` | string |  | Only return reviews whose title or text contains this keyword, case-insensitively (e.g. battery).  |
| `product` | string | yes | Amazon product ASIN (e.g. B07CMS5Q6P) or a product link on one of the marketplaces listed under region, such as https://www.amazon.co.uk/dp/<ASIN>, with the ASIN after /dp/, /gp/product/ or /product-reviews/. A link…  |
| `ratings` | array |  | Only return reviews whose star rating is in this set (e.g. ["5", "4"] for 4 and 5 star reviews); omit for all ratings.  |
| `startDate` | string |  | Only return reviews on or after this date, inclusive, in YYYY-MM-DD format (e.g. 2026-01-01).  |
| `verifiedOnly` | boolean |  | Set true to return only verified-purchase reviews (e.g. true).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `url`, and it is served only by a source that returns every one of…  |

## Details

Pull customer reviews for any Amazon product by ASIN or URL: rating, title, text, date, and verified-buyer badge.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "amazon/reviews", "limit": 3, "product": "B07PXGQC1Q"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product` | string | Yes | Amazon product ASIN (e.g. B07CMS5Q6P) or a product link on one of the marketplaces listed under region, such as https://www.amazon.co.uk/dp/<ASIN>, with the ASIN after /dp/, /gp/product/ or /product-reviews/. A link with |
| `endDate` | string | No | Only return reviews on or before this date, inclusive, in YYYY-MM-DD format (e.g. 2026-06-30). |
| `keyword` | string | No | Only return reviews whose title or text contains this keyword, case-insensitively (e.g. battery). |
| `limit` | integer | No | Maximum number of results to return (1-50, default 50). |
| `ratings` | array | No | Only return reviews whose star rating is in this set (e.g. ["5", "4"] for 4 and 5 star reviews); omit for all ratings. |
| `region` | string | No | Amazon marketplace domain the product ASIN belongs to (e.g. amazon.co.uk). One of: `amazon.com`, `amazon.ca`, `amazon.de`, `amazon.fr`, `amazon.co.uk`, `amazon.it`, `amazon.es`, `amazon.com.au`, `amazon.co.jp`, `amazon.c |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `url`, and it is served only by a source that returns every one of the |
| `sort` | string | No | Review sort order: most helpful first or most recent first (e.g. recent). One of: `helpful`, `recent`. |
| `startDate` | string | No | Only return reviews on or after this date, inclusive, in YYYY-MM-DD format (e.g. 2026-01-01). |
| `verifiedOnly` | boolean | No | Set true to return only verified-purchase reviews (e.g. true). |

### Pricing

Billed at the actual cost of each call, about $0.016 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/amazon/reviews.json`](../../../catalog/models/amazon/reviews.json) · Store page: https://www.sandbase.ai/model/amazon/reviews

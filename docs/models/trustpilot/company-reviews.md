# Trustpilot Company Reviews API: pricing, parameters and code examples

`trustpilot/company-reviews` · data API · Trustpilot · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0008 per call · **Modes:** sync

Pull Trustpilot reviews for any company by brand name: star ratings, review text, dates, and reviewer details as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0008**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "trustpilot/company-reviews", "company": "stripe.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('trustpilot/company-reviews', {'company': 'stripe.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("trustpilot/company-reviews", {
  "company": "stripe.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "trustpilot/company-reviews", sandbase.Params{
	"company": "stripe.com",
})
```

Same call via the path form: `POST /v1/api/trustpilot/company-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results to return (1-200, default 200). Trustpilot serves at most 200 reviews per company. default `200`; range 1–200 |
| `stars` | string |  | Limit reviews to a single star rating from 1 to 5 (e.g. 5).  |
| `sortBy` | string |  | Review ordering: auto, relevancy, or recent (e.g. recent). one of: `auto`, `relevancy`, `recent`; default `"auto"` |
| `company` | string | yes | Brand name or Trustpilot review-page URL to fetch reviews for (e.g. nike or https://www.trustpilot.com/review/nike.com).  |
| `countries` | array |  | Only return reviews from reviewers in these ISO 3166-1 alpha-2 countries (e.g. ["US", "GB"]). Omit this field for all countries and to stay on the cheapest price; a country filter routes to the dearest source.  |
| `languages` | array |  | Only return reviews in these ISO 639-1 languages (e.g. ["en", "de"]). Omit this field for all languages and to stay on the cheapest price; a language filter routes to the dearest source.  |
| `startDate` | string |  | Only return reviews on or after this date, inclusive, in YYYY-MM-DD format (e.g. 2026-01-01). Omit this field to stay on the cheapest price; a date floor routes to the dearest source.  |
| `verifiedOnly` | boolean |  | Set true to return only verified reviews (e.g. true). Omit this field, or send false, to stay on the cheapest price; true routes to a dearer source. default `false` |

## Details

Pull Trustpilot reviews for any company by brand name: star ratings, review text, dates, and reviewer details as clean JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "trustpilot/company-reviews", "limit": 3, "company": "stripe.com"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `company` | string | Yes | Brand name or Trustpilot review-page URL to fetch reviews for (e.g. nike or https://www.trustpilot.com/review/nike.com). |
| `countries` | array | No | Only return reviews from reviewers in these ISO 3166-1 alpha-2 countries (e.g. ["US", "GB"]). Omit this field for all countries and to stay on the cheapest price; a country filter routes to the dearest source. |
| `languages` | array | No | Only return reviews in these ISO 639-1 languages (e.g. ["en", "de"]). Omit this field for all languages and to stay on the cheapest price; a language filter routes to the dearest source. |
| `limit` | integer | No | Maximum number of results to return (1-200, default 200). Trustpilot serves at most 200 reviews per company. |
| `sortBy` | string | No | Review ordering: auto, relevancy, or recent (e.g. recent). One of: `auto`, `relevancy`, `recent`. |
| `stars` | string | No | Limit reviews to a single star rating from 1 to 5 (e.g. 5). |
| `startDate` | string | No | Only return reviews on or after this date, inclusive, in YYYY-MM-DD format (e.g. 2026-01-01). Omit this field to stay on the cheapest price; a date floor routes to the dearest source. |
| `verifiedOnly` | boolean | No | Set true to return only verified reviews (e.g. true). Omit this field, or send false, to stay on the cheapest price; true routes to a dearer source. |

### Pricing

Billed at the actual cost of each call, about $0.0008 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/trustpilot/company-reviews.json`](../../../catalog/models/trustpilot/company-reviews.json) · Store page: https://www.sandbase.ai/model/trustpilot/company-reviews

# Clutch Company Reviews API: pricing, parameters and code examples

`clutch/company-reviews` · data API · Clutch · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Get paginated reviews for a company. Returns review titles, ratings, dates, and project information (services, project size, project length).

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "clutch/company-reviews", "slug": "simform"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('clutch/company-reviews', {'slug': 'simform'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("clutch/company-reviews", {
  "slug": "simform"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "clutch/company-reviews", sandbase.Params{
	"slug": "simform",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/clutch/company-reviews` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, 0-based. range -9007199254740991–9007199254740991 |
| `slug` | string | yes | Company profile slug from search_companies results.  |

## Details

Returns one page of Clutch reviews for a company. Each review has a title, rating, date, and project details. You pass the company `slug` and an optional 0-based `page`.

### Use cases

- Pull recent client reviews for an agency to check how past projects went.
- Collect review ratings and dates for a company to track how feedback changes over time.
- Filter reviews by `project_info.services` to find projects similar to yours.
- Build a dataset of review titles and project details for a list of vendors.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/clutch/company-reviews" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "simform", "page": 0}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | Company profile slug from search_companies results. |
| `page` | integer | No | Page number, 0-based. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "has_more": true,
    "page": 0,
    "reviews": [
      {
        "date": "Jun 8, 2026",
        "project_info": {
          "project_length": "Apr. 2025 - Ongoing",
          "project_size": "Confidential",
          "services": "Custom Software Development Web Development"
        },
        "rating": "5.0",
        "reviewer": null,
        "summary": null,
        "title": "Custom Software Development for Education Company"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.reviews[].title` | Title of the review. It often describes the service and the client type. |
| `data.reviews[].rating` | Review rating as a string, for example `5.0` or `4.5`. |
| `data.reviews[].date` | Review date as text, for example `Jun 8, 2026`. |
| `data.reviews[].project_info.services` | Services the company provided on the project, as one text string. |
| `data.reviews[].project_info.project_size` | Size of the project as text. The value can be `Confidential`. |
| `data.reviews[].project_info.project_length` | Project date range as text, for example `Apr. 2025 - Ongoing`. |
| `data.reviews[].project_info.focus_areas` | Focus areas or technologies listed for the project. This key appears only on some reviews. |
| `data.reviews[].reviewer / data.reviews[].summary` | Reviewer and summary fields. Both were `null` in this response. |
| `data.has_more` | `true` when more pages of reviews exist after this one. |
| `data.page` | The page number of this result, 0-based. |

### Notes

- Get the `slug` from the results of [Clutch Search Companies](/apis/clutch/search-companies).
- Start with `page` set to `0`. Increase it by 1 while `data.has_more` is `true`.
- `rating` and `date` are returned as strings, so parse them in your own code.
- For company details beyond reviews, call [Clutch Company Profile](/apis/clutch/company-profile).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/clutch/company-reviews.json`](../../../catalog/models/clutch/company-reviews.json) · Store page: https://www.sandbase.ai/model/clutch/company-reviews

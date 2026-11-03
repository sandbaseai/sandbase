# Clutch Search Companies API: pricing, parameters and code examples

`clutch/search-companies` · data API · Clutch · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Search for companies in a specific service category on Clutch.co. Returns a paginated list of company summaries.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "clutch/search-companies"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('clutch/search-companies', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("clutch/search-companies", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "clutch/search-companies", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/clutch/search-companies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, 0-based. range -9007199254740991–9007199254740991 |
| `category` | string |  | Category slug identifying the service vertical to search.  |

## Details

Returns a page of companies listed in one service category on Clutch. Each entry has the company name, profile URL, slug, rating, review count and verification flag. Pass a `category` slug and a 0-based `page` number.

### Use cases

- Build a lead list of agencies or developers in a single service category.
- Collect company slugs and profile URLs to feed into profile, review or portfolio lookups.
- Page through a category to track which companies appear in it.
- Filter a category list by the `verified` flag to find verified companies.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/clutch/search-companies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | No | Category slug identifying the service vertical to search. |
| `page` | integer | No | Page number, 0-based. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "category": "developers",
    "companies": [
      {
        "name": "Simform",
        "profile_url": "https://clutch.co/profile/simform",
        "rating": null,
        "review_count": null,
        "slug": "simform",
        "verified": false
      }
    ],
    "page": 0
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.category` | The category slug the search ran against, for example `developers`. |
| `data.page` | The 0-based page number of this result set. |
| `data.companies[].name` | Display name of the company. |
| `data.companies[].profile_url` | Full URL of the company profile page on Clutch. |
| `data.companies[].slug` | Short identifier of the company, the last part of `profile_url`. Use it to look up the company in other Clutch APIs. |
| `data.companies[].rating / data.companies[].review_count` | Company rating and number of reviews. Both can be `null` in the list, as in the sample response. |
| `data.companies[].verified` | Boolean flag. It is `false` for every company in the sample response. |
| `status` | Result status of the call, `success` when the request worked. |

### Notes

- Both `category` and `page` are optional in the schema. The sample request was sent with `{}` and the response returned the `developers` category on page `0`.
- Increase `page` by 1 to get the next page. Page numbers start at `0`.
- Get valid `category` slugs from [Clutch List Categories](/apis/clutch/list-categories).
- Pass the `slug` to [Clutch Company Profile](/apis/clutch/company-profile) for full company details, or to [Clutch Company Reviews](/apis/clutch/company-reviews) for reviews.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/clutch/search-companies.json`](../../../catalog/models/clutch/search-companies.json) · Store page: https://www.sandbase.ai/model/clutch/search-companies

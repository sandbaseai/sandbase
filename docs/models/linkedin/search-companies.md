# LinkedIn Company Search API: pricing, parameters and code examples

`linkedin/search-companies` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.005 per call · **Modes:** sync

Search LinkedIn companies by keyword with optional location filtering, returning normalized company records.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.005**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/search-companies", "query": "fintech"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/search-companies', {'query': 'fintech'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/search-companies", {
  "query": "fintech"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/search-companies", sandbase.Params{
	"query": "fintech",
})
```

Same call via the path form: `POST /v1/api/linkedin/search-companies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results to return (1-20, default 20). default `20`; range 1–20 |
| `query` | string | yes | Keyword to search LinkedIn companies for (e.g. marketing agency).  |
| `location` | string |  | Optional location filter, written out in full (e.g. United Kingdom or San Francisco).  |

## Details

Returns a list of LinkedIn companies that match a keyword. Each record has the company name, handle, industry, location, follower count text, and a short description. The only required input is `query`, and you can add `location` to narrow the results.

### Use cases

- Build a list of companies in a niche, such as fintech or marketing agencies, for outreach.
- Narrow a market scan to one city or country with the `location` filter.
- Find the LinkedIn `handle` of a company so you can fetch its full profile or posts.
- Compare similar companies by industry and follower count.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/search-companies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "query": "fintech"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword to search LinkedIn companies for (e.g. marketing agency). |
| `limit` | integer | No | Maximum number of results to return (1-20, default 20). |
| `location` | string | No | Optional location filter, written out in full (e.g. United Kingdom or San Francisco). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "description": "Fintech, a pioneering business solutions provider, has been dedicated to serving…",
        "followersText": "109K followers",
        "handle": "fintech-net",
        "id": "2785182",
        "image": "https://media.licdn.com/dms/image/v2/D4D0BAQE405phR1bFjA/company-logo_100_100/B4…",
        "industry": "Financial Services",
        "location": "Tampa, FL",
        "name": "Fintech",
        "url": "https://www.linkedin.com/company/fintech-net/"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].name` | Display name of the company on LinkedIn. |
| `data.items[].handle` | Company slug used in the LinkedIn URL. Use it to look up the company in other LinkedIn APIs. |
| `data.items[].id` | LinkedIn company ID, returned as a string. |
| `data.items[].url` | Full LinkedIn page URL of the company. |
| `data.items[].industry` | Industry label shown on the company page, such as `Financial Services`. |
| `data.items[].location` | Headquarters or main location as written on the company page, such as `Tampa, FL`. |
| `data.items[].followersText` | Follower count as display text, such as `109K followers`. It is a rounded string, not a number. |
| `data.items[].description` | Short company description. Long text is cut off and can be in any language. |
| `data.items[].image` | URL of the company logo image. |
| `found` | `true` when the search returned results. |

### Notes

- Set `limit` between 1 and 20. The default is 20. This response shows no pagination parameter.
- Write `location` out in full, for example `United Kingdom` or `San Francisco`.
- Pass a result's `handle` or `url` to [LinkedIn Company](/apis/linkedin/company) for a full company record.
- Use [LinkedIn Company Posts](/apis/linkedin/company-posts) to read what a company has posted.

### Pricing

Billed at the actual cost of each call, about $0.005 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/search-companies.json`](../../../catalog/models/linkedin/search-companies.json) · Store page: https://www.sandbase.ai/model/linkedin/search-companies

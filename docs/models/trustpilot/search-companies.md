# Trustpilot Search Companies API: pricing, parameters and code examples

`trustpilot/search-companies` · data API · Trustpilot · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** async

Search for companies by name or keyword. Returns basic company info including domain, trust score, star rating, and review count.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "trustpilot/search-companies", "query": "airline"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('trustpilot/search-companies', {'query': 'airline'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("trustpilot/search-companies", {
  "query": "airline"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "trustpilot/search-companies", sandbase.Params{
	"query": "airline",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/trustpilot/search-companies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number range -9007199254740991–9007199254740991 |
| `limit` | integer |  | Results per page (max 20) range -9007199254740991–9007199254740991 |
| `query` | string | yes | Search keyword or company name  |

## Details

Returns Trustpilot companies that match a search keyword or company name. Each result includes the company domain, categories, trust score, star rating, review count, and a location object. The only required input is `query`.

### Use cases

- Find the Trustpilot ID and domain of a company before you pull its reviews.
- Compare trust scores and review counts across companies in one industry, such as airlines.
- Build a list of companies that match a keyword for reputation monitoring.
- Check whether a brand has a Trustpilot profile and whether it is marked as verified.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/trustpilot/search-companies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "airline"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword or company name |
| `limit` | integer | No | Results per page (max 20) |
| `page` | integer | No | Page number |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "companies": [
      {
        "categories": [
          "Airline"
        ],
        "domain": "www.lufthansa.com",
        "id": "46d421dd000064000500ba73",
        "location": {
          "approximateArea": [
            [
              -180
            ]
          ],
          "city": null,
          "coordinates": {
            "lat": 39.7837304,
            "lon": -100.445882
          },
          "country": "United States",
          "countryCode": "US",
          "postcode": null,
          "street": null
        },
        "name": "Lufthansa",
        "review_count": 15266,
        "stars": 1.5,
        "trust_score": 1.3,
        "verified": false,
        "website_url": "https://www.lufthansa.com"
      }
    ],
    "total_hits": 2811,
    "total_pages": 141
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.companies[].name` | Company name as shown on Trustpilot. |
| `data.companies[].id` | Trustpilot ID of the company. It is a 24-character hex string. |
| `data.companies[].domain / data.companies[].website_url` | Company website as a bare domain and as a full URL. |
| `data.companies[].trust_score` | Trustpilot TrustScore of the company, for example `1.3`. |
| `data.companies[].stars` | Star rating of the company, for example `1.5`. |
| `data.companies[].review_count` | Number of reviews the company has on Trustpilot. |
| `data.companies[].categories[]` | Category labels attached to the company, such as `Airline` or `Travel Agency`. |
| `data.companies[].verified` | Boolean flag that shows whether the company profile is verified. |
| `data.companies[].location.country / data.companies[].location.countryCode` | Country name and country code in the location data. `city`, `street`, and `postcode` can be `null`. |
| `data.total_hits / data.total_pages` | Total number of matching companies and the number of pages at the current page size. |

### Notes

- Use `page` and `limit` to move through results. `limit` has a maximum of 20.
- Pass the company `domain` or `id` to the next call. [Trustpilot Company Overview](/apis/trustpilot/company-overview) gives more detail on one company.
- Call [Trustpilot Company Reviews](/apis/trustpilot/company-reviews) to read the individual reviews of a company.
- To browse by industry instead of keyword, use [Trustpilot Companies By Category](/apis/trustpilot/companies-by-category).

### Pricing

$0.03 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/trustpilot/search-companies.json`](../../../catalog/models/trustpilot/search-companies.json) · Store page: https://www.sandbase.ai/model/trustpilot/search-companies

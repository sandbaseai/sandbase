# LinkedIn Company API: pricing, parameters and code examples

`linkedin/company` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

Fetch a full LinkedIn company page by URL: name, description, industry, employee count and range, follower count, founded year, headquarters and office locations, funding data, tagline, logo, website, and specialities.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/company", "url": "https://www.linkedin.com/company/stripe"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/company', {'url': 'https://www.linkedin.com/company/stripe'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/company", {
  "url": "https://www.linkedin.com/company/stripe"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/company", sandbase.Params{
	"url": "https://www.linkedin.com/company/stripe",
})
```

Same call via the path form: `POST /v1/api/linkedin/company` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full LinkedIn company page URL.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `city` or `postalCode`, and it is served only by a source that…  |

## Details

Returns a LinkedIn company page as structured data. It needs the full LinkedIn company page URL, such as `https://www.linkedin.com/company/stripe`. The response includes the company name, description, industry, employee count, follower count, headquarters, website, and similar companies.

### Use cases

- Enrich a CRM account record with industry, website, and employee count range from a company page URL.
- Track follower count and employee count for a list of competitors.
- Find the headquarters address of a company for territory or lead routing.
- Build a list of related companies from the similar organizations on a page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/company" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/company/stripe"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full LinkedIn company page URL. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `city` or `postalCode`, and it is served only by a source that returns |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "companyType": "Privately Held",
    "description": "Stripe builds programmable financial services. Millions of companies—from the wo…",
    "employeeCount": 16694,
    "employeeCountRange": {
      "end": 10000,
      "start": 5001
    },
    "followerCount": 1801972,
    "foundedOn": {},
    "fundingData": null,
    "id": "2135371",
    "industry": "Technology, Information and Internet",
    "linkedinUrl": "https://www.linkedin.com/company/stripe",
    "locations": [
      {
        "city": "South San Francisco",
        "country": "US",
        "headquarter": true,
        "line1": "354 Oyster Point Blvd",
        "postalCode": "94080"
      }
    ],
    "logoUrl": "https://media.licdn.com/dms/image/v2/D560BAQE2ZfJyfn-VCg/company-logo_200_200/B5…"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.name / data.tagline` | The company name and the short tagline shown on the page. |
| `data.description` | The company description text from the About section. |
| `data.industry / data.companyType` | The industry label and the company type, for example `Privately Held`. |
| `data.employeeCount` | The employee count shown for the company on LinkedIn. |
| `data.employeeCountRange.start / data.employeeCountRange.end` | The lower and upper bounds of the employee size band. |
| `data.followerCount` | The number of LinkedIn followers of the company page. |
| `data.locations[].city / data.locations[].country / data.locations[].line1 / data.locations[].postalCode` | The address parts of each listed office. |
| `data.locations[].headquarter` | `true` when the location is marked as the headquarters. |
| `data.website / data.linkedinUrl / data.universalName` | The company website, its LinkedIn page URL, and the short name used in the page URL. |
| `data.similarOrganizations[].name / data.similarOrganizations[].url` | The name and LinkedIn URL of each company LinkedIn lists as similar. |

### Notes

- The result is `found: true` when the page exists. `foundedOn` can be an empty object, and `fundingData`, `pageVerified` and `specialities` can be `null` or empty, so check them before use.
- Use `requireFields` with values such as `foundedOn`, `fundingData` or `similarOrganizations` when you need those fields in the result. This can change the price of the call.
- The `id` field is a string, for example `2135371`. The `universalName` value matches the last part of the company URL.
- To see the people who work at a company, call [LinkedIn Company Employees](/apis/linkedin/company-employees). For its posts, call [LinkedIn Company Posts](/apis/linkedin/company-posts).

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/company.json`](../../../catalog/models/linkedin/company.json) · Store page: https://www.sandbase.ai/model/linkedin/company

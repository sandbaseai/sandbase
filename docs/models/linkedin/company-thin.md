# LinkedIn Company (basic) API: pricing, parameters and code examples

`linkedin/company-thin` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.001 per call · **Modes:** sync

Basic company: name, description, employee count, industry, logo, website, tagline. No follower count, founded year, office locations, or funding data - for those use linkedin.company.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.001**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/company-thin", "url": "https://www.linkedin.com/company/stripe"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/company-thin', {'url': 'https://www.linkedin.com/company/stripe'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/company-thin", {
  "url": "https://www.linkedin.com/company/stripe"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/company-thin", sandbase.Params{
	"url": "https://www.linkedin.com/company/stripe",
})
```

Same call via the path form: `POST /v1/api/linkedin/company-thin` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Full LinkedIn company page URL.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `companyType` or `coverImage`, and it is served only by a source…  |

## Details

Returns basic details for a LinkedIn company page, such as name, tagline, description, industry, employee count, website and logo. It needs the full LinkedIn company page URL as `url`.

### Use cases

- Enrich a CRM account record with a company's industry, website and employee count.
- Check a company's `employeeCount` and `industry` to qualify sales leads.
- Pull the logo and tagline to show a company card in an app.
- Resolve a LinkedIn company URL to its numeric `id` and `universalName` for use in other lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/company-thin" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.linkedin.com/company/stripe"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Full LinkedIn company page URL. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `companyType` or `coverImage`, and it is served only by a source that  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "companyType": "Privately Held",
    "coverImage": null,
    "description": "Stripe builds programmable financial services. Millions of companies—from the wo…",
    "employeeCount": 16618,
    "followerCount": 1756730,
    "foundedYear": 2010,
    "id": "2135371",
    "industry": "Technology, Information and Internet",
    "linkedinUrl": "https://www.linkedin.com/company/stripe",
    "logoUrl": "https://media.licdn.com/dms/image/v2/D560BAQE2ZfJyfn-VCg/company-logo_200_200/B5…",
    "name": "Stripe",
    "tagline": "Help increase the GDP of the internet."
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.name` | Company name as shown on its LinkedIn page. |
| `data.tagline` | Short tagline from the company page. |
| `data.description` | Company description text. Long descriptions can be cut off. |
| `data.industry` | Industry label, for example `Technology, Information and Internet`. |
| `data.employeeCount` | Employee count shown for the company. |
| `data.followerCount` | Number of followers of the company page. |
| `data.foundedYear` | Year the company was founded. |
| `data.companyType` | Company type, for example `Privately Held`. It is `null` or absent when the page has none. |
| `data.website / data.linkedinUrl` | The company's own website and its LinkedIn page URL. |
| `data.id / data.universalName` | Numeric company ID and the URL slug name, for example `stripe`. |
| `data.logoUrl / data.coverImage` | Image URLs for the logo and the cover image. `coverImage` is `null` when no cover image is returned. |
| `found` | `true` when the company page was found. |

### Notes

- Pass the full page URL, such as `https://www.linkedin.com/company/stripe`. Use the [LinkedIn Company Search](/apis/linkedin/search-companies) API to find company URLs by keyword.
- Set `requireFields` to `companyType` or `coverImage` to require that the response can return those fields. A named field can still be `null` if the page lacks it.
- For office locations or funding data, use [LinkedIn Company](/apis/linkedin/company).
- To list recent posts from the same company, call [LinkedIn Company Posts (basic)](/apis/linkedin/company-posts-thin).

### Pricing

Billed at the actual cost of each call, about $0.001 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/company-thin.json`](../../../catalog/models/linkedin/company-thin.json) · Store page: https://www.sandbase.ai/model/linkedin/company-thin

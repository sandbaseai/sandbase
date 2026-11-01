# LinkedIn Profile Search (basic)

`linkedin/search-profiles-thin` · api · LinkedIn

Cheap people search: name/handle, headline, VANITY profile URL, location. No full profile or email - for full profiles per hit use linkedin.search_profiles, add emails with linkedin.search_profiles_email.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.036**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/search-profiles-thin", "query": "recruiter"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/search-profiles-thin', {'query': 'recruiter'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/search-profiles-thin", {
  "query": "recruiter"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/search-profiles-thin", sandbase.Params{
	"query": "recruiter",
})
```

Same call via the path form: `POST /v1/api/linkedin/search-profiles-thin` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search query for LinkedIn profiles - a role, name, or keywords (e.g. 'Marketing Manager').  |
| `title` | string |  | Filter by job title or headline (e.g. Head of Talent).  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; a page holds 10 profiles.  |
| `lastName` | string |  | Filter by last name (e.g. Okafor).  |
| `schoolId` | string |  | Filter by school, using a LinkedIn school id.  |
| `firstName` | string |  | Filter by first name (e.g. Jane).  |
| `industryId` | string |  | Filter by industry, using a LinkedIn industry id.  |
| `locationId` | string |  | Filter by location, using a LinkedIn geocode id.  |
| `followerOfUrn` | string |  | Return only people who follow this member, given the member's LinkedIn URN.  |
| `pastCompanyId` | string |  | Filter by a previous employer, using a numeric LinkedIn company id.  |
| `profileLanguage` | string |  | Filter by the language the profile is written in (ISO 2-letter code, e.g. en).  |
| `currentCompanyId` | string |  | Filter by current employer, using a numeric LinkedIn company id. Comma-separate for several.  |
| `serviceCategoryId` | string |  | Filter by service category, using a numeric service-category id.  |

## Details

Cheap people search: name/handle, headline, VANITY profile URL, location. No full profile or email - for full profiles per hit use linkedin.search_profiles, add emails with linkedin.search_profiles_email.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/search-profiles-thin" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "recruiter"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search query for LinkedIn profiles - a role, name, or keywords (e.g. 'Marketing Manager'). |
| `currentCompanyId` | string | No | Filter by current employer, using a numeric LinkedIn company id. Comma-separate for several. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; a page holds 10 profiles. |
| `firstName` | string | No | Filter by first name (e.g. Jane). |
| `followerOfUrn` | string | No | Return only people who follow this member, given the member's LinkedIn URN. |
| `industryId` | string | No | Filter by industry, using a LinkedIn industry id. |
| `lastName` | string | No | Filter by last name (e.g. Okafor). |
| `locationId` | string | No | Filter by location, using a LinkedIn geocode id. |
| `pastCompanyId` | string | No | Filter by a previous employer, using a numeric LinkedIn company id. |
| `profileLanguage` | string | No | Filter by the language the profile is written in (ISO 2-letter code, e.g. en). |
| `schoolId` | string | No | Filter by school, using a LinkedIn school id. |
| `serviceCategoryId` | string | No | Filter by service category, using a numeric service-category id. |
| `title` | string | No | Filter by job title or headline (e.g. Head of Talent). |

### Pricing

Billed at the actual cost of each call, usually $0.036 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/search-profiles-thin.json`](../../../catalog/models/linkedin/search-profiles-thin.json) · Store page: https://www.sandbase.ai/model/linkedin/search-profiles-thin

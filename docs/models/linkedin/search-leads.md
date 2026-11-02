# LinkedIn Sales Navigator Lead Search API: pricing, parameters and code examples

`linkedin/search-leads` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.07 per call · **Modes:** sync

LinkedIn lead search with Sales Navigator's search and filters: one call returns a page of up to 25 people matching a keyword and Sales Navigator lead filters (location, job title, current and past company, school, seniority, function, company size, and more), or the results of a Sales Navigator lead-search URL you built yourself. Each lead comes with name, current positions, location, summary, and photo, and its url opens the profile and can be passed to linkedin.profile for the full record. For full profiles in one call use linkedin.search_profiles.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.07**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/search-leads"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/search-leads', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/search-leads", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/search-leads", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/linkedin/search-leads` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Which page of up to 25 leads to return, starting at 1 (1-100, default 1). Also pages through a salesNavUrl search. Each page is billed as one request. default `1`; range 1–100 |
| `query` | string |  | Search keywords for LinkedIn leads: a role, name, or keywords (e.g. 'Marketing Manager'). Provide this or salesNavUrl.  |
| `schools` | array |  | Filter to people who attended any of these schools, by name. Commas are not allowed in a value. Up to 50 values.  |
| `jobTitle` | string |  | Optional current job title filter (e.g. 'Software Engineer'). Commas are not allowed in a value.  |
| `location` | string |  | Optional location filter (e.g. 'San Francisco'). Commas are not allowed in a value.  |
| `lastNames` | array |  | Filter to people whose last name matches any of these. Commas are not allowed in a value. Up to 70 values.  |
| `firstNames` | array |  | Filter to people whose first name matches any of these. Commas are not allowed in a value. Up to 70 values.  |
| `functionIds` | array |  | Filter by job function. Codes: 1=Accounting, 2=Administrative, 3=Arts and Design, 4=Business Development, 5=Community and Social Services, 6=Consulting, 7=Education, 8=Engineering, 9=Entrepreneurship, 10=Finance,…  |
| `salesNavUrl` | string |  | Alternatively, a LinkedIn Sales Navigator lead-search URL you built in Sales Navigator (e.g. https://www.linkedin.com/sales/search/people?query=(keywords%3Aengineer)). When set it overrides query and every other filter…  |
| `pastCompanies` | array |  | Filter to people who previously worked at any of these companies, by name. Commas are not allowed in a value. Up to 50 values.  |
| `pastJobTitles` | array |  | Filter by a past job title the person held (e.g. ['Product Manager']). Commas are not allowed in a value. Up to 70 values.  |
| `excludeSchools` | array |  | Exclude people who attended any of these schools, by name. Commas are not allowed in a value. Up to 50 values.  |
| `companyHeadcount` | array |  | Filter by current company size (employee count). Codes: A=Self-Employed, B=1-10, C=11-50, D=51-200, E=201-500, F=501-1,000, G=1,001-5,000, H=5,001-10,000, I=10,001+.  |
| `currentCompanies` | array |  | Filter to people who currently work at any of these companies, by name (e.g. ['Google','Meta']). Multiple names widen the match (OR). Commas are not allowed in a value. Up to 50 values.  |
| `excludeLocations` | array |  | Exclude people in any of these locations, by place name. Commas are not allowed in a value. Up to 70 values.  |
| `profileLanguages` | array |  | Filter by the profile's primary language.  |
| `seniorityLevelIds` | array |  | Filter by seniority level. Codes: 100=In Training, 110=Entry Level, 120=Senior, 130=Strategic, 200=Entry Level Manager, 210=Experienced Manager, 220=Director, 300=Vice President, 310=CXO, 320=Owner/Partner.  |
| `excludeFunctionIds` | array |  | Exclude these job functions (same codes as functionIds). Up to 30 values.  |
| `recentlyChangedJobs` | boolean |  | When true, only return people who recently changed jobs (a strong sales/recruiting signal).  |
| `excludePastCompanies` | array |  | Exclude people who previously worked at any of these companies, by name. Commas are not allowed in a value. Up to 50 values.  |
| `excludePastJobTitles` | array |  | Exclude people who held any of these past job titles. Commas are not allowed in a value. Up to 70 values.  |
| `yearsOfExperienceIds` | array |  | Filter by total years of experience. Codes: 1=Less than 1 year, 2=1 to 2 years, 3=3 to 5 years, 4=6 to 10 years, 5=More than 10 years.  |
| `excludeCurrentCompanies` | array |  | Exclude people who currently work at any of these companies, by name. Commas are not allowed in a value. Up to 50 values.  |
| `excludeCurrentJobTitles` | array |  | Exclude people whose current job title matches any of these. Commas are not allowed in a value. Up to 70 values.  |
| `excludeSeniorityLevelIds` | array |  | Exclude these seniority levels (same codes as seniorityLevelIds). Up to 20 values.  |
| `recentlyPostedOnLinkedIn` | boolean |  | When true, only return people who recently posted on LinkedIn (an activity signal).  |
| `yearsAtCurrentCompanyIds` | array |  | Filter by tenure at the current company. Codes: 1=Less than 1 year, 2=1 to 2 years, 3=3 to 5 years, 4=6 to 10 years, 5=More than 10 years.  |
| `companyHeadquarterLocations` | array |  | Filter by the location of the person's current company headquarters, by place name (e.g. ['United States']). Commas are not allowed in a value. Up to 70 values.  |
| `excludeCompanyHeadquarterLocations` | array |  | Exclude people whose current company is headquartered in any of these locations. Commas are not allowed in a value. Up to 70 values.  |

## Details

LinkedIn lead search with Sales Navigator's search and filters: one call returns a page of up to 25 people matching a keyword and Sales Navigator lead filters (location, job title, current and past company, school, seniority, function, company size, and more), or the results of a Sales Navigator lead-search URL you built yourself. Each lead comes with name, current positions, location, summary, and photo, and its url opens the profile and can be passed to linkedin.profile for the full record. For full profiles in one call use linkedin.search_profiles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/search-leads" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "engineer", "currentCompanies": ["Google"]}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `companyHeadcount` | array | No | Filter by current company size (employee count). Codes: A=Self-Employed, B=1-10, C=11-50, D=51-200, E=201-500, F=501-1,000, G=1,001-5,000, H=5,001-10,000, I=10,001+. |
| `companyHeadquarterLocations` | array | No | Filter by the location of the person's current company headquarters, by place name (e.g. ['United States']). Commas are not allowed in a value. Up to 70 values. |
| `currentCompanies` | array | No | Filter to people who currently work at any of these companies, by name (e.g. ['Google','Meta']). Multiple names widen the match (OR). Commas are not allowed in a value. Up to 50 values. |
| `excludeCompanyHeadquarterLocations` | array | No | Exclude people whose current company is headquartered in any of these locations. Commas are not allowed in a value. Up to 70 values. |
| `excludeCurrentCompanies` | array | No | Exclude people who currently work at any of these companies, by name. Commas are not allowed in a value. Up to 50 values. |
| `excludeCurrentJobTitles` | array | No | Exclude people whose current job title matches any of these. Commas are not allowed in a value. Up to 70 values. |
| `excludeFunctionIds` | array | No | Exclude these job functions (same codes as functionIds). Up to 30 values. |
| `excludeLocations` | array | No | Exclude people in any of these locations, by place name. Commas are not allowed in a value. Up to 70 values. |
| `excludePastCompanies` | array | No | Exclude people who previously worked at any of these companies, by name. Commas are not allowed in a value. Up to 50 values. |
| `excludePastJobTitles` | array | No | Exclude people who held any of these past job titles. Commas are not allowed in a value. Up to 70 values. |
| `excludeSchools` | array | No | Exclude people who attended any of these schools, by name. Commas are not allowed in a value. Up to 50 values. |
| `excludeSeniorityLevelIds` | array | No | Exclude these seniority levels (same codes as seniorityLevelIds). Up to 20 values. |
| `firstNames` | array | No | Filter to people whose first name matches any of these. Commas are not allowed in a value. Up to 70 values. |
| `functionIds` | array | No | Filter by job function. Codes: 1=Accounting, 2=Administrative, 3=Arts and Design, 4=Business Development, 5=Community and Social Services, 6=Consulting, 7=Education, 8=Engineering, 9=Entrepreneurship, 10=Finance, 11=Heal |
| `jobTitle` | string | No | Optional current job title filter (e.g. 'Software Engineer'). Commas are not allowed in a value. |
| `lastNames` | array | No | Filter to people whose last name matches any of these. Commas are not allowed in a value. Up to 70 values. |
| `location` | string | No | Optional location filter (e.g. 'San Francisco'). Commas are not allowed in a value. |
| `page` | integer | No | Which page of up to 25 leads to return, starting at 1 (1-100, default 1). Also pages through a salesNavUrl search. Each page is billed as one request. |
| `pastCompanies` | array | No | Filter to people who previously worked at any of these companies, by name. Commas are not allowed in a value. Up to 50 values. |
| `pastJobTitles` | array | No | Filter by a past job title the person held (e.g. ['Product Manager']). Commas are not allowed in a value. Up to 70 values. |
| `profileLanguages` | array | No | Filter by the profile's primary language. |
| `query` | string | No | Search keywords for LinkedIn leads: a role, name, or keywords (e.g. 'Marketing Manager'). Provide this or salesNavUrl. |
| `recentlyChangedJobs` | boolean | No | When true, only return people who recently changed jobs (a strong sales/recruiting signal). |
| `recentlyPostedOnLinkedIn` | boolean | No | When true, only return people who recently posted on LinkedIn (an activity signal). |
| `salesNavUrl` | string | No | Alternatively, a LinkedIn Sales Navigator lead-search URL you built in Sales Navigator (e.g. https://www.linkedin.com/sales/search/people?query=(keywords%3Aengineer)). When set it overrides query and every other filter o |
| `schools` | array | No | Filter to people who attended any of these schools, by name. Commas are not allowed in a value. Up to 50 values. |
| `seniorityLevelIds` | array | No | Filter by seniority level. Codes: 100=In Training, 110=Entry Level, 120=Senior, 130=Strategic, 200=Entry Level Manager, 210=Experienced Manager, 220=Director, 300=Vice President, 310=CXO, 320=Owner/Partner. |
| `yearsAtCurrentCompanyIds` | array | No | Filter by tenure at the current company. Codes: 1=Less than 1 year, 2=1 to 2 years, 3=3 to 5 years, 4=6 to 10 years, 5=More than 10 years. |
| `yearsOfExperienceIds` | array | No | Filter by total years of experience. Codes: 1=Less than 1 year, 2=1 to 2 years, 3=3 to 5 years, 4=6 to 10 years, 5=More than 10 years. |

### Pricing

Billed at the actual cost of each call, usually $0.07 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/search-leads.json`](../../../catalog/models/linkedin/search-leads.json) · Store page: https://www.sandbase.ai/model/linkedin/search-leads

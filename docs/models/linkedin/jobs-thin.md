# LinkedIn Jobs (index)

`linkedin/jobs-thin` · api · LinkedIn

Cheap job index: title, company, location, posted date, URL. No description, salary, applicant counts, or seniority - for those use linkedin.jobs.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00066**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/jobs-thin", "query": "software engineer"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/jobs-thin', {'query': 'software engineer'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/jobs-thin", {
  "query": "software engineer"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/jobs-thin", sandbase.Params{
	"query": "software engineer",
})
```

Same call via the path form: `POST /v1/api/linkedin/jobs-thin` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `geoId` | string |  | LinkedIn geo id to target a precise location (e.g. 103644278 for the United States); more exact than the free-text location.  |
| `limit` | integer |  | Accepted for compatibility and ignored: each call returns one full source page (10 or 25 jobs depending on source); follow nextCursor for more. range 1–25 |
| `query` | string | yes | Job title or keywords to search.  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of job listings.  |
| `location` | string |  | City, region, or country to search within.  |
| `companyId` | string |  | Filter to a specific company by its LinkedIn numeric company id.  |
| `postedLimit` | string |  | Only jobs posted within this window (past 24 hours, week, or month). one of: `24h`, `week`, `month` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `logoUrl`, and it is served only by a source that returns every one…  |
| `workplaceType` | string |  | Filter by workplace type (remote, hybrid, or onsite). one of: `remote`, `hybrid`, `onsite` |
| `employmentType` | string |  | Filter by employment type. one of: `full-time`, `part-time`, `contract`, `internship`, `temporary` |
| `experienceLevel` | string |  | Filter by required seniority/experience level. one of: `internship`, `entry`, `associate`, `mid-senior`, `director`, `executive` |

## Details

Cheap job index: title, company, location, posted date, URL. No description, salary, applicant counts, or seniority - for those use linkedin.jobs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/jobs-thin" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "query": "software engineer", "location": "United States", "workplaceType": "remote"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Job title or keywords to search. |
| `companyId` | string | No | Filter to a specific company by its LinkedIn numeric company id. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of job listings. |
| `employmentType` | string | No | Filter by employment type. One of: `full-time`, `part-time`, `contract`, `internship`, `temporary`. |
| `experienceLevel` | string | No | Filter by required seniority/experience level. One of: `internship`, `entry`, `associate`, `mid-senior`, `director`, `executive`. |
| `geoId` | string | No | LinkedIn geo id to target a precise location (e.g. 103644278 for the United States); more exact than the free-text location. |
| `limit` | integer | No | Accepted for compatibility and ignored: each call returns one full source page (10 or 25 jobs depending on source); follow nextCursor for more. |
| `location` | string | No | City, region, or country to search within. |
| `postedLimit` | string | No | Only jobs posted within this window (past 24 hours, week, or month). One of: `24h`, `week`, `month`. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `logoUrl`, and it is served only by a source that returns every one of |
| `workplaceType` | string | No | Filter by workplace type (remote, hybrid, or onsite). One of: `remote`, `hybrid`, `onsite`. |

### Pricing

Billed at the actual cost of each call, usually $0.00066 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/jobs-thin.json`](../../../catalog/models/linkedin/jobs-thin.json) · Store page: https://www.sandbase.ai/model/linkedin/jobs-thin

# LinkedIn Jobs

`linkedin/jobs` · api · LinkedIn

Search LinkedIn job listings by title and location - full records with description, salary, applicant count, seniority, company details, and benefits. Up to 25 jobs per request.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0195**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/jobs", "query": "software engineer"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/jobs', {'query': 'software engineer'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/jobs", {
  "query": "software engineer"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/jobs", sandbase.Params{
	"query": "software engineer",
})
```

Same call via the path form: `POST /v1/api/linkedin/jobs` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Accepted for compatibility and ignored: each call returns one full page of up to 25 jobs at one flat price per call; follow nextCursor for more. range 1–25 |
| `query` | string | yes | Job title or keywords to search. Supports LinkedIn boolean operators.  |
| `cursor` | string |  | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of job listings.  |
| `salary` | string |  | Filter by minimum base salary band (US dollars). one of: `40k+`, `60k+`, `80k+`, `100k+`, `120k+`, `140k+`, `160k+`, `180k+`, `200k+` |
| `sortBy` | string |  | Sort order: most recent (date) or best match (relevance). one of: `date`, `relevance` |
| `company` | string |  | Filter to a specific company by name (e.g. Google).  |
| `location` | string |  | City, region, or country to search within (e.g. United States, San Francisco).  |
| `easyApply` | boolean |  | When true, only return jobs offering LinkedIn Easy Apply.  |
| `postedLimit` | string |  | Only jobs posted within this window (past hour, 24 hours, week, or month). one of: `1h`, `24h`, `week`, `month` |
| `workplaceType` | string |  | Filter by workplace type (remote, hybrid, or onsite). one of: `remote`, `hybrid`, `onsite` |
| `employmentType` | string |  | Filter by employment type. one of: `full-time`, `part-time`, `contract`, `internship`, `temporary` |
| `experienceLevel` | string |  | Filter by required seniority/experience level. one of: `internship`, `entry`, `associate`, `mid-senior`, `director`, `executive` |
| `under10Applicants` | boolean |  | When true, only return jobs with fewer than 10 applicants (lower competition).  |

## Details

Search LinkedIn job listings by title and location - full records with description, salary, applicant count, seniority, company details, and benefits. Up to 25 jobs per request.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/jobs" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "query": "software engineer", "location": "United States", "workplaceType": "remote"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Job title or keywords to search. Supports LinkedIn boolean operators. |
| `company` | string | No | Filter to a specific company by name (e.g. Google). |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of job listings. |
| `easyApply` | boolean | No | When true, only return jobs offering LinkedIn Easy Apply. |
| `employmentType` | string | No | Filter by employment type. One of: `full-time`, `part-time`, `contract`, `internship`, `temporary`. |
| `experienceLevel` | string | No | Filter by required seniority/experience level. One of: `internship`, `entry`, `associate`, `mid-senior`, `director`, `executive`. |
| `limit` | integer | No | Accepted for compatibility and ignored: each call returns one full page of up to 25 jobs at one flat price per call; follow nextCursor for more. |
| `location` | string | No | City, region, or country to search within (e.g. United States, San Francisco). |
| `postedLimit` | string | No | Only jobs posted within this window (past hour, 24 hours, week, or month). One of: `1h`, `24h`, `week`, `month`. |
| `salary` | string | No | Filter by minimum base salary band (US dollars). One of: `40k+`, `60k+`, `80k+`, `100k+`, `120k+`, `140k+`, `160k+`, `180k+`, `200k+`. |
| `sortBy` | string | No | Sort order: most recent (date) or best match (relevance). One of: `date`, `relevance`. |
| `under10Applicants` | boolean | No | When true, only return jobs with fewer than 10 applicants (lower competition). |
| `workplaceType` | string | No | Filter by workplace type (remote, hybrid, or onsite). One of: `remote`, `hybrid`, `onsite`. |

### Pricing

Billed at the actual cost of each call, usually $0.0195 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/jobs.json`](../../../catalog/models/linkedin/jobs.json) · Store page: https://www.sandbase.ai/model/linkedin/jobs

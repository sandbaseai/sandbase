# LinkedIn Jobs API: pricing, parameters and code examples

`linkedin/jobs` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0195 per call · **Modes:** sync

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

This API searches LinkedIn job listings and returns up to 25 full job records per page. Each record has the title, location, salary, applicant count, apply link, and company details. It needs a `query` with a job title or keywords, and you can add filters such as `location` and `workplaceType`.

### Use cases

- Pull remote software engineer roles in the United States to feed a job board.
- Track which companies are hiring for a role by reading `company.name` across pages of results.
- Find roles with a posted salary range to benchmark pay for a title.
- Spot low-competition jobs by comparing `applicants` counts across listings.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/jobs" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "query": "software engineer", "location": "United States", "workplaceType": "remote"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Job title or keywords to search. Supports LinkedIn boolean operators. |
| `company` | string | No | Filter to a specific company by name (e.g. Google). |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of job listings. |
| `easyApply` | boolean | No | When true, only return jobs offering LinkedIn Easy Apply. |
| `employmentType` | string | No | Filter by employment type. |
| `experienceLevel` | string | No | Filter by required seniority/experience level. |
| `limit` | integer | No | Accepted for compatibility and ignored: each call returns one full page of up to 25 jobs at one flat price per call; follow nextCursor for more. |
| `location` | string | No | City, region, or country to search within (e.g. United States, San Francisco). |
| `postedLimit` | string | No | Only jobs posted within this window (past hour, 24 hours, week, or month). |
| `salary` | string | No | Filter by minimum base salary band (US dollars). |
| `sortBy` | string | No | Sort order: most recent (date) or best match (relevance). |
| `under10Applicants` | boolean | No | When true, only return jobs with fewer than 10 applicants (lower competition). |
| `workplaceType` | string | No | Filter by workplace type (remote, hybrid, or onsite). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "applicantTrackingSystem": "",
        "applicants": 200,
        "applyUrl": "https://www.zoominfo.com/careers?gh_jid=8606563002&gh_src=d14a9e1e2",
        "benefits": [],
        "city": "Bethesda",
        "company": {
          "employeeCount": 4179,
          "followerCount": 290946,
          "id": "16272",
          "linkedinUrl": "https://www.linkedin.com/company/zoominfo",
          "logo": "https://media.licdn.com/dms/image/v2/D4E0BAQGzMUtsP63GKw/company-logo_400_400/co…",
          "name": "ZoomInfo",
          "universalName": "zoominfo",
          "website": "https://goo.gl/bc4qew"
        },
        "country": "United States",
        "countryCode": "US",
        "createdUtc": 1792620222,
        "easyApplyUrl": "",
        "employmentType": "full_time",
        "experienceLevel": ""
      }
    ],
    "nextCursor": "cur_ZqGybXBAnO6OPPly-Qz9aw"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].title` | Job title as posted. |
| `data.items[].url` | LinkedIn page for the job. |
| `data.items[].applyUrl` | Link where the candidate applies. It often points to the employer's own careers page. |
| `data.items[].location / city / state / country / countryCode` | Where the job is based, as free text and as separate parts. Some parts can be empty strings. |
| `data.items[].workplaceType / remote / employmentType` | Workplace type (such as `remote`), a remote flag, and the employment type (such as `full_time` or `internship`). |
| `data.items[].salary.min / salary.max / salary.text` | Posted pay range and a text version such as `101,600 - 139,700 USD`. The values are `null` or empty when the listing has no salary. |
| `data.items[].applicants` | Number of applicants shown for the job. |
| `data.items[].createdUtc / expireUtc` | Unix timestamps in seconds for when the job was posted and when it expires. |
| `data.items[].company.name / universalName / linkedinUrl` | Company name, its LinkedIn slug, and the link to its LinkedIn page. |
| `data.items[].company.employeeCount / followerCount` | Employee count and follower count for the company on LinkedIn. |
| `data.nextCursor` | Cursor to pass as `cursor` to get the next page of jobs. |

### Notes

- Each call returns a full page of up to 25 jobs. The `limit` parameter is ignored, so the sample request with `limit` set to 3 still returns a full page.
- For the next page, send the same request with `cursor` set to the `nextCursor` value from the last response.
- Fields such as `descriptionText`, `company.description` and `benefits` appear only on some listings, and `experienceLevel` can be empty.
- To get one job in more detail, use [LinkedIn Job Details](/apis/linkedin/web-v2/job-detail). For the hiring company, use [LinkedIn Company](/apis/linkedin/company).

### Pricing

Billed at the actual cost of each call, about $0.0195 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/jobs.json`](../../../catalog/models/linkedin/jobs.json) · Store page: https://www.sandbase.ai/model/linkedin/jobs

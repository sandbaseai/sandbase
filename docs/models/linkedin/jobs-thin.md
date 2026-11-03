# LinkedIn Jobs (index) API: pricing, parameters and code examples

`linkedin/jobs-thin` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00066 per call · **Modes:** sync

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

Returns a page of LinkedIn job listings that match a search. Each listing has the job title, company, location, posted time, and URL. The only required input is `query`, a job title or keywords.

### Use cases

- Track new remote software engineer openings in the United States and list them in a daily digest.
- Build a lead list of companies that are hiring for a given role, using `company` and `companyUrl`.
- Monitor one employer's open roles by filtering with `companyId`.
- Collect job URLs in bulk, then fetch full details only for the listings you care about.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/jobs-thin" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "query": "software engineer", "location": "United States", "workplaceType": "remote"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Job title or keywords to search. |
| `companyId` | string | No | Filter to a specific company by its LinkedIn numeric company id. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's nextCursor. Omit for the first page; pass it to fetch the next page of job listings. |
| `employmentType` | string | No | Filter by employment type. |
| `experienceLevel` | string | No | Filter by required seniority/experience level. |
| `geoId` | string | No | LinkedIn geo id to target a precise location (e.g. 103644278 for the United States); more exact than the free-text location. |
| `limit` | integer | No | Accepted for compatibility and ignored: each call returns one full source page (10 or 25 jobs depending on source); follow nextCursor for more. |
| `location` | string | No | City, region, or country to search within. |
| `postedLimit` | string | No | Only jobs posted within this window (past 24 hours, week, or month). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `logoUrl`, and it is served only by a source that returns every one of |
| `workplaceType` | string | No | Filter by workplace type (remote, hybrid, or onsite). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "company": "JPMorganChase",
        "companyUrl": "https://www.linkedin.com/company/jpmorganchase",
        "createdUtc": 1793232000,
        "id": "4476983365",
        "location": "New York, NY",
        "logoUrl": "https://media.licdn.com/dms/image/v2/D4E0BAQGxpntCyRgsuA/company-logo_100_100/co…",
        "title": "Software Engineer II (Java/AWS)",
        "url": "https://www.linkedin.com/jobs/view/software-engineer-ii-java-aws-at-jpmorganchas…"
      }
    ],
    "nextCursor": "cur_UndpALJZYhG_2f7uy7cJJw"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].title` | Job title as shown on the listing. |
| `data.items[].company` | Name of the hiring company. |
| `data.items[].companyUrl` | LinkedIn page URL of the hiring company. |
| `data.items[].location` | Job location as free text, such as a city and state. |
| `data.items[].createdUtc` | Posted time of the listing as a Unix timestamp in seconds. |
| `data.items[].id` | LinkedIn job id. It also appears at the end of `url`. |
| `data.items[].url` | Link to the job page on LinkedIn. |
| `data.items[].logoUrl` | Image URL of the company logo. |
| `data.nextCursor` | Cursor for the next page of results. Pass it as `cursor` in the next request. |
| `found` | `true` when the search returned results. |

### Notes

- Each call returns one full page of jobs. The `limit` parameter is ignored, so follow `data.nextCursor` with `cursor` to get more.
- Use `geoId` for an exact location. For example, `103644278` is the United States.
- This API returns no description, salary, applicant counts, or seniority. Call [LinkedIn Jobs](/apis/linkedin/jobs) or [LinkedIn Job Details](/apis/linkedin/web-v2/job-detail) for those.
- To look up the hiring company, call [LinkedIn Company](/apis/linkedin/company).

### Pricing

Billed at the actual cost of each call, about $0.00066 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/linkedin/jobs-thin.json`](../../../catalog/models/linkedin/jobs-thin.json) · Store page: https://www.sandbase.ai/model/linkedin/jobs-thin

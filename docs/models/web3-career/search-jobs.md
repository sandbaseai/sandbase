# Web3.career Search Jobs API: pricing, parameters and code examples

`web3-career/search-jobs` · data API · Web3.career · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Search for jobs using a keyword query. Returns paginated job listings matching the search term.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "web3-career/search-jobs", "query": "solidity"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('web3-career/search-jobs', {'query': 'solidity'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("web3-career/search-jobs", {
  "query": "solidity"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "web3-career/search-jobs", sandbase.Params{
	"query": "solidity",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/web3-career/search-jobs` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. range -9007199254740991–9007199254740991 |
| `query` | string | yes | The search keyword (e.g., Solidity, London, Bitcoin, frontend, Rust).  |

## Details

Returns a page of Web3.career job listings that match a keyword. Each listing has the job title, company, location, salary range, posting age, and a link to the job page. The only required input is a `query` string.

### Use cases

- Find open Solidity or Rust roles by searching for the language name.
- Collect jobs in a city by searching for a place such as London.
- Track salary ranges for a skill by reading `salary` across many results.
- Build a job alert that runs a saved keyword and checks for new `job_id` values.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/web3-career/search-jobs" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "solidity"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The search keyword (e.g., Solidity, London, Bitcoin, frontend, Rust). |
| `page` | integer | No | Page number for pagination. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "jobs": [
      {
        "company": "Stellar Development Foundation",
        "job_id": "155908",
        "location": "New York, NY, United States",
        "posted_date": "3h",
        "salary": "$93k - $118k",
        "tags": [],
        "title": "Senior Content Marketing Manager Institutional",
        "url": "https://web3.career/senior-content-marketing-manager-institutional-stellardevelo…"
      }
    ],
    "page": "1",
    "query": "solidity"
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.jobs[].title` | Job title as shown on the listing. |
| `data.jobs[].company` | Name of the hiring company. |
| `data.jobs[].location` | Job location as text, for example a city, state and country. |
| `data.jobs[].salary` | Salary range shown on the listing, as a text string such as `$93k - $118k`. |
| `data.jobs[].posted_date` | How long ago the job was posted, as a short text value such as `3h`. |
| `data.jobs[].job_id` | Web3.career ID of the job, returned as a string. |
| `data.jobs[].url` | Link to the job page on Web3.career. |
| `data.jobs[].tags` | List of tags attached to the job. It can be empty. |
| `data.page / data.query` | The page number and search term that the response used. |

### Notes

- Use `page` to move through results. The response returns the current page as a string in `data.page`.
- Keywords can be skills, places or topics, such as `Solidity`, `London`, `Bitcoin`, `frontend` or `Rust`.
- Results can include roles that are not engineering jobs, so check `title` before you use a listing.
- Pass the `job_id` or `url` to [Web3.career Job Detail](/apis/web3-career/job-detail) to get more about a single job.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/web3-career/search-jobs.json`](../../../catalog/models/web3-career/search-jobs.json) · Store page: https://www.sandbase.ai/model/web3-career/search-jobs

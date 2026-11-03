# Web3.career Job Listings API: pricing, parameters and code examples

`web3-career/job-listings` · data API · Web3.career · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Fetch general job listings from the homepage with pagination. Returns Web3 job postings including title, company, location, salary, tags, and posting date.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "web3-career/job-listings"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('web3-career/job-listings', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("web3-career/job-listings", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "web3-career/job-listings", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/web3-career/job-listings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. range -9007199254740991–9007199254740991 |

## Details

Returns a page of Web3 job postings from the Web3.career homepage. Each posting has a title, company, location, salary range, tags, and a relative posting time. The only input is an optional `page` number.

### Use cases

- Build a feed of the newest Web3 jobs for a job board or newsletter.
- Track salary ranges offered for Web3 roles in cities such as New York or Chicago.
- Collect job URLs and IDs to fetch full posting details in a second call.
- Monitor which companies post new Web3 roles each day.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/web3-career/job-listings" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
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
    "page": "1"
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.jobs[].title` | Job title as shown in the listing. |
| `data.jobs[].company` | Name of the hiring company. |
| `data.jobs[].location` | Job location as text, for example `New York, NY, United States`. |
| `data.jobs[].salary` | Salary range shown in the listing, for example `$93k - $118k`. Treat it as text, not a number. |
| `data.jobs[].posted_date` | How long ago the job was posted, in a short relative form such as `3h`. |
| `data.jobs[].tags` | List of tags for the job. It can be empty. |
| `data.jobs[].job_id` | ID of the job as a string. It is also the last part of the job `url`. |
| `data.jobs[].url` | Link to the job page on Web3.career. |
| `data.page` | Page number of the returned results, as a string. |

### Notes

- Send `page` to move through results. The response echoes it in `data.page`. An empty request returns page `1`.
- Pass a `job_id` to [Web3.career Job Detail](/apis/web3-career/job-detail) to get the full posting.
- To narrow results, use [Web3.career Search Jobs](/apis/web3-career/search-jobs) or [Web3.career Remote Jobs](/apis/web3-career/remote-jobs).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/web3-career/job-listings.json`](../../../catalog/models/web3-career/job-listings.json) · Store page: https://www.sandbase.ai/model/web3-career/job-listings

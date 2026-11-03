# Web3.career Job Detail API: pricing, parameters and code examples

`web3-career/job-detail` · data API · Web3.career · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Fetch full details for a single job listing by URL. Returns the job title, company name, full description text, salary range, and application link.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "web3-career/job-detail", "url": "https://web3.career/junior-crypto-analyst-trader-empire-assets/155554"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('web3-career/job-detail', {'url': 'https://web3.career/junior-crypto-analyst-trader-empire-assets/155554'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("web3-career/job-detail", {
  "url": "https://web3.career/junior-crypto-analyst-trader-empire-assets/155554"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "web3-career/job-detail", sandbase.Params{
	"url": "https://web3.career/junior-crypto-analyst-trader-empire-assets/155554",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/web3-career/job-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The full URL of the job listing on web3.career (e.g., https://web3.career/senior-fullstack-engineer-backend-focus-rugsdotfun/150325).  |

## Details

Returns the full details of one job listing on web3.career. You pass the listing's full URL in `url`. The response includes the job title, company name, description text, salary text, and an application link.

### Use cases

- Pull the full description of a listing you found in a search so you can read the requirements.
- Collect the salary text and `apply_link` for a shortlist of Web3 jobs.
- Check which company posted a role and what it pays before you send an application.
- Store job details in an internal tracker or a job alert tool.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/web3-career/job-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://web3.career/junior-crypto-analyst-trader-empire-assets/155554"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The full URL of the job listing on web3.career (e.g., https://web3.career/senior-fullstack-engineer-backend-focus-rugsdotfun/150325). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "apply_link": "https://web3.career/i/0UTN1UTM",
    "company": "Empire Assets",
    "description": "Empire Assets is a young and rapidly developing company working in the field of …",
    "salary": "Compensation: $60k - $76k",
    "title": "Junior Crypto Analyst & Trader",
    "url": "https://web3.career/junior-crypto-analyst-trader-empire-assets/155554"
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.title` | Job title of the listing, for example `Junior Crypto Analyst & Trader`. |
| `data.company` | Name of the company that posted the job. |
| `data.description` | Description text of the job. It is a plain text string and can be long. |
| `data.salary` | Salary as shown on the listing, as one text string such as `Compensation: $60k - $76k`. It is not split into minimum and maximum values. |
| `data.apply_link` | Link to apply for the job. It is a web3.career redirect link. |
| `data.url` | The web3.career URL of the listing, the same value you sent in the request. |
| `status` | Result status of the call. It shows `success` when the listing was returned. |

### Notes

- Get listing URLs from [Web3.career Job Listings](/apis/web3-career/job-listings) or [Web3.career Search Jobs](/apis/web3-career/search-jobs).
- A listing URL ends with a numeric ID, for example `155554`.
- The call runs asynchronously. Poll the run endpoint until `status` is `completed`, then read `outputs[0].data`.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/web3-career/job-detail.json`](../../../catalog/models/web3-career/job-detail.json) · Store page: https://www.sandbase.ai/model/web3-career/job-detail

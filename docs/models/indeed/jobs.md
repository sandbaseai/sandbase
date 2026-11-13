# Indeed Jobs API: pricing, parameters and code examples

`indeed/jobs` · data API · Indeed · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search Indeed job listings by keyword and location, with title, company, location, salary, job type and posting date.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "indeed/jobs", "q": "data engineer"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('indeed/jobs', {'q': 'data engineer'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("indeed/jobs", {
  "q": "data engineer"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "indeed/jobs", sandbase.Params{
	"q": "data engineer",
})
```

Same call via the path form: `POST /v1/api/indeed/jobs` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `l` | string |  | Parameter defines the location you want to search jobs in. You can use anything that you would use in the "Where" box of a regular Indeed job search (e.g., `New York, NY`, `Austin, TX`, `94103`, or `Remote`).  |
| `q` | string | yes | Parameter defines the query you want to search. You can use anything that you would use in the "What" box of a regular Indeed job search (e.g., job title, keywords, or company).  |
| `jt` | string |  | Parameter defines the job type to filter results by. `fulltime` - Full-time `parttime` - Part-time `contract` - Contract `temporary` - Temporary `internship` - Internship  |
| `sort` | string |  | Parameter defines the sort order of the results. Results are sorted by relevance by default. Set it to `date` to sort by date posted.  |
| `radius` | string |  | Parameter defines the distance in miles around the `l` location to search jobs in. `0` - Exact location only `5` - Within 5 miles `10` - Within 10 miles `15` - Within 15 miles `25` - Within 25 miles `35` - Within 35…  |
| `fromage` | string |  | Parameter defines the maximum number of days since the job was posted. `1` - Last 24 hours `3` - Last 3 days `7` - Last 7 days `14` - Last 14 days  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Search Indeed job listings by keyword and location, with title, company, location, salary, job type and posting date.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/indeed/jobs" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "data engineer", "l": "Austin, TX"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the query you want to search. You can use anything that you would use in the "What" box of a regular Indeed job search (e.g., job title, keywords, or company). |
| `l` | string | No | Parameter defines the location you want to search jobs in. You can use anything that you would use in the "Where" box of a regular Indeed job search (e.g., `New York, NY`, `Austin, TX`, `94103`, or `Remote`). |
| `radius` | string | No | Parameter defines the distance in miles around the `l` location to search jobs in. `0` - Exact location only `5` - Within 5 miles `10` - Within 10 miles `15` - Within 15 miles `25` - Within 25 miles `35` - Within 35 miles `50` - Within 50 m |
| `jt` | string | No | Parameter defines the job type to filter results by. `fulltime` - Full-time `parttime` - Part-time `contract` - Contract `temporary` - Temporary `internship` - Internship |
| `fromage` | string | No | Parameter defines the maximum number of days since the job was posted. `1` - Last 24 hours `3` - Last 3 days `7` - Last 7 days `14` - Last 14 days |
| `sort` | string | No | Parameter defines the sort order of the results. Results are sorted by relevance by default. Set it to `date` to sort by date posted. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/indeed/jobs.json`](../../../catalog/models/indeed/jobs.json) · Store page: https://www.sandbase.ai/model/indeed/jobs

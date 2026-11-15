# Levels.fyi Jobs API: pricing, parameters and code examples

`levels-fyi/jobs` · data API · Levels.fyi · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

Search Levels.fyi job listings by title or keyword and get each job with its salary range and estimated total compensation where Levels.fyi has them, plus company, location, listing date and job link. Returns up to 20 jobs per call, grouped by company; filter by location and sort by relevance, date or compensation.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "levels-fyi/jobs", "query": "software engineer"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('levels-fyi/jobs', {'query': 'software engineer'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("levels-fyi/jobs", {
  "query": "software engineer"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "levels-fyi/jobs", sandbase.Params{
	"query": "software engineer",
})
```

Same call via the path form: `POST /v1/api/levels-fyi/jobs` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of jobs to return (1-20, default 20). Levels.fyi groups jobs by company, up to 3 per company, so several results can come from one employer. default `20`; range 1–20 |
| `query` | string | yes | Job title, keywords or company name to search, e.g. software engineer or google.  |
| `sortBy` | string |  | Sort order: best match (relevance), most recently posted (date), or highest total compensation (compensation). one of: `relevance`, `date`, `compensation`; default `"relevance"` |
| `location` | string |  | Levels.fyi location slug as it appears in Levels.fyi URLs, e.g. united-states. Not a free-text city name; omit it to search everywhere.  |

## Details

Search Levels.fyi job listings by title or keyword and get each job with its salary range and estimated total compensation where Levels.fyi has them, plus company, location, listing date and job link. Returns up to 20 jobs per call, grouped by company; filter by location and sort by relevance, date or compensation.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "levels-fyi/jobs", "limit": 10, "query": "software engineer", "location": "united-states"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Job title, keywords or company name to search, e.g. software engineer or google. |
| `limit` | integer | No | Maximum number of jobs to return (1-20, default 20). Levels.fyi groups jobs by company, up to 3 per company, so several results can come from one employer. |
| `location` | string | No | Levels.fyi location slug as it appears in Levels.fyi URLs, e.g. united-states. Not a free-text city name; omit it to search everywhere. |
| `sortBy` | string | No | Sort order: best match (relevance), most recently posted (date), or highest total compensation (compensation). One of: `relevance`, `date`, `compensation`. |

### Pricing

Billed at the actual cost of each call, about $0.00085 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/levels-fyi/jobs.json`](../../../catalog/models/levels-fyi/jobs.json) · Store page: https://www.sandbase.ai/model/levels-fyi/jobs

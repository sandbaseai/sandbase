# Upwork Jobs API: pricing, parameters and code examples

`upwork/jobs` · data API · Upwork · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.007 per call · **Modes:** sync

Search Upwork job postings by keyword, with up to 25 fresh listings per request.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.007**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "upwork/jobs", "query": "web developer"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('upwork/jobs', {'query': 'web developer'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("upwork/jobs", {
  "query": "web developer"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "upwork/jobs", sandbase.Params{
	"query": "web developer",
})
```

Same call via the path form: `POST /v1/api/upwork/jobs` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort order for listings: newest or relevance (e.g. newest). one of: `newest`, `relevance`; default `"newest"` |
| `limit` | integer |  | Maximum number of results to return (10-25, default 25). range 10–25 |
| `query` | string | yes | Keywords to search Upwork jobs for (e.g. react developer).  |
| `jobType` | string |  | Filter by payment type: fixed-price or hourly jobs. one of: `fixed`, `hourly` |
| `location` | string |  | Filter by client location - a region, subregion, or country (e.g. United States, Europe).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `premium` or `reposted`, and it is served only by a source that…  |
| `experienceLevel` | string |  | Filter by required experience level. one of: `entry`, `intermediate`, `expert` |
| `paymentVerified` | boolean |  | When true, only return jobs from clients with a verified payment method.  |

## Details

Search Upwork job postings by keyword, with up to 25 fresh listings per request.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "upwork/jobs", "limit": 10, "query": "web developer", "jobType": "fixed"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keywords to search Upwork jobs for (e.g. react developer). |
| `experienceLevel` | string | No | Filter by required experience level. One of: `entry`, `intermediate`, `expert`. |
| `jobType` | string | No | Filter by payment type: fixed-price or hourly jobs. One of: `fixed`, `hourly`. |
| `limit` | integer | No | Maximum number of results to return (10-25, default 25). |
| `location` | string | No | Filter by client location - a region, subregion, or country (e.g. United States, Europe). |
| `paymentVerified` | boolean | No | When true, only return jobs from clients with a verified payment method. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `premium` or `reposted`, and it is served only by a source that return |
| `sort` | string | No | Sort order for listings: newest or relevance (e.g. newest). One of: `newest`, `relevance`. Default `"newest"`. |

### Pricing

Billed at the actual cost of each call, about $0.007 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/upwork/jobs.json`](../../../catalog/models/upwork/jobs.json) · Store page: https://www.sandbase.ai/model/upwork/jobs

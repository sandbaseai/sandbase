# LinkedIn Company Search API: pricing, parameters and code examples

`linkedin/search-companies` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.005 per call · **Modes:** sync

Search LinkedIn companies by keyword with optional location filtering, returning normalized company records.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.005**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/search-companies", "query": "fintech"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/search-companies', {'query': 'fintech'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/search-companies", {
  "query": "fintech"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/search-companies", sandbase.Params{
	"query": "fintech",
})
```

Same call via the path form: `POST /v1/api/linkedin/search-companies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results to return (1-20, default 20). default `20`; range 1–20 |
| `query` | string | yes | Keyword to search LinkedIn companies for (e.g. marketing agency).  |
| `location` | string |  | Optional location filter, written out in full (e.g. United Kingdom or San Francisco).  |

## Details

Search LinkedIn companies by keyword with optional location filtering, returning normalized company records.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/search-companies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "query": "fintech"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword to search LinkedIn companies for (e.g. marketing agency). |
| `limit` | integer | No | Maximum number of results to return (1-20, default 20). |
| `location` | string | No | Optional location filter, written out in full (e.g. United Kingdom or San Francisco). |

### Pricing

Billed at the actual cost of each call, usually $0.005 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/search-companies.json`](../../../catalog/models/linkedin/search-companies.json) · Store page: https://www.sandbase.ai/model/linkedin/search-companies

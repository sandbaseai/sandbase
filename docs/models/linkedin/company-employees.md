# LinkedIn Company Employees

`linkedin/company-employees` · api · LinkedIn

List the employees of a LinkedIn company by name or company URL, with optional job-title filtering.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.006**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/company-employees", "company": "stripe"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/company-employees', {'company': 'stripe'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/company-employees", {
  "company": "stripe"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/company-employees", sandbase.Params{
	"company": "stripe",
})
```

Same call via the path form: `POST /v1/api/linkedin/company-employees` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results to return (1-10, default 10). range 1–10 |
| `company` | string | yes | Company name or LinkedIn company URL (e.g. google or https://www.linkedin.com/company/google/).  |
| `jobTitle` | string |  | Optional job-title filter supporting boolean operators (e.g. CEO OR CTO).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `openToWork` or `premium`, and it is served only by a source that…  |

## Details

List the employees of a LinkedIn company by name or company URL, with optional job-title filtering.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/company-employees" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "company": "stripe"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `company` | string | Yes | Company name or LinkedIn company URL (e.g. google or https://www.linkedin.com/company/google/). |
| `jobTitle` | string | No | Optional job-title filter supporting boolean operators (e.g. CEO OR CTO). |
| `limit` | integer | No | Maximum number of results to return (1-10, default 10). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `openToWork` or `premium`, and it is served only by a source that retu |

### Pricing

Billed at the actual cost of each call, usually $0.006 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/company-employees.json`](../../../catalog/models/linkedin/company-employees.json) · Store page: https://www.sandbase.ai/model/linkedin/company-employees

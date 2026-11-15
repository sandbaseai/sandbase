# Akta Companies API: pricing, parameters and code examples

`akta/companies` · data API · Akta · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.01 per call · **Modes:** async

Build a list of companies matching industry, location and funding filters.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.01**

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "akta/companies", "filters": {"location.hq.country": ["USA"], "firmographic.founded_year": {"gte": 2022}}}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('akta/companies', {'filters': {'location.hq.country': ['USA'], 'firmographic.founded_year': {'gte': 2022}}})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("akta/companies", {
  "filters": {
    "location.hq.country": [
      "USA"
    ],
    "firmographic.founded_year": {
      "gte": 2022
    }
  }
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "akta/companies", sandbase.Params{
	"filters": map[string]any{
		"location.hq.country": []any{"USA"},
		"firmographic.founded_year": map[string]any{
			"gte": 2022,
		},
	},
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/akta/companies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of rows to return (1-50, default 10). Each returned row is charged, so this caps the cost of one call. default `10`; range 1–50 |
| `offset` | integer |  | Number of companies to skip (pagination). range 0–9007199254740991 |
| `filters` | object | yes | Filter conditions keyed by field, combined with AND. List values match any of the given values; ranges take {gte, lte}. Example: {"location.hq.country": ["USA"], "firmographic.founded_year": {"gte": 2015},…  |
| `sort_by` | string |  | Field to sort by. Default relevance. one of: `relevance`, `revenue_estimate`, `valuation_estimate`, `employee_range`, `total_funding`, `founded_year` |
| `sort_order` | string |  | Sort direction. Default desc. one of: `asc`, `desc` |

## Details

Build a list of companies matching industry, location and funding filters.

### Pricing

- Inspect reference unit price: $0.01 USD per result.
- Inspect flat fee: $0.075 USD per call.
- Final settlement uses the provider-reported actual cost after strict validation; the reference price is not used to infer the final charge.

---
Machine-readable: [`catalog/models/akta/companies.json`](../../../catalog/models/akta/companies.json) · Store page: https://www.sandbase.ai/model/akta/companies

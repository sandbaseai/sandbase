# Fundable Deals API: pricing, parameters and code examples

`fundable/deals` · data API · Fundable · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.06 per call · **Modes:** async

Search and filter funding rounds by company, investor, and round details

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.06**

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fundable/deals"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fundable/deals', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fundable/deals", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fundable/deals", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/fundable/deals` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `deal` | object |  | Round attribute filters.  |
| `page` | integer |  | Page number (0-based). Default 0. range 0–9007199254740991 |
| `company` | object |  | Raising-company attribute filters.  |
| `sort_by` | string |  | Sort order. Default most_recent_deal. one of: `most_recent_deal`, `oldest_deal`, `largest_raise`, `smallest_raise` |
| `investors` | object |  | Investor participation filters.  |
| `page_size` | integer |  | Rows per page (1-20, default 10). Each returned row is charged, so this caps the cost of one call. default `10`; range 1–20 |
| `identifiers` | object |  |   |

## Details

Search and filter funding rounds by company, investor, and round details

### Pricing

- Inspect reference unit price: $0.06 USD per result.
- Final settlement uses the provider-reported actual cost after strict validation; the reference price is not used to infer the final charge.

---
Machine-readable: [`catalog/models/fundable/deals.json`](../../../catalog/models/fundable/deals.json) · Store page: https://www.sandbase.ai/model/fundable/deals

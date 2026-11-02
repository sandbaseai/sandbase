# StockAnalysis Stock List API: pricing, parameters and code examples

`stockanalysis/stock-list` · data API · StockAnalysis · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Stocks from a curated stock list by URL slug. Returns the list title, description, stock count, and an array of stock entries with symbol, name, market cap, price, change, and revenue.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "stockanalysis/stock-list", "slug": "biggest-companies"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('stockanalysis/stock-list', {'slug': 'biggest-companies'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("stockanalysis/stock-list", {
  "slug": "biggest-companies"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "stockanalysis/stock-list", sandbase.Params{
	"slug": "biggest-companies",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/stockanalysis/stock-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | List slug from the site URL path.  |

## Details

Stocks from a curated stock list by URL slug. Returns the list title, description, stock count, and an array of stock entries with symbol, name, market cap, price, change, and revenue.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/stockanalysis/stock-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "biggest-companies"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | List slug from the site URL path. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/stockanalysis/stock-list.json`](../../../catalog/models/stockanalysis/stock-list.json) · Store page: https://www.sandbase.ai/model/stockanalysis/stock-list

# StockAnalysis Market Movers Premarket API: pricing, parameters and code examples

`stockanalysis/market-movers-premarket` · data API · StockAnalysis · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Top gainers, losers, and most active stocks in the pre-market session. Each category contains query metadata and a data array of stock entries with symbol, name, premarket change percent, premarket price, premarket.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "stockanalysis/market-movers-premarket"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('stockanalysis/market-movers-premarket', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("stockanalysis/market-movers-premarket", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "stockanalysis/market-movers-premarket", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/stockanalysis/market-movers-premarket` with the body above minus `model`.

## Details

Top gainers, losers, and most active stocks in the pre-market session. Each category contains query metadata and a data array of stock entries with symbol, name, premarket change percent, premarket price, premarket.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/stockanalysis/market-movers-premarket" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

This API takes no parameters.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/stockanalysis/market-movers-premarket.json`](../../../catalog/models/stockanalysis/market-movers-premarket.json) · Store page: https://www.sandbase.ai/model/stockanalysis/market-movers-premarket

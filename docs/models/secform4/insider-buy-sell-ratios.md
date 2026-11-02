# SECForm4 Insider Buy Sell Ratios API: pricing, parameters and code examples

`secform4/insider-buy-sell-ratios` · data API · SECForm4 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns aggregate insider buy/sell ratio data with daily data points going back to 2003. Includes buy count, sell count, buy dollar volume, sell dollar volume per day, plus market index comparison data for S&P 500,.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "secform4/insider-buy-sell-ratios"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('secform4/insider-buy-sell-ratios', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("secform4/insider-buy-sell-ratios", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "secform4/insider-buy-sell-ratios", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/secform4/insider-buy-sell-ratios` with the body above minus `model`.

## Details

Returns aggregate insider buy/sell ratio data with daily data points going back to 2003. Includes buy count, sell count, buy dollar volume, sell dollar volume per day, plus market index comparison data for S&P 500,.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/secform4/insider-buy-sell-ratios" \
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
Machine-readable: [`catalog/models/secform4/insider-buy-sell-ratios.json`](../../../catalog/models/secform4/insider-buy-sell-ratios.json) · Store page: https://www.sandbase.ai/model/secform4/insider-buy-sell-ratios

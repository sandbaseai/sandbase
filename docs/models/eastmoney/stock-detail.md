# Eastmoney Stock Detail API: pricing, parameters and code examples

`eastmoney/stock-detail` · data API · Eastmoney · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get details for a specific stock by searching its code through the AI stock screener. Returns the stock's market data including latest price, PE ratio, market cap, PB ratio, and trading volume. Uses the same screening engine as screen_stocks but optimized for single-stock lookup.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "eastmoney/stock-detail", "code": "600519"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('eastmoney/stock-detail', {'code': '600519'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("eastmoney/stock-detail", {
  "code": "600519"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "eastmoney/stock-detail", sandbase.Params{
	"code": "600519",
})
```

Same call via the path form: `POST /v1/api/eastmoney/stock-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `code` | string | yes | Stock code to look up (e.g. '600519' for Kweichow Moutai, '000001' for Ping An Bank). Leading zeros are significant.  |

## Details

Get details for a specific stock by searching its code through the AI stock screener. Returns the stock's market data including latest price, PE ratio, market cap, PB ratio, and trading volume. Uses the same screening engine as screen_stocks but optimized for single-stock lookup.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "eastmoney/stock-detail", "code": "600519"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `code` | string | Yes | Stock code to look up (e.g. '600519' for Kweichow Moutai, '000001' for Ping An Bank). Leading zeros are significant. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/eastmoney/stock-detail.json`](../../../catalog/models/eastmoney/stock-detail.json) · Store page: https://www.sandbase.ai/model/eastmoney/stock-detail

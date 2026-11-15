# TradingView Quote API: pricing, parameters and code examples

`tradingview/quote` · data API · TradingView · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get a comprehensive real-time forex quote including current price, OHLC, bid/ask spread, volume, change, technical summary, key indicators, and performance metrics.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tradingview/quote"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tradingview/quote', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tradingview/quote", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tradingview/quote", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tradingview/quote` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `symbol` | string |  | Forex pair symbol (e.g., EURUSD, GBPUSD, USDJPY, AUDUSD, USDCAD, NZDUSD, EURGBP, EURJPY) default `"EURUSD"` |
| `exchange` | string |  | Exchange/data source (FX, OANDA, FX_IDC) one of: `FX`, `OANDA`, `FX_IDC`; default `"FX"` |

## Details

Get a comprehensive real-time forex quote including current price, OHLC, bid/ask spread, volume, change, technical summary, key indicators, and performance metrics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "tradingview/quote", "symbol": "EURUSD", "exchange": "FX"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `exchange` | string | No | Exchange/data source (FX, OANDA, FX_IDC) One of: `FX`, `OANDA`, `FX_IDC`. |
| `symbol` | string | No | Forex pair symbol (e.g., EURUSD, GBPUSD, USDJPY, AUDUSD, USDCAD, NZDUSD, EURGBP, EURJPY) |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tradingview/quote.json`](../../../catalog/models/tradingview/quote.json) · Store page: https://www.sandbase.ai/model/tradingview/quote

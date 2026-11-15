# TradingView Chart API: pricing, parameters and code examples

`tradingview/chart` · data API · TradingView · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get recent OHLC bar data for a forex pair at the specified interval.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tradingview/chart"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tradingview/chart', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tradingview/chart", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tradingview/chart", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tradingview/chart` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `bars` | integer |  | Maximum number of bars to return (1-30). Fewer bars may be returned depending on available data. default `10` |
| `symbol` | string |  | Forex pair symbol (e.g., EURUSD, GBPUSD, USDJPY, AUDUSD, USDCAD, NZDUSD, EURGBP, EURJPY) default `"EURUSD"` |
| `exchange` | string |  | Exchange/data source (FX, OANDA, FX_IDC) one of: `FX`, `OANDA`, `FX_IDC`; default `"FX"` |
| `interval` | string |  | Bar interval/timeframe one of: `1m`, `5m`, `15m`, `1H`, `4H`, `1D`, `1W`; default `"1D"` |

## Details

Get recent OHLC bar data for a forex pair at the specified interval.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "tradingview/chart", "bars": 10, "symbol": "EURUSD", "exchange": "FX", "interval": "1m"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `bars` | integer | No | Maximum number of bars to return (1-30). Fewer bars may be returned depending on available data. |
| `exchange` | string | No | Exchange/data source (FX, OANDA, FX_IDC) One of: `FX`, `OANDA`, `FX_IDC`. |
| `interval` | string | No | Bar interval/timeframe One of: `1m`, `5m`, `15m`, `1H`, `4H`, `1D`, `1W`. |
| `symbol` | string | No | Forex pair symbol (e.g., EURUSD, GBPUSD, USDJPY, AUDUSD, USDCAD, NZDUSD, EURGBP, EURJPY) |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tradingview/chart.json`](../../../catalog/models/tradingview/chart.json) · Store page: https://www.sandbase.ai/model/tradingview/chart

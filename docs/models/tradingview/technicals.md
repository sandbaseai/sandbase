# TradingView Technicals API: pricing, parameters and code examples

`tradingview/technicals` · data API · TradingView · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get detailed technical analysis for a forex pair including all oscillators (RSI, MACD, CCI, ADX, Stochastic, etc.), moving averages (EMA/SMA at 10/20/30/50/100/200 periods), and pivot points (Classic and Fibonacci). Use this for a full technical breakdown; use get_quote for a quick summary.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tradingview/technicals"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tradingview/technicals', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tradingview/technicals", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tradingview/technicals", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tradingview/technicals` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `symbol` | string |  | Forex pair symbol (e.g., EURUSD, GBPUSD, USDJPY, AUDUSD, USDCAD, NZDUSD, EURGBP, EURJPY) default `"EURUSD"` |
| `exchange` | string |  | Exchange/data source (FX, OANDA, FX_IDC) one of: `FX`, `OANDA`, `FX_IDC`; default `"FX"` |

## Details

Get detailed technical analysis for a forex pair including all oscillators (RSI, MACD, CCI, ADX, Stochastic, etc.), moving averages (EMA/SMA at 10/20/30/50/100/200 periods), and pivot points (Classic and Fibonacci). Use this for a full technical breakdown; use get_quote for a quick summary.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "tradingview/technicals", "symbol": "EURUSD", "exchange": "FX"}'
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
Machine-readable: [`catalog/models/tradingview/technicals.json`](../../../catalog/models/tradingview/technicals.json) · Store page: https://www.sandbase.ai/model/tradingview/technicals

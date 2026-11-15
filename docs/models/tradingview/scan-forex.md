# TradingView Scan Forex API: pricing, parameters and code examples

`tradingview/scan-forex` · data API · TradingView · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Scan multiple forex pairs at once, returning price, change, bid/ask, volume, and key technical indicators for each pair. Useful for building a watchlist or screening for trading signals across the forex market. Each pair includes a Buy/Sell/Neutral recommendation and RSI.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tradingview/scan-forex"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tradingview/scan-forex', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tradingview/scan-forex", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tradingview/scan-forex", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tradingview/scan-forex` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `symbols` | string |  | Comma-separated list of forex pair symbols (e.g., EURUSD,GBPUSD,USDJPY) default `"EURUSD,GBPUSD,USDJPY,AUDUSD,USDCAD"` |
| `exchange` | string |  | Exchange/data source for all symbols (FX, OANDA, FX_IDC) one of: `FX`, `OANDA`, `FX_IDC`; default `"FX"` |

## Details

Scan multiple forex pairs at once, returning price, change, bid/ask, volume, and key technical indicators for each pair. Useful for building a watchlist or screening for trading signals across the forex market. Each pair includes a Buy/Sell/Neutral recommendation and RSI.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "tradingview/scan-forex", "symbols": "EURUSD,GBPUSD,USDJPY", "exchange": "FX"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `exchange` | string | No | Exchange/data source for all symbols (FX, OANDA, FX_IDC) One of: `FX`, `OANDA`, `FX_IDC`. |
| `symbols` | string | No | Comma-separated list of forex pair symbols (e.g., EURUSD,GBPUSD,USDJPY) |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tradingview/scan-forex.json`](../../../catalog/models/tradingview/scan-forex.json) · Store page: https://www.sandbase.ai/model/tradingview/scan-forex

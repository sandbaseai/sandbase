# Yahoo Finance Historical Data API: pricing, parameters and code examples

`yahoo-finance/historical-data` · data API · Yahoo Finance · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.05 per call · **Modes:** async

Extract historical OHLCV price data for a single ticker over a configurable date range and interval. Returns timestamped records suitable for charting and technical analysis.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yahoo-finance/historical-data", "symbol": "AAPL"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yahoo-finance/historical-data', {'symbol': 'AAPL'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yahoo-finance/historical-data", {
  "symbol": "AAPL"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yahoo-finance/historical-data", sandbase.Params{
	"symbol": "AAPL",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/yahoo-finance/historical-data` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `range` | string |  | Date range for historical data.  |
| `symbol` | string | yes | Stock ticker symbol (e.g., AAPL).  |
| `interval` | string |  | Data interval granularity.  |

## Details

Extract historical OHLCV price data for a single ticker over a configurable date range and interval. Returns timestamped records suitable for charting and technical analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/yahoo-finance/historical-data" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"symbol": "AAPL"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `symbol` | string | Yes | Stock ticker symbol (e.g., AAPL). |
| `interval` | string | No | Data interval granularity. |
| `range` | string | No | Date range for historical data. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yahoo-finance/historical-data.json`](../../../catalog/models/yahoo-finance/historical-data.json) · Store page: https://www.sandbase.ai/model/yahoo-finance/historical-data

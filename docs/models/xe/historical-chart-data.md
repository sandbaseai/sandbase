# XE Historical Chart Data API: pricing, parameters and code examples

`xe/historical-chart-data` · data API · XE · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Retrieve historical exchange rate data points for a currency pair. Returns multiple time-series batches at different intervals (daily, hourly, 15-minute). Each batch contains a start time, interval in milliseconds, and an array of rate values.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xe/historical-chart-data", "to": "EUR", "from": "USD"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xe/historical-chart-data', {'to': 'EUR', 'from': 'USD'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xe/historical-chart-data", {
  "to": "EUR",
  "from": "USD"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xe/historical-chart-data", sandbase.Params{
	"to": "EUR",
	"from": "USD",
})
```

Same call via the path form: `POST /v1/api/xe/historical-chart-data` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `to` | string | yes | Target currency code (e.g. EUR). Supports all codes returned by get_currency_symbols.  |
| `from` | string | yes | Source currency code (e.g. USD). Supports all codes returned by get_currency_symbols.  |

## Details

Retrieve historical exchange rate data points for a currency pair. Returns multiple time-series batches at different intervals (daily, hourly, 15-minute). Each batch contains a start time, interval in milliseconds, and an array of rate values.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "xe/historical-chart-data", "to": "EUR", "from": "USD"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `from` | string | Yes | Source currency code (e.g. USD). Supports all codes returned by get_currency_symbols. |
| `to` | string | Yes | Target currency code (e.g. EUR). Supports all codes returned by get_currency_symbols. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xe/historical-chart-data.json`](../../../catalog/models/xe/historical-chart-data.json) · Store page: https://www.sandbase.ai/model/xe/historical-chart-data

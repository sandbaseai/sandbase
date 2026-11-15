# X-Rates Graph Data API: pricing, parameters and code examples

`x-rates/graph-data` · data API · X-Rates · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Returns exchange rate trend data points for a currency pair for the current year, suitable for generating graphs. Each data point contains a month abbreviation label and that month's average rate value, in calendar order up to the current month. One page fetch per call; no pagination.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "x-rates/graph-data", "to": "JPY", "from": "USD"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('x-rates/graph-data', {'to': 'JPY', 'from': 'USD'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("x-rates/graph-data", {
  "to": "JPY",
  "from": "USD"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "x-rates/graph-data", sandbase.Params{
	"to": "JPY",
	"from": "USD",
})
```

Same call via the path form: `POST /v1/api/x-rates/graph-data` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `to` | string | yes | Target currency code (e.g. EUR).  |
| `from` | string | yes | Source currency code (e.g. USD). one of: `USD`, `EUR`, `GBP`, `JPY`, `CHF`, `CAD`, `AUD` |
| `amount` | number |  | Amount to calculate rates for. default `1` |

## Details

Returns exchange rate trend data points for a currency pair for the current year, suitable for generating graphs. Each data point contains a month abbreviation label and that month's average rate value, in calendar order up to the current month. One page fetch per call; no pagination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "x-rates/graph-data", "to": "JPY", "from": "USD", "amount": 1.0}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `from` | string | Yes | Source currency code (e.g. USD). One of: `USD`, `EUR`, `GBP`, `JPY`, `CHF`, `CAD`, `AUD`. |
| `to` | string | Yes | Target currency code (e.g. EUR). |
| `amount` | number | No | Amount to calculate rates for. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/x-rates/graph-data.json`](../../../catalog/models/x-rates/graph-data.json) · Store page: https://www.sandbase.ai/model/x-rates/graph-data

# XE Live Exchange Rate API: pricing, parameters and code examples

`xe/live-exchange-rate` · data API · XE · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get the live mid-market exchange rate for a specific currency pair. Computes the cross-rate from USD-based rates. When amount is provided, also returns the converted value.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xe/live-exchange-rate", "to": "EUR", "from": "USD"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xe/live-exchange-rate', {'to': 'EUR', 'from': 'USD'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xe/live-exchange-rate", {
  "to": "EUR",
  "from": "USD"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xe/live-exchange-rate", sandbase.Params{
	"to": "EUR",
	"from": "USD",
})
```

Same call via the path form: `POST /v1/api/xe/live-exchange-rate` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `to` | string | yes | Target currency code (e.g. EUR, JPY, INR). Supports all codes returned by get_currency_symbols.  |
| `from` | string | yes | Source currency code (e.g. USD, EUR, GBP). Supports all codes returned by get_currency_symbols.  |
| `amount` | number |  | Amount to convert default `1` |

## Details

Get the live mid-market exchange rate for a specific currency pair. Computes the cross-rate from USD-based rates. When amount is provided, also returns the converted value.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "xe/live-exchange-rate", "to": "EUR", "from": "USD", "amount": 1.0}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `from` | string | Yes | Source currency code (e.g. USD, EUR, GBP). Supports all codes returned by get_currency_symbols. |
| `to` | string | Yes | Target currency code (e.g. EUR, JPY, INR). Supports all codes returned by get_currency_symbols. |
| `amount` | number | No | Amount to convert |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xe/live-exchange-rate.json`](../../../catalog/models/xe/live-exchange-rate.json) · Store page: https://www.sandbase.ai/model/xe/live-exchange-rate

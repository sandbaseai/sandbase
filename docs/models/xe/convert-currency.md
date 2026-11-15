# XE Convert Currency API: pricing, parameters and code examples

`xe/convert-currency` · data API · XE · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Convert a specific amount from source to target currency. Returns the same structure as get_live_exchange_rate with the specified amount applied to the mid-market rate.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xe/convert-currency", "to": "USD", "from": "EUR", "amount": 100}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xe/convert-currency', {'to': 'USD', 'from': 'EUR', 'amount': 100})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xe/convert-currency", {
  "to": "USD",
  "from": "EUR",
  "amount": 100
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xe/convert-currency", sandbase.Params{
	"to": "USD",
	"from": "EUR",
	"amount": 100,
})
```

Same call via the path form: `POST /v1/api/xe/convert-currency` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `to` | string | yes | Target currency code (e.g. USD, JPY). Supports all codes returned by get_currency_symbols.  |
| `from` | string | yes | Source currency code (e.g. EUR, GBP). Supports all codes returned by get_currency_symbols.  |
| `amount` | number | yes | Amount to convert  |

## Details

Convert a specific amount from source to target currency. Returns the same structure as get_live_exchange_rate with the specified amount applied to the mid-market rate.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "xe/convert-currency", "to": "USD", "from": "EUR", "amount": 100.0}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `amount` | number | Yes | Amount to convert |
| `from` | string | Yes | Source currency code (e.g. EUR, GBP). Supports all codes returned by get_currency_symbols. |
| `to` | string | Yes | Target currency code (e.g. USD, JPY). Supports all codes returned by get_currency_symbols. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xe/convert-currency.json`](../../../catalog/models/xe/convert-currency.json) · Store page: https://www.sandbase.ai/model/xe/convert-currency

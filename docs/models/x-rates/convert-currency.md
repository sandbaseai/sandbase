# X-Rates Convert Currency API: pricing, parameters and code examples

`x-rates/convert-currency` · data API · X-Rates · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Performs a currency conversion from one currency to another for a given amount. Returns the converted value and a text representation. Conversion uses the latest available rate.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "x-rates/convert-currency", "to": "EUR", "from": "USD"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('x-rates/convert-currency', {'to': 'EUR', 'from': 'USD'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("x-rates/convert-currency", {
  "to": "EUR",
  "from": "USD"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "x-rates/convert-currency", sandbase.Params{
	"to": "EUR",
	"from": "USD",
})
```

Same call via the path form: `POST /v1/api/x-rates/convert-currency` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `to` | string | yes | Target currency code (e.g. EUR, JPY, GBP).  |
| `from` | string | yes | Source currency code (e.g. USD, EUR, GBP). one of: `USD`, `EUR`, `GBP`, `JPY`, `CHF`, `CAD`, `AUD` |
| `amount` | number |  | Amount to convert. default `1` |

## Details

Performs a currency conversion from one currency to another for a given amount. Returns the converted value and a text representation. Conversion uses the latest available rate.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "x-rates/convert-currency", "to": "EUR", "from": "USD", "amount": 100.0}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `from` | string | Yes | Source currency code (e.g. USD, EUR, GBP). One of: `USD`, `EUR`, `GBP`, `JPY`, `CHF`, `CAD`, `AUD`. |
| `to` | string | Yes | Target currency code (e.g. EUR, JPY, GBP). |
| `amount` | number | No | Amount to convert. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/x-rates/convert-currency.json`](../../../catalog/models/x-rates/convert-currency.json) · Store page: https://www.sandbase.ai/model/x-rates/convert-currency

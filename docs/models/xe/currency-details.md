# XE Currency Details API: pricing, parameters and code examples

`xe/currency-details` · data API · XE · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get the ISO 2-letter country code associated with a specific currency. Useful for mapping currencies to their issuing country.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xe/currency-details", "currency": "USD"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xe/currency-details', {'currency': 'USD'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xe/currency-details", {
  "currency": "USD"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xe/currency-details", sandbase.Params{
	"currency": "USD",
})
```

Same call via the path form: `POST /v1/api/xe/currency-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `currency` | string | yes | Currency code (e.g. USD, EUR, GBP). Supports all codes returned by get_currency_symbols.  |

## Details

Get the ISO 2-letter country code associated with a specific currency. Useful for mapping currencies to their issuing country.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "xe/currency-details", "currency": "USD"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `currency` | string | Yes | Currency code (e.g. USD, EUR, GBP). Supports all codes returned by get_currency_symbols. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xe/currency-details.json`](../../../catalog/models/xe/currency-details.json) · Store page: https://www.sandbase.ai/model/xe/currency-details

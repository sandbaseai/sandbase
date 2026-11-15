# X-Rates Historical Rates Table API: pricing, parameters and code examples

`x-rates/historical-rates-table` · data API · X-Rates · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Fetches historical exchange rates for a base currency against all supported currencies on a specific date. The date must be in ISO YYYY-MM-DD format. Returns the same structure as the current rates table but for the specified historical date.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "x-rates/historical-rates-table", "date": "2026-10-16"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('x-rates/historical-rates-table', {'date': '2026-10-16'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("x-rates/historical-rates-table", {
  "date": "2026-10-16"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "x-rates/historical-rates-table", sandbase.Params{
	"date": "2026-10-16",
})
```

Same call via the path form: `POST /v1/api/x-rates/historical-rates-table` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `date` | string | yes | Historical date in ISO format YYYY-MM-DD.  |
| `from` | string |  | Base currency code. one of: `USD`, `EUR`, `GBP`, `JPY`, `CHF`, `CAD`, `AUD`; default `"USD"` |
| `amount` | number |  | Amount to calculate rates for. default `1` |

## Details

Fetches historical exchange rates for a base currency against all supported currencies on a specific date. The date must be in ISO YYYY-MM-DD format. Returns the same structure as the current rates table but for the specified historical date.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "x-rates/historical-rates-table", "date": "2026-10-16", "from": "USD", "amount": 1.0}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date` | string | Yes | Historical date in ISO format YYYY-MM-DD. |
| `amount` | number | No | Amount to calculate rates for. |
| `from` | string | No | Base currency code. One of: `USD`, `EUR`, `GBP`, `JPY`, `CHF`, `CAD`, `AUD`. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/x-rates/historical-rates-table.json`](../../../catalog/models/x-rates/historical-rates-table.json) · Store page: https://www.sandbase.ai/model/x-rates/historical-rates-table

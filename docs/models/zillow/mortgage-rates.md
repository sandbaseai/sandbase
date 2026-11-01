# Zillow Mortgage Rates

`zillow/mortgage-rates` · api · Zillow

Retrieve current mortgage interest rates from Zillow Home Loans. Returns rates for various loan types including conventional fixed (10/15/20/30-year), FHA fixed, VA fixed, jumbo fixed, and adjustable-rate mortgages.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zillow/mortgage-rates"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zillow/mortgage-rates', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zillow/mortgage-rates", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zillow/mortgage-rates", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/zillow/mortgage-rates` with the body above minus `model`.

## Details

Retrieve current mortgage interest rates from Zillow Home Loans. Returns rates for various loan types including conventional fixed (10/15/20/30-year), FHA fixed, VA fixed, jumbo fixed, and adjustable-rate mortgages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zillow/mortgage-rates" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

This API takes no parameters.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/zillow/mortgage-rates.json`](../../../catalog/models/zillow/mortgage-rates.json) · Store page: https://www.sandbase.ai/model/zillow/mortgage-rates

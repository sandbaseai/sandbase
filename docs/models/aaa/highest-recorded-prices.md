# AAA Highest Recorded Prices API: pricing, parameters and code examples

`aaa/highest-recorded-prices` · data API · AAA · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns all-time highest recorded average gas prices for a specific state or nationally. If no state_code is provided, returns national records.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/highest-recorded-prices"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aaa/highest-recorded-prices', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aaa/highest-recorded-prices", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aaa/highest-recorded-prices", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/aaa/highest-recorded-prices` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `state_code` | string |  | Two-letter US state code (e.g. TX, CA). Omitting returns national highest recorded prices.  |

## Details

Returns all-time highest recorded average gas prices for a specific state or nationally. If no state_code is provided, returns national records.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aaa/highest-recorded-prices" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `state_code` | string | No | Two-letter US state code (e.g. TX, CA). Omitting returns national highest recorded prices. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/aaa/highest-recorded-prices.json`](../../../catalog/models/aaa/highest-recorded-prices.json) · Store page: https://www.sandbase.ai/model/aaa/highest-recorded-prices

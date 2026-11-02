# AAA State Price Details API: pricing, parameters and code examples

`aaa/state-price-details` · data API · AAA · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Returns detailed gas price data for a specific state including current prices for all fuel grades, historical averages (yesterday, week ago, month ago, year ago), and all-time highest recorded prices with their dates.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/state-price-details", "state_code": "WA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aaa/state-price-details', {'state_code': 'WA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aaa/state-price-details", {
  "state_code": "WA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aaa/state-price-details", sandbase.Params{
	"state_code": "WA",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/aaa/state-price-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `state_code` | string | yes | Two-letter US state code (e.g. TX, CA, NY, FL). All 50 states and DC are supported.  |

## Details

Returns detailed gas price data for a specific state including current prices for all fuel grades, historical averages (yesterday, week ago, month ago, year ago), and all-time highest recorded prices with their dates.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aaa/state-price-details" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"state_code": "WA"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `state_code` | string | Yes | Two-letter US state code (e.g. TX, CA, NY, FL). All 50 states and DC are supported. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/aaa/state-price-details.json`](../../../catalog/models/aaa/state-price-details.json) · Store page: https://www.sandbase.ai/model/aaa/state-price-details

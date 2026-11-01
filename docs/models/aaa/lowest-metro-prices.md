# AAA Lowest Metro Prices

`aaa/lowest-metro-prices` · api · AAA

Returns metro areas within a state sorted by lowest regular gas price ascending. Useful for finding the cheapest metros within a state.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "aaa/lowest-metro-prices", "state_code": "WA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('aaa/lowest-metro-prices', {'state_code': 'WA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("aaa/lowest-metro-prices", {
  "state_code": "WA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "aaa/lowest-metro-prices", sandbase.Params{
	"state_code": "WA",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/aaa/lowest-metro-prices` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `state_code` | string | yes | Two-letter US state code (e.g. TX, CA, NY, FL). All 50 states and DC are supported.  |

## Details

Returns metro areas within a state sorted by lowest regular gas price ascending. Useful for finding the cheapest metros within a state.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/aaa/lowest-metro-prices" \
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
Machine-readable: [`catalog/models/aaa/lowest-metro-prices.json`](../../../catalog/models/aaa/lowest-metro-prices.json) · Store page: https://www.sandbase.ai/model/aaa/lowest-metro-prices

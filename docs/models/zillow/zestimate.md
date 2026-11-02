# Zillow Zestimate API: pricing, parameters and code examples

`zillow/zestimate` · data API · Zillow · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** async

Get the Zestimate (automated home value estimate) and rent Zestimate for a property by zpid.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zillow/zestimate", "zpid": "<zpid>"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zillow/zestimate', {'zpid': '<zpid>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zillow/zestimate", {
  "zpid": "<zpid>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zillow/zestimate", sandbase.Params{
	"zpid": "<zpid>",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/zillow/zestimate` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `zpid` | string | yes | Zillow property ID (numeric string, e.g., '2080998636')  |

## Details

Get the Zestimate (automated home value estimate) and rent Zestimate for a property by zpid.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zillow/zestimate" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"zpid": "2080998636"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `zpid` | string | Yes | Zillow property ID (numeric string, e.g., '2080998636') |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/zillow/zestimate.json`](../../../catalog/models/zillow/zestimate.json) · Store page: https://www.sandbase.ai/model/zillow/zestimate

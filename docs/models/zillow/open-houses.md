# Zillow Open Houses API: pricing, parameters and code examples

`zillow/open-houses` · data API · Zillow · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** async

Retrieve the scheduled open houses for a property listing by its Zillow property ID (zpid), together with the property's address for confirmation. Returns one record per property with an openHouses array (each entry.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zillow/open-houses", "zpid": "29505949"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zillow/open-houses', {'zpid': '29505949'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zillow/open-houses", {
  "zpid": "29505949"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zillow/open-houses", sandbase.Params{
	"zpid": "29505949",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/zillow/open-houses` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `zpid` | string | yes | Zillow property ID (numeric string, e.g., '29505949')  |

## Details

Retrieve the scheduled open houses for a property listing by its Zillow property ID (zpid), together with the property's address for confirmation. Returns one record per property with an openHouses array (each entry.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zillow/open-houses" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"zpid": "29505949"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `zpid` | string | Yes | Zillow property ID (numeric string, e.g., '29505949') |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/zillow/open-houses.json`](../../../catalog/models/zillow/open-houses.json) · Store page: https://www.sandbase.ai/model/zillow/open-houses

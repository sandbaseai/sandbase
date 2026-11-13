# Realtor.com Property API: pricing, parameters and code examples

`realtor/property` · data API · Realtor.com · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call · **Modes:** async

Get a Realtor.com property by listing URL with price, history, beds, baths, size, lot, year built, schools, agent and photos.

## Pricing

- **$0.00015 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "realtor/property", "url": "https://www.realtor.com/realestateandhomes-detail/13409-Madrone-Mountain-Way_Austin_TX_78737_M93328-41646"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('realtor/property', {'url': 'https://www.realtor.com/realestateandhomes-detail/13409-Madrone-Mountain-Way_Austin_TX_78737_M93328-41646'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("realtor/property", {
  "url": "https://www.realtor.com/realestateandhomes-detail/13409-Madrone-Mountain-Way_Austin_TX_78737_M93328-41646"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "realtor/property", sandbase.Params{
	"url": "https://www.realtor.com/realestateandhomes-detail/13409-Madrone-Mountain-Way_Austin_TX_78737_M93328-41646",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/realtor/property` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Realtor.com property URL under /realestateandhomes-detail/, without query parameters. Alpha: availability may vary by location or property. Returns available fields for the requested property.  |
| `timeout` | number |  | Seconds the data source may spend before giving up (max 50, default 50). A timed-out call is not billed. default `50`; range –50 |

## Details

Get a Realtor.com property by listing URL with price, history, beds, baths, size, lot, year built, schools, agent and photos.

---
Machine-readable: [`catalog/models/realtor/property.json`](../../../catalog/models/realtor/property.json) · Store page: https://www.sandbase.ai/model/realtor/property

# Apartments.com Property API: pricing, parameters and code examples

`apartments-com/property` · data API · Apartments.com · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call · **Modes:** async

Get an Apartments.com rental property by URL with floor plans, rent, availability, amenities, fees, pet policy and contact info.

## Pricing

- **$0.00015 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apartments-com/property", "url": "https://www.apartments.com/edison-austin-austin-tx/40n18nj/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('apartments-com/property', {'url': 'https://www.apartments.com/edison-austin-austin-tx/40n18nj/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("apartments-com/property", {
  "url": "https://www.apartments.com/edison-austin-austin-tx/40n18nj/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "apartments-com/property", sandbase.Params{
	"url": "https://www.apartments.com/edison-austin-austin-tx/40n18nj/",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/apartments-com/property` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Apartments.com property URL ending in its seven-character listing ID, without query parameters. Alpha: availability may vary by location or property. Returns available fields for the requested property. Prices may…  |
| `timeout` | number |  | Seconds the data source may spend before giving up (max 50, default 50). A timed-out call is not billed. default `50`; range –50 |

## Details

Get an Apartments.com rental property by URL with floor plans, rent, availability, amenities, fees, pet policy and contact info.

---
Machine-readable: [`catalog/models/apartments-com/property.json`](../../../catalog/models/apartments-com/property.json) · Store page: https://www.sandbase.ai/model/apartments-com/property

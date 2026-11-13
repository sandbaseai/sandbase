# Realtor.com Search API: pricing, parameters and code examples

`realtor/search` · data API · Realtor.com · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call · **Modes:** async

Get Realtor.com listings from a search results URL with address, price, beds, baths, size, status and listing link.

## Pricing

- **$0.00015 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "realtor/search", "url": "https://www.realtor.com/realestateandhomes-search/Austin_TX"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('realtor/search', {'url': 'https://www.realtor.com/realestateandhomes-search/Austin_TX'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("realtor/search", {
  "url": "https://www.realtor.com/realestateandhomes-search/Austin_TX"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "realtor/search", sandbase.Params{
	"url": "https://www.realtor.com/realestateandhomes-search/Austin_TX",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/realtor/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Realtor.com city_STATE or ZIP search URL under /realestateandhomes-search/ or /apartments/. Alpha: availability may vary by location or property.  |
| `limit` | integer |  | Listings per results page, from 1 to 200. range 1–200 |
| `timeout` | number |  | Seconds the data source may spend before giving up (max 50, default 50). A timed-out call is not billed. default `50`; range –50 |

## Details

Get Realtor.com listings from a search results URL with address, price, beds, baths, size, status and listing link.

---
Machine-readable: [`catalog/models/realtor/search.json`](../../../catalog/models/realtor/search.json) · Store page: https://www.sandbase.ai/model/realtor/search

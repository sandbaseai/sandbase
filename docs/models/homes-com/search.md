# Homes.com Search API: pricing, parameters and code examples

`homes-com/search` · data API · Homes.com · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call · **Modes:** async

Get Homes.com listings from a search results URL with address, price, beds, baths, size and listing link.

## Pricing

- **$0.00015 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "homes-com/search", "url": "https://www.homes.com/austin-tx/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('homes-com/search', {'url': 'https://www.homes.com/austin-tx/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("homes-com/search", {
  "url": "https://www.homes.com/austin-tx/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "homes-com/search", sandbase.Params{
	"url": "https://www.homes.com/austin-tx/",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/homes-com/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Homes.com location search URL, including sale, rental, price, property-type or page filters. Alpha: availability may vary by location or property. Use the site URL to set filters or select a page. Follow…  |
| `timeout` | number |  | Seconds the data source may spend before giving up (max 50, default 50). A timed-out call is not billed. default `50`; range –50 |

## Details

Get Homes.com listings from a search results URL with address, price, beds, baths, size and listing link.

---
Machine-readable: [`catalog/models/homes-com/search.json`](../../../catalog/models/homes-com/search.json) · Store page: https://www.sandbase.ai/model/homes-com/search

# Channel3 Lookup API: pricing, parameters and code examples

`channel3/lookup` · data API · Channel3 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.007 per call · **Modes:** async

Resolve a retailer product-page URL to a canonical product with offers and variants.

## Pricing

- **$0.007 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "channel3/lookup", "url": "https://www.nike.com/t/air-force-1-07-mens-shoes-jBrhbr/CW2288-111"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('channel3/lookup', {'url': 'https://www.nike.com/t/air-force-1-07-mens-shoes-jBrhbr/CW2288-111'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("channel3/lookup", {
  "url": "https://www.nike.com/t/air-force-1-07-mens-shoes-jBrhbr/CW2288-111"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "channel3/lookup", sandbase.Params{
	"url": "https://www.nike.com/t/air-force-1-07-mens-shoes-jBrhbr/CW2288-111",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/channel3/lookup` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Retailer product-page URL to resolve.  |
| `realtime_fetch` | boolean |  | Fetch the page live when the URL is not in the catalog or its data is older than max_staleness_hours. false = catalog only: stale data is returned as-is and unknown URLs return 404. Channel3 default: true.  |
| `max_staleness_hours` | integer |  | Maximum age in hours of cached product data before a fresh fetch. Channel3 default: 3. range 1–9007199254740991 |

## Details

Resolve a retailer product-page URL to a canonical product with offers and variants.

---
Machine-readable: [`catalog/models/channel3/lookup.json`](../../../catalog/models/channel3/lookup.json) · Store page: https://www.sandbase.ai/model/channel3/lookup

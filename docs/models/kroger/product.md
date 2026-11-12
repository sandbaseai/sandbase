# Kroger Product API: pricing, parameters and code examples

`kroger/product` · data API · Kroger · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call · **Modes:** async

Get one Kroger grocery product by URL with title, price, size, images and store availability; pass a store ID for local pricing.

## Pricing

- **$0.00015 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kroger/product", "url": "https://www.kroger.com/p/organic-valley-whole-milk-half-gallon/0009396651300"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kroger/product', {'url': 'https://www.kroger.com/p/organic-valley-whole-milk-half-gallon/0009396651300'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kroger/product", {
  "url": "https://www.kroger.com/p/organic-valley-whole-milk-half-gallon/0009396651300"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kroger/product", sandbase.Params{
	"url": "https://www.kroger.com/p/organic-valley-whole-milk-half-gallon/0009396651300",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/kroger/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Public HTTPS product URL on this retailer's site.  |
| `timeout` | number |  | Seconds the data source may spend before giving up (max 50, default 50). A timed-out call is not billed. default `50`; range –50 |
| `store_id` | string |  | Retailer's store ID. Selects the store catalog, pricing or availability where the retailer exposes it.  |

## Details

Get one Kroger grocery product by URL with title, price, size, images and store availability; pass a store ID for local pricing.

---
Machine-readable: [`catalog/models/kroger/product.json`](../../../catalog/models/kroger/product.json) · Store page: https://www.sandbase.ai/model/kroger/product

# Sprouts Product API: pricing, parameters and code examples

`sprouts/product` · data API · Sprouts Farmers Market · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call · **Modes:** async

Get a Sprouts Farmers Market product by URL with name, price, size, description and store availability.

## Pricing

- **$0.00015 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "sprouts/product", "url": "https://shop.sprouts.com/store/sprouts/products/120137222-grazeful-dairy-grassfed-whole-a2-a2-milk-2-gal"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('sprouts/product', {'url': 'https://shop.sprouts.com/store/sprouts/products/120137222-grazeful-dairy-grassfed-whole-a2-a2-milk-2-gal'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("sprouts/product", {
  "url": "https://shop.sprouts.com/store/sprouts/products/120137222-grazeful-dairy-grassfed-whole-a2-a2-milk-2-gal"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "sprouts/product", sandbase.Params{
	"url": "https://shop.sprouts.com/store/sprouts/products/120137222-grazeful-dairy-grassfed-whole-a2-a2-milk-2-gal",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/sprouts/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Public HTTPS product URL on this retailer's site.  |
| `timeout` | number |  | Seconds the data source may spend before giving up (max 50, default 50). A timed-out call is not billed. default `50`; range –50 |
| `store_id` | string |  | Sprouts store location ID, such as 17650. Selects that store's in-store catalog.  |

## Details

Get a Sprouts Farmers Market product by URL with name, price, size, description and store availability.

---
Machine-readable: [`catalog/models/sprouts/product.json`](../../../catalog/models/sprouts/product.json) · Store page: https://www.sandbase.ai/model/sprouts/product

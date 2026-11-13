# Whole Foods Product API: pricing, parameters and code examples

`whole-foods/product` · data API · Whole Foods Market · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call · **Modes:** async

Get a Whole Foods Market product by URL with name, brand, price, size, ingredients, nutrition and dietary labels.

## Pricing

- **$0.00015 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "whole-foods/product", "url": "https://www.wholefoodsmarket.com/product/clover-sonoma-organic-milk-32-fz-b019p8vdyy"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('whole-foods/product', {'url': 'https://www.wholefoodsmarket.com/product/clover-sonoma-organic-milk-32-fz-b019p8vdyy'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("whole-foods/product", {
  "url": "https://www.wholefoodsmarket.com/product/clover-sonoma-organic-milk-32-fz-b019p8vdyy"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "whole-foods/product", sandbase.Params{
	"url": "https://www.wholefoodsmarket.com/product/clover-sonoma-organic-milk-32-fz-b019p8vdyy",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/whole-foods/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Public HTTPS product URL on this retailer's site.  |
| `timeout` | number |  | Seconds the data source may spend before giving up (max 50, default 50). A timed-out call is not billed. default `50`; range –50 |
| `store_id` | string |  | Retailer's store ID. Selects the store catalog, pricing or availability where the retailer exposes it.  |

## Details

Get a Whole Foods Market product by URL with name, brand, price, size, ingredients, nutrition and dietary labels.

---
Machine-readable: [`catalog/models/whole-foods/product.json`](../../../catalog/models/whole-foods/product.json) · Store page: https://www.sandbase.ai/model/whole-foods/product

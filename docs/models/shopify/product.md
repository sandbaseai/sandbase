# Shopify Product API: pricing, parameters and code examples

`shopify/product` · data API · Shopify · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

Look up one product on any public Shopify store by its handle or product page URL and get title, vendor, type, tags, description, price range, sale price, stock, images, options and every variant's SKU, price and stock in one normalized response.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "shopify/product", "store": "allbirds.com", "product": "mens-strider"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('shopify/product', {'store': 'allbirds.com', 'product': 'mens-strider'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("shopify/product", {
  "store": "allbirds.com",
  "product": "mens-strider"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "shopify/product", sandbase.Params{
	"store": "allbirds.com",
	"product": "mens-strider",
})
```

Same call via the path form: `POST /v1/api/shopify/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `store` | string | yes | Domain or URL of a public Shopify store, e.g. allbirds.com or https://kith.com. A store on its own domain is addressed by that domain.  |
| `product` | string | yes | Product handle, the slug after /products/ in the product URL, e.g. mens-strider; the full product page URL also works.  |

## Details

Look up one product on any public Shopify store by its handle or product page URL and get title, vendor, type, tags, description, price range, sale price, stock, images, options and every variant's SKU, price and stock in one normalized response.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "shopify/product", "store": "allbirds.com", "product": "mens-strider"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product` | string | Yes | Product handle, the slug after /products/ in the product URL, e.g. mens-strider; the full product page URL also works. |
| `store` | string | Yes | Domain or URL of a public Shopify store, e.g. allbirds.com or https://kith.com. A store on its own domain is addressed by that domain. |

### Pricing

Billed at the actual cost of each call, about $0.00085 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/shopify/product.json`](../../../catalog/models/shopify/product.json) · Store page: https://www.sandbase.ai/model/shopify/product

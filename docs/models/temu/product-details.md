# Temu Product Details API: pricing, parameters and code examples

`temu/product-details` · data API · Temu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Retrieve product details for a specific product by its numeric ID, including variant/SKU data.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "temu/product-details", "product_id": "<product_id>"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('temu/product-details', {'product_id': '<product_id>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("temu/product-details", {
  "product_id": "<product_id>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "temu/product-details", sandbase.Params{
	"product_id": "<product_id>",
})
```

Same call via the path form: `POST /v1/api/temu/product-details` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `locale` | string |  | Locale/language code for localized results (e.g. 'en', 'it', 'de', 'fr', 'es'). Controls language of titles and currency of prices. default `"en"` |
| `product_id` | string | yes | Numeric product ID from search_products.products[*].product_id or get_homepage_featured.products[*].product_id.  |

## Details

Retrieve product details for a specific product by its numeric ID, including variant/SKU data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "temu/product-details", "locale": "en"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Numeric product ID from search_products.products[*].product_id or get_homepage_featured.products[*].product_id. |
| `locale` | string | No | Locale/language code for localized results (e.g. 'en', 'it', 'de', 'fr', 'es'). Controls language of titles and currency of prices. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/temu/product-details.json`](../../../catalog/models/temu/product-details.json) · Store page: https://www.sandbase.ai/model/temu/product-details

# Temu Product Images API: pricing, parameters and code examples

`temu/product-images` · data API · Temu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Retrieve product image URLs for one or more products by their numeric IDs (up to 40 per request).

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "temu/product-images", "product_ids": "<product_ids>"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('temu/product-images', {'product_ids': '<product_ids>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("temu/product-images", {
  "product_ids": "<product_ids>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "temu/product-images", sandbase.Params{
	"product_ids": "<product_ids>",
})
```

Same call via the path form: `POST /v1/api/temu/product-images` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `locale` | string |  | Locale/language code for localized results (e.g. 'en', 'it', 'de', 'fr', 'es'). Controls regional CDN and product availability. default `"en"` |
| `product_ids` | string | yes | Comma-separated list of numeric product IDs (up to 40). Example: '606334506389973,606009615600410'.  |

## Details

Retrieve product image URLs for one or more products by their numeric IDs (up to 40 per request).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "temu/product-images", "locale": "en"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_ids` | string | Yes | Comma-separated list of numeric product IDs (up to 40). Example: '606334506389973,606009615600410'. |
| `locale` | string | No | Locale/language code for localized results (e.g. 'en', 'it', 'de', 'fr', 'es'). Controls regional CDN and product availability. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/temu/product-images.json`](../../../catalog/models/temu/product-images.json) · Store page: https://www.sandbase.ai/model/temu/product-images

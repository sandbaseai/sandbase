# Temu Batch Products API: pricing, parameters and code examples

`temu/batch-get-products` · data API · Temu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Batch fetch product data for multiple product IDs in one call (up to 40). For each product ID, returns both raw API data and a flat normalized DTO. Each product result carries its own status field so single failures don't break the batch. Products are looked up via Temu's catalog search by goods_id.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "temu/batch-get-products", "product_ids": "[\"605731197670167\"]"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('temu/batch-get-products', {'product_ids': '["605731197670167"]'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("temu/batch-get-products", {
  "product_ids": "[\"605731197670167\"]"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "temu/batch-get-products", sandbase.Params{
	"product_ids": "[\"605731197670167\"]",
})
```

Same call via the path form: `POST /v1/api/temu/batch-get-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `locale` | string |  | Locale/language code for localized results (e.g. 'en', 'it', 'de', 'fr', 'es'). default `"en"` |
| `include_dto` | boolean |  | If true, include the flat normalized DTO per product. default `true` |
| `include_raw` | boolean |  | If true, include the raw API response data per product. default `true` |
| `product_ids` | string | yes | JSON array of numeric product ID strings (up to 40). Example: '["605731197670167","605714873454696"]'.  |

## Details

Batch fetch product data for multiple product IDs in one call (up to 40). For each product ID, returns both raw API data and a flat normalized DTO. Each product result carries its own status field so single failures don't break the batch. Products are looked up via Temu's catalog search by goods_id.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "temu/batch-get-products", "locale": "en", "include_dto": true, "include_raw": true, "product_ids": "[\"605731197670167\"]"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_ids` | string | Yes | JSON array of numeric product ID strings (up to 40). Example: '["605731197670167","605714873454696"]'. |
| `include_dto` | boolean | No | If true, include the flat normalized DTO per product. |
| `include_raw` | boolean | No | If true, include the raw API response data per product. |
| `locale` | string | No | Locale/language code for localized results (e.g. 'en', 'it', 'de', 'fr', 'es'). |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/temu/batch-get-products.json`](../../../catalog/models/temu/batch-get-products.json) · Store page: https://www.sandbase.ai/model/temu/batch-get-products

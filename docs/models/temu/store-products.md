# Temu Store Products API: pricing, parameters and code examples

`temu/store-products` · data API · Temu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Retrieve products listed by a specific store/seller on Temu, identified by mall_id.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "temu/store-products", "mall_id": "2610127"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('temu/store-products', {'mall_id': '2610127'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("temu/store-products", {
  "mall_id": "2610127"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "temu/store-products", sandbase.Params{
	"mall_id": "2610127",
})
```

Same call via the path form: `POST /v1/api/temu/store-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of results to return per page (max 40). default `40` |
| `locale` | string |  | Locale/language code for localized results (e.g. 'en', 'it', 'de', 'fr', 'es'). Controls language of titles and currency of prices. default `"en"` |
| `offset` | integer |  | Offset for pagination. Advance by `limit` for the next page. default `0` |
| `mall_id` | string | yes | Numeric store/seller identifier from search_products.products[*].mall_id or get_product_details.mall_id.  |

## Details

Retrieve products listed by a specific store/seller on Temu, identified by mall_id.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "temu/store-products", "limit": 10, "locale": "en", "offset": 0, "mall_id": "2610127"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `mall_id` | string | Yes | Numeric store/seller identifier from search_products.products[*].mall_id or get_product_details.mall_id. |
| `limit` | integer | No | Number of results to return per page (max 40). |
| `locale` | string | No | Locale/language code for localized results (e.g. 'en', 'it', 'de', 'fr', 'es'). Controls language of titles and currency of prices. |
| `offset` | integer | No | Offset for pagination. Advance by `limit` for the next page. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/temu/store-products.json`](../../../catalog/models/temu/store-products.json) · Store page: https://www.sandbase.ai/model/temu/store-products

# Temu Batch Stores API: pricing, parameters and code examples

`temu/batch-get-stores` · data API · Temu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Batch fetch store products for multiple mall IDs in one call (up to 20).

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "temu/batch-get-stores", "mall_ids": "[\"2610127\"]"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('temu/batch-get-stores', {'mall_ids': '["2610127"]'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("temu/batch-get-stores", {
  "mall_ids": "[\"2610127\"]"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "temu/batch-get-stores", sandbase.Params{
	"mall_ids": "[\"2610127\"]",
})
```

Same call via the path form: `POST /v1/api/temu/batch-get-stores` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of products to return per store (max 999). Internally splits into multiple 40-item upstream requests. default `40` |
| `locale` | string |  | Locale/language code for localized results (e.g. 'en', 'it', 'de', 'fr', 'es'). default `"en"` |
| `offset` | integer |  | Offset for pagination within each store's product list. default `0` |
| `mall_ids` | string | yes | JSON array of mall ID strings (up to 20). Example: '["2610127","634418223099265"]'.  |
| `include_dto` | boolean |  | If true, include the flat normalized DTO per store. default `true` |
| `include_raw` | boolean |  | If true, include the raw API response data per store. default `true` |

## Details

Batch fetch store products for multiple mall IDs in one call (up to 20).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "temu/batch-get-stores", "limit": 10, "locale": "en", "offset": 0, "mall_ids": "[\"2610127\"]", "include_dto": true, "include_raw": true}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `mall_ids` | string | Yes | JSON array of mall ID strings (up to 20). Example: '["2610127","634418223099265"]'. |
| `include_dto` | boolean | No | If true, include the flat normalized DTO per store. |
| `include_raw` | boolean | No | If true, include the raw API response data per store. |
| `limit` | integer | No | Number of products to return per store (max 999). Internally splits into multiple 40-item upstream requests. |
| `locale` | string | No | Locale/language code for localized results (e.g. 'en', 'it', 'de', 'fr', 'es'). |
| `offset` | integer | No | Offset for pagination within each store's product list. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/temu/batch-get-stores.json`](../../../catalog/models/temu/batch-get-stores.json) · Store page: https://www.sandbase.ai/model/temu/batch-get-stores

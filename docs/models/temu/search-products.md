# Temu Search Products API: pricing, parameters and code examples

`temu/search-products` · data API · Temu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Full-text search over Temu's product catalog by keyword.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "temu/search-products", "query": "wireless earbuds"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('temu/search-products', {'query': 'wireless earbuds'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("temu/search-products", {
  "query": "wireless earbuds"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "temu/search-products", sandbase.Params{
	"query": "wireless earbuds",
})
```

Same call via the path form: `POST /v1/api/temu/search-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of results to return per page. default `48` |
| `query` | string | yes | Search keyword (e.g. 'wireless earbuds', 'kitchen gadgets').  |
| `locale` | string |  | Locale/language code for localized results (e.g. 'en', 'it', 'de', 'fr', 'es'). Controls language of titles and currency of prices. default `"en"` |
| `offset` | integer |  | Offset for pagination. Advance by `limit` for the next page. default `0` |
| `price_max` | number |  | Maximum price in USD. Only products with a price <= this value are returned.  |
| `price_min` | number |  | Minimum price in USD. Only products with a price >= this value are returned.  |

## Details

Full-text search over Temu's product catalog by keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "temu/search-products", "limit": 10, "query": "wireless earbuds", "locale": "en", "offset": 0, "price_max": 50.0, "price_min": 5.0}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (e.g. 'wireless earbuds', 'kitchen gadgets'). |
| `limit` | integer | No | Number of results to return per page. |
| `locale` | string | No | Locale/language code for localized results (e.g. 'en', 'it', 'de', 'fr', 'es'). Controls language of titles and currency of prices. |
| `offset` | integer | No | Offset for pagination. Advance by `limit` for the next page. |
| `price_max` | number | No | Maximum price in USD. Only products with a price <= this value are returned. |
| `price_min` | number | No | Minimum price in USD. Only products with a price >= this value are returned. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/temu/search-products.json`](../../../catalog/models/temu/search-products.json) · Store page: https://www.sandbase.ai/model/temu/search-products

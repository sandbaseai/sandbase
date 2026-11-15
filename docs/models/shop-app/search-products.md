# Shop Search Products API: pricing, parameters and code examples

`shop-app/search-products` · data API · Shop · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Searches shop.app products globally by a free-text keyword and returns one page of matching products from the site's global search results (actual product records, not autocomplete suggestions or merchant-only results).

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "shop-app/search-products", "query": "running shoes"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('shop-app/search-products', {'query': 'running shoes'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("shop-app/search-products", {
  "query": "running shoes"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "shop-app/search-products", sandbase.Params{
	"query": "running shoes",
})
```

Same call via the path form: `POST /v1/api/shop-app/search-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `after` | string |  | Pagination cursor taken unchanged from a previous response's end_cursor field. Omit for the first page.  |
| `first` | integer |  | Number of products to return for this page (1-100). Takes precedence over page_size when both are given; when omitted, page_size applies.  |
| `query` | string | yes | Free-text search keyword, e.g. one shape is a product type like a shoe or phone name. Must be non-empty.  |
| `page_size` | integer |  | Legacy page-size control (1-100), used only when first is omitted. default `30` |

## Details

Searches shop.app products globally by a free-text keyword and returns one page of matching products from the site's global search results (actual product records, not autocomplete suggestions or merchant-only results).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "shop-app/search-products", "first": 10, "query": "running shoes"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Free-text search keyword, e.g. one shape is a product type like a shoe or phone name. Must be non-empty. |
| `after` | string | No | Pagination cursor taken unchanged from a previous response's end_cursor field. Omit for the first page. |
| `first` | integer | No | Number of products to return for this page (1-100). Takes precedence over page_size when both are given; when omitted, page_size applies. |
| `page_size` | integer | No | Legacy page-size control (1-100), used only when first is omitted. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/shop-app/search-products.json`](../../../catalog/models/shop-app/search-products.json) · Store page: https://www.sandbase.ai/model/shop-app/search-products

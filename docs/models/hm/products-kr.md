# H&M List Products Kr API: pricing, parameters and code examples

`hm/products-kr` · data API · H&M · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

List Korean H&M products by category path. Returns paginated products with Korean names, KRW prices, member prices, images, and facets. Sort by price is supported. The category path maps to the Korean site's navigation structure. Each page returns up to page_size products (default 36).

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hm/products-kr", "category": "ladies/products/view-all"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hm/products-kr', {'category': 'ladies/products/view-all'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hm/products-kr", {
  "category": "ladies/products/view-all"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hm/products-kr", sandbase.Params{
	"category": "ladies/products/view-all",
})
```

Same call via the path form: `POST /v1/api/hm/products-kr` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination (1-based). default `1` |
| `sort` | string |  | Sort order. Supported values: 'ascPrice' (lowest first), 'descPrice' (highest first). Omit for default.  |
| `category` | string | yes | Korean site category path (e.g. 'ladies/products/view-all', 'men/new-arrivals/view-all', 'ladies/sale/view-all', 'men/jeans/view-all').  |
| `page_size` | integer |  | Number of products per page. default `36` |

## Details

List Korean H&M products by category path. Returns paginated products with Korean names, KRW prices, member prices, images, and facets. Sort by price is supported. The category path maps to the Korean site's navigation structure. Each page returns up to page_size products (default 36).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "hm/products-kr", "page": 1, "sort": "ascPrice", "category": "ladies/products/view-all", "page_size": 5}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category` | string | Yes | Korean site category path (e.g. 'ladies/products/view-all', 'men/new-arrivals/view-all', 'ladies/sale/view-all', 'men/jeans/view-all'). |
| `page` | integer | No | Page number for pagination (1-based). |
| `page_size` | integer | No | Number of products per page. |
| `sort` | string | No | Sort order. Supported values: 'ascPrice' (lowest first), 'descPrice' (highest first). Omit for default. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/hm/products-kr.json`](../../../catalog/models/hm/products-kr.json) · Store page: https://www.sandbase.ai/model/hm/products-kr

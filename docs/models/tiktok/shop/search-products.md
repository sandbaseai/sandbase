# TikTok Shop Product Search API: pricing, parameters and code examples

`tiktok/shop/search-products` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Search TikTok Shop products by keyword within a selected region, with offset and page-token pagination. Use it to discover regional products and continue through search results.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/shop/search-products", "keyword": "iphone"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/shop/search-products', {'keyword': 'iphone'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/shop/search-products", {
  "keyword": "iphone"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/shop/search-products", sandbase.Params{
	"keyword": "iphone",
})
```

Same call via the path form: `POST /v1/api/tiktok/shop/search-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Search result offset. default `0` |
| `region` | string |  | Target region for product search. one of: `US`, `GB`, `FR`, `SG`, `MY`, `PH`, `TH`, `VN`, `ID`; default `"US"` |
| `keyword` | string | yes | Search keyword.  |
| `pageToken` | string |  | Pagination token for the next page.  |

## Details

Search TikTok Shop products by keyword within a selected region, with offset and page-token pagination. Use it to discover regional products and continue through search results.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/shop/search-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "phone case"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `region` | string | No | Target region for product search. |
| `offset` | integer | No | Search result offset. |
| `pageToken` | string | No | Pagination token for the next page. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/tiktok/shop/search-products.json`](../../../../catalog/models/tiktok/shop/search-products.json) · Store page: https://www.sandbase.ai/model/tiktok/shop/search-products

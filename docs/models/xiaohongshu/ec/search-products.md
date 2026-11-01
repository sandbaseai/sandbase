# Xiaohongshu Shop Product Search

`xiaohongshu/ec/search-products` · api · Xiaohongshu

Search products sold in Xiaohongshu (RedNote) shops by keyword, with price, sales and shop info.

## Pricing

- **$0.027778 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/ec/search-products", "keyword": "防晒霜"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/ec/search-products', {'keyword': '防晒霜'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/ec/search-products", {
  "keyword": "防晒霜"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/ec/search-products", sandbase.Params{
	"keyword": "防晒霜",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/ec/search-products` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string |  | Page number, starting from 1.  |
| `keyword` | string | yes | Search keyword.  |
| `searchId` | string |  | Search ID returned by the first-page response; required when page is greater than 1.  |

## Details

Search products sold in Xiaohongshu (RedNote) shops by keyword, with price, sales and shop info.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/ec/search-products" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "防晒霜"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `page` | string | No | Page number, starting from 1. |
| `searchId` | string | No | Search ID returned by the first-page response; required when page is greater than 1. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/ec/search-products.json`](../../../../catalog/models/xiaohongshu/ec/search-products.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/ec/search-products

# Douyin Shop Product Search API: pricing, parameters and code examples

`douyin/ec/search-items` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.035714 per call · **Modes:** sync

Search products sold in Douyin shops by keyword, with price, sales and shop info; pages after the first use searchId.

## Pricing

- **$0.035714 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/ec/search-items", "keyword": "防晒霜"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/ec/search-items', {'keyword': '防晒霜'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/ec/search-items", {
  "keyword": "防晒霜"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/ec/search-items", sandbase.Params{
	"keyword": "防晒霜",
})
```

Same call via the path form: `POST /v1/api/douyin/ec/search-items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string |  | Page number for pagination.  |
| `keyword` | string | yes | Search keyword.  |
| `searchId` | string |  | Search ID; use the search_id value returned by the last response for subsequent pages.  |

## Details

Search products sold in Douyin shops by keyword, with price, sales and shop info; pages after the first use searchId.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/ec/search-items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "防晒霜"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `page` | string | No | Page number for pagination. |
| `searchId` | string | No | Search ID; use the search_id value returned by the last response for subsequent pages. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/douyin/ec/search-items.json`](../../../../catalog/models/douyin/ec/search-items.json) · Store page: https://www.sandbase.ai/model/douyin/ec/search-items

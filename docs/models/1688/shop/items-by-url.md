# 1688 Shop Products by URL

`1688/shop/items-by-url` · api · 1688

List a 1688 shop's products from its homepage URL, with sort, page size and category filters.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/shop/items-by-url", "shopUrl": "https://winport.m.1688.com/page/index.html?memberId=b2b-35345497994841a"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/shop/items-by-url', {'shopUrl': 'https://winport.m.1688.com/page/index.html?memberId=b2b-35345497994841a'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/shop/items-by-url", {
  "shopUrl": "https://winport.m.1688.com/page/index.html?memberId=b2b-35345497994841a"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/shop/items-by-url", sandbase.Params{
	"shopUrl": "https://winport.m.1688.com/page/index.html?memberId=b2b-35345497994841a",
})
```

Same call via the path form: `POST /v1/api/1688/shop/items-by-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cat` | string |  | Optional category ID filter.  |
| `page` | integer |  | Page number, starting at 1. default `1` |
| `sort` | string |  | Shop product sort order. one of: `default`, `sales`, `price_up`, `price_down`, `time_up`, `time_down`; default `"default"` |
| `catType` | string |  | Optional category mode: 0 or 1. one of: `0`, `1` |
| `shopUrl` | string | yes | 1688 shop homepage URL.  |
| `pageSize` | integer |  | Number of items requested per page. The returned count may differ. default `20` |

## Details

List a 1688 shop's products from its homepage URL, with sort, page size and category filters.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/shop/items-by-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"shopUrl": "https://winport.m.1688.com/page/index.html?memberId=b2b-35345497994841a"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `shopUrl` | string | Yes | 1688 shop homepage URL. |
| `page` | integer | No | Page number, starting at 1. |
| `pageSize` | integer | No | Number of items requested per page. The returned count may differ. |
| `sort` | string | No | Shop product sort order. |
| `cat` | string | No | Optional category ID filter. |
| `catType` | string | No | Optional category mode: 0 or 1. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/1688/shop/items-by-url.json`](../../../../catalog/models/1688/shop/items-by-url.json) · Store page: https://www.sandbase.ai/model/1688/shop/items-by-url

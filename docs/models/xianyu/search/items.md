# Xianyu Item Search API: pricing, parameters and code examples

`xianyu/search/items` · data API · Xianyu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.027778 per call · **Modes:** sync

Search Xianyu (Goofish) second-hand listings by keyword, sorted by activity, recency, seller credit or price.

## Pricing

- **$0.027778 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xianyu/search/items", "keyword": "iphone 15"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xianyu/search/items', {'keyword': 'iphone 15'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xianyu/search/items", {
  "keyword": "iphone 15"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xianyu/search/items", sandbase.Params{
	"keyword": "iphone 15",
})
```

Same call via the path form: `POST /v1/api/xianyu/search/items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string |  | Page number for pagination. The first page is 1.  |
| `sort` | string |  | Sort order for Xianyu search results. one of: `active`, `recent`, `credit`, `price_asc`, `price_desc`, `price_drop`, `newest`; default `"active"` |
| `keyword` | string | yes | Search keyword.  |

## Details

Search Xianyu (Goofish) second-hand listings by keyword, sorted by activity, recency, seller credit or price.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xianyu/search/items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "iphone 15"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `page` | string | No | Page number for pagination. The first page is 1. |
| `sort` | string | No | Sort order for Xianyu search results. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xianyu/search/items.json`](../../../../catalog/models/xianyu/search/items.json) · Store page: https://www.sandbase.ai/model/xianyu/search/items

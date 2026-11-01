# Taobao Product Search

`taobao/search/items` · api · Taobao

Search Taobao and Tmall products by keyword with titles, prices, images, sales and shop info. Sort by sales or price, filter to Tmall only and by price range.

## Pricing

- **$0.027778 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "taobao/search/items", "keyword": "蓝牙耳机"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('taobao/search/items', {'keyword': '蓝牙耳机'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("taobao/search/items", {
  "keyword": "蓝牙耳机"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "taobao/search/items", sandbase.Params{
	"keyword": "蓝牙耳机",
})
```

Same call via the path form: `POST /v1/api/taobao/search/items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `sort` | string |  | Sort order for the result set. one of: `_sale`, `_bid`, `bid`, `_coefp`; default `"_sale"` |
| `tmall` | boolean |  | Whether to filter results to Tmall only. default `false` |
| `keyword` | string | yes | Search keyword.  |
| `endPrice` | string |  | Maximum price filter (inclusive).  |
| `startPrice` | string |  | Minimum price filter (inclusive).  |

## Details

Search Taobao and Tmall products by keyword with titles, prices, images, sales and shop info. Sort by sales or price, filter to Tmall only and by price range.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/taobao/search/items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "手机壳"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `sort` | string | No | Sort order for the result set. |
| `tmall` | boolean | No | Whether to filter results to Tmall only. |
| `startPrice` | string | No | Minimum price filter (inclusive). |
| `endPrice` | string | No | Maximum price filter (inclusive). |
| `page` | integer | No | Page number for pagination. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/taobao/search/items.json`](../../../../catalog/models/taobao/search/items.json) · Store page: https://www.sandbase.ai/model/taobao/search/items

# JD.com Product Search API: pricing, parameters and code examples

`jd/search/items` · data API · JD.com · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.020834 per call · **Modes:** sync

Search JD.com products by keyword with item IDs, titles, images, categories and shop names, with page-based pagination.

## Pricing

- **$0.020834 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "jd/search/items", "keyword": "蓝牙耳机"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('jd/search/items', {'keyword': '蓝牙耳机'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("jd/search/items", {
  "keyword": "蓝牙耳机"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "jd/search/items", sandbase.Params{
	"keyword": "蓝牙耳机",
})
```

Same call via the path form: `POST /v1/api/jd/search/items` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string |  | Page number for pagination.  |
| `keyword` | string | yes | Search keyword.  |

## Details

Search JD.com products by keyword with item IDs, titles, images, categories and shop names, with page-based pagination.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/jd/search/items" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "手机壳"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `page` | string | No | Page number for pagination. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/jd/search/items.json`](../../../../catalog/models/jd/search/items.json) · Store page: https://www.sandbase.ai/model/jd/search/items

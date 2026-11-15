# Ximalaya Search Albums API: pricing, parameters and code examples

`ximalaya/search-albums` · data API · Ximalaya · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Full-text search for albums by keyword. Supports Chinese and English queries. Returns paginated results with album summaries including play counts, track counts, anchor name, and intro text.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ximalaya/search-albums", "query": "历史"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ximalaya/search-albums', {'query': '历史'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ximalaya/search-albums", {
  "query": "历史"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ximalaya/search-albums", sandbase.Params{
	"query": "历史",
})
```

Same call via the path form: `POST /v1/api/ximalaya/search-albums` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `query` | string | yes | Search keyword (supports Chinese characters and English).  |
| `page_size` | integer |  | Number of results per page. default `20` |

## Details

Full-text search for albums by keyword. Supports Chinese and English queries. Returns paginated results with album summaries including play counts, track counts, anchor name, and intro text.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "ximalaya/search-albums", "page": 1, "query": "历史", "page_size": 5}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (supports Chinese characters and English). |
| `page` | integer | No | Page number for pagination. |
| `page_size` | integer | No | Number of results per page. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/ximalaya/search-albums.json`](../../../catalog/models/ximalaya/search-albums.json) · Store page: https://www.sandbase.ai/model/ximalaya/search-albums

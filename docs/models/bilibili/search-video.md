# Bilibili Video Search

`bilibili/search-video` · api · Bilibili

Search Bilibili videos by keyword with page-based pagination and sorting by general ranking, play count, publish time, danmaku count, or favorites.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/search-video", "keyword": "原神"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/search-video', {'keyword': '原神'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/search-video", {
  "keyword": "原神"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/search-video", sandbase.Params{
	"keyword": "原神",
})
```

Same call via the path form: `POST /v1/api/bilibili/search-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | string |  | Page number for pagination.  |
| `order` | string |  | Sorting criteria for search results. one of: `general`, `click`, `pubdate`, `dm`, `stow`; default `"general"` |
| `keyword` | string | yes | Search keyword.  |

## Details

Search Bilibili videos by keyword with page-based pagination and sorting by general ranking, play count, publish time, danmaku count, or favorites.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/search-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "原神"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword. |
| `page` | string | No | Page number for pagination. |
| `order` | string | No | Sorting criteria for search results. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/bilibili/search-video.json`](../../../catalog/models/bilibili/search-video.json) · Store page: https://www.sandbase.ai/model/bilibili/search-video

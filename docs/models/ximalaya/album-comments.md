# Ximalaya Album Comments API: pricing, parameters and code examples

`ximalaya/album-comments` · data API · Ximalaya · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Retrieve comments for an album with pagination. Returns comment content, author nickname, likes, reply count, region, creation timestamp, and overall album score/rating statistics.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ximalaya/album-comments", "album_id": "81519744"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ximalaya/album-comments', {'album_id': '81519744'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ximalaya/album-comments", {
  "album_id": "81519744"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ximalaya/album-comments", sandbase.Params{
	"album_id": "81519744",
})
```

Same call via the path form: `POST /v1/api/ximalaya/album-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number for pagination. default `1` |
| `order` | string |  | Sort order for comments (e.g. content-score-desc). default `"content-score-desc"` |
| `album_id` | string | yes | Numeric album ID (e.g. 77855794). Obtainable from get_category_albums or search_albums results.  |
| `page_size` | integer |  | Number of comments per page. default `10` |

## Details

Retrieve comments for an album with pagination. Returns comment content, author nickname, likes, reply count, region, creation timestamp, and overall album score/rating statistics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "ximalaya/album-comments", "album_id": "81519744"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `album_id` | string | Yes | Numeric album ID (e.g. 77855794). Obtainable from get_category_albums or search_albums results. |
| `order` | string | No | Sort order for comments (e.g. content-score-desc). |
| `page` | integer | No | Page number for pagination. |
| `page_size` | integer | No | Number of comments per page. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/ximalaya/album-comments.json`](../../../catalog/models/ximalaya/album-comments.json) · Store page: https://www.sandbase.ai/model/ximalaya/album-comments

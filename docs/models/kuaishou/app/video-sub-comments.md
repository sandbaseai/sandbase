# Kuaishou Video Sub Comments (App) API: pricing, parameters and code examples

`kuaishou/app/video-sub-comments` · data API · Kuaishou · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns sub comments and replies under a root comment for a Kuaishou video. Supports pagination using a cursor and page size configuration.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "kuaishou/app/video-sub-comments", "photo_id": "1", "root_comment_id": "1"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('kuaishou/app/video-sub-comments', {'photo_id': '1', 'root_comment_id': '1'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("kuaishou/app/video-sub-comments", {
  "photo_id": "1",
  "root_comment_id": "1"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "kuaishou/app/video-sub-comments", sandbase.Params{
	"photo_id": "1",
	"root_comment_id": "1",
})
```

Same call via the path form: `POST /v1/api/kuaishou/app/video-sub-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Page size, default 8, range 1-20  |
| `pcursor` | string |  | Cursor, empty for first page  |
| `photo_id` | string | yes | 作品ID/Photo ID  |
| `root_comment_id` | string | yes | 一级评论ID/Root comment ID  |

## Details

Retrieve nested replies under a specific root comment on Kuaishou. Pass `photo_id` and `root_comment_id` to retrieve comment thread details.

### Use cases

- Display threaded reply discussions beneath main video comments.
- Monitor community responses and conversations for a specific comment.
- Extract conversation threads for audience interaction analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/kuaishou/app/video-sub-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"photo_id": "<photo_id>", "root_comment_id": "<root_comment_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `photo_id` | string | Yes | — |
| `root_comment_id` | string | Yes | — |
| `count` | integer | No | Page size, default 8, range 1-20 |
| `pcursor` | string | No | Cursor, empty for first page |

### Notes

- Set `count` between 1 and 20 to control page size (defaults to 8).
- Provide `pcursor` for subsequent pages or leave it empty for the first page.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Kuaishou Brand Top List](/model/kuaishou/app/brand-top-list): Returns top brand rankings and related live stream links from Kuaishou.
- [Kuaishou App Share Link](/model/kuaishou/app/generate-share-link): Generates a shareable URL for Kuaishou application content using a specified object identifier.
- [Kuaishou Hot Board Categories](/model/kuaishou/app/hot-board-categories): Returns the active list of hot board categories available in the Kuaishou app.

---
Machine-readable: [`catalog/models/kuaishou/app/video-sub-comments.json`](../../../../catalog/models/kuaishou/app/video-sub-comments.json) · Store page: https://www.sandbase.ai/model/kuaishou/app/video-sub-comments

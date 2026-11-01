# Xiaohongshu (RED) Note Comments

`xiaohongshu/app-v2/note-comments` · api · Xiaohongshu

Get the comments on a Xiaohongshu note: comment text, time, likes, reply counts and location, with sorting and cursor pagination.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/note-comments", "cursor": "", "index": 0, "note_id": "6a59e720000000000f033247", "pageArea": "UNFOLDED", "sort_strategy": "like_count"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/note-comments', {'cursor': '', 'index': 0, 'note_id': '6a59e720000000000f033247', 'pageArea': 'UNFOLDED', 'sort_strategy': 'like_count'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/note-comments", {
  "cursor": "",
  "index": 0,
  "note_id": "6a59e720000000000f033247",
  "pageArea": "UNFOLDED",
  "sort_strategy": "like_count"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/note-comments", sandbase.Params{
	"cursor": "",
	"index": 0,
	"note_id": "6a59e720000000000f033247",
	"pageArea": "UNFOLDED",
	"sort_strategy": "like_count",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/note-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `index` | integer |  | Comment index, pass 0 for first request, pass index value from previous response for next page default `0` |
| `cursor` | string |  | Pagination cursor, leave empty for first request, pass cursor value from previous response for next page default `""` |
| `note_id` | string |  | Note ID, e.g. "697c0eee000000000a03c308" default `""` |
| `pageArea` | string |  | Fold status, default "UNFOLDED" (unfolded), pass pageArea value from previous response for next page default `"UNFOLDED"` |
| `share_text` | string |  | Xiaohongshu sharing link (support APP and Web sharing link) default `""` |
| `sort_strategy` | string |  | Sort strategy default `"latest_v2"` |

## Details

Pass a Xiaohongshu note ID (or a share link) and get its comments.

### Use cases

- Analyze consumer feedback on products.
- Find questions and pain points in comments.
- Monitor comments on brand notes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/note-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"note_id": "697c0eee000000000a03c308"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `index` | integer | No | Comment index, pass 0 for first request, pass index value from previous response for next page |
| `cursor` | string | No | Pagination cursor, leave empty for first request, pass cursor value from previous response for next page |
| `note_id` | string | No | Note ID, e.g. "697c0eee000000000a03c308" |
| `pageArea` | string | No | Fold status, default "UNFOLDED" (unfolded), pass pageArea value from previous response for next page |
| `share_text` | string | No | Xiaohongshu sharing link (support APP and Web sharing link) |
| `sort_strategy` | string | No | Sort strategy |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "cursor": "<cursor>",
    "has_more": true,
    "comments": [
      {
        "id": "69cb9fa90000000015001832",
        "note_id": "697c0eee000000000a03c308",
        "time": 1774952362,
        "like_count": 0,
        "sub_comment_count": 0,
        "content": "想起来一部纪录片，忘了名字🧐",
        "user": {
          "nickname": "<user>"
        }
      }
    ]
  }
}
```

### Notes

- Paginate with `cursor`, `index` and `pageArea` from the previous response.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Note Search](/model/xiaohongshu/app-v2/search-notes): Search Xiaohongshu (RED / Little Red Book) notes by keyword and get titles, authors, cover images and like, collect, comment and share counts, with sort, note-…
- [Get creator hot inspiration feed](/model/xiaohongshu/app-v2/creator-hot-inspiration-feed): Get creator center hot inspiration feed, using cursor pagination.
- [Get creator inspiration feed](/model/xiaohongshu/app-v2/creator-inspiration-feed): Get creator center recommended inspiration feed, using cursor pagination.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/note-comments.json`](../../../../catalog/models/xiaohongshu/app-v2/note-comments.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/note-comments

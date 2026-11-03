# Xiaohongshu (RED) Note Comments API: pricing, parameters and code examples

`xiaohongshu/app-v2/note-comments` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Get the comments on a Xiaohongshu note: comment text, time, likes, reply counts and location, with sorting and cursor pagination.

## Pricing

- **$0.01 per call** (USD)
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

Returns the comments on a Xiaohongshu note: comment text, post time, like count, reply count and the commenter's name and ID. It needs a `note_id`, or a Xiaohongshu share link in `share_text`. Results come in pages, with a choice of sort order.

### Use cases

- Read what viewers say about a brand note to spot praise and complaints.
- Collect questions from comment threads to find topics for new content.
- Rank comments by likes to find the most supported opinions on a note.
- Export comment text and timestamps to track how discussion on a note builds over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/note-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"note_id": "697c0eee000000000a03c308"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Pagination cursor, leave empty for first request, pass cursor value from previous response for next page |
| `index` | integer | No | Comment index, pass 0 for first request, pass index value from previous response for next page |
| `note_id` | string | No | Note ID, e.g. "697c0eee000000000a03c308" |
| `pageArea` | string | No | Fold status, default "UNFOLDED" (unfolded), pass pageArea value from previous response for next page |
| `share_text` | string | No | Xiaohongshu sharing link (support APP and Web sharing link) |
| `sort_strategy` | string | No | Sort strategy |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "all_sort_strategies": [
      {
        "optional_name": "Default",
        "suffix_name": "",
        "type": "default"
      }
    ],
    "comment_count": 192,
    "comment_count_l1": 153,
    "comments": [
      {
        "at_users": [],
        "biz_label": {
          "group_invite": "false",
          "product_review": false,
          "rich_text": "unknown"
        },
        "collected": false,
        "comment_type": 0,
        "content": "长桌",
        "downvoted": false,
        "friend_liked_msg": "",
        "hidden": false,
        "id": "6aa08562000000000a01d66e",
        "invalid": false,
        "like_count": 0,
        "liked": false
      }
    ],
    "current_sort_strategy": "latest_v2",
    "cursor": "{\"contextId\":\"9a8084a1a39f4b71a9017f187eccdd83\",\"cursor\":\"69aaee1e00000000190009…",
    "has_more": true,
    "page_context": "{\"exposed_l1_ids\":\"6aa08562000000000a01d66e,69da730e00000000160162d2,69cb9fa9000…",
    "user_id": "5efc6e660000000001006da1"
  },
  "debug_id": "148260f1",
  "debug_info": "gAAAAABq6ZFn2PL9M17PFWysU5DHuRD_A1yM_0-38jtmjB-9zRE4mL6L2gXqR3_LP5_F2oecc1ua16Fy…",
  "msg": "",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.comments[].content` | Text of the comment. |
| `data.comments[].id` | ID of the comment. Use it to tell comments apart across pages. |
| `data.comments[].time` | Time the comment was posted, as a Unix timestamp in seconds. |
| `data.comments[].like_count` | Number of likes on the comment. |
| `data.comments[].sub_comment_count` | Number of replies to the comment. The replies themselves appear in `data.comments[].sub_comments`. |
| `data.comments[].user.nickname / data.comments[].user.red_id` | Display name and RED ID of the commenter. |
| `data.comment_count / data.comment_count_l1` | Total comments on the note, and the count of top-level comments only. |
| `data.all_sort_strategies[].type` | Sort values you can send in `sort_strategy`, such as `default`, `latest_v2` and `like_count`. |
| `data.current_sort_strategy` | Sort order used for this response. |
| `data.has_more` | `true` when more comments are available on a next page. |
| `data.cursor` | Pagination token to pass as `cursor` to get the next page. |

### Notes

- The first request needs only `note_id`. The default sort is `latest_v2`.
- To get the next page, pass the `data.cursor` value as `cursor`. Also pass the matching `index` and `pageArea` values from the previous response. Stop when `data.has_more` is `false`.
- Note IDs are 24-character hex strings, such as `697c0eee000000000a03c308`. Take them from a note search or a user's posted notes, for example [Xiaohongshu (RED) Note Search](/apis/xiaohongshu/app-v2/search-notes) or [Xiaohongshu (RED) User Posted Notes](/apis/xiaohongshu/app-v2/user-posted-notes).
- For the note itself, call [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail) or [Xiaohongshu (RED) Video Note Detail](/apis/xiaohongshu/app-v2/video-note-detail).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Xiaohongshu (RED) Note Search](/apis/xiaohongshu/app-v2/search-notes): Search Xiaohongshu (RED / Little Red Book) notes by keyword and get titles, authors, cover images and like, collect, comment and share counts, with sort, note-…
- [Get creator hot inspiration feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Get creator center hot inspiration feed, using cursor pagination.
- [Get creator inspiration feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Get creator center recommended inspiration feed, using cursor pagination.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/note-comments.json`](../../../../catalog/models/xiaohongshu/app-v2/note-comments.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/note-comments

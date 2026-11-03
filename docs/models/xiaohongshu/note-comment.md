# Xiaohongshu Note Comments API: pricing, parameters and code examples

`xiaohongshu/note-comment` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get comments for a Xiaohongshu (RedNote) note with cursor pagination and normal, latest, or like-count sorting. Use it to support feedback review, discussion analysis, and comment moderation workflows.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/note-comment", "noteId": "6ae00b99000000001200a9f9"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/note-comment', {'noteId': '6ae00b99000000001200a9f9'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/note-comment", {
  "noteId": "6ae00b99000000001200a9f9"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/note-comment", sandbase.Params{
	"noteId": "6ae00b99000000001200a9f9",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/note-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Sort strategy for the result set. one of: `normal`, `latest`, `like_count`; default `"latest"` |
| `noteId` | string | yes | A Xiaohongshu note ID or an explore URL containing /explore/.  |
| `lastCursor` | string |  | Pagination cursor from the previous page (use the cursor value returned by the last response).  |

## Details

Returns the comments on one Xiaohongshu (RedNote) note, one page at a time. It needs a note ID or an explore URL as `noteId`, and it can sort by `normal`, `latest`, or `like_count`.

### Use cases

- Pull the newest comments on a brand note to review customer feedback.
- Sort by `like_count` to find the most supported opinions in a discussion.
- Collect comment text, author, and location to analyze audience reactions to a post.
- Page through all comments on a note to check for spam or comments that need moderation.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/note-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"noteId": "6ae00b99000000001200a9f9"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `noteId` | string | Yes | A Xiaohongshu note ID or an explore URL containing /explore/. |
| `lastCursor` | string | No | Pagination cursor from the previous page (use the cursor value returned by the last response). |
| `sort` | string | No | Sort strategy for the result set. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "all_sort_strategies": [
    {
      "optional_name": "默认",
      "suffix_name": "",
      "type": "default"
    }
  ],
  "comment_count": 511,
  "comment_count_l1": 509,
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
      "content": "支持",
      "downvoted": false,
      "friend_liked_msg": "",
      "hidden": false,
      "id": "6ae1ef66000000000b013365",
      "ip_location": "福建",
      "like_count": 1,
      "liked": false
    }
  ],
  "current_sort_strategy": "latest_v2",
  "cursor": "{\"contextId\":\"18776461ea634fadb544f0bfa4d12332\",\"cursor\":\"6ae14ceb00000000120342…",
  "has_more": true,
  "page_context": "{\"exposed_l1_ids\":\"6ae1ef66000000000b013365,6ae1eb02000000001202bc7c,6ae1e8a4000…",
  "user_id": "64b898310000000014037b21"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comment_count / comment_count_l1` | Total comments on the note, and the count of top-level comments only. In this response they are 511 and 509. |
| `comments[].id` | ID of the comment. |
| `comments[].content` | Comment text. It can include platform emoji codes such as `[点赞R]`. |
| `comments[].like_count` | Number of likes on the comment. |
| `comments[].time` | Comment time as a Unix timestamp in seconds. |
| `comments[].ip_location` | Location label shown with the comment, such as a province or country. |
| `comments[].sub_comment_count / comments[].sub_comments[]` | Count of replies to the comment, and the reply items that came with this page. |
| `comments[].user.nickname / comments[].user.red_id / comments[].user.userid` | Display name, public RED ID, and internal user ID of the commenter. |
| `has_more` | `true` when more comments are available on the next page. |
| `cursor` | Cursor string for the next page. Pass it as `lastCursor`. |
| `current_sort_strategy` | Sort that was applied to this result. The default request returned `latest_v2`. |

### Notes

- Take the note ID from the `/explore/` part of a note URL, or pass the full explore URL as `noteId`.
- To get the next page, send the `cursor` value from the response as `lastCursor`. Keep going while `has_more` is `true`.
- Use the same `sort` value on every page of one note.
- To get note details, call [Xiaohongshu Note Details](/apis/xiaohongshu/note-detail).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/note-comment.json`](../../../catalog/models/xiaohongshu/note-comment.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/note-comment

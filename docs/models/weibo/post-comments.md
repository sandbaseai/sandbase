# Weibo Post Comments API: pricing, parameters and code examples

`weibo/post-comments` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get comments for a Weibo post identified by MID, with optional maxId cursor pagination and time or hot sorting.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/post-comments", "mid": "4799069542679480"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/post-comments', {'mid': '4799069542679480'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/post-comments", {
  "mid": "4799069542679480"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/post-comments", sandbase.Params{
	"mid": "4799069542679480",
})
```

Same call via the path form: `POST /v1/api/weibo/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `mid` | string | yes | Weibo post mid.  |
| `sort` | string |  | Sort order for the result set. one of: `TIME`, `HOT`; default `"TIME"` |
| `maxId` | string |  | Pagination cursor returned by the previous response.  |

## Details

Returns the comments on a Weibo post. It needs the post `mid` and returns a page of comments with text, author, like count and posting time. You can sort by `TIME` or `HOT` and page through results with a cursor.

### Use cases

- Collect public reactions to a Weibo post for sentiment analysis.
- Track how many comments a post has gathered and which ones get the most likes.
- Study where commenters are posting from using the `source` field.
- Export comment text and author details for moderation or research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"mid": "5359793518938198"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `mid` | string | Yes | Weibo post mid. |
| `maxId` | string | No | Pagination cursor returned by the previous response. |
| `sort` | string | No | Sort order for the result set. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "allow_follow": false,
      "analysis_extra": "author_uid:2803301701|mid:5359793518938198|rid:2022842004866702828",
      "biz_mark_type": 0,
      "cmt_ext": "level_type:1",
      "comment_bubble": {
        "end_color": "#1AA55DAB",
        "end_color_dark": "#33A55DAB",
        "icon_url": "https://h5.sinaimg.cn/upload/100/1720/2023/06/14/commentbubble_zuan_A55DAB.png",
        "id": "zuan_0001",
        "name": "钻粉专属",
        "obtain_type": 3,
        "start_color": "#00A55DAB",
        "start_color_dark": "#00A55DAB"
      },
      "comments": [],
      "created_at": "Fri Oct 30 19:21:31 +0800 2026",
      "degrade_type": "normal",
      "disable_reply": 0,
      "floor_number": 79,
      "hasvisible": false,
      "id": 5359799699247641
    }
  ],
  "filter_group": [
    {
      "isDefault": 0,
      "param": "flow=0",
      "scheme": "",
      "title": "按热度"
    }
  ],
  "header_text": "以下为博主精选评论 ",
  "max_id": 0,
  "ok": 1,
  "rootComment": [],
  "tip_msg": "",
  "total_number": 384,
  "trendsText": "博主已开启评论精选"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | The list of comments on this page. Each item is one top-level comment. |
| `data[].text_raw / data[].text` | The comment text as written by the user. |
| `data[].created_at` | When the comment was posted, in a format like `Fri Oct 30 19:21:31 +0800 2026`. |
| `data[].like_counts` | Number of likes on the comment. |
| `data[].floor_number` | The comment's floor number in the thread. |
| `data[].idstr / data[].mid` | The comment's own ID as a string. It differs from the `mid` of the post you requested. |
| `data[].source` | Where the comment was posted from, such as a province name with a `来自` prefix. |
| `data[].user.followers_count` | Follower count of the commenter. The `user` object also holds avatar URLs and the profile `description`. |
| `data[].comments` | Nested replies to the comment. It is empty in this response. |
| `total_number` | Total number of comments reported for the post. |
| `max_id` | Cursor for the next page. A value of `0` means the response gives no further cursor. |

### Notes

- Take the post `mid` from a post detail or user feed response. [Weibo Post Detail](/apis/weibo/web-v2/post-detail) returns post data.
- For the next page, pass the `max_id` value from the response as `maxId`. Stop when `max_id` is `0`.
- `sort` accepts `TIME` (default) or `HOT`.
- To read replies under a comment, call [Weibo Post Sub-Comments](/apis/weibo/web-v2/post-sub-comments).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/weibo/post-comments.json`](../../../catalog/models/weibo/post-comments.json) · Store page: https://www.sandbase.ai/model/weibo/post-comments

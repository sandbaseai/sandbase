# Weibo Post Comments API: pricing, parameters and code examples

`weibo/web-v2/post-comments` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get the first-level comments on a Weibo post: comment text, author, time, likes and reply counts, with cursor pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/post-comments", "id": "5350554563773695"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/post-comments', {'id': '5350554563773695'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/post-comments", {
  "id": "5350554563773695"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/post-comments", sandbase.Params{
	"id": "5350554563773695",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string | yes | Weibo post ID (required)  |
| `count` | integer |  | Number of comments (default 10) default `10` |
| `max_id` | string |  | Pagination cursor, pass empty for first request, use returned max_id for subsequent requests default `""` |

## Details

Returns the first-level comments on a Weibo post, with comment text, author, time, like count and reply count. It needs the Weibo post `id`. Results come in pages that you walk through with the `max_id` cursor.

### Use cases

- Read the most recent reactions to a brand post on Weibo.
- Rank comments by `like_counts` to find the most supported opinions on a post.
- Export comment text and author follower counts for sentiment analysis.
- Find comments with replies and fetch those replies in a second call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"id": "5350554563773695"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | Yes | Weibo post ID (required) |
| `count` | integer | No | Number of comments (default 10) |
| `max_id` | string | No | Pagination cursor, pass empty for first request, use returned max_id for subsequent requests |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "allow_follow": false,
      "analysis_extra": "author_uid:1727858283|mid:5350554563773695|rid:162412728022526544",
      "biz_mark_type": 0,
      "cmt_ext": "level_type:1",
      "comment_bubble": {
        "end_color": "#1AFEAD3A",
        "end_color_dark": "#33FEAD3A",
        "icon_url": "https://h5.sinaimg.cn/upload/100/1720/2023/06/14/commentbubble_jin_FEAD3A.png",
        "id": "jin_0001",
        "name": "金粉专属",
        "obtain_type": 3,
        "start_color": "#00FEAD3A",
        "start_color_dark": "#00FEAD3A"
      },
      "comments": [
        {
          "allow_follow": false,
          "analysis_extra": "author_uid:1727858283|mid:5350554563773695|rid:162412728022526544",
          "biz_mark_type": 0,
          "blogger_icons": [
            {
              "actionlog": {
                "act_code": "3671",
                "ext": "status:author"
              },
              "length": "1.33",
              "name": "blogger",
              "url": "https://h5.sinaimg.cn/upload/116/1347/2020/12/15/bozhu.png"
            }
          ],
          "cmt_ext": "level_type:2",
          "created_at": "Mon Oct 05 07:49:58 +0800 2026",
          "degrade_type": "normal",
          "disable_reply": 0
        }
      ],
      "created_at": "Mon Oct 05 07:09:09 +0800 2026",
      "degrade_type": "normal",
      "disable_reply": 0,
      "floor_number": 2,
      "id": 5350555695188006,
      "idstr": "5350555695188006"
    }
  ],
  "filter_group": [
    {
      "isDefault": 1,
      "param": "flow=0",
      "scheme": "",
      "title": "按热度"
    }
  ],
  "max_id": 138895166347417,
  "ok": 1,
  "rootComment": [],
  "tip_msg": "",
  "total_number": 36,
  "trendsText": "已加载全部评论"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].text_raw` | Plain text of the comment. Emoji appear as bracket tags such as `[打call]`. The `text` field holds the same comment as HTML with image tags. |
| `data[].id / data[].idstr` | ID of the comment, as a number and as a string. Use the string form to avoid number precision loss. |
| `data[].created_at` | Time the comment was posted, in a format like `Mon Oct 05 07:09:09 +0800 2026`. |
| `data[].like_counts` | Number of likes on the comment. |
| `data[].total_number` | Number of replies to this comment. The `data[].comments[]` list holds a few of those replies, and `data[].more_info.text` shows a label such as `共3条回复`. |
| `data[].source` | Location label shown with the comment, for example `来自 上海`. |
| `data[].user.followers_count` | Follower count of the commenter. `data[].user.description` holds the commenter's profile bio and `data[].user.avatar_large` holds the avatar URL. |
| `data[].floor_number` | Floor position of the comment in the thread. |
| `max_id` | Cursor for the next page. Pass it as `max_id` in the next request. |
| `total_number` | Total comment count reported for the post. `trendsText` holds a status message such as `已加载全部评论`. |

### Notes

- Leave `max_id` empty on the first call. For later pages, pass the top-level `max_id` from the previous response.
- `count` sets how many comments to return per page and defaults to 10.
- The `filter_group` list shows two sort modes, `flow=0` (by heat, the default) and `flow=1` (by time).
- To read all replies under a comment, call [Weibo Post Sub-Comments](/apis/weibo/web-v2/post-sub-comments). For the post itself, use [Weibo Post Detail](/apis/weibo/web-v2/post-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo Real-Time Hot Search](/apis/weibo/web-v2/hot-search): Get the Weibo real-time hot search ranking: trending keywords with rank, heat value and labels such as new or hot.
- [Weibo Hot Search List](/apis/weibo/web-v2/hot-search-summary): Get the complete real-time Weibo hot search ranking (top 50): keyword, rank, heat tag and search link for each trending topic.

---
Machine-readable: [`catalog/models/weibo/web-v2/post-comments.json`](../../../../catalog/models/weibo/web-v2/post-comments.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/post-comments

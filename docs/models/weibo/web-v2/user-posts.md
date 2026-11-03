# Weibo User Posts API: pricing, parameters and code examples

`weibo/web-v2/user-posts` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get the posts published by a Weibo user: text, publish time, images, videos and repost, comment and like counts, with pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/user-posts", "uid": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/user-posts', {'uid': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/user-posts", {
  "uid": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/user-posts", sandbase.Params{
	"uid": "example",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |
| `page` | integer |  | Page number, starts from 1 (default 1)  |
| `feature` | integer |  | Data feature value (default 0)  |
| `since_id` | string |  | Pagination identifier for next page  |

## Details

Returns the posts published by a Weibo account, newest pinned post first, with text, publish time, images and engagement counts. It needs the numeric user ID in `uid`, and it pages through older posts.

### Use cases

- Track what an official account or media outlet posts and how people react to each post.
- Compare like and comment counts across an account's posts to see which content performs best.
- Download the image URLs of an account's posts to build a media archive.
- Collect an account's post history page by page for offline analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "2803301701"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |
| `feature` | integer | No | Data feature value (default 0) |
| `page` | integer | No | Page number, starts from 1 (default 1) |
| `since_id` | string | No | Pagination identifier for next page |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "bottom_tips_text": "",
    "bottom_tips_visible": false,
    "list": [
      {
        "analysis_extra": "follow:0",
        "annotations": [
          {
            "photo_sub_type": "0,0,0,0,0,0,0,0,0"
          }
        ],
        "attitudes_count": 1103,
        "attitudes_status": 0,
        "can_edit": false,
        "cardid": "star_1624",
        "comment_manage_info": {
          "approval_comment_type": 0,
          "comment_anon_type": 0,
          "comment_permission_type": -1,
          "comment_sort_type": 0
        },
        "comments_count": 567,
        "content_auth": 3,
        "content_auth_list": [
          {
            "content_auth": 3,
            "rank": 90,
            "show_type": 0
          }
        ],
        "created_at": "Tue Nov 03 07:44:51 +0800 2026",
        "favorited": false
      }
    ],
    "since_id": "5360945434198751kp2",
    "status_visible": 0,
    "topicList": [],
    "total": 154903
  },
  "ok": 1
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.list[]` | One post per item. Each item holds the post text, time, media and counts. |
| `data.list[].id / idstr / mid` | Numeric and string forms of the post ID. `idstr` and `mid` are the same value as a string. |
| `data.list[].mblogid` | Short code for the post. Use it to identify the post in other calls. |
| `data.list[].created_at` | Publish time as a text date with a `+0800` offset, for example `Tue Nov 03 07:44:51 +0800 2026`. |
| `data.list[].attitudes_count / comments_count` | Number of likes and number of comments on the post. |
| `data.list[].isTop` | Shows `1` when the post is pinned to the top of the account's page. |
| `data.list[].pic_ids[]` | IDs of the images attached to the post. Each ID is a key in `pic_infos`. |
| `data.list[].pic_infos.<pic_id>.original.url / large.url / bmiddle.url` | Image URLs at different sizes for one picture. Each size also gives `width` and `height`. |
| `data.list[].isLongText` | Tells you whether the post is marked as long text. |
| `data.list[].number_display_strategy.display_text` | Short display form of a large count, for example `100万+`. |

### Notes

- Get the `uid` from a Weibo profile. Use [Weibo User Search](/apis/weibo/web-v2/user-search) to find it from a name.
- Send `page` starting at 1 to get later pages. You can also pass the `since_id` value from the previous response.
- Call [Weibo Post Comments](/apis/weibo/web-v2/post-comments) or [Weibo Post Detail](/apis/weibo/web-v2/post-detail) to go deeper on one post.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo Real-Time Hot Search](/apis/weibo/web-v2/hot-search): Get the Weibo real-time hot search ranking: trending keywords with rank, heat value and labels such as new or hot.
- [Weibo Hot Search List](/apis/weibo/web-v2/hot-search-summary): Get the complete real-time Weibo hot search ranking (top 50): keyword, rank, heat tag and search link for each trending topic.

---
Machine-readable: [`catalog/models/weibo/web-v2/user-posts.json`](../../../../catalog/models/weibo/web-v2/user-posts.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/user-posts

# Douyin Video Comments (Web) API: pricing, parameters and code examples

`douyin/web/video-comments` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comments for a specific Douyin video using its video ID. Supports pagination controls via cursor and item count parameters.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/video-comments", "aweme_id": "7372484719365098803", "count": 20, "cursor": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/video-comments', {'aweme_id': '7372484719365098803', 'count': 20, 'cursor': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/video-comments", {
  "aweme_id": "7372484719365098803",
  "count": 20,
  "cursor": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/video-comments", sandbase.Params{
	"aweme_id": "7372484719365098803",
	"count": 20,
	"cursor": 0,
})
```

Same call via the path form: `POST /v1/api/douyin/web/video-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number default `20` |
| `cursor` | integer |  | Cursor default `0` |
| `aweme_id` | string | yes | Video id  |

## Details

Returns a page of comments for one Douyin video. Each comment includes its text, post time, like count, location label and author info. The only required input is the video's `aweme_id`.

### Use cases

- Collect the comment text of a video to review audience reactions.
- Find the most liked or hot comments on a post by reading `digg_count` and `is_hot`.
- Group commenters by region using the `ip_label` value.
- Export comment IDs to fetch the replies under a comment with a second call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/video-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7372484719365098803"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |
| `count` | integer | No | Number |
| `cursor` | integer | No | Cursor |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "comment_common_data": "MS4wLjAAAAAAyPjaKBZMlThAfoQKVHBP8mFqDbgerrYSqQ3sAlLKDOHul-CTJTHcEtNlhv0TjepZVbpT…",
  "comment_config": {},
  "comment_insert_bars": null,
  "comments": [
    {
      "aweme_id": "7372484719365098803",
      "can_collect": false,
      "can_share": true,
      "cid": "7625716139537204017",
      "content_type": 1,
      "create_time": 1775500406,
      "decorated_emoji_info": null,
      "digg_count": 0,
      "ent_parachute_tip": 0,
      "enter_from": "general_search_scan",
      "image_list": null,
      "ip_label": "广东"
    }
  ],
  "cursor": 20,
  "extra": {
    "fatal_item_ids": null,
    "now": 1793691157000,
    "scenes": null
  },
  "fast_response_comment": {
    "constant_response_words": [
      "赞"
    ],
    "timed_response_words": [
      "早上好"
    ]
  },
  "folded_comment_count": 0,
  "general_comment_config": {},
  "has_more": 1,
  "hotsoon_filtered_count": 0,
  "log_pb": {
    "impr_id": "20261103153237B3CE67C40AB352E0F687"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comments[].cid` | ID of the comment. Use it to identify one comment. |
| `comments[].text` | The comment text. Mentions appear as `@name` in the text. |
| `comments[].create_time` | When the comment was posted, as a Unix timestamp in seconds. |
| `comments[].digg_count` | Number of likes on the comment. |
| `comments[].reply_comment_total` | Number of replies under the comment. |
| `comments[].ip_label` | Region label shown for the commenter, such as `广东`. |
| `comments[].is_hot / comments[].is_author_digged` | `is_hot` marks a comment flagged as hot. `is_author_digged` shows whether the video author liked it. |
| `comments[].image_list` | Images attached to the comment, in several sizes. It is `null` when the comment has no image. |
| `comments[].user.avatar_thumb.url_list` | URLs of the commenter's avatar thumbnail. |
| `total / has_more / cursor` | `total` is the comment count of the video. `has_more` is `1` when more comments exist. `cursor` is the value to send for the next page. |

### Notes

- Send `aweme_id` as a string. It is the long numeric video ID, for example `7372484719365098803`.
- To page through results, pass the `cursor` value from the response into the next request. `count` sets the number of comments per page and defaults to 20.
- Each comment repeats `item_comment_total` and `aweme_id` for the video.
- To read replies under a comment, use [Douyin Video Comment Replies (Web)](/apis/douyin/web/video-comment-replies).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/video-comments.json`](../../../../catalog/models/douyin/web/video-comments.json) · Store page: https://www.sandbase.ai/model/douyin/web/video-comments

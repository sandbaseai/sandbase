# Douyin Video Comments API: pricing, parameters and code examples

`douyin/video-comment` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get top-level comments for a Douyin (TikTok China) video by aweme ID with page-based pagination. Use it to review audience feedback or analyze discussion around a known video.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/video-comment", "awemeId": "7372484719365098803"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/video-comment', {'awemeId': '7372484719365098803'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/video-comment", {
  "awemeId": "7372484719365098803"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/video-comment", sandbase.Params{
	"awemeId": "7372484719365098803",
})
```

Same call via the path form: `POST /v1/api/douyin/video-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number (starting from 1). default `1` |
| `awemeId` | string | yes | The unique video identifier (aweme_id).  |

## Details

Returns one page of top-level comments for a Douyin video. It needs the video's `awemeId` and accepts an optional `page` number.

### Use cases

- Read the most liked comments on a Douyin video to see how viewers react.
- Export comment text and timestamps for a known video to run sentiment or topic analysis.
- Find comments with many replies, then pull those reply threads for a closer look.
- Track the total comment count of a video across repeated calls.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/video-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"awemeId": "7372484719365098803"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `awemeId` | string | Yes | The unique video identifier (aweme_id). |
| `page` | integer | No | Page number (starting from 1). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "comment_common_data": "MS4wLjAAAAAA03AR1UylNkrCf7SwwA_uox3YUqEopM_e4IoBI8NFKBa2iC7iyWiGQOg2QpHeTlsXSneK…",
  "comment_config": {},
  "comment_insert_bars": null,
  "comments": [
    {
      "aweme_id": "7372484719365098803",
      "can_collect": false,
      "can_share": true,
      "cid": "7381090289870521126",
      "content_type": 1,
      "create_time": 1718544006,
      "decorated_emoji_info": null,
      "digg_count": 6,
      "ent_parachute_tip": 0,
      "enter_from": "homepage_hot",
      "image_list": null,
      "is_author_digged": false
    }
  ],
  "cursor": 20,
  "extra": {
    "fatal_item_ids": null,
    "now": 1793691143000,
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
    "impr_id": "2026110315322310E25D481EBDE823BE1B"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comments[]` | List of top-level comments on the requested page. |
| `comments[].cid` | ID of the comment. |
| `comments[].text` | Text of the comment. Emoji appear as bracketed tags such as `[惊喜]`. |
| `comments[].create_time` | Time the comment was posted, as a Unix timestamp in seconds. |
| `comments[].digg_count` | Number of likes on the comment. |
| `comments[].reply_comment_total` | Number of replies under the comment. |
| `comments[].is_hot` | Whether the comment is flagged as a hot comment. |
| `comments[].text_extra[].user_id / comments[].text_extra[].sec_uid` | IDs of users @-mentioned in the comment. `start` and `end` give the position of the mention in `text`. |
| `comments[].user` | Profile data of the commenter, including avatar objects. Some avatar `url_list` values can be empty. |
| `total` | Total number of comments on the video. |
| `has_more` | `1` when more comments are available on a later page. |
| `cursor` | Position value returned with this page. |

### Notes

- Start with `page` set to `1`. Increase `page` while `has_more` is `1`.
- Each comment also repeats `aweme_id` and `item_comment_total`, which match the video and the `total` value.
- Use [Douyin Video Comment Replies (App V3)](/apis/douyin/app-v3/video-comment-replies) to read replies under a comment with a high `reply_comment_total`.
- [Douyin Video Comments](/apis/douyin/app-v3/video-comments) is another comment API for the same kind of input.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/douyin/video-comment.json`](../../../catalog/models/douyin/video-comment.json) · Store page: https://www.sandbase.ai/model/douyin/video-comment

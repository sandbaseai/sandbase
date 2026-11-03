# TikTok Video Comments (Web) API: pricing, parameters and code examples

`tiktok/web/post-comment` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns user comments for a specific TikTok video using its video ID. Supports cursor-based pagination and optional region filtering.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/post-comment", "aweme_id": "7350810998023949599"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/post-comment', {'aweme_id': '7350810998023949599'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/post-comment", {
  "aweme_id": "7350810998023949599"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/post-comment", sandbase.Params{
	"aweme_id": "7350810998023949599",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/post-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page  |
| `cursor` | integer |  | Page cursor  |
| `aweme_id` | string | yes | Video id  |
| `current_region` | string |  | Current region, default is empty.  |

## Details

Returns the comments on a single TikTok video, plus the total comment count and a cursor for the next page. It needs the video ID in `aweme_id`.

### Use cases

- Pull the top comments on a video to review audience reactions.
- Rank comments by `digg_count` to find the most liked replies.
- Export comment text and timestamps for sentiment or language analysis.
- Page through all comments on a video and compare the total with the number collected.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/post-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7350810998023949599"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |
| `count` | integer | No | Number per page |
| `current_region` | string | No | Current region, default is empty. |
| `cursor` | integer | No | Page cursor |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "alias_comment_deleted": false,
  "comments": [
    {
      "allow_download_photo": false,
      "author_pin": false,
      "aweme_id": "7350810998023949599",
      "cid": "7350848249060934442",
      "collect_stat": 0,
      "comment_language": "en",
      "comment_post_item_ids": null,
      "content_type": 1,
      "create_time": 1711502748,
      "digg_count": 28938,
      "fold_status": -1,
      "image_list": null
    }
  ],
  "cookie": "tt_chain…",
  "cursor": 20,
  "extra": {
    "api_debug_info": null,
    "fatal_item_ids": null,
    "now": 1793691867000
  },
  "has_filtered_comments": 0,
  "has_more": 1,
  "log_pb": {
    "impr_id": "2026110307442781A45D1471276802F43E"
  },
  "reply_style": 2,
  "status_code": 0,
  "status_msg": "",
  "top_gifts": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `total` | Total number of comments on the video. |
| `comments[].text` | The comment text. |
| `comments[].cid` | ID of the comment. |
| `comments[].digg_count` | Number of likes on the comment. |
| `comments[].reply_comment_total` | Number of replies to the comment. |
| `comments[].create_time` | Time the comment was posted, as a Unix timestamp in seconds. |
| `comments[].comment_language` | Language code of the comment, such as `en`. |
| `comments[].share_info.url` | Share link that points to the video and this specific comment. |
| `comments[].user.avatar_thumb.url_list[]` | Image URLs for the commenter's avatar thumbnail. |
| `has_more / cursor` | `has_more` is `1` when more comments exist. `cursor` is the position value returned for the current page. |

### Notes

- Get the `aweme_id` from a video link with [TikTok Video ID from URL](/apis/tiktok/web/aweme-id), or for many links at once with [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id).
- To page, send the returned `cursor` value (`20` in the example) in the next request. Use `count` to set the page size.
- Replies to a comment are not in the list. `reply_comment_total` gives their count, and top-level comments have `reply_id` set to `"0"`.
- `current_region` is optional and empty by default.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/post-comment.json`](../../../../catalog/models/tiktok/web/post-comment.json) · Store page: https://www.sandbase.ai/model/tiktok/web/post-comment

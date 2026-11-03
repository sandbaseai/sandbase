# Douyin Video Detail API: pricing, parameters and code examples

`douyin/app-v3/one-video-v3` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get the full data of a single Douyin post by ID (video, photo or article): description, author, hashtags, music, statistics and play URLs.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/one-video-v3", "aweme_id": "7662510757757603122"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/one-video-v3', {'aweme_id': '7662510757757603122'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/one-video-v3", {
  "aweme_id": "7662510757757603122"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/one-video-v3", sandbase.Params{
	"aweme_id": "7662510757757603122",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/one-video-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_id` | string | yes | Video id  |

## Details

This API looks up a single Douyin post by its `aweme_id`. For a post that can be viewed, it returns the description, author, hashtags, music, statistics and play URLs. For a post that cannot be viewed, it returns a short notice with the reason instead.

### Use cases

- Check whether a Douyin post is still public before you save or analyze it.
- Find out why a post cannot be viewed by reading the notice and filter reason.
- Fetch the details of a post whose ID came from a search, hashtag or user video list.
- Archive the description, author and media URLs of a public post.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/one-video-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7592116912205630761"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "fatal_item_ids": [],
    "logid": "2026110315313840D96157933C965B7D7E",
    "now": 1793691098000
  },
  "filter_detail": {
    "aweme_id": "7592116912205630761",
    "detail_msg": "因作品权限或已被删除，无法观看，去看看其他作品吧",
    "filter_reason": "status_self_see",
    "icon": "https://p3.douyinpic.com/aweme-server-static-resource/reflow_notice_icon1.png~tp…",
    "notice": "抱歉，作品不见了"
  },
  "log_pb": {
    "impr_id": "2026110315313840D96157933C965B7D7E"
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `status_code` | Status of the request. `0` appears in this response. |
| `filter_detail.aweme_id` | ID of the post that was looked up. It matches the `aweme_id` you sent. |
| `filter_detail.filter_reason` | Short code that says why the post is hidden. This response shows `status_self_see`. |
| `filter_detail.notice / filter_detail.detail_msg` | Text shown to the viewer when the post cannot be watched. `notice` is the short title and `detail_msg` is the longer message. Both are in Chinese. |
| `filter_detail.icon` | URL of the icon shown with the notice. |
| `extra.fatal_item_ids` | List of post IDs that failed with a fatal error. It is empty in this response. |
| `extra.logid / log_pb.impr_id` | Request identifiers. Keep them if you need to trace a specific call. |
| `extra.now` | Server time in the response, as a 13-digit number that looks like Unix milliseconds. |

### Notes

- The `aweme_id` is the numeric ID of the post, for example `7592116912205630761`. It appears in Douyin share links of the form `/share/video/<aweme_id>/`.
- When a post is hidden, the response has a `filter_detail` object and no `aweme_detail` object. Check for `filter_detail` before you read post fields.
- To resolve a share link into a post, use [Douyin Single Video by Share URL](/apis/douyin/app-v3/one-video-by-share-url).
- To get only counts for many posts, use [Douyin Video Statistics (Batch)](/apis/douyin/app-v3/multi-video-statistics).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Hot Search List](/apis/douyin/app-v3/hot-search-list): Get the Douyin hot search list and other boards (seeding, entertainment, social and challenge lists): trending words with heat values and video counts.
- [Douyin Video Statistics (Batch)](/apis/douyin/app-v3/multi-video-statistics): Get play, like, share and download counts for up to 50 Douyin videos in one request by passing comma-separated video IDs.
- [Douyin User Videos](/apis/douyin/app-v3/user-post-videos): Get the videos on a Douyin user's profile with descriptions, publish time and play, like, comment and share counts.

---
Machine-readable: [`catalog/models/douyin/app-v3/one-video-v3.json`](../../../../catalog/models/douyin/app-v3/one-video-v3.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/one-video-v3

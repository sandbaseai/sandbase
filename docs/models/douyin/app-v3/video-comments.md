# Douyin Video Comments API: pricing, parameters and code examples

`douyin/app-v3/video-comments` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Get the comments on a Douyin video: comment text, publish time, like count, reply count and commenter location, with cursor pagination.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/video-comments", "aweme_id": "7448118827402972455", "count": 20, "cursor": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/video-comments', {'aweme_id': '7448118827402972455', 'count': 20, 'cursor': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/video-comments", {
  "aweme_id": "7448118827402972455",
  "count": 20,
  "cursor": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/video-comments", sandbase.Params{
	"aweme_id": "7448118827402972455",
	"count": 20,
	"cursor": 0,
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/video-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number Please keep the default, otherwise there will be BUG. default `20` |
| `cursor` | integer |  | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. default `0` |
| `aweme_id` | string | yes | Video id  |

## Details

Pass a Douyin video ID (`aweme_id`) and get its first-level comments with text, likes, reply counts and IP location.

### Use cases

- Analyze audience sentiment on a video.
- Collect feedback on a product or campaign video.
- Find frequently asked questions in comments.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/video-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7565738211130035491"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |
| `count` | integer | No | Number Please keep the default, otherwise there will be BUG. |
| `cursor` | integer | No | Cursor, used for paging, the first page is 0, the second page is the cursor value in the first response. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "total": 4960,
  "has_more": 1,
  "cursor": "<next cursor>",
  "comments": [
    {
      "cid": "7693474478307853091",
      "aweme_id": "7565738211130035491",
      "create_time": 1791276616,
      "digg_count": 0,
      "reply_comment_total": 0,
      "text": "我家小猫很活泼了才3个月[捂脸]",
      "ip_label": "河南",
      "user": {
        "nickname": "<user>"
      }
    }
  ]
}
```

### Notes

- Keep `count` at the default 20.
- Paginate with the `cursor` from the previous response.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Hot Search List](/model/douyin/app-v3/hot-search-list): Get the Douyin hot search list and other boards (seeding, entertainment, social and challenge lists): trending words with heat values and video counts.
- [Douyin Video Statistics (Batch)](/model/douyin/app-v3/multi-video-statistics): Get play, like, share and download counts for up to 50 Douyin videos in one request by passing comma-separated video IDs.
- [Douyin Video Detail](/model/douyin/app-v3/one-video-v3): Get the full data of a single Douyin post by ID (video, photo or article): description, author, hashtags, music, statistics and play URLs.

---
Machine-readable: [`catalog/models/douyin/app-v3/video-comments.json`](../../../../catalog/models/douyin/app-v3/video-comments.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/video-comments

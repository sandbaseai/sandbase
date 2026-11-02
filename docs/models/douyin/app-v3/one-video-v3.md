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

Pass a Douyin `aweme_id` and get the complete post: description, author, hashtags, statistics, and media URLs.

### Use cases

- Get up-to-date statistics for a specific video.
- Download or archive Douyin videos.
- Enrich IDs from search or ranking APIs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/one-video-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7592116912205630761"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "aweme_detail": {
    "aweme_id": "7592116912205630761",
    "create_time": 1767781500,
    "desc": "<video description>",
    "author": {
      "nickname": "<user>",
      "sec_uid": "<sec_uid>"
    },
    "statistics": {
      "play_count": 0,
      "digg_count": 5078,
      "comment_count": 34,
      "share_count": 1580,
      "collect_count": 2606
    },
    "share_url": "https://www.iesdouyin.com/share/video/7592116912205630761/?…",
    "video": {
      "duration": 0,
      "play_addr": {
        "url_list": [
          "https://…"
        ]
      }
    }
  }
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Hot Search List](/model/douyin/app-v3/hot-search-list): Get the Douyin hot search list and other boards (seeding, entertainment, social and challenge lists): trending words with heat values and video counts.
- [Douyin Video Statistics (Batch)](/model/douyin/app-v3/multi-video-statistics): Get play, like, share and download counts for up to 50 Douyin videos in one request by passing comma-separated video IDs.
- [Douyin User Videos](/model/douyin/app-v3/user-post-videos): Get the videos on a Douyin user's profile with descriptions, publish time and play, like, comment and share counts.

---
Machine-readable: [`catalog/models/douyin/app-v3/one-video-v3.json`](../../../../catalog/models/douyin/app-v3/one-video-v3.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/one-video-v3

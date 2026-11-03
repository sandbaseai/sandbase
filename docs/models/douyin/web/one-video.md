# Douyin Single Video Details (V1) API: pricing, parameters and code examples

`douyin/web/one-video` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed metadata for a single Douyin video using its video ID. Supports optional inclusion of anchor details such as location and merchant data.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/one-video", "aweme_id": "7372484719365098803", "need_anchor_info": false}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/one-video', {'aweme_id': '7372484719365098803', 'need_anchor_info': False})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/one-video", {
  "aweme_id": "7372484719365098803",
  "need_anchor_info": false
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/one-video", sandbase.Params{
	"aweme_id": "7372484719365098803",
	"need_anchor_info": false,
})
```

Same call via the path form: `POST /v1/api/douyin/web/one-video` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_id` | string | yes | Video id  |
| `need_anchor_info` | boolean |  | Whether anchor information is needed, default is False, enabling it will show some anchor information about the video, such as location, merchant information, product showcase, etc., which may increase the interface… default `false` |

## Details

Get one Douyin video by `aweme_id`: caption, publish time, like, comment, save and share counts, author, music, cover and play URLs, in the format of the Douyin web API.

### Use cases

- Track a video's engagement over time.
- Get the author and music behind a video.
- Get a play URL for downloading.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/one-video" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7372484719365098803"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |
| `need_anchor_info` | boolean | No | Whether anchor information is needed, default is False, enabling it will show some anchor information about the video, such as location, merchant information, product showcase, etc., which may increase the interface resp |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "aweme_detail": {
    "aweme_id": "7372484719365098803",
    "desc": "你对我的好我一直记得 因为只有你把我当小孩#双子座",
    "create_time": 1716540374,
    "statistics": {
      "digg_count": 312975,
      "comment_count": 4071,
      "collect_count": 19906,
      "share_count": 79966
    },
    "author": {
      "nickname": "萧萧不吃辣",
      "uid": "95823111667",
      "sec_uid": "MS4wLjABAAAAGhTVHcr1tmaen43gOC…",
      "unique_id": "L99612"
    },
    "video": {
      "duration": 8010,
      "width": 1920,
      "height": 1080,
      "play_addr": {
        "url_list": [
          "https://v5-dy-ov-experiment.zjcdn.com/2e74462642e907c5f71c07…"
        ]
      }
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `aweme_id` | Video ID. |
| `desc` | Caption with hashtags. |
| `create_time` | Publish time, Unix seconds. |
| `statistics` | `digg_count` (likes), `comment_count`, `collect_count` (saves), `share_count`. |
| `author` | `nickname`, numeric `uid`, `sec_uid` (used by profile APIs) and `unique_id` (抖音号). |
| `video.play_addr.url_list` | Play URLs; signed and temporary. |
| `video.duration` | Length in milliseconds. |

### Notes

- Get `aweme_id` from a link with [Douyin Aweme ID](/apis/douyin/web/aweme-id), or use [Douyin Video by Share URL](/apis/douyin/app-v3/one-video-by-share-url) directly with a link.

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/one-video.json`](../../../../catalog/models/douyin/web/one-video.json) · Store page: https://www.sandbase.ai/model/douyin/web/one-video

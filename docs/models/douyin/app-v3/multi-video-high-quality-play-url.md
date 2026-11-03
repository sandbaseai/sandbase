# Douyin Multi-Video High Quality Play URLs API: pricing, parameters and code examples

`douyin/app-v3/multi-video-high-quality-play-url` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.25 per call · **Modes:** sync

Returns highest-quality direct video playback URLs for multiple Douyin videos based on comma-separated video IDs, with optional CDN region targeting.

## Pricing

- **$0.25 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/multi-video-high-quality-play-url"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/multi-video-high-quality-play-url', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/multi-video-high-quality-play-url", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/multi-video-high-quality-play-url", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/multi-video-high-quality-play-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` |  |  | Optional ISO country code (for example, CN, US, or HK). Pass CN for users in mainland China to get China-region CDN URLs for faster downloads.  |
| `aweme_ids` | string |  | Video id list, separated by commas, for example: "123,456,789", up to 50.  |

## Details

Returns direct playback URLs for the highest-quality version of several Douyin videos in one call. You pass a comma-separated list of video IDs in `aweme_ids`, up to 50, and can set `region` to pick CDN links for a country.

### Use cases

- Download a batch of Douyin videos in original quality for offline storage.
- Feed video files into an editing or transcoding pipeline after collecting IDs from a list endpoint.
- Check file sizes before download to plan storage or bandwidth for a large batch.
- Build a dataset of Douyin video files from a set of known video IDs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/multi-video-high-quality-play-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_ids` | string | No | Video id list, separated by commas, for example: "123,456,789", up to 50. |
| `region` | string | No | Optional ISO country code (for example, CN, US, or HK). Pass CN for users in mainland China to get China-region CDN URLs for faster downloads. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "failed_count": 0,
  "success_count": 2,
  "total": 3,
  "videos": [
    {
      "content_type": "video/mp4",
      "file_size": "82274121",
      "file_size_in_mb": 78.46,
      "original_video_url": "https://v9-colds.douyinvod.com/31f864e664d608324689b1e440a60021/6ae99bf4/video/t…",
      "success": true,
      "video_id": "7512756548356492544"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `total` | Number of video IDs in the request. |
| `success_count / failed_count` | How many videos returned a URL and how many failed. |
| `videos[].video_id` | ID of the Douyin video this entry belongs to. Use it to match results to your input list. |
| `videos[].success` | `true` when a play URL was returned for this video. |
| `videos[].original_video_url` | Direct URL of the video file. The URL contains signed path segments, so request it again if a saved link stops working. |
| `videos[].content_type` | Media type of the file, for example `video/mp4`. |
| `videos[].file_size` | File size as a string. The matching `file_size_in_mb` field shows the same size in megabytes. |
| `videos[].file_size_in_mb` | File size in megabytes as a number, rounded to two decimals. |

### Notes

- `aweme_ids` is a single string such as `123,456,789`. Do not send a JSON array.
- Pass `region` as an ISO country code such as `CN`, `US` or `HK`. Use `CN` for users in mainland China to get China-region CDN URLs.
- In the sample, `total` is 3 but `success_count` is 2 and `failed_count` is 0, so always compare `videos[].video_id` against your input list instead of relying on the counts.
- To get video IDs first, use [Douyin User Videos](/apis/douyin/app-v3/user-post-videos) or [Douyin Hashtag Video List](/apis/douyin/app-v3/hashtag-video-list). For one video at a time, use [Douyin High Quality Video Play URL (App V3)](/apis/douyin/app-v3/video-high-quality-play-url).

### Pricing

$0.25 per successful call. Failed calls are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/multi-video-high-quality-play-url.json`](../../../../catalog/models/douyin/app-v3/multi-video-high-quality-play-url.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/multi-video-high-quality-play-url

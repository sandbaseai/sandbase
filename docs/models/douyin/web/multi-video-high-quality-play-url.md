# Douyin High-Quality Video Play URLs API: pricing, parameters and code examples

`douyin/web/multi-video-high-quality-play-url` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.25 per call · **Modes:** sync

Returns direct high-quality playback URLs for multiple Douyin videos using comma-separated video IDs and an optional region code.

## Pricing

- **$0.25 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/multi-video-high-quality-play-url"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/multi-video-high-quality-play-url', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/multi-video-high-quality-play-url", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/multi-video-high-quality-play-url", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/web/multi-video-high-quality-play-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` |  |  | Optional ISO country code (for example, CN, US, or HK). Pass CN for users in mainland China to get China-region CDN URLs for faster downloads.  |
| `aweme_ids` | string |  | Video id list, separated by commas, for example: "123,456,789", up to 50.  |

## Details

Returns direct playback URLs for several Douyin videos in one call. You pass a comma-separated list of video IDs in `aweme_ids`, and you can add a `region` code to get regional CDN links.

### Use cases

- Download the source files of a batch of Douyin videos for offline archiving.
- Check the file size of each video with `file_size_in_mb` before you start a bulk download.
- Feed direct video links into an editing or transcoding pipeline.
- Find which video IDs in a batch failed by reading `success` and `failed_count`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/multi-video-high-quality-play-url" \
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
      "content_type": "video/quicktime",
      "file_size": "82274121",
      "file_size_in_mb": 78.46,
      "original_video_url": "https://v26-colds.douyinvod.com/b47516d962cf6197d827b82ce6f0b6da/6ae99c28/video/…",
      "success": true,
      "video_id": "7512756548356492544"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `videos[].video_id` | The Douyin video ID this entry belongs to. |
| `videos[].original_video_url` | Direct URL of the video file. The link contains signed path parts, so use it soon after you receive it. |
| `videos[].success` | Whether the URL lookup worked for this video ID. |
| `videos[].content_type` | MIME type of the video file, for example `video/mp4` or `video/quicktime`. |
| `videos[].file_size` | File size as a string. It matches `file_size_in_mb` once converted to megabytes. |
| `videos[].file_size_in_mb` | File size in megabytes, rounded to two decimals. |
| `success_count / failed_count` | Number of videos that returned a URL and number that did not. |
| `total` | Total count reported for the request. |

### Notes

- Send up to 50 IDs in `aweme_ids`, separated by commas, for example `123,456,789`.
- Set `region` to `CN` to get China-region CDN URLs. Other examples are `US` and `HK`.
- In the sample response `total` is `3` while `videos` holds 2 entries, so compare `total` with `success_count` and `failed_count` when you check results.
- To get video IDs from video links, call [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id).

### Pricing

$0.25 per successful call. Failed calls are not charged.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/multi-video-high-quality-play-url.json`](../../../../catalog/models/douyin/web/multi-video-high-quality-play-url.json) · Store page: https://www.sandbase.ai/model/douyin/web/multi-video-high-quality-play-url

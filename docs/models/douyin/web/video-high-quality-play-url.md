# Douyin High Quality Video Play URL (Web) API: pricing, parameters and code examples

`douyin/web/video-high-quality-play-url` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

Returns the highest quality playback URL for a Douyin video using a video ID or share URL, with an optional exit region specification.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/web/video-high-quality-play-url", "aweme_id": "7512756548356492544", "region": "CN", "share_url": "https://static.sandbase.ai/examples/2d775896-4018-4f17-b056-55b641a736b3/input/7e844029-329b-4b7a-a407-bd7e1f15f4ca.bin"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/web/video-high-quality-play-url', {'aweme_id': '7512756548356492544', 'region': 'CN', 'share_url': 'https://static.sandbase.ai/examples/2d775896-4018-4f17-b056-55b641a736b3/input/7e844029-329b-4b7a-a407-bd7e1f15f4ca.bin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/web/video-high-quality-play-url", {
  "aweme_id": "7512756548356492544",
  "region": "CN",
  "share_url": "https://static.sandbase.ai/examples/2d775896-4018-4f17-b056-55b641a736b3/input/7e844029-329b-4b7a-a407-bd7e1f15f4ca.bin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/web/video-high-quality-play-url", sandbase.Params{
	"aweme_id": "7512756548356492544",
	"region": "CN",
	"share_url": "https://static.sandbase.ai/examples/2d775896-4018-4f17-b056-55b641a736b3/input/7e844029-329b-4b7a-a407-bd7e1f15f4ca.bin",
})
```

Same call via the path form: `POST /v1/api/douyin/web/video-high-quality-play-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Optional, ISO country code (e.g. "CN" / "US" / "HK") used as the request exit region.  |
| `aweme_id` | string |  | Video id, prefer to use aweme_id, if not available, use share_url.  |
| `share_url` | string |  | Optional, share link, if the video id is provided, this parameter can be omitted.  |

## Details

Returns a direct playback URL for the highest quality version of a Douyin video. It needs an `aweme_id` or a `share_url`, and you can set an exit `region`.

### Use cases

- Download a Douyin video file to store in your own media archive.
- Feed the playback URL into a video player or transcoding job.
- Check the file size of a Douyin video before you fetch it.
- Convert a Douyin share link into a direct video link for review tools.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/web/video-high-quality-play-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7512756548356492544", "share_url": "https://www.douyin.com/video/7512756548356492544", "region": "CN"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | No | Video id, prefer to use aweme_id, if not available, use share_url. |
| `region` | string | No | Optional, ISO country code (e.g. "CN" / "US" / "HK") used as the request exit region. |
| `share_url` | string | No | Optional, share link, if the video id is provided, this parameter can be omitted. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "content_type": "text/html",
  "file_size": "564",
  "file_size_in_mb": 0.0,
  "original_video_url": "https://v96-hcc.douyinvod.com/07b591ad2101ff883bf64842bc3366c5/6ae99c31/video/to…",
  "video_id": "7512756548356492544"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `original_video_url` | Direct playback URL of the video file. The URL is long and contains query parameters, so keep it whole. |
| `video_id` | ID of the video the URL belongs to. It matches the `aweme_id` you sent. |
| `file_size` | Size of the file as a string. Compare it with `file_size_in_mb` to see the scale. |
| `file_size_in_mb` | File size in megabytes as a number. It can show `0.0` for very small files. |
| `content_type` | Content type value returned with the result. In this sample it is `text/html`. |

### Notes

- Send `aweme_id` when you have it. Use `share_url` only when the ID is not available.
- The `aweme_id` is the numeric ID at the end of a video link, for example `7512756548356492544` in `https://www.douyin.com/video/7512756548356492544`.
- To get an ID from a link, call [Douyin Video ID Extractor](/apis/douyin/web/aweme-id).
- To look up several videos in one call, use [Douyin High-Quality Video Play URLs](/apis/douyin/web/multi-video-high-quality-play-url).

### Pricing

$0.005 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Batch Video ID Extraction](/apis/douyin/web/all-aweme-id): Extracts video IDs from a list of Douyin video URLs.
- [Douyin sec_user_ids from URLs (Batch)](/apis/douyin/web/all-sec-user-id): Extracts Douyin sec_user_id values in bulk from a list of user homepage URLs.
- [Douyin Webcast ID Extraction](/apis/douyin/web/all-webcast-id): Extracts webcast IDs from a submitted list of Douyin live room links.

---
Machine-readable: [`catalog/models/douyin/web/video-high-quality-play-url.json`](../../../../catalog/models/douyin/web/video-high-quality-play-url.json) · Store page: https://www.sandbase.ai/model/douyin/web/video-high-quality-play-url

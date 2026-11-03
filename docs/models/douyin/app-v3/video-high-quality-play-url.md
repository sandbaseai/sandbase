# Douyin High Quality Video Play URL (App V3) API: pricing, parameters and code examples

`douyin/app-v3/video-high-quality-play-url` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

Returns the highest quality playback URL for a Douyin video using a video identifier or share link, with optional region filtering.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/video-high-quality-play-url", "aweme_id": "7662510757757603122", "region": "CN", "share_url": "https://static.sandbase.ai/examples/83222b01-babd-47a9-a612-3a92a4e7c4bb/input/19f248e9-c747-4994-8b9f-285f2826271f.bin"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/video-high-quality-play-url', {'aweme_id': '7662510757757603122', 'region': 'CN', 'share_url': 'https://static.sandbase.ai/examples/83222b01-babd-47a9-a612-3a92a4e7c4bb/input/19f248e9-c747-4994-8b9f-285f2826271f.bin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/video-high-quality-play-url", {
  "aweme_id": "7662510757757603122",
  "region": "CN",
  "share_url": "https://static.sandbase.ai/examples/83222b01-babd-47a9-a612-3a92a4e7c4bb/input/19f248e9-c747-4994-8b9f-285f2826271f.bin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/video-high-quality-play-url", sandbase.Params{
	"aweme_id": "7662510757757603122",
	"region": "CN",
	"share_url": "https://static.sandbase.ai/examples/83222b01-babd-47a9-a612-3a92a4e7c4bb/input/19f248e9-c747-4994-8b9f-285f2826271f.bin",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/video-high-quality-play-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `region` | string |  | Optional, ISO country code (e.g. "CN" / "US" / "HK") used as the request exit region.  |
| `aweme_id` | string |  | Video id, prefer to use aweme_id, if not available, use share_url.  |
| `share_url` | string |  | Optional, share link, if the video id is provided, this parameter can be omitted.  |

## Details

Returns a direct playback URL for a Douyin video, plus basic file details. It needs an `aweme_id` or a `share_url`. You can also set an optional `region` to choose the request exit region.

### Use cases

- Download or cache a Douyin video file from its `aweme_id` for offline review.
- Turn a Douyin share link into a direct video file address.
- Feed a video URL into a transcription or content analysis pipeline.
- Request the video URL through a chosen exit region such as `CN`, `US` or `HK`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/video-high-quality-play-url" \
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
  "content_type": "application/xml",
  "file_size": "0",
  "file_size_in_mb": 0.0,
  "original_video_url": "https://v11-cold-src.douyinvod.com/9cc3869316e50941773fa3830c54be27/6ae99bfb/vid…",
  "video_id": "7512756548356492544"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `original_video_url` | Direct address of the video file on Douyin's video host. Use this as the playback or download link. |
| `video_id` | ID of the video the URL belongs to. In the sample it matches the `aweme_id` that was sent. |
| `content_type` | Content type reported for the file. The sample shows `application/xml`, so check this value before treating the URL as a plain video file. |
| `file_size / file_size_in_mb` | File size values. The sample returns `"0"` and `0.0`, so these may not be filled in for every video. |

### Notes

- Send `aweme_id` when you have it. Use `share_url` only when the ID is not available.
- `aweme_id` is a long numeric string, for example `7512756548356492544`.
- To fetch several videos in one call, use [Douyin Multi-Video High Quality Play URLs](/apis/douyin/app-v3/multi-video-high-quality-play-url).
- For title, author and other video details, call [Douyin Single Video Details](/apis/douyin/app-v3/one-video).

### Pricing

$0.005 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/video-high-quality-play-url.json`](../../../../catalog/models/douyin/app-v3/video-high-quality-play-url.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/video-high-quality-play-url

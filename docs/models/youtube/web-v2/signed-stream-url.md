# YouTube Signed Video Stream URL

`youtube/web-v2/signed-stream-url` · api · YouTube

Returns a signed playback stream URL for a specific YouTube video format. Requires a format itag identifier alongside either a video ID or full video link.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/signed-stream-url", "itag": 18, "video_id": "dQw4w9WgXcQ"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/signed-stream-url', {'itag': 18, 'video_id': 'dQw4w9WgXcQ'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/signed-stream-url", {
  "itag": 18,
  "video_id": "dQw4w9WgXcQ"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/signed-stream-url", sandbase.Params{
	"itag": 18,
	"video_id": "dQw4w9WgXcQ",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/signed-stream-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itag` | integer | yes | Format identifier, selected from formats list returned by get_video_streams  |
| `video_id` | string |  | Video ID (recommended)  |
| `video_url` | string |  | Full video URL (optional)  |

## Details

Returns a signed playback stream URL ready for playback using a format `itag` and either a `video_id` or `video_url`.

### Use cases

- Stream a selected YouTube video format in a media player.
- Obtain direct playback links based on a specific format itag.
- Access playable video streams using either a video ID or full URL.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/signed-stream-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itag": 18}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itag` | integer | Yes | Format identifier, selected from formats list returned by get_video_streams |
| `video_id` | string | No | Video ID (recommended) |
| `video_url` | string | No | Full video URL (optional) |

### Notes

- The `itag` value must come from the formats list returned by the video streams endpoint.
- Supply either `video_id` (recommended) or `video_url` to specify the target video.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/model/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/model/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/model/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/signed-stream-url.json`](../../../../catalog/models/youtube/web-v2/signed-stream-url.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/signed-stream-url

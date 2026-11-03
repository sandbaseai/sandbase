# YouTube Video Streams (V2) API: pricing, parameters and code examples

`youtube/web-v2/video-streams-v2` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.004 per call (free daily quota) · **Modes:** sync

Retrieves stream information and playback details for a YouTube video. Queries data using either a video ID or a full video URL.

## Pricing

- **$0.004 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/video-streams-v2"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/video-streams-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/video-streams-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/video-streams-v2", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/video-streams-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video_id` | string |  | Video ID (recommended)  |
| `video_url` | string |  | Full video URL (optional, ignored if video_id is provided)  |

## Details

Returns stream details for one YouTube video: title, author, length, view count, and lists of downloadable video and audio formats with their URLs. It needs a `video_id` or a full `video_url`.

### Use cases

- List the audio-only formats of a video to build a podcast-style player.
- Pick a progressive MP4 format by `quality_label` and `height` for in-app playback.
- Check `is_live` and `length_seconds` before queuing a video for processing.
- Compare `content_length` across formats to estimate download sizes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/video-streams-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video_id": "dQw4w9WgXcQ", "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `video_id` | string | No | Video ID (recommended) |
| `video_url` | string | No | Full video URL (optional, ignored if video_id is provided) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "adaptive_formats": [
    {
      "audio_quality": 30.813,
      "audio_sample_rate": 22050,
      "bitrate": 30.813,
      "content_length": 821022,
      "fps": null,
      "has_signature": false,
      "height": null,
      "itag": 599,
      "mime_type": "audio/mp4",
      "quality": "ultralow",
      "quality_label": "audio only",
      "type": "audio"
    }
  ],
  "author": "Rick Astley",
  "available_qualities": [
    "audio only"
  ],
  "expires_in_seconds": 21600,
  "formats": [
    {
      "audio_quality": null,
      "audio_sample_rate": 44100,
      "bitrate": 444.226,
      "content_length": 11832459,
      "fps": 25,
      "has_signature": false,
      "height": 360,
      "itag": 18,
      "mime_type": "video/mp4",
      "quality": "360p",
      "quality_label": "640x360",
      "type": "video"
    }
  ],
  "is_live": false,
  "length_seconds": 213,
  "short_description": "The official video for “Never Gonna Give You Up” by Rick Astley. \n\nNever: The Au…",
  "strategy": "account_mweb",
  "thumbnail": [
    {
      "url": "https://i.ytimg.com/vi_webp/dQw4w9WgXcQ/maxresdefault.webp"
    }
  ],
  "title": "Rick Astley - Never Gonna Give You Up (Official Video) (4K Remaster)",
  "video_id": "dQw4w9WgXcQ"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `title / author / video_id` | Video title, channel name, and the 11-character video ID. |
| `length_seconds / view_count` | Video length in seconds and the view count. |
| `is_live` | `true` if the video is a live stream, `false` otherwise. |
| `short_description` | Start of the video description text. Long descriptions are cut. |
| `thumbnail[].url` | Link to a thumbnail image for the video. |
| `formats[]` | Formats that carry video in a single file. Each row has `itag`, `mime_type`, `quality`, `quality_label`, `width`, `height` and `fps`. |
| `adaptive_formats[]` | Separate audio-only or video-only formats. Check `type` to tell them apart, and `audio_sample_rate` for audio rows. |
| `formats[].url / adaptive_formats[].url` | Direct stream URL for that format. It stops working after the time set in `expires_in_seconds`. |
| `bitrate / content_length` | Bitrate value and file size of the format. `content_length` is the size of the stream data. |
| `available_qualities / expires_in_seconds` | Quality labels found in the response, and the number of seconds the stream URLs stay valid. |

### Notes

- Send `video_id` when you can. The API ignores `video_url` if `video_id` is set.
- The `video_id` is the value after `v=` in a watch URL, such as `dQw4w9WgXcQ`.
- Stream URLs are time-limited. Use them within `expires_in_seconds` of the call.
- For title, description and stats without stream links, see [YouTube Video Information (V2)](/apis/youtube/web-v2/video-info-v2). For captions, see [YouTube Video Captions](/apis/youtube/web-v2/video-captions).

### Pricing

$0.004 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/video-streams-v2.json`](../../../../catalog/models/youtube/web-v2/video-streams-v2.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/video-streams-v2

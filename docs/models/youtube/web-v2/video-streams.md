# YouTube Video Streams API: pricing, parameters and code examples

`youtube/web-v2/video-streams` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns stream details and media information for a specified YouTube video. Queries accept either a direct video identifier or a full video URL.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/video-streams"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/video-streams', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/video-streams", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/video-streams", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/video-streams` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `video_id` | string |  | Video ID (recommended)  |
| `video_url` | string |  | Full video URL (optional, ignored if video_id is provided)  |

## Details

Returns the downloadable stream formats for one YouTube video, with basic video details such as title, author and length. It needs a `video_id` or a full `video_url`.

### Use cases

- List the available audio and video formats for a video before choosing one to download.
- Pick an audio-only stream by `itag` and `mime_type` for a podcast or transcription tool.
- Check the available resolutions for a video before building a playback or preview tool.
- Read the title, author, duration and view count of a video in the same call as its streams.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/video-streams" \
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
| `title / author / video_id` | Title of the video, name of the channel that published it, and the video ID. |
| `length_seconds` | Length of the video in seconds. |
| `view_count` | Number of views on the video. |
| `is_live` | Whether the video is a live stream (`false` for this video). |
| `available_qualities` | List of quality labels offered, such as `audio only`, `854x480` and `640x360`. |
| `formats[]` | Streams that carry video and audio together. Each row has `itag`, `mime_type`, `quality_label`, `width`, `height`, `fps`, `bitrate` and `content_length`. |
| `adaptive_formats[]` | Separate streams, such as audio only. Each row has `type`, `itag`, `mime_type`, `quality_label`, `audio_sample_rate`, `bitrate` and `content_length`. |
| `formats[].url / adaptive_formats[].url` | Direct link to the media stream for that format. |
| `expires_in_seconds` | Number of seconds given for the stream URLs, `21600` in this response. |
| `thumbnail[].url` | Link to a thumbnail image of the video. |

### Notes

- Send `video_id` when you have it. `video_url` is ignored if `video_id` is provided.
- The `video_id` is the 11-character value after `v=` in a YouTube watch URL, such as `dQw4w9WgXcQ`.
- Fields like `width`, `height` and `fps` are `null` for audio-only streams.
- For video details without stream links, see [YouTube Video Information](/apis/youtube/web-v2/video-info). For another stream response, see [YouTube Video Streams (V2)](/apis/youtube/web-v2/video-streams-v2).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/video-streams.json`](../../../../catalog/models/youtube/web-v2/video-streams.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/video-streams

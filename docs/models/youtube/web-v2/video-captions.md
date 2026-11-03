# YouTube Video Captions API: pricing, parameters and code examples

`youtube/web-v2/video-captions` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns available video caption tracks or transcripts in multiple formats, filtered by video identifier and language code.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/video-captions", "format": "srt", "language_code": "en", "video_id": "l4tHKJFQvRg"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/video-captions', {'format': 'srt', 'language_code': 'en', 'video_id': 'l4tHKJFQvRg'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/video-captions", {
  "format": "srt",
  "language_code": "en",
  "video_id": "l4tHKJFQvRg"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/video-captions", sandbase.Params{
	"format": "srt",
	"language_code": "en",
	"video_id": "l4tHKJFQvRg",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/video-captions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `format` | string |  | Caption format one of: `srt`, `xml`, `json3`, `txt`; default `"srt"` |
| `video_id` | string |  | Video ID (recommended)  |
| `video_url` | string |  | Full video URL (optional)  |
| `language_code` | string |  | Language code (e.g. en, zh-Hans, a.en), returns available caption list if empty  |

## Details

Returns the caption text of a YouTube video for one language, in the format you choose (`srt`, `xml`, `json3` or `txt`). It needs a `video_id` or a `video_url`, plus a `language_code`. If you leave `language_code` empty, it returns the list of available caption tracks instead.

### Use cases

- Pull English subtitles as `txt` to feed a video summarization workflow.
- Download `srt` files with timestamps to build subtitles for a re-upload or translation.
- Fetch `json3` captions to index spoken words for search.
- Check which caption languages a video offers before choosing one to download.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/video-captions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video_id": "dQw4w9WgXcQ", "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "language_code": "en", "format": "srt"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `format` | string | No | Caption format |
| `language_code` | string | No | Language code (e.g. en, zh-Hans, a.en), returns available caption list if empty |
| `video_id` | string | No | Video ID (recommended) |
| `video_url` | string | No | Full video URL (optional) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "content": "1\n00:00:01,360 --> 00:00:03,040\n[♪♪♪]\n\n2\n00:00:18,640 --> 00:00:21,880\n♪ We're n…",
  "format": "srt",
  "language_code": "en",
  "language_name": "English",
  "video_id": "dQw4w9WgXcQ"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `content` | The full caption text in the requested format. For `srt`, each cue has a number, a start and end time in `HH:MM:SS,mmm` form, and the caption line. Sound cues such as `[♪♪♪]` appear as text. |
| `format` | The caption format of `content`, matching the `format` you requested. |
| `language_code` | The language code of the returned captions, for example `en`. |
| `language_name` | The readable name of the caption language, for example `English`. |
| `video_id` | The ID of the video the captions belong to. |

### Notes

- Send `video_id` when you can. `video_url` is optional and is not needed if you have the ID.
- The `video_id` is the value after `v=` in a watch URL, for example `dQw4w9WgXcQ`.
- Language codes can be plain, like `en` or `zh-Hans`, or auto-generated tracks like `a.en`.
- `format` defaults to `srt` when you leave it out.

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/video-captions.json`](../../../../catalog/models/youtube/web-v2/video-captions.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/video-captions

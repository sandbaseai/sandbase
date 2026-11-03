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

Fetch YouTube caption lists or full subtitle text by providing `video_id` or `video_url`. Specify `language_code` to retrieve subtitle text or leave it empty to inspect available caption tracks.

### Use cases

- Extract subtitles in TXT or SRT formats for video summarization workflows.
- Inspect all available subtitle tracks and languages for a specific video.
- Download structured JSON3 transcript data for search indexing.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/video-captions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video_id": "dQw4w9WgXcQ", "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ", "language_code": "en", "format": "srt"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `format` | string | No | Caption format |
| `video_id` | string | No | Video ID (recommended) |
| `video_url` | string | No | Full video URL (optional) |
| `language_code` | string | No | Language code (e.g. en, zh-Hans, a.en), returns available caption list if empty |

### Notes

- Leaving `language_code` empty returns the list of available caption tracks.
- Supported `format` options include `srt`, `xml`, `json3`, and `txt`.
- Providing `video_id` is recommended instead of `video_url`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/video-captions.json`](../../../../catalog/models/youtube/web-v2/video-captions.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/video-captions

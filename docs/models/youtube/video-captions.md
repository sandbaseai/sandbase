# YouTube Video Captions API: pricing, parameters and code examples

`youtube/video-captions` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get available caption tracks for a YouTube video or request captions in SRT, XML, JSON3, or plain-text format. Use it to support transcription, accessibility, localization, or text analysis.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/video-captions", "videoId": "dQw4w9WgXcQ"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/video-captions', {'videoId': 'dQw4w9WgXcQ'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/video-captions", {
  "videoId": "dQw4w9WgXcQ"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/video-captions", sandbase.Params{
	"videoId": "dQw4w9WgXcQ",
})
```

Same call via the path form: `POST /v1/api/youtube/video-captions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `format` | string |  | Caption output format. one of: `srt`, `xml`, `json3`, `txt`; default `"srt"` |
| `videoId` | string | yes | The unique identifier for a YouTube video.  |
| `languageCode` | string |  | Caption language code, such as en, zh-Hans, or a.en. Leave it empty to retrieve available caption tracks.  |

## Details

This API returns the caption tracks available for a YouTube video. It needs a `videoId`. If you also pass `languageCode`, it returns the captions for that language in the format you set with `format`.

### Use cases

- List which caption languages a video offers before you decide what to download.
- Check whether a video has English captions before you queue it for transcription.
- Build a language picker for a video player or localization tool from the track list.
- Collect caption text in `srt`, `xml`, `json3`, or `txt` format for text analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/video-captions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"videoId": "dQw4w9WgXcQ"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `videoId` | string | Yes | The unique identifier for a YouTube video. |
| `format` | string | No | Caption output format. |
| `languageCode` | string | No | Caption language code, such as en, zh-Hans, or a.en. Leave it empty to retrieve available caption tracks. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "captions": [
    {
      "language_code": "en",
      "language_name": "English"
    }
  ],
  "video_id": "dQw4w9WgXcQ"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `video_id` | The ID of the video the caption tracks belong to. It matches the `videoId` you sent. |
| `captions[]` | One entry for each caption track available for the video. |
| `captions[].language_code` | The code for the track language, such as `en`, `de`, or `ja`. Pass this value as `languageCode` to request the captions for that track. |
| `captions[].language_name` | The language name for the track in English, such as `English` or `German`. |

### Notes

- Send only `videoId` to get the list of tracks. Add `languageCode` to request the caption content.
- `format` accepts `srt`, `xml`, `json3`, or `txt`. The default is `srt`.
- Get the `videoId` from a video URL, or from [YouTube Search](/apis/youtube/search) or [YouTube Channel Videos](/apis/youtube/channel-videos).
- For a transcript endpoint, see [YouTube Video Transcript](/apis/youtube/video-transcript).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/youtube/video-captions.json`](../../../catalog/models/youtube/video-captions.json) · Store page: https://www.sandbase.ai/model/youtube/video-captions

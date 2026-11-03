# TikTok Video Transcript (Speech to Text) API: pricing, parameters and code examples

`tiktok/video-transcript-full` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0085 per call · **Modes:** sync

Transcribe the spoken audio of a TikTok video with speech-to-text: timed sentence-level segments, speaker labels, detected language, and optional per-word timings, for videos TikTok publishes no caption track for and for videos whose caption track gets the words wrong. The API downloads the video and runs the audio through MAI-Transcribe-2 rather than reading anything TikTok wrote, which is why it handles non-English speech and hears words the native captions mishear. The answer also carries the video's id, URL, creator handle, and cover image. If you only want whatever TikTok itself published and you want it for a tenth of the price, tiktok.video_transcript is that.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/video-transcript-full", "url": "https://www.tiktok.com/@thatdudecancook/video/7649086431641521421"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/video-transcript-full', {'url': 'https://www.tiktok.com/@thatdudecancook/video/7649086431641521421'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/video-transcript-full", {
  "url": "https://www.tiktok.com/@thatdudecancook/video/7649086431641521421"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/video-transcript-full", sandbase.Params{
	"url": "https://www.tiktok.com/@thatdudecancook/video/7649086431641521421",
})
```

Same call via the path form: `POST /v1/api/tiktok/video-transcript-full` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | TikTok video URL (e.g. "https://www.tiktok.com/@user/video/1234567890").  |
| `wordTimestamps` | boolean |  | Return per-word timings inside each segment. Words carry timings only; the recognizer scores a phrase rather than a word, so there is no per-word confidence to report. default `false` |

## Details

Returns a speech-to-text transcript of the spoken audio in a TikTok video. It needs the video `url`, and returns timed sentence-level segments, speaker labels, the detected language, and basic video details.

### Use cases

- Index the full spoken text of a recipe or tutorial video so you can search it.
- Build subtitles from the start and end times of each segment.
- Read what a creator said in a video that has no TikTok caption track.
- Check the spoken language of a video before you send it to a translation step.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/video-transcript-full" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@thatdudecancook/video/7649086431641521421"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | TikTok video URL (e.g. "https://www.tiktok.com/@user/video/1234567890"). |
| `wordTimestamps` | boolean | No | Return per-word timings inside each segment. Words carry timings only; the recognizer scores a phrase rather than a word, so there is no per-word confidence to report. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "durationSeconds": 69.55,
    "id": "7649086431641521421",
    "language": "en",
    "ownerUsername": "thatdudecancook",
    "segments": [
      {
        "endSeconds": 3.919,
        "language": "en",
        "speaker": "0",
        "startSeconds": 0.6,
        "text": "If your thing is spicy pasta, then I have got you covered."
      }
    ],
    "source": "audio_asr",
    "thumbnailUrl": "https://p19-common-sign.tiktokcdn-us.com/tos-useast5-p-0068-tx/ocBPi8SaADAAr6GsB…",
    "transcript": "If your thing is spicy pasta, then I have got you covered. And you want to start…",
    "url": "https://www.tiktok.com/@thatdudecancook/video/7649086431641521421"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.transcript` | The full spoken text of the video as one string. |
| `data.segments[].text` | The text of one sentence-level segment. |
| `data.segments[].startSeconds / data.segments[].endSeconds` | Start and end time of the segment, in seconds from the start of the video. |
| `data.segments[].speaker` | Speaker label for the segment, such as `0`. Segments with the same value come from the same detected speaker. |
| `data.segments[].language / data.language` | Detected language code for the segment and for the whole video, such as `en`. |
| `data.durationSeconds` | Length of the video in seconds. |
| `data.id / data.url / data.ownerUsername` | The video ID, its TikTok URL, and the creator's username. |
| `data.thumbnailUrl` | Link to the video's cover image. The link is signed, so save the image if you need it long term. |
| `data.source` | How the transcript was made. The value `audio_asr` means it came from speech recognition on the audio. |
| `found` | `true` when the video was found and transcribed. |

### Notes

- Copy the `url` from the TikTok share link or browser address bar. It has the form `https://www.tiktok.com/@user/video/<id>`.
- Set `wordTimestamps` to `true` to get per-word timings inside each segment. Words carry timings only, with no per-word confidence.
- For video metadata such as stats and the play URL, call [TikTok Video Details](/apis/tiktok/app-v3/one-video).

### Pricing

Billed at the actual cost of each call, about $0.0085 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/video-transcript-full.json`](../../../catalog/models/tiktok/video-transcript-full.json) · Store page: https://www.sandbase.ai/model/tiktok/video-transcript-full

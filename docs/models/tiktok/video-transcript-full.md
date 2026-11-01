# TikTok Video Transcript (speech to text)

`tiktok/video-transcript-full` · api · TikTok

Transcribe the spoken audio of a TikTok video with speech-to-text: timed sentence-level segments, speaker labels, detected language, and optional per-word timings, for videos TikTok publishes no caption track for and for videos whose caption track gets the words wrong. The service downloads the video and runs the audio through MAI-Transcribe-2 rather than reading anything TikTok wrote, which is why it handles non-English speech and hears words the native captions mishear. The answer also carries the video's id, URL, creator handle, and cover image. Turn on hostVideo to also get the MP4 on a hosted link that plays without TikTok's signed, short-lived CDN URL expiring on you. If you only want whatever TikTok itself published and you want it for a tenth of the price, tiktok.video_transcript is that.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.095**

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
| `hostVideo` | boolean |  | Also store the video and return a hosted MP4 link that plays without TikTok's signed CDN URL. Charged as an extra on top of the transcript. default `false` |
| `wordTimestamps` | boolean |  | Return per-word timings inside each segment. Words carry timings only; the recognizer scores a phrase rather than a word, so there is no per-word confidence to report. default `false` |

## Details

Transcribe the spoken audio of a TikTok video with speech-to-text: timed sentence-level segments, speaker labels, detected language, and optional per-word timings, for videos TikTok publishes no caption track for and for videos whose caption track gets the words wrong. The service downloads the video and runs the audio through MAI-Transcribe-2 rather than reading anything TikTok wrote, which is why it handles non-English speech and hears words the native captions mishear. The answer also carries the video's id, URL, creator handle, and cover image. Turn on hostVideo to also get the MP4 on a hosted link that plays without TikTok's signed, short-lived CDN URL expiring on you. If you only want whatever TikTok itself published and you want it for a tenth of the price, tiktok.video_transcript is that.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/video-transcript-full" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@thatdudecancook/video/7649086431641521421"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | TikTok video URL (e.g. "https://www.tiktok.com/@user/video/1234567890"). |
| `hostVideo` | boolean | No | Also store the video and return a hosted MP4 link that plays without TikTok's signed CDN URL. Charged as an extra on top of the transcript. Default `false`. |
| `wordTimestamps` | boolean | No | Return per-word timings inside each segment. Words carry timings only; the recognizer scores a phrase rather than a word, so there is no per-word confidence to report. Default `false`. |

### Pricing

Billed at the actual cost of each call, usually $0.095 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/tiktok/video-transcript-full.json`](../../../catalog/models/tiktok/video-transcript-full.json) · Store page: https://www.sandbase.ai/model/tiktok/video-transcript-full

# TikTok Video Transcript (native captions) API: pricing, parameters and code examples

`tiktok/video-transcript` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

Fetch the caption track TikTok itself published for a video, as TikTok wrote it. It is the cheapest way to get the words, and it is only as good as TikTok's own transcription: it mishears names and uncommon words, and many videos - especially non-English ones - have no caption track at all, which comes back as not found. When you need the words to be right, or there is no track to read, tiktok.video_transcript_full transcribes the audio with speech-to-text instead.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/video-transcript", "url": "https://www.tiktok.com/@washingtonpost/video/7609177768793787679"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/video-transcript', {'url': 'https://www.tiktok.com/@washingtonpost/video/7609177768793787679'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/video-transcript", {
  "url": "https://www.tiktok.com/@washingtonpost/video/7609177768793787679"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/video-transcript", sandbase.Params{
	"url": "https://www.tiktok.com/@washingtonpost/video/7609177768793787679",
})
```

Same call via the path form: `POST /v1/api/tiktok/video-transcript` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | TikTok video URL on tiktok.com: a video or photo post (https://www.tiktok.com/@<user>/video/<id> or /photo/<id>) or a vm.tiktok.com, vt.tiktok.com or tiktok.com/t/ share link. A profile link…  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `language`, and it is served only by a source that returns every one…  |

## Details

Returns the caption track TikTok published for one video, as a WebVTT text with timestamps. It needs a TikTok video or photo post URL. If the video has no caption track, the call succeeds and returns `found: false`.

### Use cases

- Pull the spoken words from a news clip to quote or search them.
- Index captions from many videos to find which ones mention a brand, product or topic.
- Read the caption `language` to sort videos by spoken language before further analysis.
- Feed the caption text into a summary or sentiment pipeline without downloading the video.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/video-transcript" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/@washingtonpost/video/7609177768793787679"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | TikTok video URL on tiktok.com: a video or photo post (https://www.tiktok.com/@<user>/video/<id> or /photo/<id>) or a vm.tiktok.com, vt.tiktok.com or tiktok.com/t/ share link. A profile link (https://www.tiktok.com/@<use |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `language`, and it is served only by a source that returns every one o |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "id": "7609177768793787679",
    "language": "en",
    "transcript": "WEBVTT\n\n\n00:00:00.020 --> 00:00:01.540\nYour tariffs are illegal. They're not.\n\n0…",
    "url": "https://www.tiktok.com/@washingtonpost/video/7609177768793787679"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when TikTok has a caption track for the video. `false` means no track was found. |
| `data.id` | The numeric TikTok video ID, taken from the URL. |
| `data.language` | Language code of the caption track, for example `en`. |
| `data.transcript` | The caption track in WebVTT format. Each cue has a start and end time (`HH:MM:SS.mmm`) followed by the caption text. |
| `data.url` | The TikTok video URL the transcript belongs to. |

### Notes

- Pass a full video URL such as `https://www.tiktok.com/@<user>/video/<id>`, a `/photo/<id>` URL, or a `vm.tiktok.com`, `vt.tiktok.com` or `tiktok.com/t/` share link. Profile links and video file links are refused as invalid input.
- Set `requireFields` to `["language"]` to make sure the serving source returns `data.language`. This can change the price of the call.
- The text is TikTok's own transcription, so names and uncommon words can be wrong. If the track is missing or must be accurate, use the full transcription API `tiktok.video_transcript_full`.

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tiktok/video-transcript.json`](../../../catalog/models/tiktok/video-transcript.json) · Store page: https://www.sandbase.ai/model/tiktok/video-transcript

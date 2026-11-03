# YouTube Video Transcript API: pricing, parameters and code examples

`youtube/video-transcript` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0009 per call · **Modes:** sync

Fetch the transcript/captions of a YouTube video or Short by URL or ID.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0009**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/video-transcript"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/video-transcript', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/video-transcript", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/video-transcript", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/youtube/video-transcript` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `id` | string |  | YouTube video ID. A Short uses the same ID as any other video.  |
| `url` | string |  | Full YouTube video URL. Shorts (youtube.com/shorts/...), youtu.be, live, and embed URLs all work.  |

## Details

Returns the transcript of a YouTube video or Short as plain text and as timed segments. You pass either a video `url` or a video `id`.

### Use cases

- Index what a video says so you can search across many videos by spoken words.
- Feed the transcript text into a summarizer or a question-answering tool.
- Build subtitles or clickable timestamps from the timed segments.
- Check whether a video mentions a brand, product, or phrase.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/video-transcript" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `id` | string | No | YouTube video ID. A Short uses the same ID as any other video. |
| `url` | string | No | Full YouTube video URL. Shorts (youtube.com/shorts/...), youtu.be, live, and embed URLs all work. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "language": "en",
    "segments": [
      {
        "durationSeconds": 1.68,
        "startSeconds": 1.36,
        "text": "[♪♪♪]"
      }
    ],
    "transcript": "[♪♪♪]\n♪ We're no strangers to love ♪\n♪ You know the rules and so do I ♪\n♪ A full…"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when a transcript was found for the video. A lookup that finds nothing returns `found: false`. |
| `data.language` | Language code of the transcript, for example `en`. |
| `data.transcript` | The full transcript as one string. Each caption line is separated by a newline. |
| `data.segments[].text` | The text of one caption line. Music cues such as `[♪♪♪]` can appear as text. |
| `data.segments[].startSeconds` | Start time of the segment, in seconds from the beginning of the video. |
| `data.segments[].durationSeconds` | How long the segment lasts, in seconds. |

### Notes

- Send either `url` or `id`. A Short uses the same ID as any other video, and `youtube.com/shorts/...`, `youtu.be`, live, and embed URLs all work for `url`.
- The `id` is the value after `v=` in a standard watch URL, for example `dQw4w9WgXcQ`.
- Use `data.transcript` for the whole text and `data.segments` when you need timing.
- To get video metadata such as title and stats, call [YouTube Video Details](/apis/youtube/video-detail).

### Pricing

Billed at the actual cost of each call, about $0.0009 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/youtube/video-transcript.json`](../../../catalog/models/youtube/video-transcript.json) · Store page: https://www.sandbase.ai/model/youtube/video-transcript

# Instagram Reel Transcript API: pricing, parameters and code examples

`instagram/reel-transcript` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0083 per call · **Modes:** sync

Transcribe any public Instagram reel or video post: the full speech transcript, speaker labels, and word-level timestamps, from a reel, /p/, or /tv/ URL or an Instagram CDN media URL you already hold. A video post is transcribed exactly like a reel. A photo post comes back found with its record and an empty transcript, charged the request price only. Transcription runs on MAI-Transcribe-2, chosen for its accuracy and its speaker labels. If you only want the text, instagram.media_transcript is the cheaper transcript-only option; if you only want the file, instagram.post is where you go.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0083**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/reel-transcript", "url": "https://www.instagram.com/reel/CfY6jCIgH-P/"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/reel-transcript', {'url': 'https://www.instagram.com/reel/CfY6jCIgH-P/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/reel-transcript", {
  "url": "https://www.instagram.com/reel/CfY6jCIgH-P/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/reel-transcript", sandbase.Params{
	"url": "https://www.instagram.com/reel/CfY6jCIgH-P/",
})
```

Same call via the path form: `POST /v1/api/instagram/reel-transcript` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | The URL of a public Instagram reel or video post (e.g. https://www.instagram.com/reel/C8yKXdRxKqK/), or an Instagram CDN media URL you already hold.  |
| `wordTimestamps` | boolean |  | Set true to include a precise timestamp for every word in the transcript (e.g. true). default `false` |

## Details

This API returns the speech transcript of a public Instagram reel or video post. The transcript comes as one text string and as timed segments with speaker labels. It needs one input, the `url` of a reel, /p/, or /tv/ post, or an Instagram CDN media URL.

### Use cases

- Pull the spoken text of a creator's reel to quote it or build captions.
- Index what is said across many reels so you can search them by keyword.
- Split an interview reel by speaker to see who said what.
- Check the language of a reel's speech before you route it to a translation step.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/reel-transcript" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.instagram.com/reel/CfY6jCIgH-P/", "wordTimestamps": false}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The URL of a public Instagram reel or video post (e.g. https://www.instagram.com/reel/C8yKXdRxKqK/), or an Instagram CDN media URL you already hold. |
| `wordTimestamps` | boolean | No | Set true to include a precise timestamp for every word in the transcript (e.g. true). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "durationSeconds": 67.319,
        "id": "2871302256618143631",
        "language": "en",
        "likeCount": 769107,
        "mediaType": "XDTGraphVideo",
        "ownerUsername": "garyvee",
        "segments": [
          {
            "end": 4.799,
            "speaker": "0",
            "start": 0.16,
            "text": "How can I keep my daughter, 9 years old, away from these dangers from the intern…"
          }
        ],
        "shortcode": "CfY6jCIgH-P",
        "source": "audio_asr",
        "text": "How can I keep my daughter, 9 years old, away from these dangers from the intern…",
        "thumbnailUrl": "https://scontent-fra3-1.cdninstagram.com/v/t51.71878-15/496316259_10363060147067…",
        "url": "https://www.instagram.com/reel/CfY6jCIgH-P/"
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].text` | The full transcript as one string, with a new line between segments. |
| `data.items[].segments[].text` | The words spoken in one segment of the transcript. |
| `data.items[].segments[].start / data.items[].segments[].end` | Start and end time of the segment, as numbers measured from the start of the video. |
| `data.items[].segments[].speaker` | Label for the speaker of the segment, such as `0`, `1`, or `2`. Segments with the same label come from the same voice. |
| `data.items[].language` | Language code of the transcript, such as `en`. |
| `data.items[].durationSeconds` | Length of the video in seconds. |
| `data.items[].ownerUsername / data.items[].likeCount` | Username of the account that posted the reel and the like count of the post. |
| `data.items[].shortcode / data.items[].id` | The post shortcode taken from the URL and the numeric media ID. |
| `data.items[].mediaType` | The kind of media, such as `XDTGraphVideo` for a video post. |
| `data.items[].thumbnailUrl` | Link to a thumbnail image of the post on the Instagram CDN. |

### Notes

- Copy the `url` from the reel's address bar. Reel, /p/, and /tv/ links all work.
- Set `wordTimestamps` to `true` to get a timestamp for every word. It is `false` by default.
- If the post is not found, the call returns `found: false`. A photo post returns `found: true` with an empty transcript.
- If you only need the text, use [Instagram Media Transcript](/apis/instagram/media-transcript). For post metadata and the video file, use [Instagram Post Details](/apis/instagram/post-detail).

### Pricing

Billed at the actual cost of each call, about $0.0083 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/reel-transcript.json`](../../../catalog/models/instagram/reel-transcript.json) · Store page: https://www.sandbase.ai/model/instagram/reel-transcript

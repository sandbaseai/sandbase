# Instagram Reel Transcript API: pricing, parameters and code examples

`instagram/reel-transcript` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.095 per call · **Modes:** sync

Transcribe any public Instagram reel or video post: the full speech transcript, speaker labels, and word-level timestamps, from a reel, /p/, or /tv/ URL or an Instagram CDN media URL you already hold. A video post is transcribed exactly like a reel. A photo post comes back found with its record and an empty transcript, charged the request price only. Transcription runs on MAI-Transcribe-2, chosen for its accuracy and its speaker labels. Turn on hostVideo to also get the MP4 on a hosted link that plays without an Instagram session. If you only want the text, instagram.media_transcript is the cheaper transcript-only option; if you only want the file, instagram.post is where you go.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.095**

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
| `hostVideo` | boolean |  | Set true to also get the reel's MP4 on a hosted link you can play without an Instagram session. Charged as an extra on top of the transcript (e.g. true). A photo post has no file to host, so a request that sets this on… default `false` |
| `wordTimestamps` | boolean |  | Set true to include a precise timestamp for every word in the transcript (e.g. true). default `false` |

## Details

Transcribe any public Instagram reel or video post: the full speech transcript, speaker labels, and word-level timestamps, from a reel, /p/, or /tv/ URL or an Instagram CDN media URL you already hold. A video post is transcribed exactly like a reel. A photo post comes back found with its record and an empty transcript, charged the request price only. Transcription runs on MAI-Transcribe-2, chosen for its accuracy and its speaker labels. Turn on hostVideo to also get the MP4 on a hosted link that plays without an Instagram session. If you only want the text, instagram.media_transcript is the cheaper transcript-only option; if you only want the file, instagram.post is where you go.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/reel-transcript" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.instagram.com/reel/CfY6jCIgH-P/", "hostVideo": true, "wordTimestamps": false}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | The URL of a public Instagram reel or video post (e.g. https://www.instagram.com/reel/C8yKXdRxKqK/), or an Instagram CDN media URL you already hold. |
| `hostVideo` | boolean | No | Set true to also get the reel's MP4 on a hosted link you can play without an Instagram session. Charged as an extra on top of the transcript (e.g. true). A photo post has no file to host, so a request that sets this on o |
| `wordTimestamps` | boolean | No | Set true to include a precise timestamp for every word in the transcript (e.g. true). Default `false`. |

### Pricing

Billed at the actual cost of each call, usually $0.095 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/instagram/reel-transcript.json`](../../../catalog/models/instagram/reel-transcript.json) · Store page: https://www.sandbase.ai/model/instagram/reel-transcript

# YouTube Video Transcript (Provenance)

`youtube/video-transcript-full` · api · YouTube

Fetch a YouTube video or Short transcript with timed segments and its provenance: whether the words are creator-written captions or machine speech recognition.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.002**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/video-transcript-full", "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/video-transcript-full', {'url': 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/video-transcript-full", {
  "url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/video-transcript-full", sandbase.Params{
	"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
})
```

Same call via the path form: `POST /v1/api/youtube/video-transcript-full` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | YouTube video or Short URL (e.g. "https://www.youtube.com/watch?v=dQw4w9WgXcQ" or "https://www.youtube.com/shorts/Fir1x9cw2vg").  |
| `language` | string |  | Preferred caption language code (e.g. "en", "es"). Defaults to English. If the video has no captions in that language, you get the transcript in another language the video has; the `language` field in the result says…  |
| `captionKind` | string |  | Which caption track to accept: "manual" only creator-written captions, "automatic" only YouTube's speech recognition, "any" whichever exists. one of: `manual`, `automatic`, `any`; default `"any"` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `views`, and it is served only by a source that returns every one of…  |

## Details

Fetch a YouTube video or Short transcript with timed segments and its provenance: whether the words are creator-written captions or machine speech recognition.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/video-transcript-full" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | YouTube video or Short URL (e.g. "https://www.youtube.com/watch?v=dQw4w9WgXcQ" or "https://www.youtube.com/shorts/Fir1x9cw2vg"). |
| `captionKind` | string | No | Which caption track to accept: "manual" only creator-written captions, "automatic" only YouTube's speech recognition, "any" whichever exists. One of: `manual`, `automatic`, `any`. Default `"any"`. |
| `language` | string | No | Preferred caption language code (e.g. "en", "es"). Defaults to English. If the video has no captions in that language, you get the transcript in another language the video has; the `language` field in the result says whi |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `views`, and it is served only by a source that returns every one of t |

### Pricing

Billed at the actual cost of each call, usually $0.002 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/youtube/video-transcript-full.json`](../../../catalog/models/youtube/video-transcript-full.json) · Store page: https://www.sandbase.ai/model/youtube/video-transcript-full

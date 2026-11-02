# YouTube Video Captions API: pricing, parameters and code examples

`youtube/video-captions` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Get available caption tracks for a YouTube video or request captions in SRT, XML, JSON3, or plain-text format. Use it to support transcription, accessibility, localization, or text analysis.

## Pricing

- **$0.013889 per call** (USD)
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

Get available caption tracks for a YouTube video or request captions in SRT, XML, JSON3, or plain-text format. Use it to support transcription, accessibility, localization, or text analysis.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/video-captions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"videoId": "dQw4w9WgXcQ"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `videoId` | string | Yes | The unique identifier for a YouTube video. |
| `languageCode` | string | No | Caption language code, such as en, zh-Hans, or a.en. Leave it empty to retrieve available caption tracks. |
| `format` | string | No | Caption output format. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/youtube/video-captions.json`](../../../catalog/models/youtube/video-captions.json) · Store page: https://www.sandbase.ai/model/youtube/video-captions

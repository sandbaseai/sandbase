# YouTube Video Details API: pricing, parameters and code examples

`youtube/video-detail` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get public details for a YouTube video identified by video ID. Use it to inspect a known video before further content or comment analysis.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/video-detail", "videoId": "dQw4w9WgXcQ"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/video-detail', {'videoId': 'dQw4w9WgXcQ'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/video-detail", {
  "videoId": "dQw4w9WgXcQ"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/video-detail", sandbase.Params{
	"videoId": "dQw4w9WgXcQ",
})
```

Same call via the path form: `POST /v1/api/youtube/video-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `lang` | string |  | Optional IETF language tag for localized video details, such as en-US. Leave empty to use the default language.  |
| `videoId` | string | yes | The unique identifier for a YouTube video.  |

## Details

Get public details for a YouTube video identified by video ID. Use it to inspect a known video before further content or comment analysis.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/video-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"videoId": "dQw4w9WgXcQ"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `videoId` | string | Yes | The unique identifier for a YouTube video. |
| `lang` | string | No | Optional IETF language tag for localized video details, such as en-US. Leave empty to use the default language. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/youtube/video-detail.json`](../../../catalog/models/youtube/video-detail.json) · Store page: https://www.sandbase.ai/model/youtube/video-detail

# Bilibili Single Video Play Info API: pricing, parameters and code examples

`bilibili/web/video-play-info` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns playback stream information, including video stream URLs, MIME types, and frame rates, for a single Bilibili video URL.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/video-play-info", "url": "https://www.bilibili.com/video/BV1S5uKzzE4r"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/video-play-info', {'url': 'https://www.bilibili.com/video/BV1S5uKzzE4r'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/video-play-info", {
  "url": "https://www.bilibili.com/video/BV1S5uKzzE4r"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/video-play-info", sandbase.Params{
	"url": "https://www.bilibili.com/video/BV1S5uKzzE4r",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/video-play-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Video URL  |

## Details

Fetch playback and stream details for a specific Bilibili video by providing its `url`.

### Use cases

- Retrieve direct stream URLs for Bilibili video playback.
- Inspect video stream quality metrics such as frame rate.
- Verify media formats and MIME types for external players.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/video-play-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.bilibili.com/video/BV1S5uKzzE4r"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Video URL |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "dash": {
    "video": [
      {
        "base_url": "https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/81/89/30966218981/3096621898…",
        "frameRate": "30.000",
        "frame_rate": "30.000",
        "id": 32,
        "mimeType": "video/mp4",
        "mime_type": "video/mp4"
      }
    ]
  }
}
```

### Notes

- Requires a valid Bilibili video link passed in the `url` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/video-play-info.json`](../../../../catalog/models/bilibili/web/video-play-info.json) · Store page: https://www.sandbase.ai/model/bilibili/web/video-play-info

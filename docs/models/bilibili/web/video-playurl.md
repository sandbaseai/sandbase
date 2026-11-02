# Bilibili Video Playback URL API: pricing, parameters and code examples

`bilibili/web/video-playurl` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns video playback stream URLs and DASH metadata for a specified Bilibili video. Requires both the video identifier and the content identifier.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/web/video-playurl", "bv_id": "BV1dVbC6WE6p", "cid": "40931491951"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/web/video-playurl', {'bv_id': 'BV1dVbC6WE6p', 'cid': '40931491951'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/web/video-playurl", {
  "bv_id": "BV1dVbC6WE6p",
  "cid": "40931491951"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/web/video-playurl", sandbase.Params{
	"bv_id": "BV1dVbC6WE6p",
	"cid": "40931491951",
})
```

Same call via the path form: `POST /v1/api/bilibili/web/video-playurl` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cid` | string | yes | Video cid  |
| `bv_id` | string | yes | Video id  |

## Details

Fetch playback stream URLs and stream qualities for Bilibili videos by providing `bv_id` and `cid`.

### Use cases

- Retrieve direct DASH video stream URLs for playback integration.
- Inspect available frame rates and stream codecs for a specific video.
- Automate media player setups with official streaming endpoints.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/video-playurl" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"bv_id": "BV1y7411Q7Eq", "cid": "171776208"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cid` | string | Yes | Video cid |
| `bv_id` | string | Yes | Video id |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "dash": {
      "video": [
        {
          "base_url": "https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/08/62/171776208/171776208_nb…",
          "frameRate": "29.412",
          "frame_rate": "29.412",
          "id": 32,
          "mimeType": "video/mp4",
          "mime_type": "video/mp4"
        }
      ]
    }
  }
}
```

### Notes

- Requires both `bv_id` (Bilibili video ID) and `cid` (video content ID) to locate the playback stream.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili Streaming Areas](/model/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/model/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/model/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/video-playurl.json`](../../../../catalog/models/bilibili/web/video-playurl.json) · Store page: https://www.sandbase.ai/model/bilibili/web/video-playurl

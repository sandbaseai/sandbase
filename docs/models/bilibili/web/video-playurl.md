# Bilibili Video Playback URL API: pricing, parameters and code examples

`bilibili/web/video-playurl` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns video playback stream URLs and DASH metadata for a specified Bilibili video. Requires both the video identifier and the content identifier.

## Pricing

- **$0.001 per call** (USD)
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

Get the stream URLs of a Bilibili video: separate DASH video and audio tracks with codec, resolution, frame rate and bitrate, for the qualities available to a guest viewer.

### Use cases

- Download a video for archiving or analysis.
- Read available resolutions and codecs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/web/video-playurl" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"bv_id": "BV1y7411Q7Eq", "cid": "171776208"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `bv_id` | string | Yes | Video id |
| `cid` | string | Yes | Video cid |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "quality": 64,
    "accept_description": [
      "高清 1080P+",
      "高清 1080P",
      "高清 720P",
      "清晰 480P",
      "流畅 360P"
    ],
    "timelength": 283723,
    "dash": {
      "duration": 284,
      "video": [
        {
          "id": 32,
          "codecs": "avc1.64001F",
          "width": 852,
          "height": 480,
          "frameRate": "29.412",
          "bandwidth": 746163,
          "baseUrl": "https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/08/62/17…"
        }
      ],
      "audio": [
        {
          "id": 30232,
          "codecs": "mp4a.40.2",
          "bandwidth": 132686,
          "baseUrl": "https://upos-sz-mirrorcosov.bilivideo.com/upgcxcode/08/62/17…"
        }
      ]
    }
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.quality / accept_description` | Quality served and qualities available. |
| `data.dash.video[]` | Video tracks: `id` (quality), `codecs`, `width`, `height`, `frameRate`, `bandwidth`, `baseUrl`. |
| `data.dash.audio[]` | Audio tracks: `codecs`, `bandwidth`, `baseUrl`. |
| `data.timelength` | Duration in milliseconds. |

### Notes

- Video and audio are separate files; merge them, for example with `ffmpeg -i video.m4s -i audio.m4s -c copy out.mp4`.
- Stream URLs expire and the CDN expects a `Referer: https://www.bilibili.com` header.
- Get `cid` from a video detail API.

### Pricing

$0.001 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Bilibili Streaming Areas](/apis/bilibili/web/all-live-areas): Returns the complete list of streaming broadcast areas and categories on Bilibili.
- [Bilibili BV to AID Converter](/apis/bilibili/web/bv-to-aid): Converts a Bilibili BV identifier to its corresponding numeric AID value.
- [Bilibili User Collection Folders](/apis/bilibili/web/collect-folders): Returns the collection folders owned by a specific Bilibili user.

---
Machine-readable: [`catalog/models/bilibili/web/video-playurl.json`](../../../../catalog/models/bilibili/web/video-playurl.json) · Store page: https://www.sandbase.ai/model/bilibili/web/video-playurl

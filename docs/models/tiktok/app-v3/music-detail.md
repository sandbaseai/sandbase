# TikTok Music Details

`tiktok/app-v3/music-detail` · api · TikTok

Returns detailed track information for a specific audio track on TikTok using its identifier, including connected DSP song mappings.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/music-detail", "music_id": "6943027371519772674"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/music-detail', {'music_id': '6943027371519772674'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/music-detail", {
  "music_id": "6943027371519772674"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/music-detail", sandbase.Params{
	"music_id": "6943027371519772674",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/music-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `music_id` | string | yes | Music id  |

## Details

Retrieve detailed information about a specific TikTok audio track by providing its unique identifier in `music_id`.

### Use cases

- Look up audio track metadata by music ID.
- Inspect DSP song mappings linked to TikTok audio.
- Verify audio identifiers across platform catalogs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/music-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"music_id": "6943027371519772674"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `music_id` | string | Yes | Music id |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "music_info": {
    "tt_to_dsp_song_infos": [
      {
        "button_type": 2,
        "song_id": "1867885635"
      }
    ]
  }
}
```

### Notes

- Provide a valid TikTok audio identifier in `music_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/music-detail.json`](../../../../catalog/models/tiktok/app-v3/music-detail.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/music-detail

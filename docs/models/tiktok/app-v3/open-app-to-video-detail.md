# TikTok Video App Share Link API: pricing, parameters and code examples

`tiktok/app-v3/open-app-to-video-detail` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a shareable short URL that opens a specific video directly in the TikTok mobile application. Requires the target video identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/open-app-to-video-detail", "aweme_id": "7440436579409153311"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/open-app-to-video-detail', {'aweme_id': '7440436579409153311'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/open-app-to-video-detail", {
  "aweme_id": "7440436579409153311"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/open-app-to-video-detail", sandbase.Params{
	"aweme_id": "7440436579409153311",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/open-app-to-video-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_id` | string | yes | Video id  |

## Details

Generate a direct mobile application share URL by providing the video identifier in `aweme_id`.

### Use cases

- Direct users from external platforms into the TikTok mobile app.
- Generate short shareable links for specific video clips.
- Route mobile traffic directly to video details pages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/open-app-to-video-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7440436579409153311"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Video id |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "aweme_id": "7440436579409153311",
  "short_url": "https://www.tiktok.com/t/ZP9D9bnSdX695-XhTyt/",
  "status": 0
}
```

### Notes

- Requires `aweme_id` representing the target video identifier.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/open-app-to-video-detail.json`](../../../../catalog/models/tiktok/app-v3/open-app-to-video-detail.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/open-app-to-video-detail

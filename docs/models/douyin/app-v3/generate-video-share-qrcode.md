# Douyin Video Share QR Code API: pricing, parameters and code examples

`douyin/app-v3/generate-video-share-qrcode` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a Douyin share QR code for a designated target. Takes a video ID or author UID to retrieve the scannable code.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/generate-video-share-qrcode", "object_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/generate-video-share-qrcode', {'object_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/generate-video-share-qrcode", {
  "object_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/generate-video-share-qrcode", sandbase.Params{
	"object_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/generate-video-share-qrcode` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `object_id` | string | yes | Video id or author uid  |

## Details

Retrieve a Douyin share QR code for a video or author profile by specifying `object_id`.

### Use cases

- Display Douyin video QR codes on external marketing materials.
- Direct mobile users to Douyin author profiles via scannable codes.
- Embed Douyin share codes into web and desktop interfaces.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/generate-video-share-qrcode" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"object_id": "<object_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `object_id` | string | Yes | Video id or author uid |

### Notes

- The `object_id` parameter accepts either a video ID or an author UID.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/generate-video-share-qrcode.json`](../../../../catalog/models/douyin/app-v3/generate-video-share-qrcode.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/generate-video-share-qrcode

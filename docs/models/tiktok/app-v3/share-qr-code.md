# TikTok Share QR Code API: pricing, parameters and code examples

`tiktok/app-v3/share-qr-code` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a shareable QR code for a target TikTok profile. Requests require an object identifier and accept an optional schema type configuration.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/share-qr-code", "object_id": "6762244951259661318"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/share-qr-code', {'object_id': '6762244951259661318'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/share-qr-code", {
  "object_id": "6762244951259661318"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/share-qr-code", sandbase.Params{
	"object_id": "6762244951259661318",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/share-qr-code` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `object_id` | string | yes | Object id, currently supports the uid in the response of the personal homepage interface as a parameter.  |
| `schema_type` | integer |  | Schema type  |

## Details

Retrieve a TikTok profile share QR code using `object_id` and an optional `schema_type`.

### Use cases

- Generate QR codes to link users directly to a specific TikTok account.
- Display scannable profile badges on external marketing materials.
- Direct mobile audiences to targeted creator pages through scan links.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/share-qr-code" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"object_id": "<object_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `object_id` | string | Yes | Object id, currently supports the uid in the response of the personal homepage interface as a parameter. |
| `schema_type` | integer | No | Schema type |

### Notes

- `object_id` accepts the uid obtained from personal homepage responses.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/model/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/share-qr-code.json`](../../../../catalog/models/tiktok/app-v3/share-qr-code.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/share-qr-code

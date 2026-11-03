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

Returns a QR code image for a TikTok profile. The request needs an `object_id`, which is the user's uid, and accepts an optional `schema_type` integer. The response lists signed image URLs for the QR code.

### Use cases

- Print a scannable QR code on flyers or packaging that opens a creator's TikTok profile.
- Show a profile QR code on a website or in a media kit so visitors can follow an account from their phone.
- Add a QR code to event slides or stream overlays that points to a speaker's TikTok page.
- Build a link-in-bio tool that creates a downloadable QR image for each saved TikTok account.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/share-qr-code" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"object_id": "6762244951259661318"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `object_id` | string | Yes | Object id, currently supports the uid in the response of the personal homepage interface as a parameter. |
| `schema_type` | integer | No | Schema type |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "fatal_item_ids": [],
    "logid": "20261103074359D5CDAF63A5538401C815",
    "now": 1793691839000
  },
  "log_pb": {
    "impr_id": "20261103074359D5CDAF63A5538401C815"
  },
  "qrcode_url": {
    "uri": "tikcode-tx2/7703847789901709343",
    "url_list": [
      "https://p16-common-sign.tiktokcdn-us.com/tikcode-tx2/7703847789901709343~tplv-ti…"
    ]
  },
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `qrcode_url.url_list[]` | Image URLs for the QR code. The sample contains two `.webp` links and one `.jpeg` link, each sized 720 by 720. Each URL carries `x-expires` and `x-signature` query parameters. |
| `qrcode_url.uri` | Internal path of the QR code image. It also appears inside every URL in `url_list`. |
| `status_code / status_msg` | Result of the call. The sample returns `0` and an empty message. |
| `extra.logid / log_pb.impr_id` | Request identifiers. They carry the same value in the sample. |
| `extra.now` | Timestamp attached to the response. The sample value `1793691839000` has 13 digits, which fits milliseconds. |
| `extra.fatal_item_ids` | List of item IDs that failed. It is empty in the sample. |

### Notes

- Get `object_id` from the `uid` field in a profile response, for example from [TikTok User Profile Details](/apis/tiktok/app-v3/user-profile).
- If you only have a username, call [TikTok User ID by Username](/apis/tiktok/app-v3/user-id-and-sec-user-id-by-username) first.
- The image URLs are signed and include an `x-expires` value, so download or store the image soon after the call.
- For a link instead of an image, see [TikTok User Profile Share Link](/apis/tiktok/app-v3/open-app-to-user-profile).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/share-qr-code.json`](../../../../catalog/models/tiktok/app-v3/share-qr-code.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/share-qr-code

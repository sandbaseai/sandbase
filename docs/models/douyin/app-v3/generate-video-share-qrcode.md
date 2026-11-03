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

Returns a Douyin share QR code image for one video or one author. It needs a single `object_id`, which is either a video ID or an author UID.

### Use cases

- Print a QR code for a Douyin video on posters, flyers or packaging.
- Show a scannable link to a creator's Douyin profile on a web page or event screen.
- Call the API once per video to build a set of QR codes for a campaign.
- Store the image URLs to attach a share code to each video in an internal content tracker.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/generate-video-share-qrcode" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"object_id": "7348044435755846962"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `object_id` | string | Yes | Video id or author uid |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "event_extra": "{\"schema_type\":1,\"schema_type_name\":\"SCHEMA_VIDEO\",\"object_id\":\"7348044435755846…",
  "extra": {
    "fatal_item_ids": [],
    "logid": "2026110315313347516FB785280F4DBE3A",
    "now": 1793691094000
  },
  "log_pb": {
    "impr_id": "2026110315313347516FB785280F4DBE3A"
  },
  "qrcode_url": {
    "uri": "aweme-qrcode/IyCJbk7703844581313447714",
    "url_list": [
      "https://p3-sign.douyinpic.com/aweme-qrcode/IyCJbk7703844581313447714~c5_400x400.…"
    ]
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `qrcode_url.url_list[]` | Image URLs for the QR code. The sample returns the same 400x400 image in `webp` and `jpeg` formats. The URLs carry `x-expires` and `x-signature` query parameters. |
| `qrcode_url.uri` | Path of the QR code image, for example `aweme-qrcode/IyCJbk7703844581313447714`. |
| `status_code` | Result code of the call. `0` appears in the successful sample. |
| `event_extra` | A JSON string with details about the share target, including the object ID and a share ID. Parse it as JSON before you read the values. |
| `extra.logid / log_pb.impr_id` | Request log ID. Both hold the same value in the sample. |
| `extra.now` | A 13-digit number that looks like a Unix timestamp in milliseconds. |

### Notes

- Pass a video ID such as `7348044435755846962` or an author UID in `object_id`. The sample response shows `SCHEMA_VIDEO` in `event_extra` for a video ID.
- `event_extra` is a string, not an object. Parse it as JSON to read its contents.
- To find a video ID first, call [Douyin Single Video by Share URL](/apis/douyin/app-v3/one-video-by-share-url). To make a shorter link instead of a QR code, use [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/generate-video-share-qrcode.json`](../../../../catalog/models/douyin/app-v3/generate-video-share-qrcode.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/generate-video-share-qrcode

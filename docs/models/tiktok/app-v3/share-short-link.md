# TikTok Share Short Link API: pricing, parameters and code examples

`tiktok/app-v3/share-short-link` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Converts standard TikTok long links into shortened shareable URLs. Supply the full target web address to return the compressed redirect URL.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/share-short-link", "url": "https://www.tiktok.com/passport/web/logout/"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/share-short-link', {'url': 'https://www.tiktok.com/passport/web/logout/'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/share-short-link", {
  "url": "https://www.tiktok.com/passport/web/logout/"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/share-short-link", sandbase.Params{
	"url": "https://www.tiktok.com/passport/web/logout/",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/share-short-link` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | Long link or link to convert  |

## Details

This API turns a long TikTok web address into a short shareable TikTok link. It needs one input, the full address in `url`, and returns the short link in `shorten_url`.

### Use cases

- Shorten a long TikTok page address before adding it to a text message or email.
- Store compact TikTok links in a spreadsheet or database instead of long addresses.
- Build a share button that creates a short link for a TikTok page on demand.
- Create a short link first, then pass it to a QR code tool for printed material.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/share-short-link" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://www.tiktok.com/passport/web/logout/"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | Long link or link to convert |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "extra": {
    "fatal_item_ids": [],
    "logid": "2026110307435967BCE759FE246C01DC13",
    "now": 1793691839000
  },
  "log_pb": {
    "impr_id": "2026110307435967BCE759FE246C01DC13"
  },
  "shorten_url": "https://www.tiktok.com/t/ZP9ytcNX27cY3-4p1bB/",
  "status_code": 0,
  "status_msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `shorten_url` | The shortened TikTok link for the address you sent. It has the form `https://www.tiktok.com/t/<code>/`. |
| `status_code` | Result code of the request. The value `0` appears in a successful response. |
| `status_msg` | Status text. It is an empty string in the sample response. |
| `extra.logid / log_pb.impr_id` | Request identifiers. In the sample response both fields hold the same value. |
| `extra.now` | Timestamp of the response, as a number. The sample value looks like Unix time in milliseconds. |
| `extra.fatal_item_ids` | List of item IDs that caused a fatal error. It is empty in the sample response. |

### Notes

- Send the full address, including `https://`, in `url`.
- Read the short link from `shorten_url` and check that `status_code` is `0`.
- To make a QR code for a link, try [TikTok Share QR Code](/apis/tiktok/app-v3/share-qr-code).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/share-short-link.json`](../../../../catalog/models/tiktok/app-v3/share-short-link.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/share-short-link

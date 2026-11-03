# Douyin Xingtu User Profile QR Code API: pricing, parameters and code examples

`douyin/xingtu-v2/user-profile-qrcode` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns a QR code for a Douyin Xingtu creator profile. Look up the profile QR code by providing either a user core ID or sec_uid.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/user-profile-qrcode"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/user-profile-qrcode', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/user-profile-qrcode", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/user-profile-qrcode", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/user-profile-qrcode` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_uid` |  |  | User sec_uid (pick one with core_user_id)  |
| `core_user_id` |  |  | User core ID (pick one with sec_uid)  |

## Details

Returns a link to a QR code image for a Douyin Xingtu creator profile. Pass either `core_user_id` or `sec_uid` to identify the creator.

### Use cases

- Show a scannable profile code next to a creator row in an internal talent dashboard.
- Add a creator QR code to a pitch deck or campaign brief so a client can open the profile on a phone.
- Print or embed a creator's profile code in offline materials for a brand partnership event.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/user-profile-qrcode" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"core_user_id": "1113181577281568"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `core_user_id` | string | No | User core ID (pick one with sec_uid) |
| `sec_uid` | string | No | User sec_uid (pick one with core_user_id) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": "成功"
  },
  "qrcode": "https://p3.douyinpic.com/img/aweme-qrcode/TSQBWe7703844895601002240~c5_720x720.p…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `qrcode` | URL of the QR code image (a PNG file) for the creator profile. Download or embed this URL to show the code. |
| `base_resp.status_code` | Result code of the call. A value of `0` means the lookup succeeded. |
| `base_resp.status_message` | Text message that goes with the status code. It reads `成功` (success) in the sample response. |

### Notes

- Send either `core_user_id` or `sec_uid`. The request schema marks both as optional strings and describes them as pick one.
- The sample call used `core_user_id` set to `1113181577281568`.
- To find a creator ID first, call [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v2/search-creator). To convert a `sec_uid` into a Xingtu author ID, call [Douyin XingTu kolId by sec_user_id (V2)](/apis/douyin/xingtu-v2/xingtu-kolid-by-sec-user-id).
- For more profile data on the same creator, call [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/user-profile-qrcode.json`](../../../../catalog/models/douyin/xingtu-v2/user-profile-qrcode.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/user-profile-qrcode

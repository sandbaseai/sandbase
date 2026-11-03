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

Retrieve a profile QR code for a Douyin Xingtu creator using either `core_user_id` or `sec_uid`. This allows direct linking to creator profiles.

### Use cases

- Display creator profile QR codes in marketing dashboards.
- Facilitate direct mobile navigation to Douyin creator profiles.
- Share Xingtu profile links via scannable QR codes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/user-profile-qrcode" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"core_user_id": "1113181577281568"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | No | User sec_uid (pick one with core_user_id) |
| `core_user_id` | string | No | User core ID (pick one with sec_uid) |

### Notes

- Requires either `core_user_id` or `sec_uid` as an identifier.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/apis/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/apis/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/apis/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/user-profile-qrcode.json`](../../../../catalog/models/douyin/xingtu-v2/user-profile-qrcode.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/user-profile-qrcode

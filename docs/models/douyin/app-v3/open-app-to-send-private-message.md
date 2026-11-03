# Douyin Direct Message Deep Link API: pricing, parameters and code examples

`douyin/app-v3/open-app-to-send-private-message` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Generates a Douyin deep link to open the mobile application directly to a user conversation. Requires the target user's uid and sec_uid to return a shortened URL.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/open-app-to-send-private-message", "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_", "uid": "92769419069"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/open-app-to-send-private-message', {'sec_uid': 'MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_', 'uid': '92769419069'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/open-app-to-send-private-message", {
  "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_",
  "uid": "92769419069"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/open-app-to-send-private-message", sandbase.Params{
	"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_",
	"uid": "92769419069",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/open-app-to-send-private-message` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User id  |
| `sec_uid` | string | yes | User sec_uid  |

## Details

Returns a short Douyin link that opens the Douyin mobile app to a private message conversation with a given user. It needs the target user's `uid` and `sec_uid`.

### Use cases

- Add a "Message us on Douyin" button to a website that opens the brand's chat in the app.
- Put a chat link in a customer support email or QR code so users reach your Douyin account in one tap.
- Build outreach tools that give each creator a ready-to-use direct message link.
- Generate message links in bulk for a list of accounts you already track.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/open-app-to-send-private-message" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_", "uid": "92769419069"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | Yes | User sec_uid |
| `uid` | string | Yes | User id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_",
  "short_url": "https://v.douyin.com/mA8jwqgb6sA/",
  "status": "success",
  "uid": "92769419069"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `short_url` | Shortened `v.douyin.com` link. Opening it on a phone with Douyin installed launches the app to the conversation with the target user. |
| `status` | Result of the call. The value `success` means the link was created. |
| `uid` | The user id you sent, echoed back in the response. |
| `sec_uid` | The user `sec_uid` you sent, echoed back in the response. |

### Notes

- Send both `uid` and `sec_uid`. Both are required and both must belong to the same account.
- Get the `uid` and `sec_uid` pair from a user lookup such as [Douyin User Profile (App V3)](/apis/douyin/app-v3/user-profile).
- To link to a profile page instead of a chat, use [Douyin User Profile Share Link](/apis/douyin/app-v3/open-app-to-user-profile).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/open-app-to-send-private-message.json`](../../../../catalog/models/douyin/app-v3/open-app-to-send-private-message.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/open-app-to-send-private-message

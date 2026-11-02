# Douyin Direct Message Deep Link API: pricing, parameters and code examples

`douyin/app-v3/open-app-to-send-private-message` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Generates a Douyin deep link to open the mobile application directly to a user conversation. Requires the target user's uid and sec_uid to return a shortened URL.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/open-app-to-send-private-message", "sec_uid": "<sec_uid>", "uid": "<uid>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/open-app-to-send-private-message', {'sec_uid': '<sec_uid>', 'uid': '<uid>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/open-app-to-send-private-message", {
  "sec_uid": "<sec_uid>",
  "uid": "<uid>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/open-app-to-send-private-message", sandbase.Params{
	"sec_uid": "<sec_uid>",
	"uid": "<uid>",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/open-app-to-send-private-message` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User id  |
| `sec_uid` | string | yes | User sec_uid  |

## Details

Generates a short deep link that launches the Douyin application to message a targeted account using `uid` and `sec_uid`.

### Use cases

- Direct users to chat with official brand accounts in the Douyin app.
- Guide audience members from external websites into native app conversations.
- Facilitate one-click messaging workflows for customer support.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/open-app-to-send-private-message" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_", "uid": "92769419069"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User id |
| `sec_uid` | string | Yes | User sec_uid |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "short_url": "https://v.douyin.com/Zy_7aAP2O2w/",
  "status": "success"
}
```

### Notes

- Both `uid` and `sec_uid` are required to target the account.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/open-app-to-send-private-message.json`](../../../../catalog/models/douyin/app-v3/open-app-to-send-private-message.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/open-app-to-send-private-message

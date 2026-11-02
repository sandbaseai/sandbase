# Douyin User Profile Share Link API: pricing, parameters and code examples

`douyin/app-v3/open-app-to-user-profile` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Generates a Douyin app share link that redirects to a specific user profile using a provided user ID and secure user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/open-app-to-user-profile", "sec_uid": "example", "uid": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/open-app-to-user-profile', {'sec_uid': 'example', 'uid': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/open-app-to-user-profile", {
  "sec_uid": "example",
  "uid": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/open-app-to-user-profile", sandbase.Params{
	"sec_uid": "example",
	"uid": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/open-app-to-user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User id  |
| `sec_uid` | string | yes | User sec_uid  |

## Details

Provides a short URL that opens the Douyin app to a targeted profile using `uid` and `sec_uid`.

### Use cases

- Direct users to a Douyin profile from external marketing pages.
- Embed profile deep links inside mobile applications or web portals.
- Route traffic to specific Douyin creators through standardized short URLs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/open-app-to-user-profile" \
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
  "short_url": "https://v.douyin.com/yXDBC0IkXRQ/",
  "status": "success"
}
```

### Notes

- Requires both `uid` and `sec_uid` to identify the target user account.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/open-app-to-user-profile.json`](../../../../catalog/models/douyin/app-v3/open-app-to-user-profile.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/open-app-to-user-profile

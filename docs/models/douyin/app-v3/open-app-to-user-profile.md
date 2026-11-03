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

Returns a Douyin short link that opens the Douyin app on a specific user profile. It needs the user's `uid` and `sec_uid`.

### Use cases

- Add a button on a landing page that opens a creator's Douyin profile in the app.
- Build a list of profile deep links for a set of creators you track.
- Send a profile link in a campaign message so users land on the right account.
- Check that a `uid` and `sec_uid` pair resolves to a working profile link.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/open-app-to-user-profile" \
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
  "short_url": "https://v.douyin.com/Ihlbayv701k/",
  "status": "success",
  "uid": "92769419069"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `short_url` | Short Douyin link that opens the app on the requested user profile. |
| `status` | Result of the request. The value is `success` when the link was generated. |
| `uid` | The user ID from the request, echoed back. |
| `sec_uid` | The secure user ID from the request, echoed back. |

### Notes

- Both `uid` and `sec_uid` are required. Send them as strings.
- Use [Douyin User Profile (App V3)](/apis/douyin/app-v3/user-profile) to look up profile details for the same user.
- Use [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url) to shorten a standard Douyin web link instead.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Brand Hot Search List](/apis/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/apis/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/apis/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/open-app-to-user-profile.json`](../../../../catalog/models/douyin/app-v3/open-app-to-user-profile.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/open-app-to-user-profile

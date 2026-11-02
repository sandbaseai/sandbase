# Douyin User Profile (App V3) API: pricing, parameters and code examples

`douyin/app-v3/user-profile` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns profile information and follower statistics for a specified Douyin user based on their unique secure user identifier.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/app-v3/user-profile", "sec_user_id": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/app-v3/user-profile', {'sec_user_id': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/app-v3/user-profile", {
  "sec_user_id": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/app-v3/user-profile", sandbase.Params{
	"sec_user_id": "example",
})
```

Same call via the path form: `POST /v1/api/douyin/app-v3/user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_user_id` | string | yes | User sec_user_id  |

## Details

Retrieve profile details and follower metadata for a specific Douyin account by supplying `sec_user_id`.

### Use cases

- Analyze audience reach and follower counts for a target Douyin account.
- Extract user profile data for influencer research and creator monitoring.
- Inspect Douyin account details within social media analytics workflows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/app-v3/user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_user_id": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_user_id` | string | Yes | User sec_user_id |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "user": {
    "followers_detail": [
      {
        "app_name": "aweme",
        "apple_id": "1142110895",
        "fans_count": 163334,
        "name": "抖音",
        "open_url": "snssdk1128://user/profile/3635433641882579?",
        "package_name": "com.ss.android.ugc.aweme"
      }
    ]
  }
}
```

### Notes

- Requires a valid `sec_user_id` parameter to identify the target profile.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Brand Hot Search List](/model/douyin/app-v3/brand-hot-search-list): Returns the current Douyin brand hot search list and category data.
- [Douyin Brand Hot Search List Detail](/model/douyin/app-v3/brand-hot-search-list-detail): Returns detailed brand hot search list data from Douyin for a specific category.
- [Douyin Short Link Generator](/model/douyin/app-v3/generate-short-url): Converts a standard Douyin web link into a shortened Douyin URL.

---
Machine-readable: [`catalog/models/douyin/app-v3/user-profile.json`](../../../../catalog/models/douyin/app-v3/user-profile.json) · Store page: https://www.sandbase.ai/model/douyin/app-v3/user-profile

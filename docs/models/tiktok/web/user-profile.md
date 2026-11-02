# TikTok User Profile API: pricing, parameters and code examples

`tiktok/web/user-profile` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns public profile information for a specified TikTok user. Look up accounts by providing either the unique handle or secure user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/user-profile", "uniqueId": "srlechuza2.0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/user-profile', {'uniqueId': 'srlechuza2.0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/user-profile", {
  "uniqueId": "srlechuza2.0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/user-profile", sandbase.Params{
	"uniqueId": "srlechuza2.0",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `secUid` | string |  | User secUid default `""` |
| `uniqueId` | string |  | User uniqueId default `""` |

## Details

Retrieve detailed TikTok user profile information using either `uniqueId` or `secUid`.

### Use cases

- Display public creator profile details within external dashboards.
- Verify TikTok usernames and identify creator accounts.
- Retrieve creator metadata using either a handle or secure user identifier.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `secUid` | string | No | User secUid |
| `uniqueId` | string | No | User uniqueId |

### Notes

- Look up user profiles using either `uniqueId` or `secUid`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/user-profile.json`](../../../../catalog/models/tiktok/web/user-profile.json) · Store page: https://www.sandbase.ai/model/tiktok/web/user-profile

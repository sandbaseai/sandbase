# Instagram User Profile API: pricing, parameters and code examples

`instagram/v2/user-info` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Get an Instagram user profile by username or user ID: full name, bio, website, follower, following and post counts, verification and category.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/user-info", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/user-info', {'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/user-info", {
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/user-info", sandbase.Params{
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string |  | User ID (either username or user_id required)  |
| `username` | string |  | Username (either username or user_id required)  |

## Details

Pass an Instagram username (or user ID) and get the public profile with follower counts and bio details.

### Use cases

- Vet influencers before a campaign.
- Track follower growth for accounts.
- Enrich handles with profile data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "nasa"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | No | User ID (either username or user_id required) |
| `username` | string | No | Username (either username or user_id required) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "id": "528817151",
    "username": "nasa",
    "full_name": "NASA",
    "biography": "Making the seemingly impossible, possible. ✨",
    "external_url": "https://www.nasa.gov",
    "follower_count": 104283919,
    "following_count": 90,
    "media_count": 4947,
    "is_verified": true
  }
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Reels Search](/model/instagram/v2/search-reels): Search Instagram Reels by keyword: reel IDs, captions, creators, play, like and comment counts, with pagination.
- [Get comment replies](/model/instagram/v2/comment-replies): Get list of replies to a comment Need to get comment ID from fetch_post_comments first Support pagination.
- [General search](/model/instagram/v2/general-search): Perform general search on Instagram by keyword Support pagination.

---
Machine-readable: [`catalog/models/instagram/v2/user-info.json`](../../../../catalog/models/instagram/v2/user-info.json) · Store page: https://www.sandbase.ai/model/instagram/v2/user-info

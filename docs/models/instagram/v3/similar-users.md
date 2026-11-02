# Instagram Similar Users (V3) API: pricing, parameters and code examples

`instagram/v3/similar-users` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

Returns recommended Instagram accounts similar to a target profile. Provide a numeric user ID to look up related accounts, usernames, and profile details.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/similar-users", "user_id": "25025320"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/similar-users', {'user_id': '25025320'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/similar-users", {
  "user_id": "25025320"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/similar-users", sandbase.Params{
	"user_id": "25025320",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/similar-users` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Target user ID (numeric), obtainable via get_user_id_by_username  |

## Details

Look up suggested accounts similar to a specified profile by providing the numeric `user_id` parameter.

### Use cases

- Discover relevant influencers in the same niche as a target profile.
- Analyze competitor networks and related account suggestions.
- Expand audience targeting lists by identifying closely related users.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/similar-users" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "25025320"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Target user ID (numeric), obtainable via get_user_id_by_username |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "users": [
    {
      "full_name": "LISA",
      "id": "8012033210",
      "pk_id": "8012033210",
      "profile_pic_id": "4001908869835700028_8012033210",
      "profile_pic_url": "https://scontent-hou1-1.cdninstagram.com/v/t51.82787-19/839490332_18373632106265…",
      "social_context": "LISA",
      "username": "<user>"
    }
  ]
}
```

### Notes

- The `user_id` parameter requires a numeric account ID, obtainable via the user ID lookup endpoint.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Instagram Comment Bulk Translation](/model/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/model/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/model/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/similar-users.json`](../../../../catalog/models/instagram/v3/similar-users.json) · Store page: https://www.sandbase.ai/model/instagram/v3/similar-users

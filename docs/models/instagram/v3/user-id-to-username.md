# Instagram User Info by ID API: pricing, parameters and code examples

`instagram/v3/user-id-to-username` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns an Instagram profile's details, including username, full name, follower count, and media metrics using an account ID.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-id-to-username", "user_id": "1935268808"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-id-to-username', {'user_id': '1935268808'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-id-to-username", {
  "user_id": "1935268808"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-id-to-username", sandbase.Params{
	"user_id": "1935268808",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-id-to-username` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Instagram user ID (numeric string)  |

## Details

Find the current username of an Instagram account from its numeric user ID, together with the profile: full name, bio, follower, following and post counts, verification and privacy flags.

### Use cases

- Show readable handles for IDs stored in your database or returned by other APIs.
- Detect username changes by re-checking stored IDs.
- Get basic audience size for influencer screening.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-id-to-username" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "25025320"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Instagram user ID (numeric string) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "_rid": "351695735c9af",
  "biography": "Discover what's new on Instagram 🔎✨",
  "category": "",
  "edge_follow": {
    "count": 165
  },
  "edge_followed_by": {
    "count": 686358280
  },
  "edge_owner_to_timeline_media": {
    "count": 8634
  },
  "external_url": "http://help.instagram.com",
  "follower_count": 686358280,
  "following_count": 165,
  "full_name": "Instagram",
  "id": "25025320",
  "is_private": false
}
```

### Response fields

| Field | Meaning |
|---|---|
| `username` | Current handle, without `@`. |
| `full_name` | Display name. |
| `biography` | Profile bio. |
| `follower_count / following_count / media_count` | Followers, accounts followed and number of posts. |
| `is_verified / is_private` | Verification badge and private-account flag. |
| `profile_pic_url` | Avatar URL; signed and expires after some days. |
| `external_url` | Link in bio. |

### Notes

- The ID is the numeric `pk`, not a shortcode. Get it with [Instagram User ID Lookup](/apis/instagram/v3/user-id-by-username).

### Pricing

$0.008 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-id-to-username.json`](../../../../catalog/models/instagram/v3/user-id-to-username.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-id-to-username

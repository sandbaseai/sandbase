# Instagram User Brief Info API: pricing, parameters and code examples

`instagram/v3/user-brief` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns summary profile metrics and metadata for an Instagram account, including follower counts, media count, and profile picture URL, using user_id and username.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-brief", "user_id": "25025320", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-brief', {'user_id': '25025320', 'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-brief", {
  "user_id": "25025320",
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-brief", sandbase.Params{
	"user_id": "25025320",
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-brief` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Instagram user ID (numeric, required)  |
| `username` | string | yes | Instagram username (required)  |

## Details

Returns a short profile summary for one Instagram account, including follower count, following count, media count, bio, and profile picture URLs. It needs both the numeric `user_id` and the `username`.

### Use cases

- Show follower, following, and post counts for a creator on a dashboard.
- Check whether an account is verified or private before you add it to an outreach list.
- Save the bio, `external_url`, and profile picture of an account for a creator database.
- Track how `follower_count` and `media_count` change by calling the API on a schedule.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-brief" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "25025320", "username": "instagram"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Instagram user ID (numeric, required) |
| `username` | string | Yes | Instagram username (required) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "_rid": "3148cbeadeb94",
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
| `follower_count / edge_followed_by.count` | Number of accounts that follow this account. Both fields hold the same value in this response. |
| `following_count / edge_follow.count` | Number of accounts this account follows. |
| `media_count / edge_owner_to_timeline_media.count` | Number of posts on the account. |
| `full_name / username` | Display name and handle of the account. |
| `biography` | Bio text shown on the profile. It can include emoji. |
| `external_url` | Link the account lists on its profile. |
| `is_verified / is_private` | Booleans that show whether the account has a verified badge and whether it is private. |
| `profile_pic_url / profile_pic_url_hd` | Links to the profile picture. The `_hd` field points to a larger version. |
| `id / pk` | Instagram user ID as a string. Both fields hold the same value. |
| `category` | Account category label. It is an empty string when the account sets none. |

### Notes

- Send both `user_id` and `username`. Both are required.
- If you only know the handle, call [Instagram User ID Lookup](/apis/instagram/v3/user-id-by-username) first to get the `user_id`.
- For a fuller profile view, use [Instagram User Profile (V3)](/apis/instagram/v3/user-profile).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-brief.json`](../../../../catalog/models/instagram/v3/user-brief.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-brief

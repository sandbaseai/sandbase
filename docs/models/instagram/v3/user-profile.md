# Instagram User Profile (V3) API: pricing, parameters and code examples

`instagram/v3/user-profile` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns complete profile details for an Instagram account, including follower counts, media metrics, and bio links based on the provided username.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-profile", "username": "nasa"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-profile', {'username': 'nasa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-profile", {
  "username": "nasa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-profile", sandbase.Params{
	"username": "nasa",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Instagram username (required)  |

## Details

Returns public profile details for an Instagram account, including the display name, bio, follower and following counts, post count, and profile picture URLs. It needs one input, the account `username`.

### Use cases

- Track the follower count of a brand or public figure over time.
- Check whether an account is verified or private before you process it.
- Read the bio and `external_url` to find the website an account links to.
- Get the numeric account ID and profile picture URL to save with a user record.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "nasa"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username (required) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "_rid": "35a785539570a",
  "biography": "Making the seemingly impossible, possible. ✨",
  "category": "",
  "edge_follow": {
    "count": 90
  },
  "edge_followed_by": {
    "count": 104427280
  },
  "edge_owner_to_timeline_media": {
    "count": 4987
  },
  "external_url": "https://www.nasa.gov",
  "follower_count": 104427280,
  "following_count": 90,
  "full_name": "NASA",
  "id": "528817151",
  "is_private": false
}
```

### Response fields

| Field | Meaning |
|---|---|
| `username / full_name` | The account handle and the display name shown on the profile. |
| `id / pk` | The numeric account ID as a string. Both fields hold the same value in this response. |
| `biography` | The bio text of the profile. |
| `external_url` | The link shown in the bio. |
| `follower_count / edge_followed_by.count` | Number of accounts that follow this account. Both fields hold the same value. |
| `following_count / edge_follow.count` | Number of accounts this account follows. |
| `media_count / edge_owner_to_timeline_media.count` | Number of posts on the account. |
| `is_verified / is_private` | Booleans that show whether the account has a verified badge and whether it is private. |
| `profile_pic_url / profile_pic_url_hd` | Links to the profile picture, in a standard and a larger version. |
| `category` | The account category label. It can be an empty string. |

### Notes

- Pass the handle without the `@` sign, for example `nasa`.
- To get only the numeric ID for a username, call [Instagram User ID Lookup](/apis/instagram/v3/user-id-by-username).
- To list the account's content, call [Instagram User Posts (V3)](/apis/instagram/v3/user-posts) or [Instagram User Reels (V3)](/apis/instagram/v3/user-reels).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-profile.json`](../../../../catalog/models/instagram/v3/user-profile.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-profile

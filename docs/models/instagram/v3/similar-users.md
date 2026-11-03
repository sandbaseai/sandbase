# Instagram Similar Users (V3) API: pricing, parameters and code examples

`instagram/v3/similar-users` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns recommended Instagram accounts similar to a target profile. Provide a numeric user ID to look up related accounts, usernames, and profile details.

## Pricing

- **$0.008 per call** (USD)
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

Returns a list of Instagram accounts that Instagram suggests as similar to a target profile. It needs one input, the numeric `user_id` of the target account. Each result includes the username, full name, verification and privacy flags, and a profile picture URL.

### Use cases

- Find accounts in the same niche as a creator or brand for influencer research.
- Build a list of competitor or peer accounts around a known brand profile.
- Expand an audience targeting list starting from one seed account.
- Check which verified accounts Instagram groups with a given profile.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/similar-users" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "25025320"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Target user ID (numeric), obtainable via get_user_id_by_username |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "chaining_upsell_cards": [],
  "follow_ranking_token": "556cc6e8…",
  "is_backup": false,
  "is_recommend_account": false,
  "status": "ok",
  "users": [
    {
      "chaining_info": {
        "algorithm": null,
        "sources": ""
      },
      "full_name": "Kevin Systrom",
      "id": "3",
      "is_private": false,
      "is_verified": true,
      "pk": "3",
      "pk_id": "3",
      "profile_pic_id": "1295922680046102746_3",
      "profile_pic_url": "https://scontent-atl3-1.cdninstagram.com/v/t51.2885-19/13732144_1764457777134045…",
      "social_context": "Kevin Systrom",
      "strong_id__": "3",
      "username": "kevin"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `users[]` | List of suggested accounts similar to the target profile. |
| `users[].username` | Instagram handle of the suggested account. |
| `users[].full_name` | Display name shown on the suggested account's profile. |
| `users[].id / users[].pk / users[].pk_id / users[].strong_id__` | Numeric ID of the suggested account, returned as a string. All four hold the same value in this response. Use it as `user_id` in other calls. |
| `users[].is_verified` | `true` if the suggested account has a verified badge. |
| `users[].is_private` | `true` if the suggested account is private. |
| `users[].profile_pic_url` | URL of the account's profile picture. |
| `users[].profile_pic_id` | Identifier of the profile picture. It ends with an underscore and the account ID. |
| `users[].social_context` | Short text label Instagram shows with the suggestion. In this response it repeats the full name. |
| `follow_ranking_token` | Token string returned with the recommendations. It contains the pipe-separated parts of a ranking identifier. |

### Notes

- Get the numeric `user_id` from a username with [Instagram User ID Lookup](/apis/instagram/v3/user-id-by-username).
- The request has no pagination parameter. The response returns one list in `users`.
- To see full details for a suggested account, pass its `id` to [Instagram User Profile (V3)](/apis/instagram/v3/user-profile).
- The `chaining_upsell_cards` list is empty and `chaining_info` holds empty values in the sample response.

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/similar-users.json`](../../../../catalog/models/instagram/v3/similar-users.json) · Store page: https://www.sandbase.ai/model/instagram/v3/similar-users

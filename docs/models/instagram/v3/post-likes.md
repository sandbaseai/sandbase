# Instagram Post Likes (V3) API: pricing, parameters and code examples

`instagram/v3/post-likes` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns a list of users who liked a specific Instagram post. Queries engagement details using the unique post shortcode from the post URL.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/post-likes", "code": "Dd9RyBWBVih"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/post-likes', {'code': 'Dd9RyBWBVih'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/post-likes", {
  "code": "Dd9RyBWBVih"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/post-likes", sandbase.Params{
	"code": "Dd9RyBWBVih",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/post-likes` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `code` | string | yes | Post shortcode (from post URL, e.g. instagram.com/p/{code}/)  |

## Details

Returns a list of Instagram users who liked a post, plus the total like count for the post. It needs one input, the post shortcode `code`, which is the part of the post URL after `/p/`.

### Use cases

- Build a list of accounts that engaged with a brand post and check which ones are verified.
- Compare `user_count` across several posts to measure how much like activity each one gets.
- Collect usernames and profile pictures of people who liked a campaign post for outreach research.
- Check whether a set of known accounts liked a specific post by matching `username` or `pk`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/post-likes" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"code": "Dd9RyBWBVih"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `code` | string | Yes | Post shortcode (from post URL, e.g. instagram.com/p/{code}/) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "follow_ranking_token": "658b7c11…",
  "status": "ok",
  "user_count": 915443,
  "users": [
    {
      "account_badges": [],
      "friendship_status": {
        "blocking": false,
        "followed_by": false,
        "following": false,
        "incoming_request": false,
        "is_bestie": false,
        "is_blocking_reel": false,
        "is_eligible_to_subscribe": false,
        "is_feed_favorite": false
      },
      "full_name": "Nele",
      "id": "48566646275",
      "is_private": true,
      "is_verified": false,
      "latest_reel_media": 0,
      "pk": "48566646275",
      "pk_id": "48566646275",
      "profile_pic_id": "3486491172489676304_48566646275",
      "profile_pic_url": "https://scontent-lga3-3.cdninstagram.com/v/t51.2885-19/464549156_767778562141792…",
      "strong_id__": "48566646275"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `user_count` | Total number of users reported for the post's likes. It can be larger than the number of items in `users` returned in one response. |
| `users[]` | List of user profiles that liked the post. |
| `users[].username / users[].full_name` | The account handle and the display name. `full_name` can be an empty string. |
| `users[].pk / users[].pk_id / users[].id / users[].strong_id__` | The numeric user ID as a string. These fields hold the same value in the sample. |
| `users[].is_private / users[].is_verified` | Whether the account is private and whether it is verified. |
| `users[].profile_pic_url` | URL of a small profile picture for the user. |
| `users[].profile_pic_id` | ID of the profile picture. It starts with the picture ID and ends with the user ID, joined by an underscore. |
| `users[].friendship_status.following / users[].friendship_status.followed_by` | Whether the account tied to the request follows this user, and whether this user follows it back. |
| `users[].latest_reel_media` | Value for the user's latest reel media. It is `0` for every user in the sample. |
| `follow_ranking_token` | Token string returned with the list. The response does not explain its use. |

### Notes

- Take `code` from the post URL: for `instagram.com/p/Dd9RyBWBVih/`, the value is `Dd9RyBWBVih`.
- The request has no pagination parameter. The sample response returns only a few users even though `user_count` is 915443.
- User IDs are strings of digits. Pass them to [Instagram User Profile (V3)](/apis/instagram/v3/user-profile) or [Instagram User Brief Info](/apis/instagram/v3/user-brief) for more detail on a liker, if those APIs accept that ID.
- To get post details such as caption or media, call [Instagram Post Details (V3)](/apis/instagram/v3/post-info).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/post-likes.json`](../../../../catalog/models/instagram/v3/post-likes.json) · Store page: https://www.sandbase.ai/model/instagram/v3/post-likes

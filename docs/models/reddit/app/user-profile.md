# Reddit App User Profile API: pricing, parameters and code examples

`reddit/app/user-profile` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed profile information for a specified Reddit app user by username. Supports an optional flag to clean and format the output data.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/app/user-profile", "username": "spez"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/app/user-profile', {'username': 'spez'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/app/user-profile", {
  "username": "spez"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/app/user-profile", sandbase.Params{
	"username": "spez",
})
```

Same call via the path form: `POST /v1/api/reddit/app/user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Reddit username (without u/ prefix)  |
| `need_format` | boolean |  | Whether to clean and format the data default `false` |

## Details

Returns the public profile of a Reddit user, including karma, post and comment counts, account flags, and profile settings. It needs one input: the `username` without the `u/` prefix.

### Use cases

- Check the karma totals and contribution counts of an account before you trust its posts.
- Confirm whether an account is an employee, verified, or gilded.
- Read the account creation date and bio text to build a user record.
- Get the `t2_` user ID to use in other Reddit lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/app/user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "spez"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Reddit username (without u/ prefix) |
| `need_format` | boolean | No | Whether to clean and format the data |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "redditorInfoByName": {
    "__typename": "Redditor",
    "accountType": "USER",
    "contributionStats": {
      "commentCount": 3228,
      "postCount": 851
    },
    "contributorPublicProfile": {
      "tier": "NON_CONTRIBUTOR"
    },
    "id": "t2_1w72",
    "isAcceptingChats": true,
    "isAcceptingFollowers": true,
    "isAcceptingPMs": true,
    "isBlocked": false,
    "isEmployee": true,
    "isFriend": false,
    "isGilded": true
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `redditorInfoByName.name / redditorInfoByName.prefixedName` | The username, and the same name with the `u/` prefix. |
| `redditorInfoByName.id` | The account ID, in the form `t2_1w72`. |
| `redditorInfoByName.karma.total` | Total karma. `fromPosts` and `fromComments` show the split between the two sources. |
| `redditorInfoByName.contributionStats.postCount / redditorInfoByName.contributionStats.commentCount` | The number of posts and comments counted for the account. |
| `redditorInfoByName.isEmployee / redditorInfoByName.isVerified / redditorInfoByName.isGilded` | Boolean flags for employee status, verification, and gilded status. |
| `redditorInfoByName.isAcceptingChats / redditorInfoByName.isAcceptingFollowers / redditorInfoByName.isAcceptingPMs` | Boolean flags that show whether the account accepts chats, followers, and private messages. |
| `redditorInfoByName.profile.createdAt` | Account creation time as an ISO 8601 timestamp. |
| `redditorInfoByName.profile.publicDescriptionText` | The public bio text shown on the profile. |
| `redditorInfoByName.profile.styles.icon` | URL of the profile icon image. |
| `redditorInfoByName.trophyCase.totalUnlocked` | The number of trophies the account has unlocked. |

### Notes

- Pass `username` without the `u/` prefix. The response gives the prefixed form in `prefixedName`.
- `need_format` is optional and defaults to `false`. Set it to `true` to clean and format the data.
- Call [Reddit User Public Trophies](/apis/reddit/app/user-trophies) for trophy details, [Reddit User Posts](/apis/reddit/app/user-posts) for the posts of this user, or [Reddit User Comments](/apis/reddit/app/user-comments) for the comments.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Reddit Subreddit Mute Status](/apis/reddit/app/check-subreddit-muted): Checks whether a specified Reddit subreddit is muted by the current account using its ID.
- [Reddit App Comment Replies](/apis/reddit/app/comment-replies): Returns replies and nested sub-comments under a Reddit post comment using a continuation cursor.
- [Reddit Community Highlights](/apis/reddit/app/community-highlights): Returns featured highlight content for a designated Reddit community, such as popular posts and announcements, by subreddit ID.

---
Machine-readable: [`catalog/models/reddit/app/user-profile.json`](../../../../catalog/models/reddit/app/user-profile.json) · Store page: https://www.sandbase.ai/model/reddit/app/user-profile

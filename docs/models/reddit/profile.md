# Reddit Profile API: pricing, parameters and code examples

`reddit/profile` · data API · Reddit · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0008 per call · **Modes:** sync

Fetch a Reddit user's public profile (karma split, post and comment counts, bio, avatar, account age) by username.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0008**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/profile", "username": "spez"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/profile', {'username': 'spez'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/profile", {
  "username": "spez"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/profile", sandbase.Params{
	"username": "spez",
})
```

Same call via the path form: `POST /v1/api/reddit/profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Reddit username, without the u/ prefix. Example: "spez".  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `verified`, and it is served only by a source that returns every one…  |

## Details

Returns the public profile of a Reddit user: karma split, post and comment counts, bio, avatar, trophy count and account creation time. It needs one input, the Reddit `username` without the u/ prefix.

### Use cases

- Check how old a Reddit account is and how much karma it has before you trust its posts.
- Pull the bio, avatar and profile link of a user to show on a creator or lead card.
- Compare post karma and comment karma to see whether an account mostly posts or mostly comments.
- Flag Reddit employee accounts with the `employee` field.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "spez"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Reddit username, without the u/ prefix. Example: "spez". |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `verified`, and it is served only by a source that returns every one o |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "avatarUrl": "https://styles.redditmedia.com/t5_3k30p/styles/profileIcon_uj015iwx9s7g1.png",
    "bio": "Reddit CEO",
    "commentKarma": 756623,
    "comments": 3228,
    "createdUtc": 1118030400,
    "displayName": "spez",
    "employee": true,
    "followers": 0,
    "id": "1w72",
    "karma": 941388,
    "nsfw": false,
    "postKarma": 184765
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the username exists. A lookup that finds nothing returns `false`. |
| `data.username / data.displayName` | The account name and its display name. Both are `spez` in this example. |
| `data.id` | Reddit's short ID for the user, such as `1w72`. |
| `data.karma` | Total karma for the account. It is the sum of `postKarma` and `commentKarma` in this example. |
| `data.postKarma / data.commentKarma` | Karma earned from posts and from comments. |
| `data.posts / data.comments` | Number of posts and comments on the account. |
| `data.createdUtc` | Account creation time as a Unix timestamp in seconds. |
| `data.bio / data.avatarUrl / data.profileUrl` | The profile bio text, the avatar image URL and the link to the Reddit profile page. |
| `data.employee / data.verified / data.nsfw` | Boolean flags for Reddit employee status, verified status and NSFW profile. `verified` can be `null` when the serving source does not return it. |
| `data.trophies / data.followers` | Count of trophies on the profile and the follower count. |

### Notes

- Pass `username` without the u/ prefix, for example `spez`.
- Set `requireFields` to `["verified"]` if you need a real `verified` value. Without it, `verified` can come back as `null`.
- For the content a user wrote, call [Reddit User Posts](/apis/reddit/user-posts) or [Reddit User Comments](/apis/reddit/user-comments).
- [Reddit User Public Trophies](/apis/reddit/app/user-trophies) lists the trophies behind the `trophies` count.

### Pricing

Billed at the actual cost of each call, about $0.0008 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/reddit/profile.json`](../../../catalog/models/reddit/profile.json) · Store page: https://www.sandbase.ai/model/reddit/profile

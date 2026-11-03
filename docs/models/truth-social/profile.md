# Truth Social Profile API: pricing, parameters and code examples

`truth-social/profile` · data API · Truth Social · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

Get a Truth Social account's public profile by handle - display name, bio, follower/following counts, and post count as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "truth-social/profile", "handle": "DevinNunes"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('truth-social/profile', {'handle': 'DevinNunes'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("truth-social/profile", {
  "handle": "DevinNunes"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "truth-social/profile", sandbase.Params{
	"handle": "DevinNunes",
})
```

Same call via the path form: `POST /v1/api/truth-social/profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | Truth Social handle without the @, e.g. "realDonaldTrump".  |

## Details

This API returns the public profile of a Truth Social account. It needs one input, the account `handle` without the @. The response includes the display name, bio, follower and following counts, post count, and join date.

### Use cases

- Track the follower count of a public figure on Truth Social over time.
- Check whether an account is `verified` before you treat it as the real person or organization.
- Collect the numeric account `id` to use in other tools that need a stable account reference.
- Build a profile card that shows the avatar, display name, bio, and link to the account.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/truth-social/profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "DevinNunes"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | Truth Social handle without the @, e.g. "realDonaldTrump". |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "avatarUrl": "https://static-assets-1.truthsocial.com/tmtg:prime-ts-assets/accounts/avatars/10…",
    "bio": "Wine Maker RT≠endorsement",
    "displayName": "Devin Nunes",
    "followers": 4461040,
    "following": 712,
    "id": "107777378958166346",
    "joinedAt": "2022-02-11T04:04:53.373Z",
    "postsCount": 21542,
    "private": false,
    "url": "https://truthsocial.com/@DevinNunes",
    "username": "DevinNunes",
    "verified": true
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.displayName` | The name shown on the profile. |
| `data.username` | The account handle, without the @. |
| `data.bio` | The profile bio text. |
| `data.followers / data.following` | The number of accounts that follow this account, and the number of accounts it follows. |
| `data.postsCount` | The total number of posts on the account. |
| `data.verified` | `true` if the account is marked as verified. |
| `data.private` | `true` if the account is private. It is `false` for an open account. |
| `data.joinedAt` | The time the account was created, as an ISO 8601 timestamp in UTC. |
| `data.id` | The numeric account ID, returned as a string. |
| `data.avatarUrl / data.url` | The link to the avatar image, and the link to the profile page on Truth Social. |
| `found` | `true` when the handle matched an account. |

### Notes

- Use the handle from the profile URL, for example `DevinNunes` from `truthsocial.com/@DevinNunes`. Leave out the @.
- Check `found` first. A handle that matches no account still returns a successful response with `found: false`.
- To read what the account has posted, call [Truth Social User Posts](/apis/truth-social/user-posts). To look at a single post, call [Truth Social Post](/apis/truth-social/post).

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/truth-social/profile.json`](../../../catalog/models/truth-social/profile.json) · Store page: https://www.sandbase.ai/model/truth-social/profile

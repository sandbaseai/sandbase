# Bluesky Profile API: pricing, parameters and code examples

`bluesky/profile` · data API · Bluesky · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

Get a Bluesky user's public profile by handle - display name, bio, follower and post counts as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bluesky/profile", "handle": "bsky.app"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bluesky/profile', {'handle': 'bsky.app'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bluesky/profile", {
  "handle": "bsky.app"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bluesky/profile", sandbase.Params{
	"handle": "bsky.app",
})
```

Same call via the path form: `POST /v1/api/bluesky/profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | Bluesky handle, e.g. "bsky.app" or "jay.bsky.team".  |

## Details

This API returns the public profile of a Bluesky account. It needs one input, the account `handle`, such as `bsky.app`. The response includes the display name, bio, avatar URL, follower and following counts, post count, and creation time.

### Use cases

- Show a Bluesky account card with name, bio, and avatar in a dashboard or CRM.
- Track follower and post counts for an account over repeated calls.
- Resolve a handle to its `did:plc:` ID before you call other Bluesky APIs.
- Check whether a handle exists by reading the `found` flag.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bluesky/profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "bsky.app"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | Bluesky handle, e.g. "bsky.app" or "jay.bsky.team". |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "avatarUrl": "https://cdn.bsky.app/img/avatar/plain/did:plc:z72i7hdynmk6r22z27h6tvur/bafkreihw…",
    "createdUtc": 1681275237,
    "description": "official Bluesky account (check username👆)\n\nBugs, feature requests, feedback: su…",
    "displayName": "Bluesky",
    "followers": 35503774,
    "following": 34,
    "handle": "bsky.app",
    "id": "did:plc:z72i7hdynmk6r22z27h6tvur",
    "postsCount": 907
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the handle was found. A lookup that finds nothing returns `false`. |
| `data.id` | The account's permanent ID, in the form `did:plc:...`. |
| `data.handle` | The Bluesky handle that was looked up. |
| `data.displayName` | The name the account shows on its profile. |
| `data.description` | The profile bio. It can contain line breaks written as `\n`. |
| `data.followers / data.following` | Number of accounts that follow this account, and number of accounts it follows. |
| `data.postsCount` | Number of posts the account has made. |
| `data.createdUtc` | Account creation time as a Unix timestamp in seconds, in UTC. |
| `data.avatarUrl` | URL of the profile picture image. |

### Notes

- Use the handle without the `@` sign, for example `bsky.app` or `jay.bsky.team`.
- The `data.id` value is a `did:plc:` identifier that stays with the account.
- To read what this account has posted, call [Bluesky User Posts](/apis/bluesky/user-posts).
- To fetch one specific post, call [Bluesky Post](/apis/bluesky/post).

### Pricing

Billed at the actual cost of each call, about $0.0011 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/bluesky/profile.json`](../../../catalog/models/bluesky/profile.json) · Store page: https://www.sandbase.ai/model/bluesky/profile

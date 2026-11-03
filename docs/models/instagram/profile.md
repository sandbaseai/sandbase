# Instagram Profile API: pricing, parameters and code examples

`instagram/profile` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.001 per call · **Modes:** sync

Fetch an Instagram account's public profile (followers, posts, bio, verification) by handle.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.001**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/profile", "handle": "nasa"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/profile', {'handle': 'nasa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/profile", {
  "handle": "nasa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/profile", sandbase.Params{
	"handle": "nasa",
})
```

Same call via the path form: `POST /v1/api/instagram/profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | Instagram username without the leading @.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `contactMethod`, and it is served only by a source that returns…  |

## Details

Returns the public profile of an Instagram account, including bio, follower and following counts, verification status and bio links. It needs one input: the account `handle` without the leading @.

### Use cases

- Check follower count and verification status of a brand or creator before a partnership.
- Pull the bio, bio links and website of an account to enrich a lead or CRM record.
- Convert a known `handle` into its numeric `userId` for lookups that need an ID.
- Monitor whether an account is private or has changed its display name or bio.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "nasa"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | Instagram username without the leading @. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `contactMethod`, and it is served only by a source that returns every  |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "avatarUrl": "https://scontent-ams2-1.cdninstagram.com/v/t51.2885-19/29090066_159271188110124_…",
    "bio": "Making the seemingly impossible, possible. ✨",
    "bioLinks": [
      {
        "title": "NASA.gov Homepage",
        "url": "https://www.nasa.gov"
      }
    ],
    "displayName": "NASA",
    "externalUrl": "https://www.nasa.gov",
    "followers": 104427283,
    "following": 90,
    "handle": "nasa",
    "highlightsCount": null,
    "isBusiness": true,
    "posts": null,
    "private": false
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `found` | `true` when the account exists. A lookup that finds nothing returns `false`. |
| `data.handle / data.displayName` | The account username and the name shown on the profile. |
| `data.userId` | Numeric Instagram ID of the account, returned as a string. |
| `data.followers / data.following` | Number of accounts that follow this profile and number of accounts it follows. |
| `data.verified` | `true` when the account has the verified badge. |
| `data.private` | `true` when the account is private. |
| `data.bio` | Text of the profile biography. |
| `data.bioLinks[].title / data.bioLinks[].url` | Label and address of each link listed in the bio. |
| `data.externalUrl` | The main website link on the profile. |
| `data.isBusiness / data.highlightsCount / data.posts` | Business account flag, highlight count and posts. The last two can be `null`, as they are in this response. Name them in `requireFields` to ask for a source that returns them. |

### Notes

- Pass the username only, for example `nasa`, with no leading @.
- `requireFields` accepts `contactMethod`, `highlightsCount`, `isBusiness` and `posts`. Naming a field can change which source serves the call and its price.
- Use [Instagram User Highlights](/apis/instagram/user-highlights) to list the highlights of the account, or [Instagram Similar Profiles](/apis/instagram/similar-profiles) to find related accounts.

### Pricing

Billed at the actual cost of each call, about $0.001 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/profile.json`](../../../catalog/models/instagram/profile.json) · Store page: https://www.sandbase.ai/model/instagram/profile

# Instagram Basic Profile API: pricing, parameters and code examples

`instagram/basic-profile` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.001 per call · **Modes:** sync

Fetch an Instagram account's core public profile fields (followers, posts, bio, verification) by user id.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.001**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/basic-profile", "userId": "314216"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/basic-profile', {'userId': '314216'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/basic-profile", {
  "userId": "314216"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/basic-profile", sandbase.Params{
	"userId": "314216",
})
```

Same call via the path form: `POST /v1/api/instagram/basic-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | Instagram numeric user id (the account's internal all-digits id, e.g. 314216), NOT the @handle or profile URL. Passing a handle here returns no profile.  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `posts`, and it is served only by a source that returns every one of…  |

## Details

Returns the core public profile fields of an Instagram account, such as handle, display name, bio, follower count and verification status. It needs the account's numeric Instagram user id, not the @handle.

### Use cases

- Check the follower and following counts of an account when you already know its numeric user id.
- Confirm that an account is verified and whether it is marked as a business or private account.
- Pull the bio, bio links and avatar URL to show a profile card in your own app.
- Map a stored numeric user id back to its current `handle` and `displayName`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/basic-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "314216"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | Instagram numeric user id (the account's internal all-digits id, e.g. 314216), NOT the @handle or profile URL. Passing a handle here returns no profile. |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `posts`, and it is served only by a source that returns every one of t |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "avatarUrl": "https://scontent-ams2-1.cdninstagram.com/v/t51.82787-19/825351924_18634676146058…",
    "bio": "I build stuff",
    "bioLinks": [
      {
        "title": "",
        "url": "http://muse.ai/join"
      }
    ],
    "displayName": "Mark Zuckerberg",
    "externalUrl": "http://muse.ai/join",
    "followers": 17348743,
    "following": 628,
    "handle": "zuck",
    "isBusiness": false,
    "posts": null,
    "private": false,
    "userId": "314216"
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.handle` | The account's Instagram username, without the @ sign. |
| `data.displayName` | The name shown on the profile. |
| `data.userId` | The numeric Instagram user id, returned as a string. It matches the id you sent. |
| `data.followers / data.following` | Number of accounts that follow this profile, and number of accounts this profile follows. |
| `data.bio` | The profile biography text. |
| `data.bioLinks[].url / data.bioLinks[].title` | Links listed in the bio, each with a URL and a title. The title can be an empty string. |
| `data.externalUrl` | The main external link on the profile. |
| `data.verified / data.private / data.isBusiness` | Boolean flags for verification, private account status and business account status. |
| `data.posts` | Post count for the account. It can be `null` when the serving source does not return it. |
| `data.avatarUrl` | URL of the profile picture image. |
| `found` | `true` when the profile was found. A lookup that finds nothing returns `false`. |

### Notes

- `userId` must be the all-digits id. A handle returns no profile, so use [Instagram User Info by Username](/apis/instagram/v1/user-info-by-username) to look up a handle first.
- `posts` came back as `null` in this response. Pass `requireFields: ["posts"]` to be served only by a source that returns it. This can raise the price.
- `requireFields` accepts `bioLinks`, `isBusiness`, `posts`, `title` and `url`.
- For a larger profile payload, try [Instagram Profile](/apis/instagram/profile).

### Pricing

Billed at the actual cost of each call, about $0.001 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/basic-profile.json`](../../../catalog/models/instagram/basic-profile.json) · Store page: https://www.sandbase.ai/model/instagram/basic-profile

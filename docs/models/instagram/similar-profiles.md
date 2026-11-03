# Instagram Similar Profiles API: pricing, parameters and code examples

`instagram/similar-profiles` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00175 per call · **Modes:** sync

List the accounts Instagram recommends as similar to a public profile, with each account's handle, display name, verified flag and avatar.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00175**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/similar-profiles", "handle": "nasa"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/similar-profiles', {'handle': 'nasa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/similar-profiles", {
  "handle": "nasa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/similar-profiles", sandbase.Params{
	"handle": "nasa",
})
```

Same call via the path form: `POST /v1/api/instagram/similar-profiles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | Instagram username without the leading @.  |

## Details

This API returns the accounts Instagram recommends as similar to a public profile. Send the `handle` of the profile, without the leading @. Each result has the account's username, display name, user ID, verified flag and avatar URL.

### Use cases

- Build a list of competitor or peer accounts for a brand by starting from one known handle.
- Find related creators in the same niche for influencer outreach.
- Expand a set of accounts to monitor by following the recommended profiles of each seed account.
- Check which verified accounts Instagram groups with a given profile.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/similar-profiles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"handle": "nasa"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | Instagram username without the leading @. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "profiles": [
      {
        "avatarUrl": "https://scontent-phl2-1.cdninstagram.com/v/t51.2885-19/265195576_626729471802765…",
        "displayName": "HISTORY",
        "private": null,
        "userId": "1385204914",
        "username": "history",
        "verified": true
      }
    ]
  },
  "found": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.profiles[]` | List of accounts Instagram recommends as similar to the requested profile. |
| `data.profiles[].username` | Handle of the recommended account. Use it as `handle` in other Instagram APIs. |
| `data.profiles[].displayName` | Public display name of the recommended account. |
| `data.profiles[].userId` | Numeric Instagram ID of the account, returned as a string. |
| `data.profiles[].verified` | `true` if the account has the verified badge, `false` if not. |
| `data.profiles[].avatarUrl` | Link to the account's profile picture. The sample URLs point to a 150x150 image. |
| `data.profiles[].private` | Whether the account is private. The sample response returns `null` for every account, so treat it as unknown. |
| `found` | `true` when the lookup returned a result. A lookup that finds nothing returns `false`. |

### Notes

- The `handle` is the username in the profile URL, for example `nasa` for instagram.com/nasa.
- The request takes only `handle`. There are no pagination parameters.
- To get full details for a recommended account, pass its `username` to [Instagram Profile](/apis/instagram/profile) or [Instagram User Profile](/apis/instagram/user-detail).
- To use the numeric `userId` instead, call [Instagram User Profile by ID](/apis/instagram/v1/user-info-by-id).

### Pricing

Billed at the actual cost of each call, about $0.00175 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/instagram/similar-profiles.json`](../../../catalog/models/instagram/similar-profiles.json) · Store page: https://www.sandbase.ai/model/instagram/similar-profiles

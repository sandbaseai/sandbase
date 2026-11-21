# Instagram User ID Lookup API: pricing, parameters and code examples

`instagram/v3/user-id-by-username` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Convert an Instagram username into its numeric user ID, the internal identifier needed by most Instagram profile, posts and followers APIs.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-id-by-username", "username": "nima.vahed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-id-by-username', {'username': 'nima.vahed'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-id-by-username", {
  "username": "nima.vahed"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-id-by-username", sandbase.Params{
	"username": "nima.vahed",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-id-by-username` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Instagram username  |

## Details

Look up the numeric user ID (`pk`) of an Instagram account from its username. The ID stays the same when the account changes its username, so it is the safer key to store.

### Use cases

- Store a stable key for each account you track, so your records survive a rename.
- Get the ID that [Similar users](/apis/instagram/v3/similar-users) and [User brief](/apis/instagram/v3/user-brief) require.
- Match accounts across datasets that store IDs, such as exports or third-party tools.

### Username or user ID: which to use

| | Username | User ID |
|---|---|---|
| Example | `nasa` | `528817151` |
| Changes when the account renames | Yes | No |
| Where you find it | Profile URL, bio, mentions | Not shown on the profile; returned by APIs |
| Accepted by | [User profile](/apis/instagram/v3/user-profile), [User posts](/apis/instagram/v3/user-posts), [User reels](/apis/instagram/v3/user-reels), followers and following | [Similar users](/apis/instagram/v3/similar-users), [User brief](/apis/instagram/v3/user-brief) |

Use the username for one-off requests, since most Instagram APIs here accept it directly. Save the user ID next to it when you track accounts over time. If a request by username starts failing, look the stored ID up with [Instagram ID to Username](/apis/instagram/v3/user-id-to-username) to find the new name. The [Instagram ID lookup guide](/guides/instagram-id-lookup) covers both directions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-id-by-username" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "nasa"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "user_id": "528817151"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `user_id` | Numeric user ID as a string. |

### Notes

- Pass the username without `@`. Usernames that do not exist fail and are not charged.
- To go the other way, use [Instagram ID to Username](/apis/instagram/v3/user-id-to-username).

### Pricing

$0.008 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram ID to Username](/apis/instagram/v3/user-id-to-username): find the current username of a stored user ID.
- [User profile](/apis/instagram/v3/user-profile): profile details, follower counts and bio by username.
- [Similar users](/apis/instagram/v3/similar-users): accounts similar to a given user ID.

---
Machine-readable: [`catalog/models/instagram/v3/user-id-by-username.json`](../../../../catalog/models/instagram/v3/user-id-by-username.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-id-by-username

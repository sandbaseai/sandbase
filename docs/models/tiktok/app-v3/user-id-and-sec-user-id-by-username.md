# TikTok User ID by Username API: pricing, parameters and code examples

`tiktok/app-v3/user-id-and-sec-user-id-by-username` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the user_id and sec_user_id associated with a specific TikTok username. Provide a profile username to resolve account identifiers.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-id-and-sec-user-id-by-username", "username": "tiktok"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-id-and-sec-user-id-by-username', {'username': 'tiktok'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-id-and-sec-user-id-by-username", {
  "username": "tiktok"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-id-and-sec-user-id-by-username", sandbase.Params{
	"username": "tiktok",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-id-and-sec-user-id-by-username` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Username  |

## Details

Returns the `user_id` and `sec_user_id` for a TikTok account. You send the profile `username` and get both identifiers back in a flat JSON object.

### Use cases

- Convert a TikTok handle into the numeric `user_id` for storage in a database.
- Get the `sec_user_id` needed to call profile and video list endpoints for an account.
- Keep a stable identifier for a creator in case you track them over time.
- Check that a handle resolves to a real account before you run other lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-id-and-sec-user-id-by-username" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "tiktok"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Username |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "sec_user_id": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
  "user_id": "107955"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `user_id` | Numeric account ID for the username, returned as a string. |
| `sec_user_id` | Long encoded account ID for the same user. Other TikTok user endpoints take this value as input. |

### Notes

- Pass the handle in `username` without the `@` sign, for example `tiktok`.
- Use the returned `sec_user_id` in [TikTok User Profile Details](/apis/tiktok/app-v3/user-profile) or [TikTok User Videos (App V3)](/apis/tiktok/app-v3/user-post-videos) to get profile data and posts.
- To find the country of an account from its handle, call [TikTok User Country by Username](/apis/tiktok/app-v3/user-country-by-username).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-id-and-sec-user-id-by-username.json`](../../../../catalog/models/tiktok/app-v3/user-id-and-sec-user-id-by-username.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-id-and-sec-user-id-by-username

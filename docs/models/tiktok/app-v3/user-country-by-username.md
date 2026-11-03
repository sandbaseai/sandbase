# TikTok User Country by Username API: pricing, parameters and code examples

`tiktok/app-v3/user-country-by-username` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the registered country code, user IDs, and username modification timestamp for a specified TikTok profile using their username.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/user-country-by-username", "username": "tiktok"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/user-country-by-username', {'username': 'tiktok'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/user-country-by-username", {
  "username": "tiktok"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/user-country-by-username", sandbase.Params{
	"username": "tiktok",
})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/user-country-by-username` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `username` | string | yes | Username, which can be obtained from the user's homepage link, for example: https://www.tiktok.com/@tiktok, the username is tiktok.  |

## Details

Returns the registered country code, the numeric and secure user IDs, and a username modification timestamp for a TikTok account. It needs one input: the account `username`, without the @ sign.

### Use cases

- Check which country a creator account is registered in before you plan a regional campaign.
- Filter a list of TikTok handles by registered country.
- Convert a `username` into `user_id` and `sec_user_id` for later API calls.
- Check when an account last changed its username.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/user-country-by-username" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "tiktok"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Username, which can be obtained from the user's homepage link, for example: https://www.tiktok.com/@tiktok, the username is tiktok. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "api_version": "v1",
  "country": "US",
  "sec_user_id": "MS4wLjABAAAAv7iSuuXDJGDvJkmH_vz1qkDZYo1apxgzaxdBSeIuPiM",
  "user_id": 107955,
  "username": "tiktok",
  "username_modify_time": 1793691840
}
```

### Response fields

| Field | Meaning |
|---|---|
| `country` | Two-letter country code for the account, such as `US`. |
| `user_id` | Numeric ID of the TikTok user. |
| `sec_user_id` | Secure user ID string for the same account. Other TikTok endpoints accept it in place of the username. |
| `username` | The username that was looked up, returned as the account currently holds it. |
| `username_modify_time` | Unix timestamp in seconds for the account's username modification. |
| `api_version` | Version label of the response format, `v1` in this response. |

### Notes

- Take `username` from the profile URL. In https://www.tiktok.com/@tiktok, the value is `tiktok`.
- To get more ID details for a username, call [TikTok User ID by Username](/apis/tiktok/app-v3/user-id-and-sec-user-id-by-username).
- For profile details such as bio and counts, call [TikTok User Profile Details](/apis/tiktok/app-v3/user-profile).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/user-country-by-username.json`](../../../../catalog/models/tiktok/app-v3/user-country-by-username.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/user-country-by-username

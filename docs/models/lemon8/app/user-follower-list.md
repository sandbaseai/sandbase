# Lemon8 User Followers List API: pricing, parameters and code examples

`lemon8/app/user-follower-list` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the followers list for a specified Lemon8 user. Accepts a user identifier and an optional pagination cursor to browse through followers.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/user-follower-list", "user_id": "7428056850216862763"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/user-follower-list', {'user_id': '7428056850216862763'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/user-follower-list", {
  "user_id": "7428056850216862763"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/user-follower-list", sandbase.Params{
	"user_id": "7428056850216862763",
})
```

Same call via the path form: `POST /v1/api/lemon8/app/user-follower-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the cursor returned by the last request is used for subsequent requests.  |
| `user_id` | string | yes | User ID, can be obtained from the interface `/lemon8/app/get_user_id`  |

## Details

Returns a page of followers for a Lemon8 account. Each follower entry has a name, handle, avatar URL and profile link. The only required input is the account's `user_id`.

### Use cases

- Build a list of accounts that follow a Lemon8 creator for audience research.
- Collect follower handles and profile links to review who engages with a brand account.
- Page through a creator's followers and store their `user_id` values for later profile lookups.
- Compare follower lists of several creators to find shared followers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/user-follower-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "7428056850216862763"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User ID, can be obtained from the interface `/lemon8/app/get_user_id` |
| `cursor` | string | No | Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the cursor returned by the last request is used for subsequent requests. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "cursor": 20,
    "data": [
      {
        "description": "",
        "hide_follow_button": 0,
        "icon_url": "https://p16-lemon8-cross-sign.tiktokcdn-us.com/user-avatar-alisg/d322cea4d51ddf0…",
        "is_canceled": false,
        "is_follow_apply": 0,
        "is_followed": 0,
        "is_following": 0,
        "name": "Matt t💔🇨🇦",
        "privacy_status": 1,
        "relation": 2,
        "share_url": "https://www.lemon8-app.com/@matttabak2018",
        "user_auth_info": "{\"auth_type\":0,\"show_auth_symbol\":false}"
      }
    ],
    "has_more": true
  },
  "error_code": 0,
  "error_message": "",
  "message": "success",
  "server_time": "1793691395.6"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.data[]` | List of follower accounts on the current page. |
| `data.data[].user_id` | Numeric ID of the follower. Use it to look up that account in other Lemon8 APIs. |
| `data.data[].name` | Display name of the follower. It can contain emoji. |
| `data.data[].user_unique_name` | Unique handle of the follower. It matches the part after `@` in `share_url`. |
| `data.data[].share_url` | Link to the follower's public Lemon8 profile. |
| `data.data[].icon_url` | Avatar image URL of the follower. |
| `data.data[].description` | Profile bio of the follower. It is an empty string when none is set. |
| `data.data[].is_following / data.data[].is_followed` | Flags for the follow relationship between the follower and the requesting context. Values are `0` or `1`. |
| `data.cursor` | Cursor value for the next page. Pass it as `cursor` in the next request. |
| `data.has_more` | `true` when more followers are available after this page. |

### Notes

- Get `user_id` from [Lemon8 User ID from Share Link](/apis/lemon8/app/user-id).
- Leave `cursor` empty on the first call. For later pages, send the `data.cursor` value from the last response and stop when `data.has_more` is `false`.
- `user_id` values in the response are numbers, while the request takes `user_id` as a string.
- To see the accounts a user follows instead, call [Lemon8 User Following List](/apis/lemon8/app/user-following-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Lemon8 Discover Page Banners](/apis/lemon8/app/discover-banners): Returns the current promotional and featured banners displayed on the Lemon8 discover page.
- [Lemon8 Discover Page Content](/apis/lemon8/app/discover-tab): Returns the main content featured on the Lemon8 discover tab.
- [Lemon8 Discover Editor Picks](/apis/lemon8/app/discover-tab-information-tabs): Returns the Editor's Picks and discover tab information from the Lemon8 mobile app.

---
Machine-readable: [`catalog/models/lemon8/app/user-follower-list.json`](../../../../catalog/models/lemon8/app/user-follower-list.json) · Store page: https://www.sandbase.ai/model/lemon8/app/user-follower-list

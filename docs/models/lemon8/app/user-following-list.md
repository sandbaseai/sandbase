# Lemon8 User Following List API: pricing, parameters and code examples

`lemon8/app/user-following-list` · data API · Lemon8 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the list of accounts followed by a specified Lemon8 user. Accepts a user identifier and supports cursor-based pagination for browsing results.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "lemon8/app/user-following-list", "user_id": "7428056850216862763"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('lemon8/app/user-following-list', {'user_id': '7428056850216862763'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("lemon8/app/user-following-list", {
  "user_id": "7428056850216862763"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "lemon8/app/user-following-list", sandbase.Params{
	"user_id": "7428056850216862763",
})
```

Same call via the path form: `POST /v1/api/lemon8/app/user-following-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination parameter, can be obtained from the return result of the last request. It is empty for the first request, and the cursor returned by the last request is used for subsequent requests.  |
| `user_id` | string | yes | User ID, can be obtained from the interface `/lemon8/app/get_user_id`  |

## Details

Returns the accounts that a Lemon8 user follows. Each entry has the account's name, handle, avatar, and profile link. The API needs the numeric `user_id` of the user whose following list you want.

### Use cases

- Check which creators a specific Lemon8 account follows.
- Build a graph of connections between Lemon8 accounts.
- Collect handles and profile links of followed accounts for audience research.
- Page through a long following list to export it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/lemon8/app/user-following-list" \
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
    "cursor": 30,
    "data": [
      {
        "description": "",
        "hide_follow_button": 0,
        "icon_url": "https://p16-lemon8-cross-sign.tiktokcdn-us.com/tos-useast5-i-pyavlv3z7u-tx/deb33…",
        "is_canceled": false,
        "is_follow_apply": 0,
        "is_followed": 0,
        "is_following": 0,
        "name": "Anna Kate",
        "privacy_status": 1,
        "share_url": "https://www.lemon8-app.com/@anna.kate832",
        "user_auth_info": "{\"auth_type\":0,\"show_auth_symbol\":false}",
        "user_id": 7415435863247127594
      }
    ],
    "has_more": true
  },
  "error_code": 0,
  "error_message": "",
  "message": "success",
  "server_time": "1793691395.56"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.data[].user_id` | Numeric ID of the followed account. Use it in other Lemon8 calls that take a `user_id`. |
| `data.data[].name` | Display name of the followed account. It can contain emoji and special characters. |
| `data.data[].user_unique_name` | Unique handle of the account. It matches the part after `@` in `share_url`. |
| `data.data[].share_url` | Public Lemon8 profile link of the followed account. |
| `data.data[].icon_url` | Avatar image URL, sized 150x150 in the sample. |
| `data.data[].description` | Profile description text. It is an empty string for the sample accounts. |
| `data.data[].is_following / data.data[].is_followed` | Follow-state flags for the account, returned as `0` or `1` numbers. Both are `0` in the sample. |
| `data.data[].user_auth_info` | JSON string with verification details, such as `auth_type` and `show_auth_symbol`. |
| `data.cursor` | Cursor value for the next page. The sample returns `30`. |
| `data.has_more` | `true` when more accounts remain after this page. |

### Notes

- Get `user_id` from [Lemon8 User ID from Share Link](/apis/lemon8/app/user-id) if you only have a profile share link.
- Leave `cursor` empty on the first call. For the next page, pass the value of `data.cursor` as `cursor`, and stop when `data.has_more` is `false`.
- `user_id` in each list item is a number, while the request parameter `user_id` is a string.
- To see who follows a user instead, call [Lemon8 User Followers List](/apis/lemon8/app/user-follower-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Lemon8 Discover Page Banners](/apis/lemon8/app/discover-banners): Returns the current promotional and featured banners displayed on the Lemon8 discover page.
- [Lemon8 Discover Page Content](/apis/lemon8/app/discover-tab): Returns the main content featured on the Lemon8 discover tab.
- [Lemon8 Discover Editor Picks](/apis/lemon8/app/discover-tab-information-tabs): Returns the Editor's Picks and discover tab information from the Lemon8 mobile app.

---
Machine-readable: [`catalog/models/lemon8/app/user-following-list.json`](../../../../catalog/models/lemon8/app/user-following-list.json) · Store page: https://www.sandbase.ai/model/lemon8/app/user-following-list

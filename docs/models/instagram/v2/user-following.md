# Instagram User Following API: pricing, parameters and code examples

`instagram/v2/user-following` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns the list of accounts that a specified Instagram user follows. Queries can be made using an account username or user ID, with support for pagination tokens.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/user-following", "user_id": "18527", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/user-following', {'user_id': '18527', 'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/user-following", {
  "user_id": "18527",
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/user-following", sandbase.Params{
	"user_id": "18527",
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/user-following` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string |  | User ID (either username or user_id required)  |
| `username` | string |  | Username (either username or user_id required)  |
| `pagination_token` | string |  | Pagination token from previous response  |

## Details

Returns a page of the accounts that an Instagram user follows. Send either a `username` or a `user_id`. Each item includes the followed account's ID, username, display name, and verification and privacy flags.

### Use cases

- Audit which accounts a brand or creator profile follows.
- Map follow networks by collecting the accounts followed by several related profiles.
- Check which followed accounts are verified or private before outreach.
- Compare saved following lists from different dates to spot new follows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/user-following" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram", "user_id": "18527"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `pagination_token` | string | No | Pagination token from previous response |
| `user_id` | string | No | User ID (either username or user_id required) |
| `username` | string | No | Username (either username or user_id required) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "count": 47,
    "items": [
      {
        "account_badges": [],
        "fbid_v2": "17841428227230889",
        "full_name": "Meta",
        "has_anonymous_profile_picture": false,
        "id": "28247116907",
        "is_favorite": false,
        "is_private": false,
        "is_verified": true,
        "latest_reel_media": 0,
        "profile_pic_id": "3994229046456396292",
        "profile_pic_url": "https://scontent-cph2-1.cdninstagram.com/v/t51.82787-19/825322335_18128714404940…",
        "third_party_downloads_enabled": 1
      }
    ],
    "total": 163
  },
  "pagination_token": "Ik1ICwEp…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].username` | Handle of the followed account. |
| `data.items[].full_name` | Display name of the followed account. |
| `data.items[].id` | ID of the followed account. Pass it as `user_id` in other Instagram calls. |
| `data.items[].is_verified` | `true` when the followed account is verified. |
| `data.items[].is_private` | `true` when the followed account is private. |
| `data.items[].profile_pic_url` | Link to a small profile picture of the followed account. |
| `data.items[].latest_reel_media` | Numeric value for the latest reel media of the account. `0` appears when there is none. Nonzero values look like Unix timestamps. |
| `data.count / data.total` | `count` is a number returned with the list and `total` is a larger number. Their exact meaning is not documented, so do not rely on them as page size or full following count without checking. |
| `pagination_token` | Token that you send back as `pagination_token` to request the next page. |

### Notes

- Send either `username` or `user_id`. You do not need both.
- To get the next page, pass the `pagination_token` from the previous response with the same user.
- Call [Instagram User Profile](/apis/instagram/v2/user-info) to look up a `user_id` from a username.
- To see who follows the account instead, use [Instagram User Followers (V2)](/apis/instagram/v2/user-followers).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/user-following.json`](../../../../catalog/models/instagram/v2/user-following.json) · Store page: https://www.sandbase.ai/model/instagram/v2/user-following

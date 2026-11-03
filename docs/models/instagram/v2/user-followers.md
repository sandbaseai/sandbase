# Instagram User Followers (V2) API: pricing, parameters and code examples

`instagram/v2/user-followers` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns a list of followers for a specified Instagram account. Supports looking up accounts by identifier or handle, with pagination token support for retrieving full follower lists.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v2/user-followers", "user_id": "18527", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v2/user-followers', {'user_id': '18527', 'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v2/user-followers", {
  "user_id": "18527",
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v2/user-followers", sandbase.Params{
	"user_id": "18527",
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v2/user-followers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string |  | User ID (either username or user_id required)  |
| `username` | string |  | Username (either username or user_id required)  |
| `pagination_token` | string |  | Pagination token from previous response  |

## Details

Returns a page of followers for an Instagram account. Each item holds the follower's username, display name, ID, and privacy and verification flags. You pass either `username` or `user_id`.

### Use cases

- Sample the accounts that follow a brand profile to check what kind of audience it has.
- Flag followers with `is_verified` set to true when you look for notable accounts that follow a profile.
- Spot likely empty or low-quality followers by checking `has_anonymous_profile_picture` and blank `full_name` values.
- Collect follower `username` values and pass them to a profile lookup for deeper analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v2/user-followers" \
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
    "count": 58,
    "items": [
      {
        "account_badges": [],
        "fbid_v2": "17841416077777377",
        "full_name": "Travel with Das",
        "has_anonymous_profile_picture": false,
        "id": "16059023925",
        "is_private": false,
        "is_verified": false,
        "latest_story_ts": 0,
        "profile_pic_id": "4019937364302932887",
        "profile_pic_url": "https://scontent-bru2-1.cdninstagram.com/v/t51.82787-19/878274921_18149447857535…",
        "third_party_downloads_enabled": 1,
        "username": "das_tales10"
      }
    ],
    "total": 686358280
  },
  "pagination_token": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].username` | The follower's Instagram handle. |
| `data.items[].id` | The follower's numeric user ID, returned as a string. |
| `data.items[].full_name` | The display name the follower set. It can be an empty string. |
| `data.items[].is_private / data.items[].is_verified` | Whether the follower's account is private, and whether it is verified. |
| `data.items[].has_anonymous_profile_picture` | True when the follower uses the default blank profile picture. |
| `data.items[].profile_pic_url` | URL of the follower's profile picture. |
| `data.items[].latest_story_ts` | Timestamp of the follower's latest story. The value `0` appears when no story time is set. |
| `data.items[].fbid_v2` | A second ID string for the follower account. |
| `data.count` | Number of follower items returned in this response. |
| `data.total` | Total follower count reported for the requested account. |

### Notes

- Send `username` or `user_id`. The example uses `instagram` and `18527`.
- To get the next page, pass the response's `pagination_token` as the `pagination_token` parameter. It is `null` in this response.
- Use [Instagram User Profile](/apis/instagram/v2/user-info) to get details for a follower, and [Instagram User Following](/apis/instagram/v2/user-following) to see who an account follows.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Replies (V2)](/apis/instagram/v2/comment-replies): Retrieves a paginated list of replies to an Instagram comment using the post URL or shortcode and the target comment ID.
- [Instagram General Search (V2)](/apis/instagram/v2/general-search): Returns Instagram search results matching a specified keyword, including media items, user profiles, and engagement statistics.
- [Instagram Hashtag Posts (V2)](/apis/instagram/v2/hashtag-posts): Returns posts associated with a specific hashtag.

---
Machine-readable: [`catalog/models/instagram/v2/user-followers.json`](../../../../catalog/models/instagram/v2/user-followers.json) · Store page: https://www.sandbase.ai/model/instagram/v2/user-followers

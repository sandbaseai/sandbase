# Instagram User Followers (V3) API: pricing, parameters and code examples

`instagram/v3/user-followers` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns a list of followers for a specified Instagram account. Supports pagination cursors and limits up to 100 users per request.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-followers", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-followers', {'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-followers", {
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-followers", sandbase.Params{
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-followers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number of users to fetch per request (default 12, max 100) range 1–100 |
| `max_id` | string |  | Pagination cursor, omit for first request, get from previous response `data.next_max_id`  |
| `username` | string | yes | Instagram username (required)  |

## Details

Returns a list of followers for an Instagram account. Each user entry has the username, full name, IDs, profile picture URL and privacy and verification flags. The only required input is `username`.

### Use cases

- Build a list of follower usernames and IDs for an account to use in network analysis.
- Check which followers have private accounts by reading `is_private` on each user.
- Spot verified accounts among the followers of a brand or creator with `is_verified`.
- Page through a large follower list in batches of up to 100 users.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-followers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"username": "instagram"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `username` | string | Yes | Instagram username (required) |
| `count` | integer | No | Number of users to fetch per request (default 12, max 100) |
| `max_id` | string | No | Pagination cursor, omit for first request, get from previous response `data.next_max_id` |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "_rid": "17ed67fb7dcf8",
  "big_list": false,
  "follow_ranking_token": "2cac2e8d…",
  "has_more": false,
  "page_size": 50,
  "should_limit_list_of_followers": true,
  "should_limit_list_of_followings": false,
  "show_spam_follow_request_tab": false,
  "status": "ok",
  "use_clickable_see_more": false,
  "users": [
    {
      "account_badges": [],
      "fbid_v2": "17841428736948250",
      "full_name": "¥;k@&",
      "has_anonymous_profile_picture": false,
      "id": "28626005898",
      "is_private": true,
      "is_verified": false,
      "latest_reel_media": 0,
      "pk": "28626005898",
      "pk_id": "28626005898",
      "profile_pic_id": "4018678605823597314_28626005898",
      "profile_pic_url": "https://scontent-lax3-2.cdninstagram.com/v/t51.82787-19/863891295_18120783028957…"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `users[]` | List of follower accounts returned for this request. |
| `users[].username / users[].full_name` | The follower's Instagram handle and display name. |
| `users[].pk / users[].id / users[].pk_id / users[].strong_id__` | The follower's numeric user ID as a string. All four carry the same value in this response. |
| `users[].is_private / users[].is_verified` | Whether the follower's account is private and whether it is verified. |
| `users[].profile_pic_url` | Link to the follower's profile picture. Profile picture links are long and include query parameters. |
| `users[].profile_pic_id` | ID of the profile picture. It ends with the follower's user ID after an underscore. |
| `users[].latest_reel_media` | Number that is `0` when no reel media is set and a large integer otherwise. The value looks like a Unix timestamp in seconds. |
| `has_more` | Whether more results remain after this page. It is `false` in this response. |
| `page_size` | Page size value reported with the response (`50` here). |
| `status` | Request status string. It is `ok` on success. |

### Notes

- Set `count` between 1 and 100 to change how many users come back per request.
- To get the next page, pass the cursor from the previous response as `max_id`. Omit `max_id` on the first request.
- In the sample response, `has_more` is `false` and no `next_max_id` key appears, so the list ended after one page.
- To get the account's own details first, call [Instagram User Profile (V3)](/apis/instagram/v3/user-profile). For the reverse list, call [Instagram User Following List](/apis/instagram/v3/user-following).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-followers.json`](../../../../catalog/models/instagram/v3/user-followers.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-followers

# Instagram User Following List API: pricing, parameters and code examples

`instagram/v3/user-following` · data API · Instagram · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.008 per call (free daily quota) · **Modes:** sync

Returns a paginated list of accounts followed by a specified Instagram user. Supports filtering by username and custom result counts up to 100 users per request.

## Pricing

- **$0.008 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "instagram/v3/user-following", "username": "instagram"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('instagram/v3/user-following', {'username': 'instagram'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("instagram/v3/user-following", {
  "username": "instagram"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "instagram/v3/user-following", sandbase.Params{
	"username": "instagram",
})
```

Same call via the path form: `POST /v1/api/instagram/v3/user-following` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number of users to fetch per request (default 12, max 100) range 1–100 |
| `max_id` | string |  | Pagination cursor, omit for first request, get from previous response `data.next_max_id`  |
| `username` | string | yes | Instagram username (required)  |

## Details

Returns a page of the accounts that an Instagram user follows. You send the account's `username`, and each result includes the followed account's name, ID, verification flag and profile picture URL.

### Use cases

- Map which brands, creators and public figures an influencer follows.
- Compare the following lists of two accounts to find shared interests.
- Collect the usernames and IDs of followed accounts to feed into profile lookups.
- Check whether followed accounts are private or verified when you build an outreach list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/instagram/v3/user-following" \
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
  "_rid": "1db6b1b4493f4",
  "big_list": true,
  "follow_ranking_token": "fefb50c8…",
  "has_more": true,
  "hidden_following_account_count": 0,
  "next_max_id": "12",
  "page_size": 12,
  "should_limit_list_of_followers": false,
  "should_limit_list_of_followings": false,
  "status": "ok",
  "use_clickable_see_more": false,
  "users": [
    {
      "account_badges": [],
      "fbid_v2": "17841457643088327",
      "full_name": "BOYNEXTDOOR",
      "has_anonymous_profile_picture": false,
      "id": "57666617436",
      "is_favorite": false,
      "is_private": false,
      "is_verified": true,
      "latest_reel_media": 1793678764,
      "pk": "57666617436",
      "pk_id": "57666617436",
      "profile_pic_id": "3980226050504551807_57666617436"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `users[]` | List of followed accounts on this page. |
| `users[].username` | Instagram handle of the followed account. |
| `users[].full_name` | Display name of the followed account. |
| `users[].id / users[].pk / users[].pk_id` | Numeric ID of the followed account, returned as a string. All three hold the same value in the sample. |
| `users[].is_verified` | `true` when the followed account is verified. |
| `users[].is_private` | `true` when the followed account is private. |
| `users[].profile_pic_url` | Link to a small profile picture of the followed account. |
| `users[].latest_reel_media` | Number that looks like a Unix timestamp for the latest story reel. The value is `0` when the sample shows no reel. |
| `has_more` | `true` when more accounts are available after this page. |
| `next_max_id` | Cursor to pass as `max_id` to get the next page. |
| `page_size` | Number of users requested for this page. The sample shows `12`. |

### Notes

- Pass `next_max_id` from the response as `max_id` in the next request. Omit `max_id` on the first call.
- Set `count` from 1 to 100 to change the page size. The default is 12.
- Stop paging when `has_more` is `false`.
- To get full details for a followed account, call [Instagram User Profile (V3)](/apis/instagram/v3/user-profile). To see who follows an account, call [Instagram User Followers (V3)](/apis/instagram/v3/user-followers).

### Pricing

$0.008 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Instagram Comment Bulk Translation](/apis/instagram/v3/bulk-translate-comments): Returns bulk translations for multiple Instagram comments using a list of comment identifiers.
- [Instagram Comment Replies (V3)](/apis/instagram/v3/comment-replies): Returns child comment replies for a specific Instagram comment using the post media ID and parent comment ID.
- [Instagram Explore Feed](/apis/instagram/v3/explore): Returns curated sectional items from the Instagram explore feed, including layout formats and feed types.

---
Machine-readable: [`catalog/models/instagram/v3/user-following.json`](../../../../catalog/models/instagram/v3/user-following.json) · Store page: https://www.sandbase.ai/model/instagram/v3/user-following

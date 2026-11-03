# X (Twitter) Verified Followers API: pricing, parameters and code examples

`twitter/verified-followers` · data API · X (Twitter) · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.006 per call · **Modes:** sync

Verified (blue check) followers of a user by numeric user ID, with profile details and cursor pagination.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.006**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/verified-followers", "user_id": "11348282"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/verified-followers', {'user_id': '11348282'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/verified-followers", {
  "user_id": "11348282"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/verified-followers", sandbase.Params{
	"user_id": "11348282",
})
```

Same call via the path form: `POST /v1/api/twitter/verified-followers` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | The cursor to paginate through the results. First page is empty.  |
| `user_id` | string | yes | User ID of the user.  |

## Details

Returns a page of verified (blue check) followers for an X (Twitter) account. You pass the numeric `user_id` of the account, and each follower comes back with profile details and activity counts.

### Use cases

- List the verified accounts that follow a brand or creator to see who with a blue check engages with it.
- Find follower accounts with a large `followers_count` to build an outreach or partnership list.
- Export verified followers page by page to track which verified accounts join over time.
- Check follower bios and locations to see what kind of accounts follow a crypto or media account.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/verified-followers" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "11348282"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User ID of the user. |
| `cursor` | string | No | The cursor to paginate through the results. First page is empty. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "followers": [
    {
      "can_dm": false,
      "created_at": "Thu Feb 25 16:23:17 +0000 2021",
      "description": "chasing pumps. don´t follow. \nCrypto since 2018",
      "email": null,
      "favourites_count": 1207,
      "followers_count": 71,
      "following_count": 182,
      "id": "1364974219168264192",
      "location": "Wien, Österreich",
      "media_tweets_count": 17,
      "name": "lluukaz",
      "profile_banner_url": "https://pbs.twimg.com/profile_banners/1364974219168264192/1790020833"
    }
  ],
  "has_next_page": true,
  "msg": "success",
  "next_cursor": "1880822139011071054|2117523394499969002",
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `followers[].id` | Numeric ID of the follower account, returned as a string. Use it as `user_id` in other calls. |
| `followers[].screen_name / followers[].userName` | The follower's @handle, without the @ sign. |
| `followers[].name / followers[].description / followers[].location` | Display name, bio text and free-text location set by the follower. Bio and location can be empty. |
| `followers[].followers_count / followers[].following_count` | Number of accounts that follow this user, and number of accounts this user follows. |
| `followers[].statuses_count / followers[].media_tweets_count / followers[].favourites_count` | Counts of posts, posts with media, and likes for the follower account. |
| `followers[].created_at` | Date the follower account was created, in a format like `Thu Feb 25 16:23:17 +0000 2021`. |
| `followers[].can_dm` | Boolean flag showing whether direct messages are allowed for this follower account. |
| `followers[].profile_image_url_https / followers[].profile_banner_url` | Links to the follower's avatar and banner images. |
| `has_next_page` | `true` when more followers are available after this page. |
| `next_cursor` | Value to send as `cursor` to get the next page. |

### Notes

- `user_id` is the numeric ID of the account, such as `11348282`. Use [Twitter User Profile](/apis/twitter/user-detail) to look up an ID from a handle.
- For the first page, leave `cursor` empty. For the next page, send the `next_cursor` value as `cursor` while `has_next_page` is `true`.
- The cursor is a string with two numbers separated by `|`. Pass it back unchanged.
- To list all followers, not only verified ones, use [X / Twitter Followers](/apis/twitter/followers).

### Pricing

Billed at the actual cost of each call, about $0.006 for the request above. Failed calls are not charged.

---
Machine-readable: [`catalog/models/twitter/verified-followers.json`](../../../catalog/models/twitter/verified-followers.json) · Store page: https://www.sandbase.ai/model/twitter/verified-followers

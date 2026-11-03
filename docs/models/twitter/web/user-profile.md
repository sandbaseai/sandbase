# Twitter (X) User Profile API: pricing, parameters and code examples

`twitter/web/user-profile` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get a Twitter / X user profile by screen name or user ID: name, bio, follower and following counts, post and media counts, verification and creation date.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/user-profile"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/user-profile', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/user-profile", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/user-profile", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/twitter/web/user-profile` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `rest_id` | integer |  | User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected.  |
| `screen_name` | string |  | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk  |

## Details

Returns the public profile of a Twitter / X account: name, bio, location, website, verification status, creation date and activity counts. Send either `screen_name` (for example `NASA`) or the numeric `rest_id`.

### Use cases

- Check an account's verification type and `blue_verified` flag before you partner with it.
- Resolve a handle to its stable numeric `rest_id` for use in other calls.
- Record `sub_count` and `statuses_count` on a schedule to chart account growth.
- Pull the bio, location, website and banner image to fill a profile card.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/user-profile" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"screen_name": "NASA"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `rest_id` | integer | No | User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected. |
| `screen_name` | string | No | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "affiliates": [],
  "avatar": "https://pbs.twimg.com/profile_images/1321163587679784960/0ZxKlEKB_normal.jpg",
  "blue_verified": true,
  "business_account": {
    "affiliates_count": 85
  },
  "created_at": "Wed Dec 19 20:20:32 +0000 2007",
  "desc": "Making the seemingly impossible, possible. ✨",
  "friends": 115,
  "header_image": "https://pbs.twimg.com/profile_banners/11348282/1788992290",
  "id": "11348282",
  "location": "Pale Blue Dot",
  "media_count": 28223,
  "name": "NASA"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `rest_id / id` | Numeric user ID of the account, returned as a string. It stays the same if the handle changes. |
| `name / profile` | Display name of the account. In this response both fields hold `NASA`. |
| `desc` | Bio text of the account. |
| `sub_count` | Follower count of the account. |
| `friends` | Number of accounts this user follows. |
| `statuses_count / media_count` | Total number of posts and total number of media posts for the account. |
| `blue_verified / verification_type` | `blue_verified` is a boolean for the paid verification badge. `verification_type` gives the kind of verification, such as `Government`. |
| `created_at` | Date and time the account was created, in the format `Wed Dec 19 20:20:32 +0000 2007`. |
| `pinned_tweet_ids_str[]` | IDs of the tweets pinned to the profile, as strings. |
| `avatar / header_image / website / location` | Profile image URL, banner image URL, website link and free-text location from the profile. |

### Notes

- Send only one input. If you send `rest_id`, the API ignores `screen_name`.
- Take `screen_name` from the profile URL. For https://twitter.com/elonmusk, use `elonmusk`.
- Pass an ID from `pinned_tweet_ids_str[]` to [Twitter Tweet Detail](/apis/twitter/web/tweet-detail) to read the pinned post.
- Use [Twitter (X) User Posts](/apis/twitter/web/user-post-tweet) to list the account's posts with the `rest_id` you get here.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Twitter (X) Search](/apis/twitter/web/search-timeline): Search Twitter / X posts by keyword and get tweets with text, author, time and engagement counts (likes, retweets, replies, views).
- [Twitter (X) Trending Topics](/apis/twitter/web/trending): Get trending topics on Twitter / X by country: trend names with their category context, for the United States, Japan, India, the UK and other markets.
- [Twitter Tweet Detail](/apis/twitter/web/tweet-detail): Get a single tweet (X post) by ID: full text, author, media, and like, retweet, reply, quote, bookmark and view counts.

---
Machine-readable: [`catalog/models/twitter/web/user-profile.json`](../../../../catalog/models/twitter/web/user-profile.json) · Store page: https://www.sandbase.ai/model/twitter/web/user-profile

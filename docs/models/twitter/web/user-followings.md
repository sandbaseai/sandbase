# Twitter (X) User Followings API: pricing, parameters and code examples

`twitter/web/user-followings` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of accounts followed by a specified Twitter (X) user. Results provide follower counts, friend counts, media statistics, and profile details.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/user-followings", "screen_name": "NASA"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/user-followings', {'screen_name': 'NASA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/user-followings", {
  "screen_name": "NASA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/user-followings", sandbase.Params{
	"screen_name": "NASA",
})
```

Same call via the path form: `POST /v1/api/twitter/web/user-followings` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default is None, used for paging, obtained from the last request  |
| `screen_name` | string | yes | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk  |

## Details

Returns a page of the accounts that a Twitter (X) user follows. It needs the `screen_name` of that user, such as `NASA`. Each account comes with its profile details and activity counts.

### Use cases

- Map which accounts an organization or person follows to study its interests and partners.
- Build a list of followed accounts and sort them by `followers_count` to find the most visible ones.
- Collect `user_id` values of followed accounts to look up their full profiles in bulk.
- Check the `website` and `description` of followed accounts to sort them into groups such as missions, agencies or people.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/user-followings" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"screen_name": "NASA"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `screen_name` | string | Yes | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk |
| `cursor` | string | No | Cursor, default is None, used for paging, obtained from the last request |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "following": [
    {
      "created_at": "Thu Mar 06 20:15:02 +0000 2008",
      "description": "The official X account for the NASA Hubble Space Telescope, managed and operated…",
      "followers_count": 8894641,
      "friends_count": 44,
      "media_count": 3158,
      "name": "Hubble",
      "profile_image": "https://pbs.twimg.com/profile_images/3468011581/efb985f24af0a814a722457a768f3cc5…",
      "screen_name": "NASAHubble",
      "statuses_count": 8503,
      "user_id": "14091091",
      "website": "http://www.nasa.gov/mission_pages/hubble/main/index.html"
    }
  ],
  "more_users": true,
  "next_cursor": "1597662469098825850|2117523447289479099",
  "status": "ok"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `following[]` | List of accounts that the requested user follows. Each item is one account. |
| `following[].screen_name / following[].name` | The handle and the display name of the followed account. |
| `following[].user_id` | Numeric ID of the followed account, returned as a string. |
| `following[].followers_count / following[].friends_count` | Number of followers the account has and number of accounts it follows. |
| `following[].statuses_count / following[].media_count` | Number of posts the account has made and number of media items it has posted. |
| `following[].description / following[].website` | Bio text and website link from the account profile. Some items leave them out. |
| `following[].created_at` | Date and time the account was created, in a format like `Thu Mar 06 20:15:02 +0000 2008`. |
| `following[].profile_image` | URL of the account's profile picture. |
| `more_users` | `true` when more followed accounts are available on a next page. |
| `next_cursor` | Cursor value to send as `cursor` in the next request to get the next page. |

### Notes

- Take `screen_name` from the profile link. In `https://twitter.com/elonmusk` the value is `elonmusk`.
- To page through results, pass the `next_cursor` value from the last response as `cursor`. Keep going while `more_users` is `true`.
- Some followed accounts have no `description` key, so check for it before you read it.
- To see who follows the user instead, use [Twitter (X) User Followers](/apis/twitter/web/user-followers).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Twitter (X) Latest Tweet Comments](/apis/twitter/web/latest-post-comments): Returns recent replies and comment timelines for a specific post using its tweet ID, with cursor support for multi-page results.
- [Twitter (X) Tweet Comments](/apis/twitter/web/post-comments): Returns comment threads and replies under a specified tweet.
- [Twitter (X) Retweet User List](/apis/twitter/web/retweet-user-list): Returns a list of users who reposted a specific post using its tweet ID, including follower counts, media counts, and user identifiers.

---
Machine-readable: [`catalog/models/twitter/web/user-followings.json`](../../../../catalog/models/twitter/web/user-followings.json) · Store page: https://www.sandbase.ai/model/twitter/web/user-followings

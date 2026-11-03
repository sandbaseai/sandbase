# Twitter (X) Retweet User List API: pricing, parameters and code examples

`twitter/web/retweet-user-list` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of users who reposted a specific post using its tweet ID, including follower counts, media counts, and user identifiers.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/retweet-user-list", "tweet_id": "2107237881668313108"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/retweet-user-list', {'tweet_id': '2107237881668313108'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/retweet-user-list", {
  "tweet_id": "2107237881668313108"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/retweet-user-list", sandbase.Params{
	"tweet_id": "2107237881668313108",
})
```

Same call via the path form: `POST /v1/api/twitter/web/retweet-user-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default is None, used for paging, obtained from the last request  |
| `tweet_id` | string | yes | Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in https://x.com/elonmusk/status/1808168603721650364  |

## Details

Returns the accounts that reposted a given post on Twitter (X). It needs the `tweet_id` of the post and returns one profile summary per user, plus a cursor for the next page.

### Use cases

- Build a list of accounts that amplified a launch announcement or news post.
- Rank reposters by `followers_count` to find the largest accounts that shared a post.
- Spot low-activity accounts by comparing `statuses_count` and `media_count` across reposters.
- Export reposter handles and IDs for follow-up profile lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/retweet-user-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tweet_id": "2107237881668313108"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tweet_id` | string | Yes | Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in https://x.com/elonmusk/status/1808168603721650364 |
| `cursor` | string | No | Cursor, default is None, used for paging, obtained from the last request |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "next_cursor": "HBaAgIDxlZiekTQAAA==",
  "retweets": [
    {
      "description": "Ras Emilio Heru Selassie 1..2022... X Mark Everything Wynn 93 MGM Macau 2030 D.C…",
      "followers_count": 2134,
      "friends_count": 7493,
      "media_count": 284556,
      "name": "Ras Nathan C. Selassie I",
      "profile_image": null,
      "screen_name": "RasNate001",
      "statuses_count": 810547,
      "user_id": "108682255"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `retweets[]` | One entry per user who reposted the post. |
| `retweets[].user_id` | Numeric ID of the user, returned as a string. |
| `retweets[].screen_name / retweets[].name` | The user's handle and display name. |
| `retweets[].description` | The user's profile bio text. |
| `retweets[].followers_count / retweets[].friends_count` | Number of followers the user has and number of accounts the user follows. |
| `retweets[].statuses_count / retweets[].media_count` | Total posts and total media items counted for the user's account. |
| `retweets[].profile_image` | Profile image value. It is `null` in the sample response. |
| `next_cursor` | Cursor string for the next page of reposters. |

### Notes

- Take `tweet_id` from the post link. In `https://x.com/elonmusk/status/1808168603721650364`, the ID is `1808168603721650364`.
- To get the next page, send the `next_cursor` value from the last response as `cursor`, with the same `tweet_id`.
- Send `tweet_id` and `user_id` values as strings, as they appear in the response.
- To check whether one specific user reposted a post, try [Twitter Check retweet](/apis/twitter/web/check-retweet).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Twitter (X) Latest Tweet Comments](/apis/twitter/web/latest-post-comments): Returns recent replies and comment timelines for a specific post using its tweet ID, with cursor support for multi-page results.
- [Twitter (X) Tweet Comments](/apis/twitter/web/post-comments): Returns comment threads and replies under a specified tweet.
- [Twitter (X) Search](/apis/twitter/web/search-timeline): Search Twitter / X posts by keyword and get tweets with text, author, time and engagement counts (likes, retweets, replies, views).

---
Machine-readable: [`catalog/models/twitter/web/retweet-user-list.json`](../../../../catalog/models/twitter/web/retweet-user-list.json) · Store page: https://www.sandbase.ai/model/twitter/web/retweet-user-list

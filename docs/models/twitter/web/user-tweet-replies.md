# Twitter (X) User Tweet Replies API: pricing, parameters and code examples

`twitter/web/user-tweet-replies` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a timeline of replies posted by a specific Twitter user. Filter by username and paginate through responses using cursor tokens.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/user-tweet-replies", "screen_name": "example"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/user-tweet-replies', {'screen_name': 'example'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/user-tweet-replies", {
  "screen_name": "example"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/user-tweet-replies", sandbase.Params{
	"screen_name": "example",
})
```

Same call via the path form: `POST /v1/api/twitter/web/user-tweet-replies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default is None, used for paging, obtained from the last request  |
| `screen_name` | string | yes | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk  |

## Details

Returns a timeline of replies posted by one Twitter (X) user, plus that user's profile details. It needs the `screen_name` of the account, and you can pass a `cursor` to load the next page.

### Use cases

- Track how a brand account answers customers and which posts it replies under.
- Collect the replies a public figure posts to build a record of their public conversations.
- Compare reply engagement such as `favorites`, `retweets` and `views` across a user's recent replies.
- Find the parent tweet of each reply through `in_reply_to_status_id_str` and `conversation_id`, then study the threads.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/user-tweet-replies" \
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
  "next_cursor": "DAABCgABHWL0XC5__-oKAAIdPk6_s9rwAAgAAwAAAAIAAA",
  "timeline": [
    {
      "author": {
        "avatar": "https://pbs.twimg.com/profile_images/1321163587679784960/0ZxKlEKB_normal.jpg",
        "blue_verified": true,
        "favourites_count": null,
        "followers_count": null,
        "name": "NASA",
        "rest_id": "11348282",
        "screen_name": "NASA"
      },
      "bookmarks": 22,
      "conversation_id": "2117383753139925271",
      "created_at": "Mon Nov 02 22:30:00 +0000 2026",
      "entities": {
        "urls": [
          {
            "display_url": "go.nasa.gov/3V2iiWX",
            "expanded_url": "https://go.nasa.gov/3V2iiWX",
            "url": "https://t.co/aqD1x7wzRq"
          }
        ]
      },
      "favorites": 470,
      "in_reply_to_status_id_str": null,
      "lang": "en",
      "media": {
        "photo": [
          {
            "id": "2117375637358882816",
            "media_url_https": "https://pbs.twimg.com/media/HWJt7IDXsAAa7bN.jpg"
          }
        ]
      },
      "quotes": 6,
      "replies": 39,
      "retweets": 45
    }
  ],
  "user": {
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
}
```

### Response fields

| Field | Meaning |
|---|---|
| `timeline[].tweet_id` | ID of the tweet in the timeline, as a string. |
| `timeline[].text` | Text of the tweet. Long text may be cut off with an ellipsis. |
| `timeline[].created_at` | Post time as a text date, for example `Mon Nov 02 22:30:00 +0000 2026`. |
| `timeline[].in_reply_to_status_id_str` | ID of the tweet this one replies to. It is `null` when the item is not a direct reply. |
| `timeline[].conversation_id` | ID of the tweet that started the conversation thread. |
| `timeline[].favorites / timeline[].retweets / timeline[].replies / timeline[].quotes / timeline[].bookmarks` | Engagement counts for the tweet. |
| `timeline[].views` | View count for the tweet, returned as a string. |
| `timeline[].author.screen_name / timeline[].author.name / timeline[].author.rest_id` | Handle, display name and numeric ID of the account that wrote the tweet. A timeline item can come from another account in the same thread. |
| `user.rest_id / user.screen_name` | ID and handle of the account you looked up. |
| `user.sub_count / user.statuses_count / user.friends` | Counts on the profile: `sub_count` is the subscriber count, `statuses_count` is the number of posts, and `friends` is the number of accounts it follows. |
| `next_cursor` | Cursor token to send as `cursor` to get the next page. |

### Notes

- Take `screen_name` from the profile URL. For https://twitter.com/NASA, use `NASA`.
- For the next page, send the `next_cursor` value from the last response as `cursor`, with the same `screen_name`.
- The timeline can include tweets from the looked-up user and from other accounts in the same thread. Check `timeline[].author.screen_name` to tell them apart.
- To read the replies under a single tweet, use [Twitter (X) Tweet Comments](/apis/twitter/web/post-comments) with its `tweet_id`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Twitter (X) Latest Tweet Comments](/apis/twitter/web/latest-post-comments): Returns recent replies and comment timelines for a specific post using its tweet ID, with cursor support for multi-page results.
- [Twitter (X) Tweet Comments](/apis/twitter/web/post-comments): Returns comment threads and replies under a specified tweet.
- [Twitter (X) Retweet User List](/apis/twitter/web/retweet-user-list): Returns a list of users who reposted a specific post using its tweet ID, including follower counts, media counts, and user identifiers.

---
Machine-readable: [`catalog/models/twitter/web/user-tweet-replies.json`](../../../../catalog/models/twitter/web/user-tweet-replies.json) · Store page: https://www.sandbase.ai/model/twitter/web/user-tweet-replies

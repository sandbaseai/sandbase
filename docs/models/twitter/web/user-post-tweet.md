# Twitter (X) User Posts API: pricing, parameters and code examples

`twitter/web/user-post-tweet` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns posts and tweets from a specified Twitter (X) user timeline. Users can be identified by either their screen name or numeric user ID, with cursor pagination supported.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/user-post-tweet", "screen_name": "sandbaseai"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/user-post-tweet', {'screen_name': 'sandbaseai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/user-post-tweet", {
  "screen_name": "sandbaseai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/user-post-tweet", sandbase.Params{
	"screen_name": "sandbaseai",
})
```

Same call via the path form: `POST /v1/api/twitter/web/user-post-tweet` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default is None, used for paging, obtained from the JSON in the last request.  |
| `rest_id` | integer |  | User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected.  |
| `screen_name` | string |  | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk  |

## Details

Returns a page of posts from one Twitter (X) user's timeline, plus the user's profile summary and the pinned post. Send a `screen_name` or a numeric `rest_id` to pick the account.

### Use cases

- Archive an account's recent posts with their text, timestamps and engagement counts.
- Track how many views, likes and reposts each new post from a public figure gets.
- Separate original posts, reposts and quote posts in a timeline by checking `retweeted_tweet` and `quoted`.
- Page back through older posts of an account with the returned cursor values.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/user-post-tweet" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"screen_name": "elonmusk", "rest_id": 44196397}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | string | No | Cursor, default is None, used for paging, obtained from the JSON in the last request. |
| `rest_id` | integer | No | User ID, for example: 44196397, if the user ID is used, the username will be ignored, only one of them can be selected. |
| `screen_name` | string | No | Screen Name, for example: elonmusk, can be obtained from the user's homepage link, for example: elonmusk in https://twitter.com/elonmusk |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "next_cursor": "DAAHCgABHWL0Wy7__-oLAAIAAAATMjExNzI3MjgyNDgzMDIxMDM5MQgAAwAAAAIAAA",
  "pinned": {
    "author": {
      "avatar": "https://pbs.twimg.com/profile_images/2103567689515954176/aR-Kjpp4_normal.jpg",
      "blue_verified": true,
      "followers_count": 241472218,
      "name": "Elon Musk",
      "rest_id": "44196397",
      "screen_name": "elonmusk"
    },
    "bookmarks": 21300,
    "conversation_id": "2116039632743702637",
    "created_at": "Fri Oct 30 05:28:57 +0000 2026",
    "favorites": 366432,
    "lang": "en",
    "media": [],
    "quotes": 6905,
    "replies": 41562,
    "retweets": 69933,
    "sensitive": null,
    "source": null
  },
  "prev_cursor": "DAAHCgABHWL0Wy8AJxELAAIAAAATMjExNzQ4MjU3MDc1NzY1NjgzNggAAwAAAAEAAA",
  "status": "ok",
  "timeline": [
    {
      "author": {
        "avatar": "https://pbs.twimg.com/profile_images/2103567689515954176/aR-Kjpp4_normal.jpg",
        "blue_verified": true,
        "followers_count": 241472218,
        "name": "Elon Musk",
        "rest_id": "44196397",
        "screen_name": "elonmusk"
      },
      "bookmarks": 0,
      "conversation_id": "2117482570757656836",
      "created_at": "Tue Nov 03 05:02:40 +0000 2026",
      "entities": {
        "user_mentions": [
          {
            "id_str": "1082912120",
            "name": "Jerry Tworek",
            "screen_name": "MillionInt"
          }
        ]
      },
      "favorites": 0,
      "lang": "en",
      "media": [],
      "quotes": 0,
      "replies": 0,
      "retweeted": {
        "id": "2117465116858052725"
      },
      "retweeted_tweet": {
        "author": {
          "avatar": "https://pbs.twimg.com/profile_images/1184690787419734016/7ija9HDY_normal.jpg",
          "blue_verified": true,
          "name": "Jerry Tworek",
          "rest_id": "1082912120",
          "screen_name": "MillionInt"
        },
        "bookmarks": 109,
        "conversation_id": "2117465116858052725",
        "created_at": "Tue Nov 03 03:53:19 +0000 2026",
        "entities": [],
        "favorites": 1182,
        "lang": "en",
        "media": []
      }
    }
  ],
  "user": {
    "affiliates": {
      "label": {
        "badge": {
          "url": "https://pbs.twimg.com/profile_images/1955359038532653056/OSHY3ewP_bigger.jpg"
        },
        "description": "X",
        "url": {
          "url": "https://twitter.com/X",
          "urlType": "DeepLink"
        },
        "userLabelDisplayType": "Badge",
        "userLabelType": "BusinessLabel"
      }
    },
    "avatar": "https://pbs.twimg.com/profile_images/2103567689515954176/aR-Kjpp4_normal.jpg",
    "blue_verified": true,
    "created_at": "Tue Jun 02 20:12:29 +0000 2009",
    "desc": null,
    "friends": null,
    "header_image": null,
    "id": "44196397",
    "location": "",
    "media_count": null,
    "name": "Elon Musk",
    "profile": "elonmusk"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `timeline[]` | The list of posts on this page. Each item is one post or repost from the user. |
| `timeline[].tweet_id` | ID of the post, as a string. |
| `timeline[].text` | Text of the post. Reposts start with `RT @name:` and the text may be cut short. |
| `timeline[].created_at` | Time the post was created, in a format like `Tue Nov 03 05:02:40 +0000 2026`. |
| `timeline[].favorites / timeline[].retweets / timeline[].replies / timeline[].quotes / timeline[].bookmarks` | Engagement counts for the post: likes, reposts, replies, quote posts and bookmarks. |
| `timeline[].views` | View count of the post, returned as a string. |
| `timeline[].retweeted_tweet / timeline[].quoted` | Details of the original post when the item is a repost or a quote post. Each holds the original `author`, counts and `media`. |
| `timeline[].author.screen_name / timeline[].author.followers_count` | Handle and follower count of the account that wrote the post. |
| `pinned` | The user's pinned post, with the same fields as an item in `timeline`. |
| `next_cursor / prev_cursor` | Cursor values for paging to older and newer results. |
| `user.id / user.name / user.profile / user.created_at` | Numeric ID, display name, handle and account creation time of the requested user. |

### Notes

- Send either `screen_name` or `rest_id`. If you send both, `rest_id` is used and `screen_name` is ignored.
- To page, pass `next_cursor` from the last response as `cursor` in the next request.
- Take `screen_name` from the profile link, for example `elonmusk` in `https://twitter.com/elonmusk`.
- Call [Twitter Tweet Detail](/apis/twitter/web/tweet-detail) with a `tweet_id` for one post, or [Twitter (X) Tweet Comments](/apis/twitter/web/post-comments) for its replies.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Twitter (X) Latest Tweet Comments](/apis/twitter/web/latest-post-comments): Returns recent replies and comment timelines for a specific post using its tweet ID, with cursor support for multi-page results.
- [Twitter (X) Tweet Comments](/apis/twitter/web/post-comments): Returns comment threads and replies under a specified tweet.
- [Twitter (X) Retweet User List](/apis/twitter/web/retweet-user-list): Returns a list of users who reposted a specific post using its tweet ID, including follower counts, media counts, and user identifiers.

---
Machine-readable: [`catalog/models/twitter/web/user-post-tweet.json`](../../../../catalog/models/twitter/web/user-post-tweet.json) · Store page: https://www.sandbase.ai/model/twitter/web/user-post-tweet

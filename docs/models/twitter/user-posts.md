# Twitter User Published Posts API: pricing, parameters and code examples

`twitter/user-posts` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get posts published by an X (Twitter) user identified by Rest ID, with cursor pagination. Use it to browse a known account's timeline or continue through its public post history.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/user-posts", "restId": "44196397"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/user-posts', {'restId': '44196397'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/user-posts", {
  "restId": "44196397"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/user-posts", sandbase.Params{
	"restId": "44196397",
})
```

Same call via the path form: `POST /v1/api/twitter/user-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor for navigating through long timelines.  |
| `restId` | string | yes | The unique numeric identifier (Rest ID) for the X user.  |

## Details

Returns recent posts published by an X (Twitter) account, plus the account's pinned post and basic profile data. It needs the numeric `restId` of the user and supports cursor pagination.

### Use cases

- Pull the latest posts from a known account to monitor what it publishes.
- Track likes, retweets, replies and views on each post of a public figure over time.
- Separate original posts from retweets and quote posts when you analyze an account's activity.
- Page back through an account's public post history with `next_cursor`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/user-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"restId": "44196397"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `restId` | string | Yes | The unique numeric identifier (Rest ID) for the X user. |
| `cursor` | string | No | Pagination cursor for navigating through long timelines. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "next_cursor": "DAAHCgABHWL0Tx3__-oLAAIAAAATMjExNzI3MjgyNDgzMDIxMDM5MQgAAwAAAAIAAA",
  "pinned": {
    "author": {
      "avatar": "https://pbs.twimg.com/profile_images/2103567689515954176/aR-Kjpp4_normal.jpg",
      "blue_verified": true,
      "followers_count": 241472215,
      "name": "Elon Musk",
      "rest_id": "44196397",
      "screen_name": "elonmusk"
    },
    "bookmarks": 21300,
    "conversation_id": "2116039632743702637",
    "created_at": "Fri Oct 30 05:28:57 +0000 2026",
    "favorites": 366430,
    "lang": "en",
    "media": [],
    "quotes": 6905,
    "replies": 41562,
    "retweets": 69932,
    "sensitive": null,
    "source": null
  },
  "prev_cursor": "DAAHCgABHWL0Tx4AJxELAAIAAAATMjExNzQ4MjU3MDc1NzY1NjgzNggAAwAAAAEAAA",
  "status": "ok",
  "timeline": [
    {
      "author": {
        "avatar": "https://pbs.twimg.com/profile_images/2103567689515954176/aR-Kjpp4_normal.jpg",
        "blue_verified": true,
        "followers_count": 241472215,
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
| `timeline[]` | List of posts on the account's timeline, newest first. Includes original posts, retweets and quote posts. |
| `timeline[].tweet_id / timeline[].conversation_id` | ID of the post and ID of the conversation it belongs to. Both are numeric strings. |
| `timeline[].text / timeline[].created_at / timeline[].lang` | Post text, creation time (for example `Tue Nov 03 05:02:40 +0000 2026`) and language code. |
| `timeline[].favorites / timeline[].retweets / timeline[].replies / timeline[].quotes / timeline[].bookmarks` | Engagement counts for the post. |
| `timeline[].views` | View count for the post, returned as a string. |
| `timeline[].retweeted_tweet / timeline[].quoted` | Original post details when the item is a retweet (`retweeted_tweet`) or a quote post (`quoted`). Each has its own `author`, counts and `media`. |
| `timeline[].author.screen_name / timeline[].author.rest_id / timeline[].author.followers_count` | Handle, Rest ID and follower count of the account that published the post. |
| `pinned` | The account's pinned post, with the same fields as a `timeline[]` item. |
| `user.name / user.profile / user.id / user.created_at` | Display name, handle, Rest ID and account creation time of the requested user. |
| `next_cursor / prev_cursor` | Cursor values for the next and previous page of the timeline. |

### Notes

- `restId` is the numeric user ID, such as `44196397`. Get it from the `rest_id` field of a profile call like [Twitter User Profile](/apis/twitter/user-detail).
- To get the next page, send `next_cursor` from the response as `cursor` with the same `restId`.
- Some fields in `user`, such as `desc`, `friends` and `statuses_count`, can be `null`. Use [Twitter User Profile](/apis/twitter/user-detail) for full profile data.
- To fetch full detail for one post, pass its `tweet_id` to [Twitter Post Detail](/apis/twitter/post-detail).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/twitter/user-posts.json`](../../../catalog/models/twitter/user-posts.json) · Store page: https://www.sandbase.ai/model/twitter/user-posts

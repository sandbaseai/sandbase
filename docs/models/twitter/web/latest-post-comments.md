# Twitter (X) Latest Tweet Comments API: pricing, parameters and code examples

`twitter/web/latest-post-comments` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recent replies and comment timelines for a specific post using its tweet ID, with cursor support for multi-page results.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/latest-post-comments", "tweet_id": "2107237881668313108"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/latest-post-comments', {'tweet_id': '2107237881668313108'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/latest-post-comments", {
  "tweet_id": "2107237881668313108"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/latest-post-comments", sandbase.Params{
	"tweet_id": "2107237881668313108",
})
```

Same call via the path form: `POST /v1/api/twitter/web/latest-post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default is None, used for paging, obtained from the last request  |
| `tweet_id` | string | yes | Tweet ID  |

## Details

Returns the most recent replies to a single tweet as a `timeline` list. Each reply includes its text, author handle, engagement counts and basic author profile data. The only required input is `tweet_id`.

### Use cases

- Read the newest replies under a news or product announcement tweet.
- Collect reply text and view counts for sentiment analysis on one post.
- Spot which accounts reply to a tweet, with their follower counts, to find active responders.
- Page through a long reply thread by passing back the cursor from the last call.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/latest-post-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tweet_id": "2107237881668313108"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tweet_id` | string | Yes | Tweet ID |
| `cursor` | string | No | Cursor, default is None, used for paging, obtained from the last request |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "next_cursor": "DAADDAABCgABHVrBFWqWkH8KAAIdPoa-fFeQ_AAIAAIAAAACCAADAAAAAAgABAAAAAAKAAUdYvRU5YAn…",
  "prev_cursor": "DAADDAABCgABHVrBFWqWkH8KAAIdPoa-fFeQ_AAIAAIAAAABCAADAAAAAAgABAAAAAAKAAUdYvRU5YAn…",
  "status": "ok",
  "timeline": [
    {
      "bookmarks": 0,
      "conversation_id": "2107237881668313108",
      "created_at": "Tue Oct 27 22:53:14 +0000 2026",
      "display_text_range": [
        29
      ],
      "entities": {
        "hashtags": [],
        "symbols": [],
        "timestamps": [],
        "urls": [],
        "user_mentions": [
          {
            "id_str": "11348282",
            "indices": [
              0
            ],
            "name": "NASA",
            "screen_name": "NASA"
          }
        ]
      },
      "favorites": 0,
      "in_reply_to_screen_name": "NASA",
      "in_reply_to_status_id_str": "2107237881668313108",
      "in_reply_to_user_id_str": "11348282",
      "lang": "ja",
      "media": [],
      "quotes": 0
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `timeline[].tweet_id` | ID of the reply tweet. |
| `timeline[].text` | Full text of the reply, including the leading @mentions. |
| `timeline[].screen_name` | Handle of the account that wrote the reply. |
| `timeline[].created_at` | Time the reply was posted, in a format like `Tue Oct 27 22:53:14 +0000 2026`. |
| `timeline[].conversation_id / timeline[].in_reply_to_status_id_str` | ID of the tweet being replied to. Here both match the `tweet_id` you sent. |
| `timeline[].favorites / timeline[].replies / timeline[].retweets / timeline[].quotes / timeline[].bookmarks` | Engagement counts for the reply itself. |
| `timeline[].views` | View count of the reply, returned as a string. |
| `timeline[].lang` | Language code of the reply text. |
| `timeline[].user_info.followers_count / timeline[].user_info.favorites_count` | Follower count and favorites count of the reply author. |
| `next_cursor / prev_cursor` | Cursor strings for the next and previous page of replies. |

### Notes

- Pass `next_cursor` from the response as `cursor` in the next request to get more replies.
- `tweet_id` is the numeric ID at the end of a tweet URL. Use the `tweet_id` from a [Twitter (X) User Posts](/apis/twitter/web/user-post-tweet) or [Twitter (X) Search](/apis/twitter/web/search-timeline) result.
- Some fields can be `null` or empty, such as `source`, `sensitive`, `user_info.description` and `user_info.friends_count`.
- For a different comment listing on the same tweet, see [Twitter (X) Tweet Comments](/apis/twitter/web/post-comments).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Twitter (X) Tweet Comments](/apis/twitter/web/post-comments): Returns comment threads and replies under a specified tweet.
- [Twitter (X) Retweet User List](/apis/twitter/web/retweet-user-list): Returns a list of users who reposted a specific post using its tweet ID, including follower counts, media counts, and user identifiers.
- [Twitter (X) Search](/apis/twitter/web/search-timeline): Search Twitter / X posts by keyword and get tweets with text, author, time and engagement counts (likes, retweets, replies, views).

---
Machine-readable: [`catalog/models/twitter/web/latest-post-comments.json`](../../../../catalog/models/twitter/web/latest-post-comments.json) · Store page: https://www.sandbase.ai/model/twitter/web/latest-post-comments

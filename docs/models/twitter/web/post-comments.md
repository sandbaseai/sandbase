# Twitter (X) Tweet Comments API: pricing, parameters and code examples

`twitter/web/post-comments` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns comment threads and replies under a specified tweet. Provide a tweet ID and paginate through conversations using cursor values.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/post-comments", "tweet_id": "2107237881668313108"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/post-comments', {'tweet_id': '2107237881668313108'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/post-comments", {
  "tweet_id": "2107237881668313108"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/post-comments", sandbase.Params{
	"tweet_id": "2107237881668313108",
})
```

Same call via the path form: `POST /v1/api/twitter/web/post-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default is None, used for paging, obtained from the last request  |
| `tweet_id` | string | yes | Tweet ID  |

## Details

Returns the replies under one tweet, plus the parent tweet's own details and engagement counts. The only required input is a `tweet_id`. Pass the `cursor` value from the last response to get the next page of replies.

### Use cases

- Collect public replies under an announcement to review audience reaction.
- Rank replies by `likes` and `views` to find the most visible responses.
- Export reply text and author handles for sentiment or topic analysis.
- Compare the parent tweet's `replies` count with the number of replies you have fetched.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/post-comments" \
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
  "author": {
    "blue_verified": true,
    "description": null,
    "image": "https://pbs.twimg.com/profile_images/1321163587679784960/0ZxKlEKB_normal.jpg",
    "name": "NASA",
    "rest_id": "11348282",
    "screen_name": "NASA",
    "sub_count": null
  },
  "bookmarks": 198,
  "conversation_id": "2107237881668313108",
  "created_at": "Mon Oct 05 22:33:56 +0000 2026",
  "cursor": "DAAKCgABHWL0Vva__mMLAAIAAAGoRW1QQzZ3QUFBZlEvZ0dKTjB2R3AvQUFBQUNVZFFGTVBZWmF3bkIw…",
  "display_text": "Time to bring them home 🌎\n\nAfter nearly eight months aboard the @Space_Station, …",
  "entities": {
    "media": [
      {
        "allow_download_status": {
          "allow_download": true
        },
        "display_url": "pic.x.com/Vu7At4nnQ3",
        "expanded_url": "https://x.com/NASA/status/2107237881668313108/photo/1",
        "ext_alt_text": "Inside the International Space Station NASA’s SpaceX Crew-12 members gather for …",
        "ext_media_availability": {
          "status": "Available"
        },
        "features": {
          "large": {
            "faces": [
              {
                "h": 96,
                "w": 96,
                "x": 44,
                "y": 238
              }
            ]
          },
          "medium": {
            "faces": [
              {
                "h": 56,
                "w": 56,
                "x": 25,
                "y": 139
              }
            ]
          },
          "orig": {
            "faces": [
              {
                "h": 96,
                "w": 96,
                "x": 44,
                "y": 238
              }
            ]
          },
          "small": {
            "faces": [
              {
                "h": 31,
                "w": 31,
                "x": 14,
                "y": 79
              }
            ]
          }
        },
        "id_str": "2107237609105768448",
        "indices": [
          276
        ],
        "media_key": "3_2107237609105768448",
        "media_results": {
          "result": {
            "media_key": "3_2107237609105768448"
          }
        },
        "media_url_https": "https://pbs.twimg.com/media/HT5pcNwXwAAKdoM.jpg",
        "original_info": {
          "focus_rects": [
            {
              "h": 1147,
              "w": 2048,
              "x": 0,
              "y": 0
            }
          ],
          "height": 1365,
          "width": 2048
        }
      }
    ],
    "user_mentions": [
      {
        "id_str": "1451773004",
        "indices": [
          64
        ],
        "name": "International Space Station",
        "screen_name": "Space_Station"
      }
    ]
  },
  "id": "2107237881668313108",
  "initial_tweets": null,
  "lang": "en",
  "likes": 7253,
  "media": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `thread[].text / thread[].display_text` | Reply content. `text` includes the leading @mentions and any `t.co` link. `display_text` is the same reply without the leading mentions. |
| `thread[].id` | ID of the reply tweet. |
| `thread[].created_at` | Time the reply was posted, in a string like `Mon Oct 05 22:42:28 +0000 2026`. |
| `thread[].likes / thread[].retweets / thread[].quotes / thread[].replies / thread[].bookmarks` | Engagement counts for each reply. |
| `thread[].views` | View count of the reply, returned as a string. |
| `thread[].author.screen_name / thread[].author.name / thread[].author.rest_id` | Handle, display name and numeric user ID of the person who wrote the reply. |
| `thread[].author.blue_verified` | Whether the reply author has a blue verified badge. |
| `thread[].entities.user_mentions[]` | Accounts mentioned in the reply, with `screen_name`, `id_str` and the `indices` of the mention in `text`. |
| `thread[].media` | Photos attached to the reply, with `media_url_https`. It is empty or `null` when the reply has no media. |
| `cursor` | Paging token. Send it back as the `cursor` request parameter to load the next page. |
| `id / text / likes / replies / views` | Details and engagement counts of the parent tweet whose replies are listed. `author` holds the parent tweet's author. |

### Notes

- `tweet_id` is the numeric ID at the end of a tweet URL, such as `2107237881668313108`. Every reply's `conversation_id` equals this ID.
- To page through replies, copy `cursor` from the response into the next request. Leave `cursor` out on the first call.
- Use [Twitter Tweet Detail](/apis/twitter/web/tweet-detail) for the parent tweet alone, or [Twitter (X) Latest Tweet Comments](/apis/twitter/web/latest-post-comments) for a recent-replies view of the same tweet.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Twitter (X) Latest Tweet Comments](/apis/twitter/web/latest-post-comments): Returns recent replies and comment timelines for a specific post using its tweet ID, with cursor support for multi-page results.
- [Twitter (X) Retweet User List](/apis/twitter/web/retweet-user-list): Returns a list of users who reposted a specific post using its tweet ID, including follower counts, media counts, and user identifiers.
- [Twitter (X) Search](/apis/twitter/web/search-timeline): Search Twitter / X posts by keyword and get tweets with text, author, time and engagement counts (likes, retweets, replies, views).

---
Machine-readable: [`catalog/models/twitter/web/post-comments.json`](../../../../catalog/models/twitter/web/post-comments.json) · Store page: https://www.sandbase.ai/model/twitter/web/post-comments

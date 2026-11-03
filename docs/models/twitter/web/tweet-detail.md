# Twitter Tweet Detail API: pricing, parameters and code examples

`twitter/web/tweet-detail` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Get a single tweet (X post) by ID: full text, author, media, and like, retweet, reply, quote, bookmark and view counts.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/tweet-detail", "tweet_id": "1808168603721650364"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/tweet-detail', {'tweet_id': '1808168603721650364'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/tweet-detail", {
  "tweet_id": "1808168603721650364"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/tweet-detail", sandbase.Params{
	"tweet_id": "1808168603721650364",
})
```

Same call via the path form: `POST /v1/api/twitter/web/tweet-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tweet_id` | string | yes | Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in https://x.com/elonmusk/status/1808168603721650364  |

## Details

Returns one tweet (X post) with its full text, author, media, reply context and engagement counts. It needs one input, the numeric `tweet_id`.

### Use cases

- Track likes, retweets and views on a specific post by calling it on a schedule.
- Fetch the full text and media URLs of a tweet cited in a report or news article.
- Check whether a post is still `active` before you use it in a dashboard.
- Pull the author's follower count and verification flag for a post you want to review.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/tweet-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tweet_id": "1808168603721650364"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tweet_id` | string | Yes | Tweet ID, can be obtained from the tweet link. For example: 1808168603721650364 in https://x.com/elonmusk/status/1808168603721650364 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "author": {
    "blue_verified": true,
    "image": "https://pbs.twimg.com/profile_images/2103567689515954176/aR-Kjpp4_normal.jpg",
    "name": "Elon Musk",
    "rest_id": "44196397",
    "screen_name": "elonmusk",
    "sub_count": 241472212,
    "verification": null
  },
  "bookmarks": 6534,
  "conversation_control": {
    "policy": null
  },
  "conversation_id": "1808168603721650364",
  "created_at": "Tue Jul 02 15:59:23 +0000 2024",
  "display_text": "The New York Times is attacking *your* freedom of speech!",
  "entities": {
    "hashtags": [],
    "media": [
      {
        "display_url": "pic.x.com/TRIa13TWdY",
        "expanded_url": "https://x.com/elonmusk/status/1808168603721650364/photo/1",
        "ext_media_availability": {
          "status": "Available"
        },
        "features": {
          "large": {
            "faces": []
          },
          "medium": {
            "faces": []
          },
          "orig": {
            "faces": []
          },
          "small": {
            "faces": []
          }
        },
        "id_str": "1808168600894689280",
        "indices": [
          58
        ],
        "media_key": "3_1808168600894689280",
        "media_results": {
          "result": {
            "media_key": "3_1808168600894689280"
          }
        },
        "media_url_https": "https://pbs.twimg.com/media/GRfnwy5X0AAwIK2.jpg",
        "original_info": {
          "focus_rects": [
            {
              "h": 355,
              "w": 634,
              "x": 20,
              "y": 0
            }
          ],
          "height": 355,
          "width": 712
        },
        "sizes": {
          "large": {
            "h": 355,
            "resize": "fit",
            "w": 712
          },
          "medium": {
            "h": 355,
            "resize": "fit",
            "w": 712
          },
          "small": {
            "h": 339,
            "resize": "fit",
            "w": 680
          },
          "thumb": {
            "h": 150,
            "resize": "crop",
            "w": 150
          }
        },
        "type": "photo"
      }
    ],
    "symbols": [],
    "timestamps": [],
    "urls": [],
    "user_mentions": []
  },
  "id": "1808168603721650364",
  "in_reply_to_screen_name": null,
  "in_reply_to_status_id_str": null,
  "in_reply_to_user_id_str": null,
  "initial_tweets": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id / conversation_id` | The tweet ID and the ID of the conversation it belongs to. They match for a post that starts a conversation. |
| `text / display_text` | `text` is the post text with the media short link at the end. `display_text` is the same text without the link. |
| `created_at` | Post time as a string, for example `Tue Jul 02 15:59:23 +0000 2024`. |
| `likes / retweets / replies / quotes / bookmarks` | Engagement counts for the post, as numbers. |
| `views` | View count. It comes back as a string, for example `53722244`. |
| `author.screen_name / author.name / author.rest_id` | The author's handle, display name and numeric user ID. |
| `author.sub_count / author.blue_verified` | `sub_count` is a count tied to the author account and is `241472212` in this response. `blue_verified` is a true or false flag for the author's verification. |
| `media.photo[].media_url_https` | Direct image URL for each photo attached to the tweet. |
| `entities.media[].type / entities.media[].media_url_https` | The media type, such as `photo`, and its image URL. The entry also has sizes and the short `url` used in the text. |
| `status / lang / sensitive` | Post state (`active` here), language code, and a flag for sensitive content. |

### Notes

- Take `tweet_id` from the tweet link. In `https://x.com/elonmusk/status/1808168603721650364` the ID is `1808168603721650364`.
- Reply fields such as `in_reply_to_status_id_str` and `reply_to` are `null` when the tweet is not a reply.
- To read the replies to a tweet, use [Twitter (X) Tweet Comments](/apis/twitter/web/post-comments).
- To list the accounts that retweeted it, use [Twitter (X) Retweet User List](/apis/twitter/web/retweet-user-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Twitter (X) Search](/apis/twitter/web/search-timeline): Search Twitter / X posts by keyword and get tweets with text, author, time and engagement counts (likes, retweets, replies, views).
- [Twitter (X) Trending Topics](/apis/twitter/web/trending): Get trending topics on Twitter / X by country: trend names with their category context, for the United States, Japan, India, the UK and other markets.
- [Twitter (X) User Profile](/apis/twitter/web/user-profile): Get a Twitter / X user profile by screen name or user ID: name, bio, follower and following counts, post and media counts, verification and creation date.

---
Machine-readable: [`catalog/models/twitter/web/tweet-detail.json`](../../../../catalog/models/twitter/web/tweet-detail.json) · Store page: https://www.sandbase.ai/model/twitter/web/tweet-detail

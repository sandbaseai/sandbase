# Twitter Post Detail API: pricing, parameters and code examples

`twitter/post-detail` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get the full detail of an X (Twitter) post identified by its tweet ID. Use it to inspect a known post after finding it through search, a user timeline, or an existing post URL.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/post-detail", "tweetId": "1585341984679469056"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/post-detail', {'tweetId': '1585341984679469056'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/post-detail", {
  "tweetId": "1585341984679469056"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/post-detail", sandbase.Params{
	"tweetId": "1585341984679469056",
})
```

Same call via the path form: `POST /v1/api/twitter/post-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tweetId` | string | yes | The unique identifier of the X (Twitter) post.  |

## Details

Returns the full detail of one X (Twitter) post: its text, author, engagement counts, attached media and reply context. It needs the post's `tweetId`.

### Use cases

- Pull the like, retweet, reply and quote counts of a known post to track how it performed.
- Download the video or image URLs attached to a post for archiving or review.
- Check whether a post is still `active` and read its author details before citing it.
- Read the exact post text and creation time to verify a quote or screenshot.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/post-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tweetId": "1585341984679469056"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tweetId` | string | Yes | The unique identifier of the X (Twitter) post. |

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
  "bookmarks": 14034,
  "conversation_control": {
    "policy": null
  },
  "conversation_id": "1585341984679469056",
  "created_at": "Wed Oct 26 18:45:58 +0000 2022",
  "display_text": "Entering Twitter HQ – let that sink in!",
  "entities": {
    "hashtags": [],
    "media": [
      {
        "additional_media_info": {
          "monetizable": false
        },
        "display_url": "pic.x.com/D68z4K2wq7",
        "expanded_url": "https://x.com/elonmusk/status/1585341984679469056/video/1",
        "ext_media_availability": {
          "status": "Available"
        },
        "id_str": "1585341912877146112",
        "indices": [
          40
        ],
        "media_key": "7_1585341912877146112",
        "media_results": {
          "result": {
            "media_key": "7_1585341912877146112"
          }
        },
        "media_url_https": "https://pbs.twimg.com/ext_tw_video_thumb/1585341912877146112/pu/img/DwJ7wlGIe9ir…",
        "original_info": {
          "focus_rects": [],
          "height": 1080,
          "width": 1920
        },
        "sizes": {
          "large": {
            "h": 1080,
            "resize": "fit",
            "w": 1920
          },
          "medium": {
            "h": 675,
            "resize": "fit",
            "w": 1200
          },
          "small": {
            "h": 383,
            "resize": "fit",
            "w": 680
          },
          "thumb": {
            "h": 150,
            "resize": "crop",
            "w": 150
          }
        },
        "type": "video"
      }
    ],
    "symbols": [],
    "timestamps": [],
    "urls": [],
    "user_mentions": []
  },
  "id": "1585341984679469056",
  "in_reply_to_screen_name": null,
  "in_reply_to_status_id_str": null,
  "in_reply_to_user_id_str": null,
  "initial_tweets": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `text / display_text` | The post text. `text` includes the shortened `t.co` link. `display_text` shows the text without the trailing media link. |
| `id / conversation_id` | The post's own ID and the ID of the conversation it belongs to. They match when the post starts the conversation. |
| `created_at` | When the post was created, in the format `Wed Oct 26 18:45:58 +0000 2022`. |
| `author.name / author.screen_name / author.rest_id` | The author's display name, handle and numeric user ID. |
| `author.blue_verified / author.sub_count` | Whether the author has the blue verified flag, and the `sub_count` value for the author's account. |
| `likes / retweets / replies / quotes / bookmarks` | Engagement counts for the post. |
| `views` | View count of the post. It can be `null` when no value is returned. |
| `media.video[].variants[]` | Playable video files for the post. Each entry has a `content_type` and `url`. MP4 entries also have a `bitrate`. |
| `media.video[].duration` | Length of the video. The value `9301` matches `duration_millis` in `entities.media[].video_info`, which suggests milliseconds. |
| `in_reply_to_status_id_str / in_reply_to_screen_name / reply_to` | Set when the post is a reply. They are `null` for a standalone post. |
| `status / lang / sensitive` | Post state (`active`), language code (`en`) and a flag for sensitive content. |

### Notes

- Get `tweetId` from the number at the end of a post URL, such as `https://x.com/elonmusk/status/1585341984679469056`, or from search and timeline results.
- `tweetId` is a string. Send it as text, not as a number.
- To read replies to this post, call [Twitter Post Comments](/apis/twitter/post-comments). To see quote posts, call [X (Twitter) Tweet Quotes](/apis/twitter/tweet-quotes).
- To look up the author, use the `author.screen_name` value with [Twitter User Profile](/apis/twitter/user-detail).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/twitter/post-detail.json`](../../../catalog/models/twitter/post-detail.json) · Store page: https://www.sandbase.ai/model/twitter/post-detail

# Twitter (X) Search API: pricing, parameters and code examples

`twitter/web/search-timeline` · data API · Twitter · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search Twitter / X posts by keyword and get tweets with text, author, time and engagement counts (likes, retweets, replies, views). Supports Top, Latest, Media, People and Lists results.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "twitter/web/search-timeline", "keyword": "AI agents", "search_type": "Top"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('twitter/web/search-timeline', {'keyword': 'AI agents', 'search_type': 'Top'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("twitter/web/search-timeline", {
  "keyword": "AI agents",
  "search_type": "Top"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "twitter/web/search-timeline", sandbase.Params{
	"keyword": "AI agents",
	"search_type": "Top",
})
```

Same call via the path form: `POST /v1/api/twitter/web/search-timeline` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Cursor, default is None, used for paging, obtained from the last request  |
| `keyword` | string | yes | Search keyword  |
| `search_type` | string |  | Search type, default is Top, other optional values are Latest, Media, People, Lists default `"Top"` |

## Details

Returns a page of X (Twitter) posts that match a search keyword. Each post has its text, author handle, creation time, engagement counts and any attached media. The only required input is `keyword`.

### Use cases

- Track posts that mention a brand, product or model name such as `OpenAI`.
- Rank matching posts by `views`, `favorites` or `retweets` to find the ones that spread most.
- Pull attached video links from matching posts to build a media collection on a topic.
- Check the follower count of authors who post about a topic to spot large accounts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/twitter/web/search-timeline" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `cursor` | string | No | Cursor, default is None, used for paging, obtained from the last request |
| `search_type` | string | No | Search type, default is Top, other optional values are Latest, Media, People, Lists |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "next_cursor": "DAACCgACHWL0WF5AJxAKAAMdYvRYXj_Y8AgABAAAAAILAAUAAADwRW1QQzZ3QUFBZlEvZ0dKTjB2R3Av…",
  "prev_cursor": "DAACCgACHWL0WF5AJxAKAAMdYvRYXj_Y8AgABAAAAAELAAUAAADwRW1QQzZ3QUFBZlEvZ0dKTjB2R3Av…",
  "status": "ok",
  "timeline": [
    {
      "bookmarks": 9589,
      "conversation_id": "2116963310277202003",
      "created_at": "Sun Nov 01 18:39:19 +0000 2026",
      "display_text_range": [
        0
      ],
      "entities": {
        "hashtags": [],
        "symbols": [],
        "timestamps": [],
        "urls": [],
        "user_mentions": []
      },
      "favorites": 3743,
      "lang": "en",
      "media": {
        "video": [
          {
            "aspect_ratio": [
              4
            ],
            "duration": 21000,
            "id": "2116959813636874240",
            "media_url_https": "https://pbs.twimg.com/amplify_video_thumb/2116959813636874240/img/BpM2ygu4J6yvD6…",
            "original_info": {
              "focus_rects": [],
              "height": 1350,
              "width": 1080
            },
            "variants": [
              {
                "content_type": "application/x-mpegURL",
                "url": "https://video.twimg.com/amplify_video/2116959813636874240/pl/oQiawi_tf0JmlNvI.m3…"
              }
            ]
          }
        ]
      },
      "quoted": {
        "author": {
          "avatar": "https://pbs.twimg.com/profile_images/2068434168954978304/gFJZPH-g_normal.jpg",
          "blue_verified": true,
          "created_at": "Sat May 23 18:31:55 +0000 2026",
          "name": "mojesko",
          "rest_id": "2058253770492956672",
          "screen_name": "mojeskoqq"
        },
        "bookmarks": 2118,
        "conversation_id": "2116176596466032817",
        "created_at": "Fri Oct 30 14:33:11 +0000 2026",
        "favorites": 501,
        "lang": "zxx",
        "media": [],
        "quotes": 20
      },
      "quotes": 25,
      "replies": 111,
      "retweets": 315
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `timeline[]` | One matching result per item. In this response each item has `type` set to `tweet`. |
| `timeline[].tweet_id / timeline[].conversation_id` | ID of the post and ID of the conversation it belongs to. Both are numeric strings. |
| `timeline[].text` | Text of the post. Long text may be cut with an ellipsis. |
| `timeline[].screen_name` | Handle of the author, without the @ sign. |
| `timeline[].created_at` | Time the post was created, as a string like `Mon Oct 26 18:06:27 +0000 2026`. |
| `timeline[].favorites / timeline[].retweets / timeline[].replies / timeline[].quotes / timeline[].bookmarks` | Counts of likes, retweets, replies, quote posts and bookmarks for the post. |
| `timeline[].views` | View count of the post, returned as a string. |
| `timeline[].media.video[].variants[]` | Video files for the post. Each has a `url` and a `content_type`. The `video/mp4` entries also have a `bitrate`. |
| `timeline[].user_info.followers_count / timeline[].user_info.created_at` | Follower count of the author and the time the author account was created. |
| `timeline[].quoted` | The post that this post quotes. It includes its own `author`, `text`-level counts such as `favorites` and `quotes`, and `created_at`. It appears only on quote posts. |

### Notes

- Page forward by sending `next_cursor` from the last response as `cursor`. The response also returns `prev_cursor`.
- Set `search_type` to `Top`, `Latest`, `Media`, `People` or `Lists`. The default is `Top`.
- To read the replies under a post, pass its `tweet_id` to [Twitter (X) Tweet Comments](/apis/twitter/web/post-comments).
- To get full details for one post, use [Twitter Tweet Detail](/apis/twitter/web/tweet-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Get the latest tweet comments](/apis/twitter/web/latest-post-comments): Get the latest tweet comments.
- [Get comments](/apis/twitter/web/post-comments): Get comments under the tweet.
- [ReTweet User list](/apis/twitter/web/retweet-user-list): Get ReTweet User list.

---
Machine-readable: [`catalog/models/twitter/web/search-timeline.json`](../../../../catalog/models/twitter/web/search-timeline.json) · Store page: https://www.sandbase.ai/model/twitter/web/search-timeline

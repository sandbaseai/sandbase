# YouTube Video Comment List API: pricing, parameters and code examples

`youtube/video-comment` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get first-level comments for a YouTube video with sorting, locale options, and cursor pagination. Use it to review audience discussion or continue through additional comment pages.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/video-comment", "videoId": "dQw4w9WgXcQ"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/video-comment', {'videoId': 'dQw4w9WgXcQ'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/video-comment", {
  "videoId": "dQw4w9WgXcQ"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/video-comment", sandbase.Params{
	"videoId": "dQw4w9WgXcQ",
})
```

Same call via the path form: `POST /v1/api/youtube/video-comment` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | string |  | Pagination cursor returned by the previous response.  |
| `sortBy` | string |  | Sort order for the comment list. one of: `top`, `newest`; default `"newest"` |
| `videoId` | string | yes | The unique identifier for a YouTube video.  |
| `countryCode` | string |  | Region code for response data. default `"US"` |
| `languageCode` | string |  | Language preference for response data. default `"zh-CN"` |

## Details

This API returns first-level comments for a YouTube video. It needs a `videoId` and returns one page of comments plus a token for the next page.

### Use cases

- Read the newest comments on a video to track how viewers react after a release.
- Pull the top comments of a video to find the most liked viewer opinions.
- Collect commenter channel IDs and URLs to find active fans of a video.
- Find comments with replies and fetch those threads with the reply token.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/video-comment" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"videoId": "dQw4w9WgXcQ"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `videoId` | string | Yes | The unique identifier for a YouTube video. |
| `countryCode` | string | No | Region code for response data. |
| `cursor` | string | No | Pagination cursor returned by the previous response. |
| `languageCode` | string | No | Language preference for response data. |
| `sortBy` | string | No | Sort order for the comment list. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "comments": [
    {
      "author": {
        "avatar_thumbnails": null,
        "avatar_url": "https://yt3.ggpht.com/-E_1_UKaW4IjUqAmk6N7s3qr_8PbKnu9qRPFXo6z2ifCAllcNGgSges4D6…",
        "channel_id": "UC5KHEnpHIDdKl6ALNpA9dNQ",
        "channel_url": "https://www.youtube.com/@bitkoinaz",
        "display_name": "@bitkoinaz",
        "is_artist": false,
        "is_creator": false,
        "is_verified": false
      },
      "comment_id": "Ugw9M0L8J6DB47hdd9h4AaABAg",
      "content": "о боже какая песня. ее нашел для меня ИИ бот когда я попросил его скачать какую …",
      "creator_thumbnail_url": null,
      "like_count": "0",
      "like_count_a11y": "0 次赞",
      "published_time": "22分钟前",
      "reply_count": "0",
      "reply_count_a11y": "0 条回复",
      "reply_level": 0
    }
  ],
  "continuation_token": "Eg0SC2RR…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comments[]` | List of first-level comments on the requested page. |
| `comments[].comment_id` | Unique ID of the comment. |
| `comments[].content` | Text of the comment. |
| `comments[].author.display_name / comments[].author.channel_url` | Handle and channel link of the commenter. |
| `comments[].author.channel_id` | YouTube channel ID of the commenter. |
| `comments[].author.is_verified / comments[].author.is_creator / comments[].author.is_artist` | Boolean flags for the commenter. They show whether the author is verified, is the video creator, or is an artist. |
| `comments[].like_count / comments[].reply_count` | Number of likes and replies on the comment. Both values are strings. |
| `comments[].published_time` | Relative publish time as display text, for example `22分钟前`. It is not a timestamp. |
| `comments[].reply_continuation_token` | Token that appears only on comments that have replies. Use it to load the reply thread. |
| `continuation_token` | Token for the next page of comments. Send it as `cursor` in the next request. |

### Notes

- The `videoId` is the value after `v=` in a YouTube watch URL, for example `dQw4w9WgXcQ`.
- For the next page, pass the `continuation_token` from the response as `cursor`. Keep the same `sortBy` value (`top` or `newest`).
- Text such as `published_time` and `like_count_a11y` follows the language settings, and the sample shows Chinese strings. Use `languageCode` and `countryCode` to change them.
- To read replies to a comment, call [YouTube Comment Replies](/apis/youtube/comment-replies) with the comment's `reply_continuation_token`.

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/youtube/video-comment.json`](../../../catalog/models/youtube/video-comment.json) · Store page: https://www.sandbase.ai/model/youtube/video-comment

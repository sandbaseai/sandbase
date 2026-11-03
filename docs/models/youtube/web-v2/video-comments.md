# YouTube Video Comments API: pricing, parameters and code examples

`youtube/web-v2/video-comments` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves top-level comments for a YouTube video specified by video ID. Supports sorting by top or newest, regional localization, and pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/video-comments", "video_id": "dQw4w9WgXcQ"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/video-comments', {'video_id': 'dQw4w9WgXcQ'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/video-comments", {
  "video_id": "dQw4w9WgXcQ"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/video-comments", sandbase.Params{
	"video_id": "dQw4w9WgXcQ",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/video-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort_by` | string |  | **Purpose**: Comment sorting method one of: `top`, `newest` |
| `video_id` | string | yes | **Purpose**: Video ID  |
| `need_format` | boolean |  | **Purpose**: Whether to return cleaned simplified data default `true` |
| `country_code` | string |  | **Purpose**: Set region code default `"US"` |
| `language_code` | string |  | **Purpose**: Set language preference for comments default `"zh-CN"` |
| `continuation_token` | string |  | **Purpose**: Pagination token for next page  |

## Details

Returns top-level comments for a YouTube video, with author details, like and reply counts, and a publish time for each comment. The only required input is the 11-character `video_id`.

### Use cases

- Pull the most liked comments on a video to see what viewers react to most.
- Fetch the newest comments with `sort_by` set to `newest` to feed a moderation queue.
- Collect comment text and author channel IDs to study who engages with a video.
- Find comments with many replies, then load those reply threads for deeper discussion analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/video-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video_id": "dQw4w9WgXcQ"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `video_id` | string | Yes | **Purpose**: Video ID |
| `continuation_token` | string | No | **Purpose**: Pagination token for next page |
| `country_code` | string | No | **Purpose**: Set region code |
| `language_code` | string | No | **Purpose**: Set language preference for comments |
| `need_format` | boolean | No | **Purpose**: Whether to return cleaned simplified data |
| `sort_by` | string | No | **Purpose**: Comment sorting method |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "comments": [
    {
      "author": {
        "avatar_thumbnails": null,
        "avatar_url": "https://yt3.ggpht.com/ytc/AIdro_kDD-FhIbth2qcBbI9VGxR41dJa0kE3kN9iVlGzNgRU_g=s88…",
        "channel_id": "UCKrzgYonJnMd0Dk7zQXjYXw",
        "channel_url": "https://www.youtube.com/@grustache4569",
        "display_name": "@grustache4569",
        "is_artist": false,
        "is_creator": false,
        "is_verified": false
      },
      "comment_id": "UgzKYksqeQ5gA3t0g0F4AaABAg",
      "content": "I Rick rolled my entire French class because we had to study a city in France an…",
      "creator_thumbnail_url": null,
      "like_count": "10万",
      "like_count_a11y": "10万 次赞",
      "published_time": "6年前（修改过）",
      "reply_continuation_token": "Eg0SC2RR…",
      "reply_count": "665",
      "reply_count_a11y": "665 条回复",
      "reply_count_text": "665 条回复",
      "reply_level": 0
    }
  ],
  "continuation_token": "Eg0SC2RR…"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `comments[].comment_id` | ID of the comment. |
| `comments[].content` | Text of the comment. Long comments may be shortened. |
| `comments[].like_count / comments[].like_count_a11y` | Like count as a display string, such as `10万`. The a11y version adds a text label. Both follow the language set by `language_code`. |
| `comments[].reply_count / comments[].reply_count_text` | Number of replies to the comment, as a display string. The text version adds a label. |
| `comments[].published_time` | Relative time the comment was posted, such as `6年前`. A suffix marks comments that were edited. |
| `comments[].author.display_name` | Handle of the commenter, such as `@grustache4569`. |
| `comments[].author.channel_id / comments[].author.channel_url` | ID and URL of the commenter's YouTube channel. |
| `comments[].author.is_creator / comments[].author.is_verified / comments[].author.is_artist` | Flags that show whether the commenter is the video creator, verified, or an artist. |
| `comments[].reply_continuation_token` | Token tied to this comment. Use it to load the replies to this comment. |
| `continuation_token` | Token for the next page of top-level comments. |

### Notes

- Take the 11-character `video_id` from a YouTube watch URL, the value after `v=`.
- Pass the top-level `continuation_token` from the response as the `continuation_token` parameter to get the next page.
- Counts and times come back as localized display strings, not numbers. The sample uses Chinese text because `language_code` defaults to `zh-CN`. Set `language_code` to change this.
- To read replies to a comment, call [YouTube Video Comment Replies](/apis/youtube/web-v2/video-comment-replies) with the comment's `reply_continuation_token`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/video-comments.json`](../../../../catalog/models/youtube/web-v2/video-comments.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/video-comments

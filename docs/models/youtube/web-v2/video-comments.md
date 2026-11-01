# YouTube Video Comments

`youtube/web-v2/video-comments` · api · YouTube

Retrieves top-level comments for a YouTube video specified by video ID. Supports sorting by top or newest, regional localization, and pagination.

## Pricing

- **$0.0015 per call** (USD)
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

Access first-level comments for any YouTube video using `video_id`. Organize results using `sort_by` and navigate pages with `continuation_token`.

### Use cases

- Analyze audience sentiment and reactions on specific video releases.
- Inspect top or newest viewer discussions for moderation workflows.
- Collect public feedback and reaction counts for engagement reporting.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/video-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"video_id": "dQw4w9WgXcQ"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `video_id` | string | Yes | Purpose: Video ID |
| `sort_by` | string | No | Purpose: Comment sorting method |
| `need_format` | boolean | No | Purpose: Whether to return cleaned simplified data |
| `country_code` | string | No | Purpose: Set region code |
| `language_code` | string | No | Purpose: Set language preference for comments |
| `continuation_token` | string | No | Purpose: Pagination token for next page |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "comments": [
    {
      "comment_id": "Ugzge340dBgB75hWBm54AaABAg",
      "content": "can confirm: he never gave us up",
      "creator_thumbnail_url": "https://yt3.ggpht.com/_ShEGOdg-t5YGJse14Ooq6FYBZqX_QSlhaTNjG06miYusm5lWm1UroLyVx…",
      "like_count": "32万",
      "like_count_a11y": "32万 次赞",
      "published_time": "1年前",
      "reply_count": "961",
      "reply_count_a11y": "961 条回复",
      "reply_count_text": "961 条回复",
      "author": {
        "channel_id": "UCBR8-60-B28hp2BmDPdntcQ",
        "channel_url": "https://www.youtube.com/@YouTube",
        "display_name": "@YouTube"
      }
    }
  ]
}
```

### Notes

- Set `sort_by` to either `top` or `newest` to control comment ordering.
- Supply `continuation_token` to load the next page of comments.
- Set `need_format` to true to receive cleaned and simplified comment data.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/model/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/model/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/model/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/video-comments.json`](../../../../catalog/models/youtube/web-v2/video-comments.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/video-comments

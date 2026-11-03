# YouTube General Search (Web V2, V2) API: pricing, parameters and code examples

`youtube/web-v2/general-search-v2` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns YouTube search results matching a query keyword. Supports filtering by content type, upload date, duration, features, and sorting options, with pagination via tokens.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/general-search-v2", "keyword": "deepseek harness", "sort_by": "relevance", "type": "video"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/general-search-v2', {'keyword': 'deepseek harness', 'sort_by': 'relevance', 'type': 'video'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/general-search-v2", {
  "keyword": "deepseek harness",
  "sort_by": "relevance",
  "type": "video"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/general-search-v2", sandbase.Params{
	"keyword": "deepseek harness",
	"sort_by": "relevance",
	"type": "video",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/general-search-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `type` |  |  | Result type filter - video/channel/playlist/movie  |
| `keyword` |  |  | Search keyword (required for first request)  |
| `sort_by` |  |  | Sort by - relevance/upload_date/view_count/rating  |
| `duration` |  |  | Video duration filter - short(<4min)/medium(4-20min)/long(>20min)  |
| `features` |  |  | Feature filter (comma separated) - live/4k/hd/subtitles/creative_commons/360/vr180/3d/hdr  |
| `upload_date` |  |  | Upload date filter - last_hour/today/this_week/this_month/this_year  |
| `continuation_token` |  |  | Pagination token (pass from previous response for next page)  |

## Details

Returns YouTube search results for a keyword, grouped into videos, channels, playlists and shorts. The only required input is `keyword`. Optional filters narrow results by type, upload date, duration, features and sort order.

### Use cases

- Build a list of top tutorial videos for a topic, with titles, authors, durations and links.
- Track which channels rank for a keyword by reading `author` and `channel_id` on each video.
- Find recent uploads on a subject by combining `upload_date` with `sort_by`.
- Collect thumbnails and description snippets to show search previews in your own app.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/general-search-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "Python tutorial"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `continuation_token` | string | No | Pagination token (pass from previous response for next page) |
| `duration` | string | No | Video duration filter - short(<4min)/medium(4-20min)/long(>20min) |
| `features` | string | No | Feature filter (comma separated) - live/4k/hd/subtitles/creative_commons/360/vr180/3d/hdr |
| `keyword` | string | No | Search keyword (required for first request) |
| `sort_by` | string | No | Sort by - relevance/upload_date/view_count/rating |
| `type` | string | No | Result type filter - video/channel/playlist/movie |
| `upload_date` | string | No | Upload date filter - last_hour/today/this_week/this_month/this_year |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "channels": [],
  "completion_suggestions": [],
  "continuation_token": "EvIEEg9Q…",
  "keyword": "Python tutorial",
  "playlists": [],
  "shorts": [],
  "videos": [
    {
      "author": "Indently",
      "channel_id": "UCuudpdbKmQWq2PPzYgVCWlA",
      "description_snippet": "In this crash course I'll be teaching you the basics of Python in less than 10 m…",
      "duration": "10:30",
      "published_time": "5 years ago",
      "thumbnails": [
        {
          "height": 202,
          "url": "https://i.ytimg.com/vi/fWjsdhR3z3c/hq720.jpg?sqp=-oaymwEjCOgCEMoBSFryq4qpAxUIARU…",
          "width": 360
        }
      ],
      "title": "Learn Python in Less than 10 Minutes for Beginners (Fast & Easy)",
      "url": "https://www.youtube.com/watch?v=fWjsdhR3z3c",
      "video_id": "fWjsdhR3z3c",
      "view_count": "1,897,558 views"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `videos[].title` | Title of the video. |
| `videos[].video_id / videos[].url` | The video ID and the full watch URL for the video. |
| `videos[].author / videos[].channel_id` | Name of the channel that posted the video and its channel ID. |
| `videos[].description_snippet` | Short, cut-off excerpt of the video description. |
| `videos[].duration` | Video length as text, for example `10:30`. |
| `videos[].published_time` | Relative upload age as text, for example `3 months ago`. It is not an exact date. |
| `videos[].view_count` | View count as display text, for example `1,897,558 views`. Parse it before you do math. |
| `videos[].thumbnails[].url / videos[].thumbnails[].width / videos[].thumbnails[].height` | Thumbnail image links with their pixel sizes. |
| `continuation_token` | Token to pass in the next request to get the following page of results. |
| `channels / playlists / shorts` | Lists of matching channels, playlists and shorts. They were empty in this response, which used the default search. |

### Notes

- `keyword` is required for the first request. For later pages, send the `continuation_token` from the previous response.
- Set `type` to `channel` or `playlist` to fill those lists instead of videos.
- `duration` accepts `short`, `medium` or `long`. `sort_by` accepts `relevance`, `upload_date`, `view_count` or `rating`.
- Pass a `channel_id` to [YouTube Channel Videos](/apis/youtube/web-v2/channel-videos), or a `video_id` to [YouTube Video Information (V2)](/apis/youtube/web-v2/video-info-v2), for more detail.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/general-search-v2.json`](../../../../catalog/models/youtube/web-v2/general-search-v2.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/general-search-v2

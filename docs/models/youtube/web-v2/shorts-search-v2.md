# YouTube Shorts Search (V2) API: pricing, parameters and code examples

`youtube/web-v2/shorts-search-v2` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Searches for YouTube Shorts matching a query keyword. Results can be filtered by upload date and sorted by relevance, upload date, view count, or rating.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/web-v2/shorts-search-v2", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/web-v2/shorts-search-v2', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/web-v2/shorts-search-v2", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/web-v2/shorts-search-v2", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/youtube/web-v2/shorts-search-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` |  |  | Search keyword (required for first request)  |
| `sort_by` |  |  | Sort by - relevance/upload_date/view_count/rating  |
| `upload_date` |  |  | Upload date filter - last_hour/today/this_week/this_month/this_year  |
| `continuation_token` |  |  | Pagination token (from previous response)  |

## Details

Returns a list of YouTube Shorts that match a search keyword. Each result has a title, video ID, Shorts URL, view count text, and thumbnails. You can filter by upload date and sort the results.

### Use cases

- Find popular Shorts about a topic such as coding tips.
- List recently uploaded Shorts on a keyword with the `upload_date` filter.
- Rank Shorts for a keyword by `view_count` or `rating` to see which ones perform best.
- Collect Shorts URLs and thumbnails to build a content review list.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/shorts-search-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "coding tips"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `continuation_token` | string | No | Pagination token (from previous response) |
| `keyword` | string | No | Search keyword (required for first request) |
| `sort_by` | string | No | Sort by - relevance/upload_date/view_count/rating |
| `upload_date` | string | No | Upload date filter - last_hour/today/this_week/this_month/this_year |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "continuation_token": "Eo4DEgtj…",
  "keyword": "coding tips",
  "shorts": [
    {
      "author": "",
      "channel_id": "",
      "published_time": "",
      "thumbnails": [
        {
          "height": 720,
          "url": "https://i.ytimg.com/vi/NGlX-1jhYJE/oardefault.jpg?sqp=-oaymwEkCJUDENAFSFqQAgHyq4…",
          "width": 405
        }
      ],
      "title": "How to Learn to Code",
      "url": "https://www.youtube.com/shorts/NGlX-1jhYJE",
      "video_id": "NGlX-1jhYJE",
      "view_count": "9.3M views"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `shorts[]` | List of Shorts that match the keyword. |
| `shorts[].video_id` | ID of the Short. It is also the last part of the `url` value. |
| `shorts[].title` | Title of the Short. It can include hashtags. |
| `shorts[].url` | Link to the Short on YouTube. |
| `shorts[].view_count` | View count as display text, for example `9.3M views`. It is a string, not a number. |
| `shorts[].thumbnails[]` | Thumbnail images. Each one has a `url`, `width`, and `height`. |
| `shorts[].author / shorts[].channel_id / shorts[].published_time` | Channel name, channel ID, and publish time. These were empty strings in this response. |
| `continuation_token` | Token for the next page of results. |
| `keyword` | The search keyword that the response was run for. |

### Notes

- Send `keyword` on the first request. For the next page, send the `continuation_token` from the previous response.
- `sort_by` accepts `relevance`, `upload_date`, `view_count`, or `rating`. `upload_date` accepts `last_hour`, `today`, `this_week`, `this_month`, or `this_year`.
- `author`, `channel_id`, and `published_time` can come back empty. Call [YouTube Video Information (V2)](/apis/youtube/web-v2/video-info-v2) with the `video_id` to get more details about a Short.

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [YouTube Channel Community Posts](/apis/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/apis/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/apis/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/shorts-search-v2.json`](../../../../catalog/models/youtube/web-v2/shorts-search-v2.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/shorts-search-v2

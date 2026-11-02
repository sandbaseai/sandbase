# YouTube General Search (Web V2, V2) API: pricing, parameters and code examples

`youtube/web-v2/general-search-v2` · data API · YouTube · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Returns YouTube search results matching a query keyword. Supports filtering by content type, upload date, duration, features, and sorting options, with pagination via tokens.

## Pricing

- **$0.003 per call** (USD)
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

Search YouTube items by providing a `keyword` query. Pass `continuation_token` from previous responses to paginate through additional results.

### Use cases

- Find YouTube videos, channels, or playlists matching specific search terms.
- Filter video search results by duration, definition, or upload date.
- Sort YouTube content by view count, rating, or upload date.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/general-search-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | string | No | Result type filter - video/channel/playlist/movie |
| `keyword` | string | No | Search keyword (required for first request) |
| `sort_by` | string | No | Sort by - relevance/upload_date/view_count/rating |
| `duration` | string | No | Video duration filter - short(<4min)/medium(4-20min)/long(>20min) |
| `features` | string | No | Feature filter (comma separated) - live/4k/hd/subtitles/creative_commons/360/vr180/3d/hdr |
| `upload_date` | string | No | Upload date filter - last_hour/today/this_week/this_month/this_year |
| `continuation_token` | string | No | Pagination token (pass from previous response for next page) |

### Notes

- `keyword` is required for the initial search request.
- Use `continuation_token` from the previous response to retrieve the next page of results.
- Filter by `type` for videos, channels, playlists, or movies, and combine with `features` such as 4k, hd, or subtitles.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/model/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/model/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/model/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/general-search-v2.json`](../../../../catalog/models/youtube/web-v2/general-search-v2.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/general-search-v2

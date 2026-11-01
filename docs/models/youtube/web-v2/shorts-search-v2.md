# YouTube Shorts Search (V2)

`youtube/web-v2/shorts-search-v2` · api · YouTube

Searches for YouTube Shorts matching a query keyword. Results can be filtered by upload date and sorted by relevance, upload date, view count, or rating.

## Pricing

- **$0.003 per call** (USD)
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

Use this endpoint to search YouTube Shorts videos by entering a `keyword`. You can also filter results by `upload_date` and adjust order with `sort_by`.

### Use cases

- Discover trending YouTube Shorts on specific topics.
- Monitor newly posted short-form video content using date filters.
- Track top-performing Shorts ranked by view count or rating.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/web-v2/shorts-search-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search keyword (required for first request) |
| `sort_by` | string | No | Sort by - relevance/upload_date/view_count/rating |
| `upload_date` | string | No | Upload date filter - last_hour/today/this_week/this_month/this_year |
| `continuation_token` | string | No | Pagination token (from previous response) |

### Notes

- `keyword` is required for the initial query.
- `sort_by` accepts relevance, upload_date, view_count, or rating.
- Use `continuation_token` from a previous response to fetch the next page of results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [YouTube Channel Community Posts](/model/youtube/web-v2/channel-community-posts): Returns community posts from a specific YouTube channel, including text content, polls, votes, and comment counts.
- [YouTube Channel Description](/model/youtube/web-v2/channel-description): Returns YouTube channel details including subscriber counts, video totals, view counts, joined date, and social links.
- [YouTube Channel ID from URL](/model/youtube/web-v2/channel-id): Resolves a YouTube channel URL to its canonical channel ID.

---
Machine-readable: [`catalog/models/youtube/web-v2/shorts-search-v2.json`](../../../../catalog/models/youtube/web-v2/shorts-search-v2.json) · Store page: https://www.sandbase.ai/model/youtube/web-v2/shorts-search-v2

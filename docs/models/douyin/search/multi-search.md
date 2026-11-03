# Douyin Multi Search API: pricing, parameters and code examples

`douyin/search/multi-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns multi-type search results across videos, users, music, and hashtags on Douyin. Supports filtering by keyword, sort order, content type, duration, and post date.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/multi-search"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/multi-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/multi-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/multi-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/search/multi-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for the first page, use the last response cursor for subsequent pages) default `0` |
| `keyword` | string |  | Search keyword, e.g., "Artificial Intelligence" default `"猫咪"` |
| `backtrace` | string |  | Backtrace for pagination, obtained from the last response default `""` |
| `search_id` | string |  | Search ID used for pagination default `""` |
| `sort_type` | string |  | Sorting method default `"0"` |
| `content_type` | string |  | Content type filter default `"0"` |
| `publish_time` | string |  | Publish time filter default `"0"` |
| `filter_duration` | string |  | Video duration filter default `"0"` |

## Details

Query mixed Douyin content types matching a specific `keyword`. Apply filters like `sort_type`, `content_type`, `publish_time`, and `filter_duration` to refine results.

### Use cases

- Retrieve blended Douyin search results matching target keywords.
- Filter content discovery by duration, sort order, and post date.
- Collect suggested search queries and related topic terms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/multi-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | No | Pagination cursor (0 for the first page, use the last response cursor for subsequent pages) |
| `keyword` | string | No | Search keyword, e.g., "Artificial Intelligence" |
| `backtrace` | string | No | Backtrace for pagination, obtained from the last response |
| `search_id` | string | No | Search ID used for pagination |
| `sort_type` | string | No | Sorting method |
| `content_type` | string | No | Content type filter |
| `publish_time` | string | No | Publish time filter |
| `filter_duration` | string | No | Video duration filter |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "business_config": {
    "extra": {
      "guide_search_words": [
        {
          "id": "6527573731718468871",
          "query_id": "6537523068217103624",
          "type": "recom",
          "word": "视频"
        }
      ]
    }
  }
}
```

### Notes

- Set `cursor` to 0 for the first page and use the cursor from the previous response for subsequent pages.
- Pass `backtrace` and `search_id` from the prior response to maintain pagination state.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Challenge Search](/apis/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/apis/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/apis/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/multi-search.json`](../../../../catalog/models/douyin/search/multi-search.json) · Store page: https://www.sandbase.ai/model/douyin/search/multi-search

# Douyin Hashtag Challenge Search (V2) API: pricing, parameters and code examples

`douyin/search/challenge-search-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns Douyin hashtag and challenge search results matching a query keyword. Supports filtering by sort type, content type, post date, and duration with cursor-based pagination.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/challenge-search-v2", "backtrace": "", "content_type": "0", "cursor": 0, "filter_duration": "0", "keyword": "猫咪", "publish_time": "0", "search_id": "", "sort_type": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/challenge-search-v2', {'backtrace': '', 'content_type': '0', 'cursor': 0, 'filter_duration': '0', 'keyword': '猫咪', 'publish_time': '0', 'search_id': '', 'sort_type': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/challenge-search-v2", {
  "backtrace": "",
  "content_type": "0",
  "cursor": 0,
  "filter_duration": "0",
  "keyword": "猫咪",
  "publish_time": "0",
  "search_id": "",
  "sort_type": "0"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/challenge-search-v2", sandbase.Params{
	"backtrace": "",
	"content_type": "0",
	"cursor": 0,
	"filter_duration": "0",
	"keyword": "猫咪",
	"publish_time": "0",
	"search_id": "",
	"sort_type": "0",
})
```

Same call via the path form: `POST /v1/api/douyin/search/challenge-search-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for first request) default `0` |
| `keyword` | string |  | Search keyword, e.g., "game" default `"猫咪"` |
| `backtrace` | string |  | Backtrace for pagination, obtained from the last response default `""` |
| `search_id` | string |  | Search ID for pagination default `""` |
| `sort_type` | string |  | Sorting method default `"0"` |
| `content_type` | string |  | Content type filter default `"0"` |
| `publish_time` | string |  | Publish time filter default `"0"` |
| `filter_duration` | string |  | Video duration filter default `"0"` |

## Details

Search Douyin hashtags and challenges using `keyword` alongside multiple filtering parameters. Use `cursor`, `search_id`, and `backtrace` to paginate through consecutive batches of results.

### Use cases

- Look up trending hashtag challenges across Douyin.
- Filter challenge search results by video duration and post date.
- Track content associated with specific campaign keywords.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/challenge-search-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | No | Pagination cursor (0 for first request) |
| `keyword` | string | No | Search keyword, e.g., "game" |
| `backtrace` | string | No | Backtrace for pagination, obtained from the last response |
| `search_id` | string | No | Search ID for pagination |
| `sort_type` | string | No | Sorting method |
| `content_type` | string | No | Content type filter |
| `publish_time` | string | No | Publish time filter |
| `filter_duration` | string | No | Video duration filter |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "business_data": [
    {
      "card_id": "douyin.doctype_aweme_hashtag",
      "data_id": "0",
      "type": 2
    }
  ]
}
```

### Notes

- Set `cursor` to 0 for the initial search request.
- Pass `search_id` and `backtrace` from the previous response to retrieve the next page of results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Challenge Search](/apis/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Suggestions](/apis/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.
- [Douyin Discussion Search](/apis/douyin/search/discuss-search): Returns discussion and question-and-answer search results from Douyin.

---
Machine-readable: [`catalog/models/douyin/search/challenge-search-v2.json`](../../../../catalog/models/douyin/search/challenge-search-v2.json) · Store page: https://www.sandbase.ai/model/douyin/search/challenge-search-v2

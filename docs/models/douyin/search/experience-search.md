# Douyin Experience Content Search API: pricing, parameters and code examples

`douyin/search/experience-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** sync

Returns Douyin search results for tutorial, knowledge, and experience videos based on keyword queries. Supports filtering by release timing, sorting method, and video duration.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/experience-search", "backtrace": "", "content_type": "0", "cursor": 0, "filter_duration": "0", "keyword": "猫咪", "publish_time": "0", "search_id": "", "sort_type": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/experience-search', {'backtrace': '', 'content_type': '0', 'cursor': 0, 'filter_duration': '0', 'keyword': '猫咪', 'publish_time': '0', 'search_id': '', 'sort_type': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/experience-search", {
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
run, err := c.Run(ctx, "douyin/search/experience-search", sandbase.Params{
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

Same call via the path form: `POST /v1/api/douyin/search/experience-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for first page) default `0` |
| `keyword` | string |  | Search keyword, e.g., "gaming guide" default `"猫咪"` |
| `backtrace` | string |  | Backtrace for pagination, obtained from the last response default `""` |
| `search_id` | string |  | Search ID for pagination default `""` |
| `sort_type` | string |  | Sorting method default `"0"` |
| `content_type` | string |  | Content type filter (usually fixed to video) default `"0"` |
| `publish_time` | string |  | Publish time filter default `"0"` |
| `filter_duration` | string |  | Video duration filter default `"0"` |

## Details

Search Douyin tutorial and knowledge-sharing video content using a `keyword` query. Pass `cursor`, `search_id`, and `backtrace` to paginate through ranked video results.

### Use cases

- Discover tutorial and how-to video guides on specific topics.
- Monitor educational and tip-sharing content trends across Douyin.
- Filter knowledge-focused video results by sorting order and duration.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/experience-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | No | Pagination cursor (0 for first page) |
| `keyword` | string | No | Search keyword, e.g., "gaming guide" |
| `backtrace` | string | No | Backtrace for pagination, obtained from the last response |
| `search_id` | string | No | Search ID for pagination |
| `sort_type` | string | No | Sorting method |
| `content_type` | string | No | Content type filter (usually fixed to video) |
| `publish_time` | string | No | Publish time filter |
| `filter_duration` | string | No | Video duration filter |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "business_data": [
    {
      "card_id": "douyin.doctype_aweme_video",
      "data_id": "0_7693432525880939001",
      "type": 12,
      "data": {
        "card_id": "douyin.doctype_aweme_video",
        "card_type": 1,
        "doc_type": 153,
        "provider_doc_id": 7693432525880939001,
        "provider_doc_id_str": "7693432525880939001",
        "type": 1
      },
      "log": {
        "rank": "1"
      }
    }
  ]
}
```

### Notes

- Set `cursor` to 0 for the initial page.
- Pass `search_id` and `backtrace` from previous response payloads to paginate.
- Refine queries using filters such as `sort_type` and `filter_duration`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Challenge Search](/model/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/model/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/model/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/experience-search.json`](../../../../catalog/models/douyin/search/experience-search.json) · Store page: https://www.sandbase.ai/model/douyin/search/experience-search

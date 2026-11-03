# Douyin Image Search API: pricing, parameters and code examples

`douyin/search/image-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns image-based search results from Douyin matching a search keyword. Supports sorting, content filtering, post date filters, and pagination parameters.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/image-search", "backtrace": "", "content_type": "0", "cursor": 0, "filter_duration": "0", "keyword": "猫咪", "publish_time": "0", "search_id": "", "sort_type": "0"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/image-search', {'backtrace': '', 'content_type': '0', 'cursor': 0, 'filter_duration': '0', 'keyword': '猫咪', 'publish_time': '0', 'search_id': '', 'sort_type': '0'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/image-search", {
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
run, err := c.Run(ctx, "douyin/search/image-search", sandbase.Params{
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

Same call via the path form: `POST /v1/api/douyin/search/image-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for first request) default `0` |
| `keyword` | string |  | Search keyword, e.g., "cat" default `"猫咪"` |
| `backtrace` | string |  | Backtrace for pagination, obtained from the last response default `""` |
| `search_id` | string |  | Search ID for pagination default `""` |
| `sort_type` | string |  | Sorting method default `"0"` |
| `content_type` | string |  | Content type (Fixed to 2 for images) default `"0"` |
| `publish_time` | string |  | Publish time filter default `"0"` |
| `filter_duration` | string |  | Video duration filter default `"0"` |

## Details

Look up Douyin image search results by specifying a `keyword`. Paginate through results using `cursor`, `search_id`, and `backtrace`.

### Use cases

- Search for image posts matching specific keywords.
- Track relevant graphic content and topics on Douyin.
- Filter image search results by post date and sorting criteria.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/image-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | No | Pagination cursor (0 for first request) |
| `keyword` | string | No | Search keyword, e.g., "cat" |
| `backtrace` | string | No | Backtrace for pagination, obtained from the last response |
| `search_id` | string | No | Search ID for pagination |
| `sort_type` | string | No | Sorting method |
| `content_type` | string | No | Content type (Fixed to 2 for images) |
| `publish_time` | string | No | Publish time filter |
| `filter_duration` | string | No | Video duration filter |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "business_data": [
    {
      "card_id": "douyin.doctype_aweme_image",
      "data_id": "0",
      "type": 11,
      "data": {
        "card_id": "douyin.doctype_aweme_image",
        "card_type": 1,
        "doc_type": 303,
        "provider_doc_id": 7693421414359489253,
        "provider_doc_id_str": "7693421414359489253",
        "type": 1
      }
    }
  ]
}
```

### Notes

- `cursor` starts at 0 for the initial request.
- `content_type` is fixed to 2 for images.
- `backtrace` and `search_id` are passed from previous responses for pagination.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Challenge Search](/apis/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/apis/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/apis/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/image-search.json`](../../../../catalog/models/douyin/search/image-search.json) · Store page: https://www.sandbase.ai/model/douyin/search/image-search

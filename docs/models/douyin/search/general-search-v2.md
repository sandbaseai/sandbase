# Douyin General Search (V2) API: pricing, parameters and code examples

`douyin/search/general-search-v2` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call (free daily quota) · **Modes:** sync

Returns search results from Douyin's general search tab. Supports filtering by keyword, sort method, post date, video duration, and content type.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/general-search-v2"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/general-search-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/general-search-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/general-search-v2", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/search/general-search-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for the first page, use the last response cursor for subsequent pages) default `0` |
| `keyword` | string |  | Search keyword, e.g., "cat" default `"猫咪"` |
| `backtrace` | string |  | Backtrace identifier (empty for first request, obtained from previous response for pagination) default `""` |
| `search_id` | string |  | Search ID (empty for first request, obtained from previous response for pagination) default `""` |
| `sort_type` | string |  | Sorting method default `"0"` |
| `content_type` | string |  | Content type filter default `"0"` |
| `publish_time` | string |  | Publish time filter default `"0"` |
| `filter_duration` | string |  | Video duration filter default `"0"` |

## Details

Look up Douyin general search results using a query `keyword` and optional parameters for sorting and content filtering.

### Use cases

- Retrieve mixed search cards matching specific keywords on Douyin.
- Filter Douyin search items by post date, video length, or sort order.
- Paginate through general search rankings using session tokens.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/general-search-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | No | Pagination cursor (0 for the first page, use the last response cursor for subsequent pages) |
| `keyword` | string | No | Search keyword, e.g., "cat" |
| `backtrace` | string | No | Backtrace identifier (empty for first request, obtained from previous response for pagination) |
| `search_id` | string | No | Search ID (empty for first request, obtained from previous response for pagination) |
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
      "card_id": "douyin.doctype_aweme_image",
      "data_id": "0",
      "type": 1,
      "data": {
        "card_id": "douyin.doctype_aweme_image",
        "card_type": 1,
        "doc_type": 303,
        "provider_doc_id": 7621594405576706417,
        "provider_doc_id_str": "7621594405576706417",
        "type": 1
      },
      "log": {
        "search_result_id": "7621594405576706417"
      }
    }
  ]
}
```

### Notes

- Set `cursor` to 0 for initial requests and pass the returned value for subsequent pages.
- Pass `search_id` and `backtrace` from previous responses to maintain pagination state.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Challenge Search](/model/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/model/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/model/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/general-search-v2.json`](../../../../catalog/models/douyin/search/general-search-v2.json) · Store page: https://www.sandbase.ai/model/douyin/search/general-search-v2

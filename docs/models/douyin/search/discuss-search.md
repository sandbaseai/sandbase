# Douyin Discussion Search API: pricing, parameters and code examples

`douyin/search/discuss-search` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns discussion and question-and-answer search results from Douyin. Supports filtering by keyword, sort order, content type, post time, and video duration.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/discuss-search"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/discuss-search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/discuss-search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/discuss-search", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/search/discuss-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer |  | Pagination cursor (0 for first page, use the last response cursor for subsequent pages)  |
| `keyword` | string |  | Search keyword, e.g., "study abroad"  |
| `backtrace` | string |  | Backtrace for pagination, obtained from the last response  |
| `search_id` | string |  | Search ID used for pagination  |
| `sort_type` | string |  | Sorting method  |
| `content_type` | string |  | Content type filter  |
| `publish_time` | string |  | Publish time filter  |
| `filter_duration` | string |  | Video duration filter  |

## Details

Search Douyin discussion and Q&A content using a search query via `keyword`. Supports pagination and refined filtering via parameters like `sort_type` and `content_type`.

### Use cases

- Monitor audience questions and discussions around specific topic keywords.
- Track public opinions and popular discussion threads on Douyin.
- Filter community Q&A content by duration and sorting order.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/discuss-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | No | Pagination cursor (0 for first page, use the last response cursor for subsequent pages) |
| `keyword` | string | No | Search keyword, e.g., "study abroad" |
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
  "business_data": [
    {
      "card_id": "douyin.doctype_aweme_comment",
      "data_id": "0",
      "type": 999,
      "data": {
        "card_id": "douyin.doctype_aweme_comment",
        "card_type_name": "doctype_aweme_comment",
        "origin_type": 0
      }
    }
  ]
}
```

### Notes

- Set `cursor` to 0 for the initial page, then pass values from the prior response for subsequent requests.
- Paging across result sets relies on `backtrace` and `search_id` retrieved from preceding response payloads.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Challenge Search](/model/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/model/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Hashtag Suggestions](/model/douyin/search/challenge-suggest): Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

---
Machine-readable: [`catalog/models/douyin/search/discuss-search.json`](../../../../catalog/models/douyin/search/discuss-search.json) · Store page: https://www.sandbase.ai/model/douyin/search/discuss-search

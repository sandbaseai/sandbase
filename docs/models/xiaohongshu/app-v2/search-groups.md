# Xiaohongshu (RED) Group Search API: pricing, parameters and code examples

`xiaohongshu/app-v2/search-groups` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Searches Xiaohongshu community groups by keyword with support for pagination, recommendation flags, and search filters.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/app-v2/search-groups", "is_recommend": 0, "keyword": "OpenAI", "page_no": 0, "search_id": "", "source": "unifiedSearchGroup"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/app-v2/search-groups', {'is_recommend': 0, 'keyword': 'OpenAI', 'page_no': 0, 'search_id': '', 'source': 'unifiedSearchGroup'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/app-v2/search-groups", {
  "is_recommend": 0,
  "keyword": "OpenAI",
  "page_no": 0,
  "search_id": "",
  "source": "unifiedSearchGroup"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/app-v2/search-groups", sandbase.Params{
	"is_recommend": 0,
	"keyword": "OpenAI",
	"page_no": 0,
	"search_id": "",
	"source": "unifiedSearchGroup",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/app-v2/search-groups` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `source` | string |  | Source, default "unifiedSearchGroup" default `"unifiedSearchGroup"` |
| `keyword` | string | yes | Search keyword  |
| `page_no` | integer |  | Page number, start from 0 default `0` |
| `search_id` | string |  | Search ID, pass value from first search response for pagination default `""` |
| `is_recommend` | integer |  | Is recommend, 0=no, 1=yes default `0` |

## Details

Searches Xiaohongshu community groups matching a target `keyword`, supporting pagination and recommendation settings.

### Use cases

- Discover community groups matching specific topic keywords.
- Browse group search filter options for refined queries.
- Paginate through group search results using returned identifiers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/app-v2/search-groups" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `source` | string | No | Source, default "unifiedSearchGroup" |
| `page_no` | integer | No | Page number, start from 0 |
| `search_id` | string | No | Search ID, pass value from first search response for pagination |
| `is_recommend` | integer | No | Is recommend, 0=no, 1=yes |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "group_search_filters": [
      {
        "options": [
          {
            "id": "default",
            "name": "All"
          }
        ]
      }
    ]
  }
}
```

### Notes

- Pagination starts at index 0 for `page_no`.
- Pass `search_id` from the initial search response when requesting subsequent pages.
- Set `is_recommend` to 1 to enable recommendations, or 0 for standard search.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Xiaohongshu (RED) Creator Hot Inspiration Feed](/apis/xiaohongshu/app-v2/creator-hot-inspiration-feed): Retrieves creator center hot inspiration feed items with topic titles, popularity scores, and deeplinks.
- [Xiaohongshu (RED) Inspiration Feed](/apis/xiaohongshu/app-v2/creator-inspiration-feed): Returns recommended inspiration feed items and trending topics from Xiaohongshu (RED).
- [Xiaohongshu (RED) Image Note Details](/apis/xiaohongshu/app-v2/image-note-detail): Returns detailed information for a Xiaohongshu image note.

---
Machine-readable: [`catalog/models/xiaohongshu/app-v2/search-groups.json`](../../../../catalog/models/xiaohongshu/app-v2/search-groups.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/app-v2/search-groups

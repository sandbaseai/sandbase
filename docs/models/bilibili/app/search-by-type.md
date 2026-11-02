# Bilibili Search by Type API: pricing, parameters and code examples

`bilibili/app/search-by-type` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns categorized search results from Bilibili based on a target query string. Supports filtering by search type, adjusting sort order, and cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/search-by-type", "cursor": "", "keyword": "OpenAI", "order": 0, "page_size": 20, "search_type": "video"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/search-by-type', {'cursor': '', 'keyword': 'OpenAI', 'order': 0, 'page_size': 20, 'search_type': 'video'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/search-by-type", {
  "cursor": "",
  "keyword": "OpenAI",
  "order": 0,
  "page_size": 20,
  "search_type": "video"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/search-by-type", sandbase.Params{
	"cursor": "",
	"keyword": "OpenAI",
	"order": 0,
	"page_size": 20,
	"search_type": "video",
})
```

Same call via the path form: `POST /v1/api/bilibili/app/search-by-type` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `order` | integer |  | Sort order default `0` |
| `cursor` | string |  | Pagination cursor. Leave empty for the first page; for the next page pass default `""` |
| `keyword` | string | yes | Search keyword (required)  |
| `page_size` | integer |  | Results per page default `20` |
| `search_type` | string |  | Search type default `"video"` |

## Details

Query Bilibili content categorized by type using the required `keyword` parameter. You can optionally filter by `search_type`, apply an `order` index, and paginate through results.

### Use cases

- Search for specific video items matching a keyword on Bilibili.
- Filter platform search results by specified category types.
- Paginate through Bilibili catalog queries using cursor tokens.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/search-by-type" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword (required) |
| `order` | integer | No | Sort order |
| `cursor` | string | No | Pagination cursor. |
| `page_size` | integer | No | Results per page |
| `search_type` | string | No | Search type |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "items": [
      {
        "av": {
          "author": "红客官方账号",
          "duration": "9:29",
          "ptime": "1788174347",
          "title": "全球首例！700个AI失控组团攻击，全程无人参与，OpenAI都懵了",
          "view_content": "5.9万"
        }
      }
    ]
  }
}
```

### Notes

- Leave `cursor` empty for the initial request, then pass the returned cursor string for subsequent pages.
- `keyword` is required for every search request.
- Use `search_type` to define the target category such as video.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili App Bangumi Tab](/model/bilibili/app/bangumi-tab): Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.
- [Bilibili App Cinema Tab](/model/bilibili/app/cinema-tab): Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query para…
- [Bilibili App Home Feed](/model/bilibili/app/home-feed): Returns recommended video items from the Bilibili app home feed.

---
Machine-readable: [`catalog/models/bilibili/app/search-by-type.json`](../../../../catalog/models/bilibili/app/search-by-type.json) · Store page: https://www.sandbase.ai/model/bilibili/app/search-by-type

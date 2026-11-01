# Bilibili App Search All

`bilibili/app/search-all` · api · Bilibili

Returns comprehensive search results across Bilibili content via the mobile app interface. Filters results by search keyword, sorting order, and pagination parameters.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/search-all", "cursor": "", "keyword": "OpenAI", "order": 0, "page_size": 20}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/search-all', {'cursor': '', 'keyword': 'OpenAI', 'order': 0, 'page_size': 20})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/search-all", {
  "cursor": "",
  "keyword": "OpenAI",
  "order": 0,
  "page_size": 20
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/search-all", sandbase.Params{
	"cursor": "",
	"keyword": "OpenAI",
	"order": 0,
	"page_size": 20,
})
```

Same call via the path form: `POST /v1/api/bilibili/app/search-all` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `order` | integer |  | Sort order (0=comprehensive) default `0` |
| `cursor` | string |  | Pagination cursor. Leave empty for the first page; for the next page pass default `""` |
| `keyword` | string | yes | Search keyword (required)  |
| `page_size` | integer |  | Results per page default `20` |

## Details

Query general Bilibili search results using a specified `keyword`. Supports sorting and cursor-based pagination.

### Use cases

- Discover videos and collections matching a query on Bilibili.
- Track topical discussions and trending keywords across the platform.
- Integrate Bilibili app search items into external discovery tools.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/search-all" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword (required) |
| `order` | integer | No | Sort order (0=comprehensive) |
| `cursor` | string | No | Pagination cursor. |
| `page_size` | integer | No | Results per page |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "item": [
      {
        "linktype": "collection_card"
      }
    ]
  }
}
```

### Notes

- Pass an empty `cursor` for the initial page, then supply the returned cursor value for subsequent pages.
- Use `order` set to 0 for comprehensive sorting.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili App Bangumi Tab](/model/bilibili/app/bangumi-tab): Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.
- [Bilibili App Cinema Tab](/model/bilibili/app/cinema-tab): Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query para…
- [Bilibili App Home Feed](/model/bilibili/app/home-feed): Returns recommended video items from the Bilibili app home feed.

---
Machine-readable: [`catalog/models/bilibili/app/search-all.json`](../../../../catalog/models/bilibili/app/search-all.json) · Store page: https://www.sandbase.ai/model/bilibili/app/search-all

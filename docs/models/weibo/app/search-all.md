# Weibo Comprehensive Search API: pricing, parameters and code examples

`weibo/app/search-all` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns comprehensive search results from Weibo for a specified keyword. Supports pagination and filtering by search type.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/search-all", "page": 1, "query": "OpenAI", "search_type": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/search-all', {'page': 1, 'query': 'OpenAI', 'search_type': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/search-all", {
  "page": 1,
  "query": "OpenAI",
  "search_type": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/search-all", sandbase.Params{
	"page": 1,
	"query": "OpenAI",
	"search_type": 1,
})
```

Same call via the path form: `POST /v1/api/weibo/app/search-all` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number, starts from 1 (default 1) default `1`; range 1– |
| `query` | string | yes | Search keyword (required)  |
| `search_type` | integer |  | Search type default `1` |

## Details

Query comprehensive Weibo search results by providing a search keyword in `query`. Filter results by `search_type` and paginate through `page`.

### Use cases

- Retrieve general search results matching a keyword on Weibo.
- Filter platform search results by specified search types.
- Paginate across search listings for topic research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/search-all" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (required) |
| `page` | integer | No | Page number, starts from 1 (default 1) |
| `search_type` | integer | No | Search type |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "dsl": {
    "xml": [
      {
        "name": "cardCoupon.xml"
      }
    ]
  }
}
```

### Notes

- `page` starts from 1 with a default value of 1.
- `query` is required to specify the search keyword.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo App AI Smart Search](/model/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/model/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/model/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/search-all.json`](../../../../catalog/models/weibo/app/search-all.json) · Store page: https://www.sandbase.ai/model/weibo/app/search-all

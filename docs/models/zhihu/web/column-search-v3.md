# Zhihu Column Search API: pricing, parameters and code examples

`zhihu/web/column-search-v3` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches Zhihu columns matching a specified query term. Returns matching column profiles, follower counts, article totals, and snippet highlights with pagination support.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/column-search-v3", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/column-search-v3', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/column-search-v3", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/column-search-v3", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/column-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of columns per page default `"20"` |
| `offset` | string |  | Offset default `"0"` |
| `keyword` | string | yes | Search Keywords  |
| `search_hash_id` | string |  | Search Hash ID default `""` |

## Details

Query Zhihu columns by passing a search term into `keyword`. You can paginate through matches using `offset` and `limit`.

### Use cases

- Discover topic-focused Zhihu columns by keyword.
- Track column follower counts and publication volume.
- Retrieve Zhihu column identifiers and descriptions for market research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/column-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keywords |
| `limit` | string | No | Number of columns per page |
| `offset` | string | No | Offset |
| `search_hash_id` | string | No | Search Hash ID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "id": "openai",
      "type": "search_result",
      "highlight": {
        "content": "介绍 OpenAI 的一些工作",
        "description": "介绍 OpenAI 的一些工作",
        "title": "OpenAI"
      },
      "object": {
        "articles_count": 5,
        "column_type": "normal",
        "description": "介绍 OpenAI 的一些工作",
        "followers": 3153,
        "id": "openai",
        "image_url": "https://pica.zhimg.com/v2-9d09bc4b22fc4a71c21e789f77effb48_r.jpg?source=4e949a73"
      }
    }
  ]
}
```

### Notes

- Supports pagination via `limit` to control page size and `offset` to navigate pages.
- Requires `keyword` as the search query parameter.
- Accepts an optional `search_hash_id` parameter.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/column-search-v3.json`](../../../../catalog/models/zhihu/web/column-search-v3.json) · Store page: https://www.sandbase.ai/model/zhihu/web/column-search-v3

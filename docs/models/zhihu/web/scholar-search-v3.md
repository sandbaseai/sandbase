# Zhihu Scholar Paper Search API: pricing, parameters and code examples

`zhihu/web/scholar-search-v3` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search Zhihu Scholar papers matching specified keywords and filters. Returns paper details including IDs, titles, highlight snippets, and Zhihu paper URLs.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/scholar-search-v3", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/scholar-search-v3', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/scholar-search-v3", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/scholar-search-v3", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/scholar-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of papers per page default `"25"` |
| `offset` | string |  | Offset default `"0"` |
| `keyword` | string | yes | Search Keywords  |
| `indexed_by` | string |  |  default `""` |
| `classification` | string |  |  default `""` |
| `advanced_filter` | string |  |  default `"keywords,title,authors,abstract"` |

## Details

Query Zhihu Scholar for academic papers using `keyword`. Refine results using `advanced_filter`, `classification`, and pagination parameters.

### Use cases

- Search for academic publications and research papers on Zhihu.
- Filter scholarly documents by keywords, title, authors, or abstract.
- Collect paper URLs and metadata for research analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/scholar-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keywords |
| `limit` | string | No | Number of papers per page |
| `offset` | string | No | Offset |
| `indexed_by` | string | No | — |
| `classification` | string | No | — |
| `advanced_filter` | string | No | — |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "id": "1984217783119151617",
      "type": "search_result",
      "highlight": {
        "title": "“有效加速”与“超级对齐”之争:OpenAI事件对人工智能发展方向的启示"
      },
      "object": {
        "id": "1984217783119151617",
        "title": "“有效加速”与“超级对齐”之争:OpenAI事件对人工智能发展方向的启示",
        "type": "scholar",
        "url": "https://www.zhihu.com/kvip/sku/paper/1984217783119151617"
      }
    }
  ]
}
```

### Notes

- Paginate results using `limit` and `offset`.
- Filter search scopes using `advanced_filter`, such as keywords, title, authors, or abstract.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/scholar-search-v3.json`](../../../../catalog/models/zhihu/web/scholar-search-v3.json) · Store page: https://www.sandbase.ai/model/zhihu/web/scholar-search-v3

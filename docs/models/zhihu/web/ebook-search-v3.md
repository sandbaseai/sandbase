# Zhihu Ebook Search API: pricing, parameters and code examples

`zhihu/web/ebook-search-v3` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Searches Zhihu for ebooks matching a query term. Returns publication details including commodity IDs, SKU IDs, and direct product links.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/ebook-search-v3", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/ebook-search-v3', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/ebook-search-v3", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/ebook-search-v3", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/ebook-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of ebooks per page default `"20"` |
| `offset` | string |  | Offset default `"0"` |
| `keyword` | string | yes | Search Keywords  |
| `search_hash_id` | string |  | Search Hash ID default `""` |

## Details

Search for ebooks and publications on Zhihu using `keyword`. Results support pagination using `limit` and `offset` parameters.

### Use cases

- Search for digital books and publications on Zhihu by keyword.
- Retrieve Zhihu ebook commodity IDs and SKU IDs for catalog indexing.
- Collect direct links to Zhihu ebook store pages.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/ebook-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keywords |
| `limit` | string | No | Number of ebooks per page |
| `offset` | string | No | Offset |
| `search_hash_id` | string | No | Search Hash ID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "id": 674492,
      "type": "knowledge_ad",
      "object": {
        "commodity_id": "120480981",
        "commodity_type": "publication",
        "sku_id": "1821568022831316992",
        "slave_url": "https://www.zhihu.com/kvip/sku/ebook/120480981",
        "tab_type": "publication",
        "url": "https://www.zhihu.com/kvip/sku/ebook/120480981"
      }
    }
  ]
}
```

### Notes

- Control pagination using the `limit` and `offset` query parameters.
- An optional `search_hash_id` can be supplied to track search sessions.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/ebook-search-v3.json`](../../../../catalog/models/zhihu/web/ebook-search-v3.json) · Store page: https://www.sandbase.ai/model/zhihu/web/ebook-search-v3

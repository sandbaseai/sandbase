# Zhihu Column Article Detail API: pricing, parameters and code examples

`zhihu/web/column-article-detail` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed information and metadata for a specific Zhihu column article, including author profile details, using a provided article ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/column-article-detail", "article_id": "669214677"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/column-article-detail', {'article_id': '669214677'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/column-article-detail", {
  "article_id": "669214677"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/column-article-detail", sandbase.Params{
	"article_id": "669214677",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/column-article-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `article_id` | string | yes | Article ID  |

## Details

Retrieves complete column article details from Zhihu by specifying the `article_id`.

### Use cases

- Display Zhihu column article content alongside author topic badges.
- Extract author metadata and topic expertise from specific column articles.
- Archive public column posts and contributor details for research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/column-article-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"article_id": "669214677"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `article_id` | string | Yes | Article ID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "author": {
    "badge": [
      {
        "topics": [
          {
            "id": "19609249",
            "name": "网球",
            "type": "topic",
            "url": "https://www.zhihu.com/topic/19609249"
          }
        ]
      }
    ]
  }
}
```

### Notes

- `article_id` is required to look up the column article.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/column-article-detail.json`](../../../../catalog/models/zhihu/web/column-article-detail.json) · Store page: https://www.sandbase.ai/model/zhihu/web/column-article-detail

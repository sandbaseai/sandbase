# Zhihu Similar Column Recommendations API: pricing, parameters and code examples

`zhihu/web/column-recommend` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended similar columns and articles for a specified Zhihu article ID, with support for pagination limits and offsets.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/column-recommend", "article_id": "669214677"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/column-recommend', {'article_id': '669214677'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/column-recommend", {
  "article_id": "669214677"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/column-recommend", sandbase.Params{
	"article_id": "669214677",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/column-recommend` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of columns per page default `"12"` |
| `offset` | string |  | Offset default `"0"` |
| `article_id` | string | yes | Article ID  |

## Details

Retrieve recommended columns and related content based on a Zhihu article by passing its `article_id`.

### Use cases

- Displaying related Zhihu columns alongside article content.
- Discovering relevant topics and publications based on an article ID.
- Building recommendation feeds for reading interfaces.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/column-recommend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"article_id": "669214677"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `article_id` | string | Yes | Article ID |
| `limit` | string | No | Number of columns per page |
| `offset` | string | No | Offset |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "article": {
        "article_type": "normal",
        "bar_plugins_flip_time": 3000,
        "content_need_truncated": false,
        "id": "24803672",
        "image_url": "https://pica.zhimg.com/v2-4cc88e957c3b9c3512462ee84327b108_720w.jpg?source=172ae18b",
        "title": "又被父母逼着返乡工作了吧？！"
      }
    }
  ]
}
```

### Notes

- Use `limit` to specify the number of columns returned per request.
- Use `offset` to page through recommendation results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/column-recommend.json`](../../../../catalog/models/zhihu/web/column-recommend.json) · Store page: https://www.sandbase.ai/model/zhihu/web/column-recommend

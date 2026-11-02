# Zhihu Column Article Relationship API: pricing, parameters and code examples

`zhihu/web/column-relationship` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns interaction details and relationship metadata for a Zhihu column article, including endorsement reaction text and navigation action links by article ID.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/column-relationship", "article_id": "669214677"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/column-relationship', {'article_id': '669214677'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/column-relationship", {
  "article_id": "669214677"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/column-relationship", sandbase.Params{
	"article_id": "669214677",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/column-relationship` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `article_id` | string | yes | Article ID  |

## Details

Retrieve interaction and endorsement relationship details for a Zhihu article by providing an `article_id`.

### Use cases

- Display endorsement counts and voter reaction summaries for a column article.
- Obtain in-app deep link URLs for article voter lists.
- Monitor user reaction status on specific Zhihu column articles.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/column-relationship" \
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
  "action_url": "zhihu://hybrid?zh_url=https://www.zhihu.com/appview/article/669214677/voters&zh_hide_nav_…",
  "text": "291 人赞同了该文章",
  "text_size": 14,
  "type": "reaction_endorse"
}
```

### Notes

- Requires a valid `article_id` identifying the Zhihu article.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/model/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/model/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/model/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/column-relationship.json`](../../../../catalog/models/zhihu/web/column-relationship.json) · Store page: https://www.sandbase.ai/model/zhihu/web/column-relationship

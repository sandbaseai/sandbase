# Zhihu Column Article Relationship API: pricing, parameters and code examples

`zhihu/web/column-relationship` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns interaction details and relationship metadata for a Zhihu column article, including endorsement reaction text and navigation action links by article ID.

## Pricing

- **$0.001 per call** (USD)
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

Returns the endorsement reaction summary for one Zhihu column article. It needs the `article_id` of the article. The response includes a display text such as the number of people who endorsed the article and an in-app link to the voter list.

### Use cases

- Show the endorsement summary line for a column article in a dashboard.
- Extract the voter list deep link for a given article.
- Parse the endorsement count from the `text` string to track how many people endorsed an article.
- Check which reaction type Zhihu attaches to an article through the `type` field.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/column-relationship" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"article_id": "669214677"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `article_id` | string | Yes | Article ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "Member": null,
  "action_url": "zhihu://hybrid?zh_url=https://www.zhihu.com/appview/article/669214677/voters&zh_…",
  "is_bold": false,
  "text": "291 人赞同了该文章",
  "text_color": "GBL05A",
  "text_size": 14,
  "type": "reaction_endorse"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `text` | Display string for the reaction. In the example it reads "291 人赞同了该文章" (291 people endorsed the article), so the count sits inside the text. |
| `type` | Kind of relationship item. The example value is `reaction_endorse`. |
| `action_url` | Zhihu app deep link that opens the voter list page for the article. The link embeds the article ID. |
| `text_color` | Color code Zhihu uses to style the text, for example `GBL05A`. |
| `text_size / is_bold` | Styling hints for the text. `text_size` is a number (14 in the example) and `is_bold` is a boolean. |
| `Member` | Member data tied to the reaction. It is `null` in the example response. |

### Notes

- The endorsement count is not a separate number field. Read it from the `text` string.
- `action_url` uses the `zhihu://` scheme, so it opens in the Zhihu app and not in a browser.
- To get the article title, author and body, call [Zhihu Column Article Detail](/apis/zhihu/web/column-article-detail) with the same ID.
- To find articles in a column, use [Zhihu Column Articles](/apis/zhihu/web/column-articles).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/column-relationship.json`](../../../../catalog/models/zhihu/web/column-relationship.json) · Store page: https://www.sandbase.ai/model/zhihu/web/column-relationship

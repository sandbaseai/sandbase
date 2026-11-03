# Zhihu Column Articles API: pricing, parameters and code examples

`zhihu/web/column-articles` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns articles from a specific Zhihu column, including titles, content snippets, vote counts, and author profile details.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/column-articles", "column_id": "zhangjiawei"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/column-articles', {'column_id': 'zhangjiawei'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/column-articles", {
  "column_id": "zhangjiawei"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/column-articles", sandbase.Params{
	"column_id": "zhangjiawei",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/column-articles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of articles per page default `"10"` |
| `offset` | string |  | Offset default `"0"` |
| `column_id` | string | yes | Column ID  |

## Details

Retrieve a list of articles from a Zhihu column by providing `column_id`.

### Use cases

- Retrieve articles and text excerpts from specific Zhihu columns.
- Track engagement metrics like vote counts and comment totals on column posts.
- Archive column article feeds and author metadata for content aggregation.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/column-articles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"column_id": "zhangjiawei"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `column_id` | string | Yes | Column ID |
| `limit` | string | No | Number of articles per page |
| `offset` | string | No | Offset |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "article_type": "normal",
      "comment_count": 0,
      "content": "雄鹿上季没进季后赛：就此结束了九连季后赛的旅途。当然不是巧合：扬尼斯上季，生涯第一次没打满61场比赛。“只要扬尼斯健康，总能混个肚子饱进季后赛”，如今红利吃完了。接下来的2026…",
      "content_need_truncated": true,
      "id": "2090784445787796071",
      "title": "30天30队·雄鹿：没了扬尼斯，重新试错吧？",
      "type": "article",
      "updated": 1791261900,
      "url": "https://zhuanlan.zhihu.com/p/2090784445787796071",
      "voteup_count": 25,
      "author": {
        "id": "f9de84865e3e8455a09af78bfe4d1da5",
        "name": "张佳玮",
        "type": "people",
        "url": "/people/f9de84865e3e8455a09af78bfe4d1da5",
        "user_type": "people"
      },
      "suggest_edit": {
        "status": false
      }
    }
  ]
}
```

### Notes

- Use `limit` to control the number of articles returned per page.
- Use `offset` for pagination across the article list.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/column-articles.json`](../../../../catalog/models/zhihu/web/column-articles.json) · Store page: https://www.sandbase.ai/model/zhihu/web/column-articles

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

Returns a page of articles from one Zhihu column. Each article includes its title, a text excerpt, an HTML content snippet, vote and comment counts, and author details. The only required input is `column_id`.

### Use cases

- Pull the latest posts from a Zhihu column to feed a reading list or newsletter.
- Compare `voteup_count` and `comment_count` across a column's articles to find its most popular pieces.
- Archive a column's article titles, links and publish times for offline analysis.
- Collect author headline and badge data for the writer behind a column.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/column-articles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"column_id": "zhangjiawei"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `column_id` | string | Yes | Column ID |
| `limit` | string | No | Number of articles per page |
| `offset` | string | No | Offset |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "admin_closed_comment": false,
      "article_type": "normal",
      "author": {
        "avatar_url": "https://picx.zhimg.com/v2-d626957872f9b38fa594394db2d2e6e7_l.jpg?source=d16d100b",
        "avatar_url_template": "https://pic1.zhimg.com/v2-d626957872f9b38fa594394db2d2e6e7.jpg?source=d16d100b",
        "badge": [
          {
            "description": "优秀答主",
            "topics": [],
            "type": "best_answerer"
          }
        ],
        "description": "",
        "gender": 1,
        "headline": "公号：张佳玮写字的地方",
        "id": "f9de84865e3e8455a09af78bfe4d1da5",
        "is_advertiser": false
      },
      "can_comment": {
        "reason": "",
        "status": true
      },
      "comment_count": 54,
      "comment_permission": "all",
      "content": "<p data-pid=\"1xZNrKHM\">金庸文人趣味最直白地发作，是《书剑恩仇录》里嘲讽乾隆。</p><p data-pid=\"XEJ4VBqT\">说乾隆…",
      "content_need_truncated": true,
      "copyright_permission": "need_review",
      "created": 1793358930,
      "excerpt": "金庸文人趣味最直白地发作，是《书剑恩仇录》里嘲讽乾隆。 说乾隆去嫖院： 古往今来，嫖院之人何止千万，却要算乾隆这次嫖得最为规模宏大，当真是好威风，好煞气，于日后…",
      "excerpt_title": ""
    }
  ],
  "need_force_login": false,
  "paging": {
    "is_end": false,
    "is_start": true,
    "next": "http://www.zhihu.com/api/v4/columns/zhangjiawei/items?limit=10&ws_qiangzhisafe=0…",
    "previous": "http://www.zhihu.com/api/v4/columns/zhangjiawei/items?limit=10&ws_qiangzhisafe=0…",
    "totals": 1560
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].title` | Title of the article. |
| `data[].url / data[].id` | Link to the article on zhuanlan.zhihu.com and its numeric ID. The ID is also the last part of the URL. |
| `data[].excerpt` | Plain-text excerpt of the article, cut short. Images appear as `[图片]`. |
| `data[].content` | Start of the article body as HTML. `content_need_truncated` is `true` when the text is cut. |
| `data[].voteup_count / data[].comment_count` | Number of upvotes and number of comments on the article. |
| `data[].created / data[].updated` | Unix timestamps in seconds for when the article was created and last updated. |
| `data[].author.id / data[].author.headline` | ID and short headline of the article's author. |
| `data[].author.badge[]` | Badges on the author profile. Each has a `type` and a `description`, such as `best_answerer`. |
| `paging.totals` | Total number of articles in the column. |
| `paging.is_end / paging.next` | `is_end` is `true` on the last page. `next` is the link to the following page and carries the `limit` and `offset` values. |

### Notes

- Take `column_id` from the column's URL slug. This example uses `zhangjiawei`.
- Page through results with `limit` and `offset`. The `paging.next` link shows the next `offset`, for example `10` when `limit` is `10`.
- Stop paging when `paging.is_end` is `true`.
- To get one article in full, call [Zhihu Column Article Detail](/apis/zhihu/web/column-article-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/column-articles.json`](../../../../catalog/models/zhihu/web/column-articles.json) · Store page: https://www.sandbase.ai/model/zhihu/web/column-articles

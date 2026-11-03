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

Returns a list of recommended articles that Zhihu shows as similar to a given Zhihu column article. You pass the source article ID as `article_id`. Each item has article metadata and author details, and the response includes paging links.

### Use cases

- Show a "similar articles" block under an article in a reading app.
- Find authors who write on the same topic as a source article.
- Build a related-reading feed by following the paging links page by page.
- Collect author descriptions and badges to judge who writes in a niche.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/column-recommend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"article_id": "669214677"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `article_id` | string | Yes | Article ID |
| `limit` | string | No | Number of columns per page |
| `offset` | string | No | Offset |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ad_info": {},
  "data": [
    {
      "article": {
        "ab_param": {
          "qa_hidden_voteup": "",
          "rs_interest1": "",
          "zp_zhi_style": ""
        },
        "admin_closed_comment": false,
        "allow_segment_interaction": 0,
        "annotation_action": [],
        "article_type": "normal",
        "attached_info": "kgIhCgcyMTA3OTc4EggyNDgwMzY3MhgHIgpJTUFHRV9URVhU",
        "author": {
          "avatar_url": "https://pic1.zhimg.com/v2-5e4c76e5b288f0b5d0c46601967f42e7_l.jpg?source=172ae18b",
          "avatar_url_template": "https://pic1.zhimg.com/v2-5e4c76e5b288f0b5d0c46601967f42e7.jpg?source=172ae18b",
          "badge": [],
          "badge_v2": {
            "detail_badges": [],
            "icon": "",
            "merged_badges": [],
            "night_icon": "",
            "title": ""
          },
          "description": "杨靖心理机构创始人，前审讯专家，国家二级心理咨询师，国家一级营养师，高级育婴师，广东财经大学十佳青年授课讲师，阿里巴巴UC平台首位情感心理与育儿问题专家。心理拆…",
          "gender": 1,
          "headline": "",
          "id": "87e4fb22dc2e505daa362d9b1dbcfcb9"
        },
        "bar_plugins_flip_time": 3000
      },
      "editor_choice": false
    }
  ],
  "paging": {
    "is_end": false,
    "is_start": true,
    "next": "https://zhuanlan.zhihu.com/api/articles/669214677/recommendation?include=data%5B…",
    "previous": "https://zhuanlan.zhihu.com/api/articles/669214677/recommendation?include=data%5B…"
  },
  "recommend_info": null
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | One recommended item per row. Each item holds an `article` object and an `editor_choice` flag. |
| `data[].article.article_type` | Type of the recommended article. The sample value is `normal`. |
| `data[].article.attached_info` | Opaque token attached to the recommended article. It appears to be Zhihu's own tracking value, so treat it as a string. |
| `data[].article.author.id` | Hash-style ID of the article author. |
| `data[].article.author.headline / data[].article.author.description` | Short headline and longer bio text of the author. `headline` can be an empty string. |
| `data[].article.author.avatar_url / data[].article.author.avatar_url_template` | Author avatar image URL and its template version. |
| `data[].article.author.badge_v2.title` | Main badge title of the author, such as `新知答主`. It is empty when the author has no badge. |
| `data[].article.author.badge_v2.detail_badges[]` | List of badges the author holds, each with a `title`, `description` and `icon`. |
| `data[].editor_choice` | Boolean that marks whether the item is an editor choice. |
| `paging.is_end / paging.next` | `is_end` tells you if this is the last page. `next` is the URL of the next page and includes the `limit` and `offset` values. |

### Notes

- Take `article_id` from a Zhihu column article URL, for example `669214677` in `zhuanlan.zhihu.com/p/669214677`.
- Page with `limit` and `offset`. The sample `paging.next` link uses `limit=12` and `offset=12` for the second page.
- Stop paging when `paging.is_end` is `true`.
- To read the full text of a recommended article, call [Zhihu Column Article Detail](/apis/zhihu/web/column-article-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/column-recommend.json`](../../../../catalog/models/zhihu/web/column-recommend.json) · Store page: https://www.sandbase.ai/model/zhihu/web/column-recommend

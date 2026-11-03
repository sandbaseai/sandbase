# Zhihu User Articles API: pricing, parameters and code examples

`zhihu/web/user-articles` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves articles posted by a specific Zhihu author using their user identifier. Supports sorting by post date or upvotes alongside pagination controls.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/user-articles", "user_url_token": "excited-vczh"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/user-articles', {'user_url_token': 'excited-vczh'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/user-articles", {
  "user_url_token": "excited-vczh"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/user-articles", sandbase.Params{
	"user_url_token": "excited-vczh",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/user-articles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of articles per page  |
| `offset` | string |  | Offset  |
| `sort_type` | string |  | Sort Type one of: `created`, `voteups` |
| `user_url_token` | string | yes | User ID  |

## Details

Returns a page of articles written by one Zhihu member, with titles, excerpts, full HTML content, vote and comment counts, and timestamps. The only required input is the member's `user_url_token`, such as `excited-vczh`.

### Use cases

- Build a feed of new long-form posts from a chosen Zhihu author.
- Rank an author's articles by `voteup_count` to find their most upvoted work.
- Archive an author's article titles, links and cover images for a content audit.
- Track comment and favorite counts on an author's articles to compare engagement.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/user-articles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_url_token": "excited-vczh"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_url_token` | string | Yes | User ID |
| `limit` | string | No | Number of articles per page |
| `offset` | string | No | Offset |
| `sort_type` | string | No | Sort Type |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "admin_closed_comment": false,
      "article_type": "normal",
      "author": {
        "avatar_url": "https://pic1.zhimg.com/v2-ada18a9354a3831171306f2c7ce20aaf_l.jpg?source=d16d100b",
        "avatar_url_template": "https://pica.zhimg.com/v2-ada18a9354a3831171306f2c7ce20aaf.jpg?source=d16d100b",
        "badge": [],
        "badge_v2": {
          "detail_badges": [],
          "icon": "",
          "merged_badges": [],
          "night_icon": "",
          "title": ""
        },
        "gender": -1,
        "headline": "",
        "id": "0970f947b898ecc0ec035f9126dd4e08",
        "is_advertiser": false
      },
      "can_comment": {
        "reason": "",
        "status": true
      },
      "comment_count": 28,
      "comment_permission": "all",
      "content": "<p data-pid=\"MQZ4WGyX\">思路已经有了，也开始做了。</p><p data-pid=\"t6cPGsnd\">早期GacUI为了跨平台精心设计了…",
      "content_need_truncated": false,
      "copyright_permission": "need_review",
      "created": 1705652701,
      "endorsements": [
        {
          "background_color": {
            "alpha": 0.1,
            "group": "GBL01A"
          },
          "elements": [
            {
              "content": "创作声明: 内容包含剧透",
              "font_color": {
                "alpha": 1.0,
                "group": "GBL07A"
              },
              "font_size": 13,
              "is_bold": true,
              "max_line": 1,
              "type": "TEXT"
            }
          ],
          "sub_elements": [
            {
              "elements": [
                {
                  "content": "创作声明: 内容包含剧透",
                  "font_color": {
                    "alpha": 1.0,
                    "group": "GBL07A"
                  },
                  "font_size": 13,
                  "is_bold": true,
                  "max_line": 1,
                  "type": "TEXT"
                }
              ]
            }
          ],
          "sub_elements_type": "DESCRIPTION"
        }
      ],
      "excerpt": "思路已经有了，也开始做了。早期GacUI为了跨平台精心设计了一套隔离层，可以把操作系统和渲染器的细节正交地隔离掉，后来在移植到macos和linux的时候，得到…"
    }
  ],
  "need_force_login": false,
  "paging": {
    "is_end": false,
    "is_start": true,
    "next": "http://www.zhihu.com/api/v4/members/excited-vczh/articles?user_url_token=excited…",
    "previous": "http://www.zhihu.com/api/v4/members/excited-vczh/articles?user_url_token=excited…",
    "totals": 147
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].id / data[].title` | The article ID and the article title. |
| `data[].url` | Link to the article on the Zhihu column site. |
| `data[].excerpt / data[].content` | A short preview and the article body. Both can contain HTML tags and may be cut off. |
| `data[].created / data[].updated` | Creation and last update times as Unix timestamps in seconds. |
| `data[].voteup_count / data[].comment_count` | Number of upvotes and number of comments on the article. |
| `data[].reaction.statistics.favorites / data[].reaction.statistics.like_count` | Number of favorites and number of likes on the article. |
| `data[].image_url` | Cover image URL for the article. It is an empty string when the article has no cover. |
| `data[].author.id / data[].author.headline` | The author's ID and profile headline. |
| `data[].endorsements[].elements[].content` | Label text shown with the article, such as a column name or a creator statement. |
| `paging.totals / paging.is_end / paging.next` | Total number of articles for this author, whether this is the last page, and the URL of the next page. |

### Notes

- Take `user_url_token` from the member's Zhihu profile URL. The example value is `excited-vczh`.
- Page through results with `limit` and `offset`. The `paging.next` URL in the sample response uses `limit=20` and `offset=20`.
- Set `sort_type` to `created` or `voteups` to order results by post date or upvotes.
- To list the same author's answers instead, call [Zhihu User Answers](/apis/zhihu/web/user-answers). For the author's profile, call [Zhihu Web User Profile](/apis/zhihu/web/user-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/user-articles.json`](../../../../catalog/models/zhihu/web/user-articles.json) · Store page: https://www.sandbase.ai/model/zhihu/web/user-articles

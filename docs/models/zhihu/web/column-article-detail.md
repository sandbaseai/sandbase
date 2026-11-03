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

Returns the details of one Zhihu column article, including its HTML content, engagement counts, author profile and the column it belongs to. It needs one input, the `article_id`.

### Use cases

- Archive the full HTML body and publish time of a known column article.
- Read an article's `emoji_reaction.like_count`, `comment_count` and `favlists_count` to compare its engagement with other posts.
- Collect author details such as `author.url_token` and expertise badges for a column writer.
- Find which column an article belongs to and how large that column is.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/column-article-detail" \
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
  "ab_param": {
    "qa_hidden_voteup": "",
    "rs_interest1": "",
    "zp_zhi_style": ""
  },
  "activity_topping_info": {
    "state": "untopped"
  },
  "admin_closed_comment": false,
  "allow_segment_interaction": 1,
  "annotation_action": [],
  "article_type": "normal",
  "attached_info": "kgIkCgkyMzY4NDQ3NTUSCTY2OTIxNDY3NxgHIgpJTUFHRV9URVhU",
  "author": {
    "avatar_url": "https://picx.zhimg.com/v2-d626957872f9b38fa594394db2d2e6e7_l.jpg?source=172ae18b",
    "avatar_url_template": "https://picx.zhimg.com/v2-d626957872f9b38fa594394db2d2e6e7.jpg?source=172ae18b",
    "badge": [
      {
        "description": "优秀答主",
        "topics": [
          {
            "id": "19609249",
            "name": "网球",
            "type": "topic",
            "url": "https://www.zhihu.com/topic/19609249"
          }
        ],
        "type": "best_answerer"
      }
    ],
    "badge_v2": {
      "detail_badges": [
        {
          "badge_status": "passed",
          "description": "新知答主",
          "detail_type": "zhihu_yearly_answerer",
          "icon": "https://picx.zhimg.com/v2-4a07bc69c4bb04444721f35b32125c75_l.png?source=32738c0c",
          "night_icon": "https://picx.zhimg.com/v2-4a07bc69c4bb04444721f35b32125c75_l.png?source=32738c0c",
          "sources": [
            {
              "avatar_path": "",
              "avatar_url": "",
              "description": "",
              "id": "2023",
              "name": "",
              "priority": 2023,
              "token": "",
              "type": "year"
            }
          ],
          "title": "年度新知答主",
          "type": "reward"
        }
      ],
      "icon": "https://picx.zhimg.com/v2-4a07bc69c4bb04444721f35b32125c75_l.png?source=32738c0c",
      "merged_badges": [
        {
          "badge_status": "passed",
          "description": "新知答主",
          "detail_type": "best",
          "icon": "",
          "night_icon": "",
          "sources": [],
          "title": "年度新知答主",
          "type": "best"
        }
      ],
      "night_icon": "https://picx.zhimg.com/v2-4a07bc69c4bb04444721f35b32125c75_l.png?source=32738c0c",
      "title": "新知答主"
    },
    "description": "",
    "exposed_medal": {
      "avatar_url": "https://pic1.zhimg.com/v2-05b349562f395a352a39342dccbe834f_r.png?source=172ae18b",
      "description": "2023 年度新知答主获得者",
      "medal_avatar_frame": "",
      "medal_id": "1750529444194553856",
      "medal_name": "2023 年度新知答主",
      "mini_avatar_url": "https://pic1.zhimg.com/v2-05b349562f395a352a39342dccbe834f_l.png?source=172ae18b"
    },
    "gender": 1,
    "headline": "",
    "id": "f9de84865e3e8455a09af78bfe4d1da5",
    "is_advertiser": false,
    "is_followed": false,
    "is_following": false
  },
  "bar_plugins_flip_time": 3000,
  "can_comment": {
    "reason": "因作者设置，评论已关闭",
    "status": false
  },
  "can_reference": false,
  "can_tip": false
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id / article_type` | The article ID (same as the `article_id` you sent) and the article type, `normal` in this example. |
| `content / excerpt` | `content` holds the article body as HTML. `excerpt` is a shorter HTML preview that may start with an image tag. |
| `created` | Creation time of the article as a Unix timestamp in seconds. |
| `emoji_reaction.like_count` | Number of likes on the article. |
| `comment_count / favlists_count` | Number of comments on the article and the number of favorite lists that saved it. |
| `can_comment.status / can_comment.reason` | Whether commenting is allowed. When it is `false`, `reason` explains why, for example the author closed comments. |
| `ip_info` | Location label shown for the article, `江苏` in this example. |
| `author.name / author.url_token / author.id` | The author's display name, URL slug and ID. |
| `author.badge[].topics[].name` | Topics tied to the author's best answerer badge, for example `网球`, `文学` and `绘画`. |
| `column.title / column.articles_count / column.followers` | The column's title, how many articles it holds and how many followers it has. |

### Notes

- `article_id` is the numeric string in the article ID field of the response, such as `669214677`.
- `column.url_token` and `column.id` give the column's identifier. Use [Zhihu Column Articles](/apis/zhihu/web/column-articles) to list other articles in a column.
- `created` and `column.created` are Unix timestamps in seconds.
- `author.url_token` can be used to look up the writer with [Zhihu Web User Profile](/apis/zhihu/web/user-info).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/column-article-detail.json`](../../../../catalog/models/zhihu/web/column-article-detail.json) · Store page: https://www.sandbase.ai/model/zhihu/web/column-article-detail

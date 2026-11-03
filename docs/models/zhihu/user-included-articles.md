# Zhihu User Included Articles API: pricing, parameters and code examples

`zhihu/user-included-articles` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get the included-article records exposed for a Zhihu user, with offset pagination. Use it to browse that account's included-article list.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/user-included-articles", "userUrlToken": "excited-vczh"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/user-included-articles', {'userUrlToken': 'excited-vczh'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/user-included-articles", {
  "userUrlToken": "excited-vczh"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/user-included-articles", sandbase.Params{
	"userUrlToken": "excited-vczh",
})
```

Same call via the path form: `POST /v1/api/zhihu/user-included-articles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Start offset, begins with 0. default `0` |
| `userUrlToken` | string | yes | Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`.  |

## Details

This API returns the articles that Zhihu has included for a user, 20 per page. It needs the user's URL token, such as `excited-vczh`. Each record has the article title, excerpt, HTML content, author, and vote and comment counts.

### Use cases

- Build a list of a Zhihu author's included articles with titles, links and cover images.
- Rank an author's included articles by `voteup_count` to find the most liked ones.
- Collect the article text from `content` for archiving or text analysis.
- Check which included articles carry an editor recommendation label.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/user-included-articles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userUrlToken": "excited-vczh"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userUrlToken` | string | Yes | Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`. |
| `offset` | integer | No | Start offset, begins with 0. |

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
        "avatar_url_template": "https://pic1.zhimg.com/v2-ada18a9354a3831171306f2c7ce20aaf.jpg?source=d16d100b",
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
        "reason": "因作者设置，评论已关闭",
        "status": false
      },
      "comment_count": 173,
      "comment_permission": "nobody",
      "content": "<p data-pid=\"4yDcxiAX\">旅游了一天，睡觉前刚好有点时间，就上来写点东西。后面还有将近一个星期的路程。</p><p data-pid=\"Lm…",
      "content_need_truncated": false,
      "copyright_permission": "need_review",
      "created": 1482568826,
      "excerpt": "旅游了一天，睡觉前刚好有点时间，就上来写点东西。后面还有将近一个星期的路程。在Office工作也已经超过两年了。尽管Office是微软C++新标准最有力的推手之…",
      "excerpt_title": ""
    }
  ],
  "paging": {
    "is_end": true,
    "is_start": true,
    "next": "http://www.zhihu.com/api/v4/members/excited-vczh/included-articles?user_url_toke…",
    "previous": "http://www.zhihu.com/api/v4/members/excited-vczh/included-articles?user_url_toke…",
    "totals": 2
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].title` | Title of the article. |
| `data[].url` | Link to the article on zhuanlan.zhihu.com. |
| `data[].id` | Article ID as a string. The same number appears at the end of `url`. |
| `data[].excerpt` | Short plain text preview of the article. It can contain HTML link fragments. |
| `data[].content` | Article body as HTML. The value can be long. |
| `data[].voteup_count / data[].comment_count` | Number of upvotes and number of comments on the article. |
| `data[].created / data[].updated` | Creation and last update time of the article. The values are Unix timestamps in seconds. |
| `data[].image_url` | Cover image URL for the article. |
| `data[].label_info.text` | Label text shown on the article, such as `编辑推荐` (editor recommendation). The `label_info.type` field holds the matching code `editor_recommendation`. |
| `data[].author.id` | ID of the article author. |
| `paging.is_end / paging.totals` | `is_end` tells you whether this is the last page. `totals` is the total number of records. |

### Notes

- Take `userUrlToken` from the profile address `zhihu.com/people/{userUrlToken}`.
- For the next page, send the `offset` parameter, starting at 0. The `paging.next` URL shows a page size of 20, so the next offset is 20.
- Stop paging when `paging.is_end` is `true`.
- For the author's profile, call [Zhihu User Info](/apis/zhihu/user-info).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/zhihu/user-included-articles.json`](../../../catalog/models/zhihu/user-included-articles.json) · Store page: https://www.sandbase.ai/model/zhihu/user-included-articles

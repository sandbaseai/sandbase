# Zhihu User Articles API: pricing, parameters and code examples

`zhihu/user-articles` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get articles published by a Zhihu user with offset pagination and publish-time or upvote sorting. Use it to browse a creator's articles in the selected order.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/user-articles", "userUrlToken": "excited-vczh"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/user-articles', {'userUrlToken': 'excited-vczh'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/user-articles", {
  "userUrlToken": "excited-vczh"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/user-articles", sandbase.Params{
	"userUrlToken": "excited-vczh",
})
```

Same call via the path form: `POST /v1/api/zhihu/user-articles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Start offset, begins with 0. default `0` |
| `sortType` | string |  | Sorting criteria for user articles. one of: `created`, `voteups`; default `"created"` |
| `userUrlToken` | string | yes | Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`.  |

## Details

This API returns a page of articles published by one Zhihu user. Each item has the title, excerpt, HTML content, vote and comment counts, and timestamps. You send the user's `userUrlToken`, and you can pick the sort order and the start offset.

### Use cases

- Build a list of a creator's articles ordered by newest first with `sortType` set to `created`.
- Find a creator's most upvoted articles by setting `sortType` to `voteups`.
- Track comment, upvote and favorite counts on a creator's articles over time.
- Collect article URLs and cover images to link a creator's work in a content database.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/user-articles" \
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
| `sortType` | string | No | Sorting criteria for user articles. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "admin_closed_comment": false,
      "article_type": "normal",
      "author": {
        "avatar_url": "https://pica.zhimg.com/v2-ada18a9354a3831171306f2c7ce20aaf_l.jpg?source=d16d100b",
        "avatar_url_template": "https://picx.zhimg.com/v2-ada18a9354a3831171306f2c7ce20aaf.jpg?source=d16d100b",
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
| `data[].id / data[].url` | The article ID and its link on zhuanlan.zhihu.com. |
| `data[].title` | Article title. |
| `data[].excerpt / data[].content` | A short excerpt and the article body. Both are HTML strings and may be cut short. |
| `data[].created / data[].updated` | Creation and last update times as Unix timestamps in seconds. |
| `data[].voteup_count / data[].comment_count` | Number of upvotes and number of comments on the article. |
| `data[].reaction.statistics.favorites / data[].reaction.statistics.like_count` | Number of favorites and number of likes on the article. |
| `data[].image_url` | Cover image URL. It is an empty string when the article has no cover. |
| `data[].author.id / data[].author.avatar_url` | The author's ID and avatar image URL. |
| `data[].endorsements[]` | Optional labels on the article, such as a creation statement or the column that includes it. Text sits in `elements[].content` and a column link in `action_url`. |
| `paging.totals / paging.is_end` | Total number of articles for this user, and whether the current page is the last one. |

### Notes

- Take `userUrlToken` from the profile URL `zhihu.com/people/{userUrlToken}`. For example, `excited-vczh`.
- Each page in the sample holds 20 items. The `paging.next` URL shows `limit=20&offset=20` for the next page, so send `offset` as 20, 40 and so on until `paging.is_end` is `true`.
- `sortType` accepts `created` (default) or `voteups`.
- To look up the author first, call [Zhihu User Info](/apis/zhihu/user-info).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/zhihu/user-articles.json`](../../../catalog/models/zhihu/user-articles.json) · Store page: https://www.sandbase.ai/model/zhihu/user-articles

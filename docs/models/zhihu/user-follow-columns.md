# Zhihu User Follow Columns API: pricing, parameters and code examples

`zhihu/user-follow-columns` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get Zhihu columns followed by a user, with offset pagination. Use it to browse the columns associated with a known account's follow activity.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/user-follow-columns", "userUrlToken": "excited-vczh"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/user-follow-columns', {'userUrlToken': 'excited-vczh'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/user-follow-columns", {
  "userUrlToken": "excited-vczh"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/user-follow-columns", sandbase.Params{
	"userUrlToken": "excited-vczh",
})
```

Same call via the path form: `POST /v1/api/zhihu/user-follow-columns` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `offset` | integer |  | Start offset, begins with 0. default `0` |
| `userUrlToken` | string | yes | Zhihu user URL token, such as the value in `zhihu.com/people/{userUrlToken}`.  |

## Details

Returns the Zhihu columns that a user follows, one page at a time. Each item has the column title, follower and article counts, and the column author. The input is a user URL token, with an optional `offset` for paging.

### Use cases

- List the columns a known Zhihu account follows to see what topics they read.
- Collect column IDs and compare `followers` and `voteup_count` to find popular columns in a niche.
- Find the authors behind followed columns and their headlines and badges.
- Page through all followed columns of an account and count them with `paging.totals`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/user-follow-columns" \
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
      "accept_submission": true,
      "articles_count": 4,
      "author": {
        "avatar_url": "https://pic1.zhimg.com/v2-34dcbb23e27626688ad661b65e962441_l.jpg?source=d16d100b",
        "avatar_url_template": "https://picx.zhimg.com/v2-34dcbb23e27626688ad661b65e962441.jpg?source=d16d100b",
        "badge": [],
        "badge_v2": {
          "detail_badges": [],
          "icon": "",
          "merged_badges": [],
          "night_icon": "",
          "title": ""
        },
        "gender": 1,
        "headline": "技术美术，喜欢图形",
        "id": "a93a193aaa57bec0ca22a08238edf623",
        "is_advertiser": false
      },
      "column_type": "normal",
      "comment_permission": "all",
      "followers": 1098,
      "id": "c_1215952152252121088",
      "image_url": "https://picx.zhimg.com/v2-a0b5a04ff3496a115ce4a0bcfc6bae8b_l.png?source=d16d100b",
      "intro": "",
      "items_count": 4,
      "purchase_count": 0,
      "title": "从零开始的卡通渲染"
    }
  ],
  "paging": {
    "is_end": false,
    "is_start": true,
    "next": "http://www.zhihu.com/api/v4/members/excited-vczh/following-columns?include=data%…",
    "previous": "http://www.zhihu.com/api/v4/members/excited-vczh/following-columns?include=data%…",
    "totals": 108
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].id` | Column ID. It can be a slug like `youjiezhimi` or an ID like `c_1215952152252121088`. |
| `data[].title / data[].intro` | Column name and its short description. `intro` can be an empty string. |
| `data[].followers` | Number of followers of the column. |
| `data[].articles_count / data[].items_count` | Number of articles in the column and total items in it. |
| `data[].voteup_count` | Total upvote count shown for the column. |
| `data[].updated` | Last update time of the column as a Unix timestamp in seconds. |
| `data[].author.id / data[].author.headline` | ID and profile headline of the column author. |
| `data[].author.badge[].description` | Badge text for the author, such as a verified identity or best answerer label. |
| `data[].url / data[].image_url` | API URL of the column and its cover image URL. |
| `paging.is_end / paging.totals` | `is_end` is `true` on the last page. `totals` is the total number of followed columns (108 in this example). |

### Notes

- Take `userUrlToken` from a profile URL, `zhihu.com/people/{userUrlToken}`.
- Set `offset` to 0 for the first page. Keep `offset` growing and stop when `paging.is_end` is `true`.
- `paging.next` and `paging.previous` are full URLs from the platform. Use `offset` in this API instead.
- To look up the account first, call [Zhihu User Info](/apis/zhihu/user-info). To read articles inside a column, call [Zhihu Column Articles](/apis/zhihu/web/column-articles).

### Pricing

$0.014286 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/zhihu/user-follow-columns.json`](../../../catalog/models/zhihu/user-follow-columns.json) · Store page: https://www.sandbase.ai/model/zhihu/user-follow-columns

# Douyin Creator Search Suggestions API: pricing, parameters and code examples

`douyin/index/daren-sug-great-user-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns creator suggestions on Douyin matching a query nickname. Includes profile details, content category tags, follower totals, and item counts.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/daren-sug-great-user-list", "keyword": "人工智能", "total": "20"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/daren-sug-great-user-list', {'keyword': '人工智能', 'total': '20'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/daren-sug-great-user-list", {
  "keyword": "人工智能",
  "total": "20"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/daren-sug-great-user-list", sandbase.Params{
	"keyword": "人工智能",
	"total": "20",
})
```

Same call via the path form: `POST /v1/api/douyin/index/daren-sug-great-user-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `total` | string |  | Return count, default 20 default `"20"` |
| `keyword` | string | yes | Daren nickname keyword  |

## Details

Returns a list of Douyin creators whose nicknames match a keyword. Each entry has the creator's profile link, content category tags, follower count, video count and like count. The only required input is `keyword`.

### Use cases

- Find Douyin creators in a niche by searching a topic word such as `人工智能`.
- Build a shortlist of creators with their category tags and audience size for outreach.
- Power an autocomplete box for creator names in a Douyin research tool.
- Compare candidate creators by `follow_count` and `like_count` before a deeper lookup.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/daren-sug-great-user-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Daren nickname keyword |
| `total` | string | No | Return count, default 20 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": 0,
    "StatusMessage": ""
  },
  "userlist": [
    {
      "aweme_id": "54166183587",
      "aweme_url": "https://www.douyin.com/user/MS4wLjABAAAAAwIshD25hrP7M8fkn0f3PU79tUhK_bOj0y2bhYjx…",
      "first_tag_name": "随拍",
      "follow_count": "117329",
      "item_count": "1649",
      "like_count": "2536460",
      "second_tag_name": "生活随拍",
      "user_head_logo": "https://p11.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813c000-ce_oIAh9s…",
      "user_id": "edchdcihfcdegigb",
      "user_name": "JYF人工智能"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `userlist[]` | List of creators that match the keyword. |
| `userlist[].user_name` | Creator nickname shown on Douyin. |
| `userlist[].aweme_url` | Link to the creator's Douyin profile page. |
| `userlist[].aweme_id` | Public Douyin account ID of the creator. It can be a number or a custom handle. |
| `userlist[].user_id` | Encoded creator ID string, such as `edchdcihfcdegigb`. |
| `userlist[].first_tag_name / userlist[].second_tag_name` | Top-level and sub-level content category of the creator, such as `科技` and `数码产品`. |
| `userlist[].follow_count` | Follower total for the creator, returned as a string. |
| `userlist[].item_count` | Number of videos the creator has posted, returned as a string. |
| `userlist[].like_count` | Total likes for the creator, returned as a string. |
| `userlist[].user_head_logo` | URL of the creator's avatar image. |

### Notes

- Set `total` to change how many creators come back. It is a string and defaults to `20`.
- Numeric values such as `follow_count` and `like_count` arrive as strings, so convert them before sorting.
- `BaseResp.StatusCode` is `0` on a successful call.
- To go deeper on a creator, try [Douyin Creator Top Videos](/apis/douyin/index/daren-great-user-top-video) or [Douyin Similar Daren Accounts](/apis/douyin/index/daren-similar-users).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/daren-sug-great-user-list.json`](../../../../catalog/models/douyin/index/daren-sug-great-user-list.json) · Store page: https://www.sandbase.ai/model/douyin/index/daren-sug-great-user-list

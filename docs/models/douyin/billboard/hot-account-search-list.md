# Douyin Hot Account Search API: pricing, parameters and code examples

`douyin/billboard/hot-account-search-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of Douyin accounts matching a username or Douyin ID keyword, including follower counts, like totals, and performance metrics.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-account-search-list", "cursor": 0, "keyword": "华为"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-account-search-list', {'cursor': 0, 'keyword': '华为'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-account-search-list", {
  "cursor": 0,
  "keyword": "华为"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-account-search-list", sandbase.Params{
	"cursor": 0,
	"keyword": "华为",
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-account-search-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `cursor` | integer | yes | Cursor, default empty  |
| `keyword` | string | yes | Search username or Douyin number  |

## Details

This API searches Douyin accounts by username or Douyin ID keyword. It needs a `keyword` and a `cursor`, and returns a page of matching accounts with follower counts, like totals and post counts.

### Use cases

- Find the official Douyin account of a brand by searching its name, such as `华为`.
- Compare follower counts and total likes across accounts that match the same keyword.
- Collect `user_id` values of matched creators to feed into other Douyin billboard APIs.
- Build a candidate list of influencer accounts for a topic or brand keyword.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-account-search-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"cursor": 0, "keyword": "华为"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | Yes | Cursor, default empty |
| `keyword` | string | Yes | Search username or Douyin number |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "cursor": 30,
    "has_more": true,
    "user_list": [
      {
        "avatar_url": "https://p11.douyinpic.com/aweme/100x100/aweme-avatar/tos-cn-i-0813_e6a4232118b74…",
        "fans_cnt": 14061832,
        "fans_incr_rate": 0,
        "fans_trends": null,
        "group_id": 0,
        "group_name": "",
        "like_cnt": 228400093,
        "monitor_id": 0,
        "monitor_period": 0,
        "monitor_status": 0,
        "new_fans_cnt": 0,
        "new_item_monitor": 0
      }
    ]
  },
  "extra": {
    "now": 1793691106000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.user_list[].nick_name` | Display name of the account. |
| `data.user_list[].user_id` | Identifier of the account. Use it as the account key in other Douyin billboard calls. |
| `data.user_list[].fans_cnt` | Follower count of the account. |
| `data.user_list[].like_cnt` | Total likes counted for the account. |
| `data.user_list[].publish_cnt` | Number of works the account has published. |
| `data.user_list[].avatar_url` | Link to the account avatar image. |
| `data.user_list[].fans_incr_rate / new_fans_cnt / new_like_cnt` | Follower growth and new like figures. They are `0` in this sample response. |
| `data.user_list[].monitor_status / group_id / target_type` | Monitoring and grouping settings for the account. They are `0` or empty in this sample response. |
| `data.cursor` | Cursor value returned with this page. Its value was `30` for a request with `cursor` set to `0`. |
| `data.has_more` | `true` when more matching accounts are available. |

### Notes

- Start with `cursor` set to `0`. For the next page, send the `data.cursor` value from the previous response while `data.has_more` is `true`.
- `user_id` is a long string that starts with `MS4w`. It is not the numeric Douyin ID you search with.
- Use [Douyin Account Metric Trends](/apis/douyin/billboard/hot-account-trends-list) or [Douyin Hot Account Fan Portrait](/apis/douyin/billboard/hot-account-fans-portrait-list) to look deeper into an account found here.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-account-search-list.json`](../../../../catalog/models/douyin/billboard/hot-account-search-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-account-search-list

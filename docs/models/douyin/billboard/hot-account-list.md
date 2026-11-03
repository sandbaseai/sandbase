# Douyin Hot Account List API: pricing, parameters and code examples

`douyin/billboard/hot-account-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending Douyin accounts from the billboard ranking with engagement metrics. Supports filtering by category tag via query_tag and time window via date_window.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-account-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-account-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-account-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-account-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-account-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page_num` | integer |  | Page number, default 1 default `1` |
| `page_size` | integer |  | Number of items per page, default 20 default `10` |
| `query_tag` | object |  | Sub-level vertical category tag, empty for all, multiple tags need to be passed in default `{}` |
| `date_window` | integer |  | Time window, format hour, default 24 hours default `24` |

## Details

Returns a ranked page of trending Douyin accounts from the billboard, with follower counts, like counts, and recent growth figures. All inputs are optional. Use `date_window` for the time window in hours and `query_tag` to filter by category.

### Use cases

- Find Douyin accounts that gained the most followers in the last 24 hours.
- Compare `fans_incr_rate` across accounts to spot fast-growing creators.
- Pull the daily follower change series for each ranked account to chart short-term growth.
- Collect `user_id` values from a category to feed account-level lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-account-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date_window` | integer | No | Time window, format hour, default 24 hours |
| `page_num` | integer | No | Page number, default 1 |
| `page_size` | integer | No | Number of items per page, default 20 |
| `query_tag` | object | No | Sub-level vertical category tag, empty for all, multiple tags need to be passed in |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "has_more": true,
    "user_list": [
      {
        "avatar_url": "https://p3.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-i-0813c000-ce_os7G9kX…",
        "fans_cnt": 188412691,
        "fans_incr_rate": 0.00010038017178698787,
        "fans_trends": [
          {
            "DateTime": "2026-10-27",
            "Value": 7534
          }
        ],
        "group_id": 0,
        "group_name": "",
        "like_cnt": 14047500224,
        "monitor_id": 0,
        "monitor_period": 0,
        "monitor_status": 0,
        "new_fans_cnt": 18911,
        "new_item_monitor": 0
      }
    ]
  },
  "extra": {
    "now": 1793691105000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.user_list[].nick_name` | Display name of the account. |
| `data.user_list[].user_id` | Account ID string. Use it to look up the same account in other Douyin billboard APIs. |
| `data.user_list[].fans_cnt / like_cnt` | Total follower count and total like count of the account. |
| `data.user_list[].new_fans_cnt / new_like_cnt` | Followers and likes gained in the selected time window. |
| `data.user_list[].fans_incr_rate` | Follower growth rate as a decimal fraction. A value of `0.001` means 0.1%. |
| `data.user_list[].fans_trends[]` | Daily follower change series. Each row has `DateTime` as a `YYYY-MM-DD` date and `Value` as the number for that day. Values can be negative. |
| `data.user_list[].publish_cnt` | Number of works the account has published. |
| `data.user_list[].second_tag_name` | Sub-category tag of the account. It can be an empty string. |
| `data.user_list[].avatar_url` | Link to the account's avatar image. |
| `data.has_more` | `true` when more pages are available after the current one. |

### Notes

- Raise `page_num` while `data.has_more` is `true` to read further pages. `page_size` sets how many accounts each page returns.
- Get valid values for `query_tag` from [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag). Leave it as `{}` for all categories.
- The `group_id`, `monitor_*`, `target_*` and `notice_*` fields were `0` in the sample response and carry no useful data there.
- For per-account detail, call [Douyin Account Metric Trends](/apis/douyin/billboard/hot-account-trends-list) or [Douyin Hot Account Fan Portrait](/apis/douyin/billboard/hot-account-fans-portrait-list) with the returned `user_id`.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-account-list.json`](../../../../catalog/models/douyin/billboard/hot-account-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-account-list

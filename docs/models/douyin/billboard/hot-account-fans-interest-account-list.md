# Douyin Fan Interest Account List API: pricing, parameters and code examples

`douyin/billboard/hot-account-fans-interest-account-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of 20 accounts that followers of a target creator are interested in on Douyin. Queries Douyin billboard analytics using the creator's unique `sec_uid`.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-account-fans-interest-account-list", "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-account-fans-interest-account-list', {'sec_uid': 'MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-account-fans-interest-account-list", {
  "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-account-fans-interest-account-list", sandbase.Params{
	"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_",
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-account-fans-interest-account-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_uid` | string | yes | User sec_id  |

## Details

Returns a list of Douyin accounts that followers of a target creator are interested in. It needs one input, the creator's `sec_uid`. Each row has the account's nickname, avatar, follower count, like count, post count and a short daily follower trend.

### Use cases

- Find accounts that share an audience with a given Douyin creator.
- Compare follower counts and like totals across the accounts a creator's fans also follow.
- Spot accounts whose daily follower change is rising or falling among a creator's audience.
- Build a list of related creators to review for partnership or competitor research.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-account-fans-interest-account-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | Yes | User sec_id |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": [
    {
      "avatar_url": "https://p3.douyinpic.com/aweme/720x720/aweme-avatar/tos-cn-avt-0015_83f5a859c766…",
      "fans_cnt": 1076929,
      "fans_incr_rate": 0,
      "fans_trends": [
        {
          "DateTime": "2026-10-27",
          "Value": -253
        }
      ],
      "group_id": 0,
      "group_name": "",
      "like_cnt": 45761127,
      "monitor_id": 0,
      "monitor_period": 0,
      "monitor_status": 0,
      "new_fans_cnt": 0,
      "new_item_monitor": 0
    }
  ],
  "extra": {
    "now": 1793691105000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].nick_name` | Display name of the interest account. |
| `data[].user_id` | Account ID in `sec_uid` style. Use it to look up that account in other Douyin APIs that take a `sec_uid`. |
| `data[].avatar_url` | URL of the account's avatar image. |
| `data[].fans_cnt` | Current follower count of the interest account. |
| `data[].like_cnt` | Total likes received by the interest account. |
| `data[].publish_cnt` | Number of works the account has published. |
| `data[].fans_trends[].DateTime / data[].fans_trends[].Value` | One entry per day. `DateTime` is a `YYYY-MM-DD` date and `Value` is the follower change for that day. Values can be negative. |
| `data[].fans_incr_rate` | Follower growth rate field. It is `0` in the sample response. |
| `extra.now` | Timestamp of the response in milliseconds. |
| `code` | Status code. `0` appears in a successful response. |

### Notes

- Get the input `sec_uid` from a Douyin user profile or from an account list such as [Douyin Hot Account List](/apis/douyin/billboard/hot-account-list).
- The request takes only `sec_uid`. There are no pagination parameters.
- Many fields in each row, such as `monitor_id`, `group_id`, `target_cnt` and `new_fans_cnt`, return `0` or an empty string in the sample response.
- For more audience data on the same creator, call [Douyin Account Fan Interest Search Terms](/apis/douyin/billboard/hot-account-fans-interest-search-list) or [Douyin Account Fan Interest Topics](/apis/douyin/billboard/hot-account-fans-interest-topic-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Account Fan Interest Search Terms](/apis/douyin/billboard/hot-account-fans-interest-search-list): Returns the top ten search terms reflecting fan interest over the last three days for a specified Douyin creator account using their user sec_id.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-account-fans-interest-account-list.json`](../../../../catalog/models/douyin/billboard/hot-account-fans-interest-account-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-account-fans-interest-account-list

# Douyin Hot Account Work Analysis API: pricing, parameters and code examples

`douyin/billboard/hot-account-item-analysis-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns analysis metrics for works associated with a specific hot Douyin account over the last week. Requires the target account user ID.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-account-item-analysis-list", "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-account-item-analysis-list', {'sec_uid': 'MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-account-item-analysis-list", {
  "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-account-item-analysis-list", sandbase.Params{
	"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_",
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-account-item-analysis-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sec_uid` | string | yes | User sec_id  |

## Details

Returns average engagement metrics for the works of one hot Douyin account over the last week. It needs the account's `sec_uid`. The response also gives percentile values and a change value for each metric.

### Use cases

- Compare a creator's average likes, comments and shares per work against the account's own previous period.
- Check how a creator's weekly average engagement ranks using the percentile fields.
- Screen hot Douyin accounts by average follower gain per work before a partnership.
- Track whether a creator's posting rate is rising or falling from week to week.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-account-item-analysis-list" \
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
  "data": {
    "BaseResp": null,
    "UserID": 0,
    "avg_aweme_count": 0.42857142857142855,
    "avg_aweme_count_c": 2,
    "avg_comment_count": 11.428571428571429,
    "avg_comment_count_c": -0.1752577319587629,
    "avg_follower_count": 31.285714285714285,
    "avg_follower_count_c": -0.39335180055401664,
    "avg_like_count": 3273.285714285714,
    "avg_like_count_c": -0.2215465108378067,
    "avg_share_count": 140.57142857142858,
    "avg_share_count_c": -0.5260115606936415
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
| `data.avg_aweme_count` | Average number of works posted per day or period for the account. The value is a decimal such as `0.43`. |
| `data.avg_like_count / data.avg_comment_count / data.avg_share_count` | Average likes, comments and shares per work for the account over the last week. |
| `data.avg_follower_count` | Average follower count figure for the account's works in the period. |
| `data.avg_aweme_count_c / data.avg_like_count_c / data.avg_comment_count_c / data.avg_share_count_c / data.avg_follower_count_c` | Change values for each average metric. Negative numbers such as `-0.22` point to a drop. Values look like ratios, not percentages. |
| `data.percentile_like_count / data.percentile_comment_count / data.percentile_share_count / data.percentile_follower_count / data.percentile_aweme_count` | Percentile-group reference values for each metric, given as numbers on the same scale as the matching `avg_` field. Use them as a comparison point against the account's own average. |
| `data.percentile_like_count_c / data.percentile_comment_count_c / data.percentile_share_count_c / data.percentile_follower_count_c / data.percentile_aweme_count_c` | Change values for each percentile figure. |
| `code / message` | `code` is `0` on this successful response. `message` is an empty string. |
| `extra.now` | A 13-digit timestamp (`1793691105000`) that looks like milliseconds since the Unix epoch. |

### Notes

- Pass the target account's `sec_uid` as the only request parameter. It is a string that starts with `MS4w`.
- `data.BaseResp` is `null` and `data.UserID` is `0` in this response, so do not rely on them.
- To find hot accounts first, call [Douyin Hot Account List](/apis/douyin/billboard/hot-account-list) or [Douyin Hot Account Search](/apis/douyin/billboard/hot-account-search-list).
- For metric history over time, see [Douyin Account Metric Trends](/apis/douyin/billboard/hot-account-trends-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-account-item-analysis-list.json`](../../../../catalog/models/douyin/billboard/hot-account-item-analysis-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-account-item-analysis-list

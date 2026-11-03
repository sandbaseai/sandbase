# Douyin Account Metric Trends API: pricing, parameters and code examples

`douyin/billboard/hot-account-trends-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns metric trend records for a Douyin account over time, including new likes, works, comments, or shares broken down by hour or day.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-account-trends-list", "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-account-trends-list', {'sec_uid': 'MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-account-trends-list", {
  "sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-account-trends-list", sandbase.Params{
	"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_",
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-account-trends-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `option` | integer |  | Option, 2 New like 3 New work 4 New comment 5 New share  |
| `sec_uid` | string | yes | User sec_id  |
| `date_window` | integer |  | Time window, 1 by hour 2 by day  |

## Details

Returns a time series of one metric for a Douyin account, plus the average value across the series. It needs the account's `sec_uid`. You can pick the metric with `option` and the interval with `date_window`.

### Use cases

- Chart daily new likes for a creator to see which days performed best.
- Compare new works, comments, and shares for an account over the same period.
- Switch to hourly values to find the times of day when an account gains the most engagement.
- Use the average value as a baseline to flag days that rise far above normal.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-account-trends-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | Yes | User sec_id |
| `date_window` | integer | No | Time window, 1 by hour 2 by day |
| `option` | integer | No | Option, 2 New like 3 New work 4 New comment 5 New share |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "avg": 24082.404494382023,
    "trends": [
      {
        "datetime": 1785859200,
        "value": 28479
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
| `data.trends[]` | List of data points in time order. Each item is one interval of the chosen metric. |
| `data.trends[].datetime` | Start time of the interval as a Unix timestamp in seconds. |
| `data.trends[].value` | Metric count for that interval. The metric depends on the `option` you send. |
| `data.avg` | Average of the metric across the returned interval values. |
| `code / message` | `code` is `0` on success. `message` is an empty string when there is no error. |

### Notes

- Get `sec_uid` from an account entry in [Douyin Hot Account List](/apis/douyin/billboard/hot-account-list) or [Douyin Hot Account Search](/apis/douyin/billboard/hot-account-search-list).
- `option` values: `2` new likes, `3` new works, `4` new comments, `5` new shares. `date_window` values: `1` by hour, `2` by day.
- In the example response, consecutive `datetime` values differ by `86400`, which matches one-day steps.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-account-trends-list.json`](../../../../catalog/models/douyin/billboard/hot-account-trends-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-account-trends-list

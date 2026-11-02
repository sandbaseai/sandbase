# Douyin Account Metric Trends API: pricing, parameters and code examples

`douyin/billboard/hot-account-trends-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns metric trend records for a Douyin account over time, including new likes, works, comments, or shares broken down by hour or day.

## Pricing

- **$0.0015 per call** (USD)
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

Retrieve historical trend data for an account by supplying `sec_uid`, with options to filter by metric type using `option` and aggregation period via `date_window`.

### Use cases

- Track hourly or daily engagement metrics for a Douyin creator.
- Analyze recent growth in likes, comments, and shares across user profiles.
- Monitor content output frequency and incoming engagement trends over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-account-trends-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"sec_uid": "MS4wLjABAAAAr52fXcfmzqOZJM_smap9Uuxtm16h8BupkCVaCt89BENq3E91mHCvtz5Z5TkXPHq_"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `sec_uid` | string | Yes | User sec_id |
| `option` | integer | No | Option, 2 New like 3 New work 4 New comment 5 New share |
| `date_window` | integer | No | Time window, 1 by hour 2 by day |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "trends": [
      {
        "datetime": 1783440000,
        "value": 1600
      }
    ]
  }
}
```

### Notes

- Use `option` to select the metric: 2 for new likes, 3 for new works, 4 for new comments, and 5 for new shares.
- Set `date_window` to 1 for hourly intervals or 2 for daily intervals.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/model/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/model/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/model/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-account-trends-list.json`](../../../../catalog/models/douyin/billboard/hot-account-trends-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-account-trends-list

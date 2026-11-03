# Douyin Xingtu Follower Growth Trend API: pricing, parameters and code examples

`douyin/xingtu-v3/data-sp-author-daily-fans` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Douyin Creator Marketplace (Xingtu) daily follower trend data for a specified creator and date range. Use it to review follower growth patterns during creator evaluation.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v3/data-sp-author-daily-fans", "oAuthorId": "6870161898013196295", "startDate": "2026-10-22", "endDate": "2026-10-29"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v3/data-sp-author-daily-fans', {'oAuthorId': '6870161898013196295', 'startDate': '2026-10-22', 'endDate': '2026-10-29'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v3/data-sp-author-daily-fans", {
  "oAuthorId": "6870161898013196295",
  "startDate": "2026-10-22",
  "endDate": "2026-10-29"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v3/data-sp-author-daily-fans", sandbase.Params{
	"oAuthorId": "6870161898013196295",
	"startDate": "2026-10-22",
	"endDate": "2026-10-29",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v3/data-sp-author-daily-fans` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `endDate` | string | yes | End Date (yyyy-MM-dd).  |
| `oAuthorId` | string | yes | Author's unique ID.  |
| `startDate` | string | yes | Start Date (yyyy-MM-dd).  |

## Details

Returns the daily follower count and the daily follower change for one Douyin creator on Xingtu over a date range. It needs the creator's `oAuthorId`, a `startDate` and an `endDate` in `yyyy-MM-dd` format.

### Use cases

- Check whether a creator's follower count grows steadily or jumps on a few days before you book them.
- Compare daily follower gains across several creators over the same week.
- Chart a creator's follower curve for a campaign report.
- Spot days with unusually high follower gain and match them to posted videos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v3/data-sp-author-daily-fans" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"oAuthorId": "6870161898013196295", "startDate": "2026-10-22", "endDate": "2026-10-29"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `endDate` | string | Yes | End Date (yyyy-MM-dd). |
| `oAuthorId` | string | Yes | Author's unique ID. |
| `startDate` | string | Yes | Start Date (yyyy-MM-dd). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "daily": [
    {
      "date": "2026-10-22",
      "fans_cnt": "188123075"
    }
  ],
  "delta": [
    {
      "date": "2026-10-22",
      "fans_cnt": "33258"
    }
  ],
  "description": "",
  "fans_advice": "",
  "fans_growth": "0",
  "fans_growth_rate": 0,
  "fans_growth_rate_v2": {
    "value": 42
  },
  "fans_growth_v2": {
    "value": 805004
  },
  "raw_play_rate": {}
}
```

### Response fields

| Field | Meaning |
|---|---|
| `daily[].date` | Calendar day for the row, formatted as `yyyy-MM-dd`. |
| `daily[].fans_cnt` | Total follower count of the creator on that day. The value is a string. |
| `delta[].date` | Calendar day for the follower change row. |
| `delta[].fans_cnt` | Follower change for that day. The value is a string. |
| `fans_growth_v2.value` | Follower growth number for the requested range, as a number. |
| `fans_growth_rate_v2.value` | Follower growth rate for the requested range, as a number. |
| `fans_growth / fans_growth_rate` | Older versions of the growth figures. They return `0` in this response, so use the `_v2` fields instead. |
| `base_resp.status_code` | Status of the request. `0` with an empty `status_message` means the call succeeded. |

### Notes

- Get `oAuthorId` from [Douyin Xingtu Creator Search](/apis/douyin/xingtu-v3/gsearch-search-for-author-square) or from [Douyin Xingtu Creator Profile](/apis/douyin/xingtu-v3/author-author-base-info).
- Counts in `daily[].fans_cnt` and `delta[].fans_cnt` are strings. Convert them to numbers before you do math.
- For the age, gender and region makeup of followers, call [Douyin Xingtu Follower Distribution](/apis/douyin/xingtu-v3/data-sp-author-fans-distribution).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v3/data-sp-author-daily-fans.json`](../../../../catalog/models/douyin/xingtu-v3/data-sp-author-daily-fans.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v3/data-sp-author-daily-fans

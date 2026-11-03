# Xiaohongshu Pugongying Follower Growth History API: pricing, parameters and code examples

`xiaohongshu/pgy-v2/user-id-fans-overall-new-history` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Xiaohongshu Pugongying follower history for a creator over the selected 30- or 90-day period. Use it to track total followers or new-follower growth over time.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/user-id-fans-overall-new-history", "userId": "5a73c5fa4eacab4c4ccc9778"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/user-id-fans-overall-new-history', {'userId': '5a73c5fa4eacab4c4ccc9778'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/user-id-fans-overall-new-history", {
  "userId": "5a73c5fa4eacab4c4ccc9778"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/user-id-fans-overall-new-history", sandbase.Params{
	"userId": "5a73c5fa4eacab4c4ccc9778",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/user-id-fans-overall-new-history` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | KOL's user ID.  |
| `dateType` | string |  | Time range for data. one of: `DAY_30`, `DAY_90`; default `"DAY_30"` |
| `increaseType` | string |  | Type of growth data. one of: `FANS_TOTAL`, `FANS_INCREASE`; default `"FANS_TOTAL"` |

## Details

Returns a daily follower time series for one Xiaohongshu creator listed on Pugongying (PGY), plus the total change over the period. It needs the creator's `userId`. You can pick a 30-day or 90-day window and choose total followers or new followers.

### Use cases

- Chart a creator's follower count day by day before you book a brand collaboration.
- Spot a creator whose followers are falling by comparing `fansNumInc` across a shortlist.
- Compare 30-day and 90-day windows to see whether growth is steady or came from one spike.
- Add follower trend lines to an influencer report or dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/user-id-fans-overall-new-history" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "5a73c5fa4eacab4c4ccc9778"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | KOL's user ID. |
| `dateType` | string | No | Time range for data. |
| `increaseType` | string | No | Type of growth data. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "fansNumInc": -18872,
  "fansNumIncRate": -0.0008,
  "list": [
    {
      "dateKey": "2026-10-04",
      "num": 25043018
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `fansNumInc` | Net change in the `num` value over the selected period. It is negative when the series went down. |
| `fansNumIncRate` | Change over the period as a decimal rate. For example, `-0.0008` means a drop of 0.08%. |
| `list[]` | One entry per day in the selected period, in date order. |
| `list[].dateKey` | Date of the data point, in `YYYY-MM-DD` format. |
| `list[].num` | Value for that date. With the default `increaseType` of `FANS_TOTAL` it is the total follower count. With `FANS_INCREASE` it is the new-follower figure. |

### Notes

- Pass `dateType` as `DAY_30` (default) or `DAY_90` to change the window.
- Set `increaseType` to `FANS_TOTAL` (default) for total followers or `FANS_INCREASE` for new-follower growth.
- Get the `userId` from [Xiaohongshu Pugongying Creator Search](/apis/xiaohongshu/pgy-v2/blogger-v2). It is a 24-character hex string.
- For a one-call snapshot of follower stats, use [Xiaohongshu Pugongying Follower Summary](/apis/xiaohongshu/pgy-v2/data-v3-fans-summary).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/user-id-fans-overall-new-history.json`](../../../../catalog/models/xiaohongshu/pgy-v2/user-id-fans-overall-new-history.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/user-id-fans-overall-new-history

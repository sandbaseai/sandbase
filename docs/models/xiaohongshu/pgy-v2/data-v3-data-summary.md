# Xiaohongshu Pugongying Data Summary API: pricing, parameters and code examples

`xiaohongshu/pgy-v2/data-v3-data-summary` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get the Xiaohongshu Pugongying data summary for a creator's daily or cooperation notes. Use it to compare aggregate creator performance between business modes.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/data-v3-data-summary", "userId": "64b898310000000014037b21"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/data-v3-data-summary', {'userId': '64b898310000000014037b21'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/data-v3-data-summary", {
  "userId": "64b898310000000014037b21"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/data-v3-data-summary", sandbase.Params{
	"userId": "64b898310000000014037b21",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/data-v3-data-summary` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | KOL's user ID.  |
| `business` | string |  | Business type. one of: `DAILY_NOTE`, `COOPERATE_NOTE`; default `"DAILY_NOTE"` |

## Details

Returns an aggregate performance summary for one Xiaohongshu Pugongying creator. It needs the creator's `userId` and can switch between daily notes and cooperation notes with `business`.

### Use cases

- Compare a creator's `DAILY_NOTE` summary with their `COOPERATE_NOTE` summary before booking a campaign.
- Check a creator's median reads and median interactions to set realistic campaign targets.
- Screen creators by 30-day follower growth and how they rank against others.
- Review the creator's content tag mix to confirm they fit a brand's category.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/data-v3-data-summary" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "64b898310000000014037b21"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | KOL's user ID. |
| `business` | string | No | Business type. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "activeDayInLast7": 7,
  "dateKey": "2026-11-02",
  "easyConnect": false,
  "estimatePictureCpm": 0,
  "estimatePictureCpmCompare": 0,
  "estimatePictureCpuv": 0,
  "estimatePictureCpuvCompare": 0,
  "estimatePictureEngageCost": 0,
  "estimatePictureEngageCostCompare": 0,
  "estimateVideoCpm": 0,
  "estimateVideoCpmCompare": 0,
  "estimateVideoCpuv": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `readMedian` | Median read count for the creator's notes. |
| `interactionMedian / interactionBeyondRate` | Median interaction count per note, and the share of creators the creator beats on interaction (`11.2` in the sample). |
| `fans30GrowthRate / fans30GrowthBeyondRate` | Follower growth rate over the last 30 days, and the share of creators the creator beats on that growth. Both come as strings. |
| `mAccumImpNum / mAccumImpCompare` | Accumulated impressions figure and its comparison value. |
| `mEngagementNum / mEngagementNumCompare` | Engagement count and its comparison value. |
| `mValidRawReadFeedNum / mValidRawReadFeedCompare` | Valid read count from feed and its comparison value. |
| `noteNumber` | Number of notes counted for this creator. |
| `noteType[].contentTag / noteType[].percent` | Content tag name and the share of notes under that tag, as a string. |
| `kolAdvantage / kolAdvantageHover` | Label for the creator's strength, with a short explanation. Both are returned in Chinese. |
| `activeDayInLast7 / isActive` | Number of active days in the last 7 days, and whether the creator is currently active. |

### Notes

- Pass `userId` as the creator's ID string, for example `64b898310000000014037b21`. Find it with [Xiaohongshu Pugongying Creator Search](/apis/xiaohongshu/pgy-v2/blogger-v2).
- `business` accepts `DAILY_NOTE` (default) or `COOPERATE_NOTE`. Call the API twice to compare both modes.
- Cost and CPM fields such as `estimateVideoCpm` and `estimatePictureCpm` return `0` in the sample.
- `dateKey` is a date in `YYYY-MM-DD` format. For more detail, call [Xiaohongshu Pugongying Follower Summary](/apis/xiaohongshu/pgy-v2/data-v3-fans-summary).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/data-v3-data-summary.json`](../../../../catalog/models/xiaohongshu/pgy-v2/data-v3-data-summary.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/data-v3-data-summary

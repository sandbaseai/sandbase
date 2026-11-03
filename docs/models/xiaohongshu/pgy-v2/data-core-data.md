# Xiaohongshu Pugongying Creator Core Metrics API: pricing, parameters and code examples

`xiaohongshu/pgy-v2/data-core-data` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.021429 per call · **Modes:** sync

Get Xiaohongshu Pugongying core data for a creator with business, note-type, date-range, and advertisement filters. Use it to compare creators within a selected analysis scope.

## Pricing

- **$0.021429 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy-v2/data-core-data", "userId": "5a73c5fa4eacab4c4ccc9778"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy-v2/data-core-data', {'userId': '5a73c5fa4eacab4c4ccc9778'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy-v2/data-core-data", {
  "userId": "5a73c5fa4eacab4c4ccc9778"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy-v2/data-core-data", sandbase.Params{
	"userId": "5a73c5fa4eacab4c4ccc9778",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy-v2/data-core-data` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `userId` | string | yes | KOL's user ID.  |
| `business` | string |  | Business type. one of: `DAILY_NOTE`, `COOPERATE_NOTE`; default `"DAILY_NOTE"` |
| `dateType` | string |  | Time range for data. one of: `DAY_30`, `DAY_90`; default `"DAY_30"` |
| `noteType` | string |  | Type of note. one of: `PHOTO_TEXT_AND_VIDEO`, `PHOTO_TEXT`, `VIDEO`; default `"PHOTO_TEXT_AND_VIDEO"` |
| `advertiseSwitch` | string |  | Advertisement filter. one of: `ALL`, `ORGANIC_ONLY`; default `"ALL"` |

## Details

Returns core performance metrics for one Xiaohongshu Pugongying creator: a daily series and a summary row. It needs the creator's `userId` and accepts optional filters for business type, note type, date range, and ad scope.

### Use cases

- Compare two creators on `cpm` and `cpe` under the same filters before choosing who to book.
- Chart a creator's daily `imp`, `read`, and `engage` to spot spikes or drops over 30 or 90 days.
- Check organic-only performance by setting `advertiseSwitch` to `ORGANIC_ONLY` and comparing it with the `ALL` result.
- Compare cooperation notes with daily notes by switching `business` between `COOPERATE_NOTE` and `DAILY_NOTE`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy-v2/data-core-data" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"userId": "5a73c5fa4eacab4c4ccc9778"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `userId` | string | Yes | KOL's user ID. |
| `advertiseSwitch` | string | No | Advertisement filter. |
| `business` | string | No | Business type. |
| `dateType` | string | No | Time range for data. |
| `noteType` | string | No | Type of note. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "dailyData": [
    {
      "cpe": 0.45091447660934664,
      "cpm": 14.582954416499165,
      "cpuv": 0,
      "cpv": 0,
      "dateKey": "2026-10-04",
      "engage": 332868,
      "imp": 10292496,
      "read": 1783903,
      "thirdUserNum": 0
    }
  ],
  "sumData": {
    "cpe": 0.5016533982432853,
    "cpm": 20.009503630677656,
    "cpuv": 0,
    "cpv": 0,
    "dateKey": "2026-11-02",
    "engage": 299081,
    "imp": 7498187,
    "read": 1557364,
    "thirdUserNum": 0
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `dailyData[]` | One row per day in the selected range. Use it to build a time series. |
| `dailyData[].dateKey` | Date of the row in `YYYY-MM-DD` format. |
| `dailyData[].imp / sumData.imp` | Impressions for that day, and for the summary row. |
| `dailyData[].read / sumData.read` | Reads for that day, and for the summary row. |
| `dailyData[].engage / sumData.engage` | Engagement count for that day, and for the summary row. |
| `dailyData[].cpe / sumData.cpe` | Cost per engagement. Compare it across creators under the same filters. |
| `dailyData[].cpm / sumData.cpm` | Cost per thousand impressions. Compare it across creators under the same filters. |
| `dailyData[].cpv / sumData.cpv` | Cost per view. It is `0` in the sample response. |
| `dailyData[].cpuv / sumData.cpuv` | Cost per unique viewer. It is `0` in the sample response. |
| `sumData` | Summary row for the whole selected scope. It uses the same metric keys as `dailyData[]`. |

### Notes

- `userId` is the creator's Pugongying ID, a 24-character hex string such as `5a73c5fa4eacab4c4ccc9778`. Find it with [Xiaohongshu Pugongying Creator Search](/apis/xiaohongshu/pgy-v2/blogger-v2).
- Defaults are `business` `DAILY_NOTE`, `noteType` `PHOTO_TEXT_AND_VIDEO`, `dateType` `DAY_30`, and `advertiseSwitch` `ALL`.
- For a broader view of the same creator, call [Xiaohongshu Pugongying Data Summary](/apis/xiaohongshu/pgy-v2/data-v3-data-summary).

### Pricing

$0.021429 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy-v2/data-core-data.json`](../../../../catalog/models/xiaohongshu/pgy-v2/data-core-data.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy-v2/data-core-data

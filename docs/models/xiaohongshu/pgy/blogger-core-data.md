# Xiaohongshu (RED) Blogger Core Data API: pricing, parameters and code examples

`xiaohongshu/pgy/blogger-core-data` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.02 per call · **Modes:** sync

Returns Pugongying core performance metrics and daily trend data for a specified Xiaohongshu blogger, filterable by date range, note type, and traffic source.

## Pricing

- **$0.02 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/pgy/blogger-core-data", "user_id": "60b137080000000001000301"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/pgy/blogger-core-data', {'user_id': '60b137080000000001000301'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/pgy/blogger-core-data", {
  "user_id": "60b137080000000001000301"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/pgy/blogger-core-data", sandbase.Params{
	"user_id": "60b137080000000001000301",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/pgy/blogger-core-data` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | Blogger user ID  |
| `date_type` | integer |  | Date range (~1=7d, 2=30d, 3=90d) range 1–12 |
| `note_type` | integer |  | Note type, 1=image, 2=video, 3=all (default) one of: `1`, `2`, `3` |
| `advertise_switch` | integer |  | Traffic type, 1=all (incl. ads), 0=organic only one of: `0`, `1` |

## Details

Returns core performance metrics for a Xiaohongshu blogger on the Pugongying (PGY) platform. The response has a list of daily values and one summary object. The only required input is the blogger `user_id`.

### Use cases

- Chart a blogger's daily impressions, reads and engagement over a chosen period.
- Compare organic-only numbers with numbers that include ads by setting `advertise_switch`.
- Check whether a blogger's video notes or image notes get more reads by setting `note_type`.
- Pull the summary row to screen many bloggers before a campaign.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/pgy/blogger-core-data" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "60b137080000000001000301"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | Blogger user ID |
| `advertise_switch` | integer | No | Traffic type, 1=all (incl. ads), 0=organic only |
| `date_type` | integer | No | Date range (~1=7d, 2=30d, 3=90d) |
| `note_type` | integer | No | Note type, 1=image, 2=video, 3=all (default) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "dailyData": [
      {
        "cpe": 0,
        "cpm": 0,
        "cpuv": 0,
        "cpv": 0,
        "dateKey": "2026-10-04",
        "engage": 10,
        "imp": 1467,
        "read": 138,
        "thirdUserNum": 0
      }
    ],
    "sumData": {
      "cpe": 0,
      "cpm": 0,
      "cpuv": 0,
      "cpv": 0,
      "dateKey": "2026-11-02",
      "engage": 9,
      "imp": 1577,
      "read": 115,
      "thirdUserNum": 0
    }
  },
  "msg": "成功",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.dailyData[].dateKey` | Date of the daily row, in `YYYY-MM-DD` format. |
| `data.dailyData[].imp` | Impressions for that day. |
| `data.dailyData[].read` | Reads for that day. |
| `data.dailyData[].engage` | Engagement count for that day. |
| `data.dailyData[].cpm / data.dailyData[].cpv / data.dailyData[].cpe / data.dailyData[].cpuv` | Cost metrics for that day. The sample shows `0` for all of them. |
| `data.dailyData[].thirdUserNum` | Count named `thirdUserNum`. The sample shows `0`. |
| `data.sumData.imp / data.sumData.read / data.sumData.engage` | Summary values for impressions, reads and engagement over the selected range. |
| `data.sumData.dateKey` | Date attached to the summary object. |
| `data.sumData.cpm / data.sumData.cpv / data.sumData.cpe / data.sumData.cpuv` | Cost metrics in the summary object. The sample shows `0` for all of them. |

### Notes

- `user_id` is a 24-character hex string, for example `60b137080000000001000301`.
- `date_type` takes a value from 1 to 12. The documented values are `1` for 7 days, `2` for 30 days and `3` for 90 days.
- `note_type` accepts `1` for image, `2` for video and `3` for all notes. `advertise_switch` accepts `1` for all traffic including ads and `0` for organic only.
- To find a `user_id`, use [Xiaohongshu (RED) PGY Blogger Search](/apis/xiaohongshu/pgy/blogger-list). For profile data, call [Xiaohongshu (RED) PGY Blogger Details](/apis/xiaohongshu/pgy/blogger-detail).

### Pricing

$0.02 per successful call. Failed calls are not charged.

### Related APIs

- [Xiaohongshu (RED) PGY Blogger Data Summary](/apis/xiaohongshu/pgy/blogger-data-summary): Returns an account-level data summary for a Xiaohongshu blogger on the Pugongying (PGY) platform based on the specified blogger user ID.
- [Xiaohongshu (RED) PGY Blogger Details](/apis/xiaohongshu/pgy/blogger-detail): Retrieves detailed profile information for a specific Xiaohongshu blogger on the PGY platform using their user ID.
- [Xiaohongshu (RED) PGY Blogger Fan History](/apis/xiaohongshu/pgy/blogger-fans-history): Returns historical follower growth counts for a Xiaohongshu Pugongying blogger over time based on user ID and a selected date range.

---
Machine-readable: [`catalog/models/xiaohongshu/pgy/blogger-core-data.json`](../../../../catalog/models/xiaohongshu/pgy/blogger-core-data.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/pgy/blogger-core-data

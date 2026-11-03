# Douyin Item Report Trend API: pricing, parameters and code examples

`douyin/xingtu-v2/item-report-trend` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call · **Modes:** sync

Get Item Report Trend on Douyin. Returns the platform data as structured JSON.

## Pricing

- **$0.003 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/item-report-trend", "item_id": "7372484719365098803"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/item-report-trend', {'item_id': '7372484719365098803'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/item-report-trend", {
  "item_id": "7372484719365098803"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/item-report-trend", sandbase.Params{
	"item_id": "7372484719365098803",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/item-report-trend` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `item_id` | string | yes | Video (item) ID  |

## Details

Returns a day-by-day report for one Douyin video in the Xingtu data set. The response holds daily series for views, likes, comments, shares, saves, interactions and hot score. It needs the video's `item_id`.

### Use cases

- Plot the daily views and likes of a sponsored video to see when it peaked.
- Compare `hot_score_list` with `vv_list` to check whether a video kept gaining attention after launch.
- Track daily shares and saves to judge how viewers react to a brand video over time.
- Build a campaign report that lists daily interaction counts for each video in a creator deal.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/item-report-trend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"item_id": "7372484719365098803"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `item_id` | string | Yes | Video (item) ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "base_resp": {
    "status_code": 0,
    "status_message": ""
  },
  "date_values": {
    "collect_cnt_list": [
      {
        "value": "1499",
        "visit_date": 20240524
      }
    ],
    "comment_cnt_list": [
      {
        "value": "290",
        "visit_date": 20240524
      }
    ],
    "finish_rate_list": [
      {
        "value": "1417",
        "visit_date": 20240524
      }
    ],
    "hot_score_list": [
      {
        "value": "379715",
        "visit_date": 20240524
      }
    ],
    "interact_cnt_list": [
      {
        "value": "27332",
        "visit_date": 20240524
      }
    ],
    "interact_rate_list": [
      {
        "value": "1524",
        "visit_date": 20240524
      }
    ],
    "like_cnt_list": [
      {
        "value": "23593",
        "visit_date": 20240524
      }
    ],
    "share_cnt_list": [
      {
        "value": "3449",
        "visit_date": 20240524
      }
    ],
    "valid_vv_list": [
      {
        "value": "147568",
        "visit_date": 20240524
      }
    ],
    "vv_list": [
      {
        "value": "179250",
        "visit_date": 20240524
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `date_values.vv_list[].value / date_values.valid_vv_list[].value` | Daily view count for the date in `visit_date`. `valid_vv_list` is a separate series with lower numbers, so treat it as a filtered view count. |
| `date_values.like_cnt_list[].value / date_values.comment_cnt_list[].value / date_values.share_cnt_list[].value / date_values.collect_cnt_list[].value` | Daily counts of likes, comments, shares and saves (collects) for that date. |
| `date_values.interact_cnt_list[].value` | Daily total interaction count for that date. |
| `date_values.hot_score_list[].value` | Daily hot score of the video for that date. |
| `date_values.interact_rate_list[].value / date_values.finish_rate_list[].value` | Daily interaction rate and finish rate. The values are whole numbers (for example `1524`), and the response does not state the scale. |
| `date_values.*[].visit_date` | Date of the data point as an integer in `YYYYMMDD` form, for example `20240524`. |
| `base_resp.status_code / base_resp.status_message` | Status of the call. `0` with an empty message means it succeeded. |

### Notes

- All `value` fields are strings. Convert them to numbers before you calculate.
- Each series in `date_values` is a list of `value` and `visit_date` pairs, one per day.
- Send the video ID as `item_id`. Use [Douyin Xingtu Author Homepage Videos](/apis/douyin/xingtu-v2/author-homepage-videos) to find video IDs for a creator.
- For totals and other details on the same video, call [Douyin Item Report Detail](/apis/douyin/xingtu-v2/item-report-detail).

### Pricing

$0.003 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/item-report-trend.json`](../../../../catalog/models/douyin/xingtu-v2/item-report-trend.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/item-report-trend

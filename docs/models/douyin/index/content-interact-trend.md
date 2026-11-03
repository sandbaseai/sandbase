# Douyin Category Content Interaction Trend API: pricing, parameters and code examples

`douyin/index/content-interact-trend` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns engagement rate trends over time for a specific Douyin content category between selected start and end dates.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/content-interact-trend", "end_date": "20260414", "start_date": "20260314", "tag_id": "601"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/content-interact-trend', {'end_date': '20260414', 'start_date': '20260314', 'tag_id': '601'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/content-interact-trend", {
  "end_date": "20260414",
  "start_date": "20260314",
  "tag_id": "601"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/content-interact-trend", sandbase.Params{
	"end_date": "20260414",
	"start_date": "20260314",
	"tag_id": "601",
})
```

Same call via the path form: `POST /v1/api/douyin/index/content-interact-trend` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tag_id` | string | yes | Category ID (**required, does NOT support 0=all**, must pass a specific category ID)  |
| `end_date` | string | yes | End date YYYYMMDD (inclusive)  |
| `start_date` | string | yes | Start date YYYYMMDD (inclusive)  |

## Details

Returns a daily engagement rate series for one Douyin content category between a start and end date. It also returns top videos for some dates in that range. The input is a category `tag_id` plus `start_date` and `end_date` in `YYYYMMDD` format.

### Use cases

- Chart the daily engagement rate of one Douyin category over a month.
- Spot dates where a category's engagement rate rises or drops, then check the top videos for those dates.
- Compare engagement rate between two date ranges for the same category.
- Collect example videos that performed well in a category on specific days.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/content-interact-trend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "20260414", "start_date": "20260314", "tag_id": "601"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_date` | string | Yes | End date YYYYMMDD (inclusive) |
| `start_date` | string | Yes | Start date YYYYMMDD (inclusive) |
| `tag_id` | string | Yes | Category ID (**required, does NOT support 0=all**, must pass a specific category ID) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": 0,
    "StatusMessage": ""
  },
  "interact_trend": {
    "rate_list": [
      {
        "date": "20260314",
        "rate": 0.02431060923716989
      }
    ],
    "top_list": [
      {
        "date": "20260404",
        "item_list": [
          {
            "img": "https://p6-byteindex-sign.byteimg.com/tos-cn-p-0015c000-ce/okAZEAzpeERA89MIF8QfC…",
            "item_id": "7624773628463404667",
            "title": "假装小手被绑住 动不了咯#一人分饰多角",
            "url": "https://www.douyin.com/share/video/7624773628463404667"
          }
        ]
      }
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `interact_trend.rate_list[].date` | Day of the data point, formatted as `YYYYMMDD`. |
| `interact_trend.rate_list[].rate` | Engagement rate for the category on that day, as a decimal fraction. For example, `0.0243` is about 2.4%. |
| `interact_trend.top_list[].date` | Date for which top videos are listed. Only some dates in the range appear here. |
| `interact_trend.top_list[].item_list[].item_id` | ID of a top video for that date. |
| `interact_trend.top_list[].item_list[].title` | Video caption, including hashtags. |
| `interact_trend.top_list[].item_list[].url` | Share link to the video on douyin.com. |
| `interact_trend.top_list[].item_list[].img` | Cover image URL for the video. The URL carries an expiry parameter, so it may stop working. |
| `BaseResp.StatusCode / BaseResp.StatusMessage` | Request status. `0` with an empty message appears in a successful response. |

### Notes

- `tag_id` must be a specific category ID. `0` for all categories is not supported.
- Both `start_date` and `end_date` are inclusive.
- `top_list` does not need to contain every date that appears in `rate_list`.
- To check which dates have data, call [Douyin Content Guide Valid Dates](/apis/douyin/index/content-valid-date). For volume and consumption of the same category, see [Douyin Content Volume Trend](/apis/douyin/index/content-publish-trend) and [Douyin Content Consumption Trend](/apis/douyin/index/content-consume-trend).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/content-interact-trend.json`](../../../../catalog/models/douyin/index/content-interact-trend.json) · Store page: https://www.sandbase.ai/model/douyin/index/content-interact-trend

# Douyin Billboard Hot Calendar List

`douyin/billboard/hot-calendar-list` · api · Douyin

Retrieves the Douyin trending activity calendar with event details, schedules, and categories. Supports filtering by date range, city code, and category code.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-calendar-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-calendar-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-calendar-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-calendar-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-calendar-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `end_date` | integer |  | Snapshot end time format 10 digit timestamp default `1735488000` |
| `city_code` | string |  | City code, get from city list, empty for all default `""` |
| `start_date` | integer |  | Snapshot start time format 10 digit timestamp default `1734902400` |
| `category_code` | string |  | Hot list category code, get from hot list category, empty for all default `""` |

## Details

Fetch scheduled trending events from the Douyin billboard using optional `start_date`, `end_date`, `city_code`, and `category_code` filters.

### Use cases

- Track upcoming trending events on Douyin across specific dates.
- Filter scheduled activities by city and content category.
- Monitor event schedules and status for marketing campaign planning.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-calendar-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_date` | integer | No | Snapshot end time format 10 digit timestamp |
| `city_code` | string | No | City code, get from city list, empty for all |
| `start_date` | integer | No | Snapshot start time format 10 digit timestamp |
| `category_code` | string | No | Hot list category code, get from hot list category, empty for all |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "event_list": [
      {
        "category_name": "美食",
        "cover_url": "http://p6-dyhot.byteimg.com/tos-cn-i-jid1fmi4d3/b2a4e31229c85f2d04b83278a2ce2082.png",
        "end_date": 1735660799,
        "event_status": -1,
        "hot_title": "冬日与干净饮食的适配度",
        "id": 1549,
        "parent_id": 1462,
        "publish_cnt": 0,
        "start_date": 1730304000
      }
    ]
  }
}
```

### Notes

- `start_date` and `end_date` accept 10-digit Unix timestamps.
- Pass empty strings to `city_code` and `category_code` to retrieve activities for all cities and categories.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/model/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/model/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/model/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-calendar-list.json`](../../../../catalog/models/douyin/billboard/hot-calendar-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-calendar-list

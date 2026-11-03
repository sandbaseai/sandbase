# Douyin Billboard Hot Calendar List API: pricing, parameters and code examples

`douyin/billboard/hot-calendar-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves the Douyin trending activity calendar with event details, schedules, and categories. Supports filtering by date range, city code, and category code.

## Pricing

- **$0.001 per call** (USD)
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

Returns the Douyin trending activity calendar as two lists: scheduled events and the larger topics they belong to. All inputs are optional. You can filter by `start_date`, `end_date`, `city_code` and `category_code`.

### Use cases

- Plan content around upcoming food, travel or seasonal events on Douyin by reading each event's `start_date` and `end_date`.
- Group events under their parent topics to see which campaigns, such as a new year season, contain several events.
- Filter the calendar by city to find local activities for a regional campaign.
- Build an internal editorial calendar from event titles, categories and cover images.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-calendar-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_code` | string | No | Hot list category code, get from hot list category, empty for all |
| `city_code` | string | No | City code, get from city list, empty for all |
| `end_date` | integer | No | Snapshot end time format 10 digit timestamp |
| `start_date` | integer | No | Snapshot start time format 10 digit timestamp |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": 0,
  "data": {
    "event_list": [
      {
        "category_name": "美食",
        "city_name": "",
        "cover_url": "http://p6-dyhot.byteimg.com/tos-cn-i-jid1fmi4d3/b2a4e31229c85f2d04b83278a2ce2082…",
        "end_date": 1735660799,
        "event_ids": null,
        "event_status": -1,
        "hot_title": "冬日与干净饮食的适配度",
        "id": 1549,
        "is_favorite": 0,
        "level_code": 2,
        "parent_id": 1462,
        "publish_cnt": 0
      }
    ],
    "topic_list": [
      {
        "category_name": "",
        "city_name": "",
        "cover_url": "",
        "end_date": 1738684799,
        "event_ids": [
          1718
        ],
        "event_status": -1,
        "hot_title": "抖音生活新年季",
        "id": 1717,
        "is_favorite": 0,
        "level_code": 1,
        "parent_id": 0,
        "publish_cnt": 0
      }
    ]
  },
  "extra": {
    "now": 1793691106000
  },
  "message": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.event_list[].hot_title` | Title of the scheduled event. |
| `data.event_list[].category_name` | Content category of the event, such as food. The topic entries in `topic_list` leave it empty. |
| `data.event_list[].start_date / data.event_list[].end_date` | Start and end of the event as 10-digit Unix timestamps. |
| `data.event_list[].id` | ID of the event. Topic entries list it in `event_ids`. |
| `data.event_list[].parent_id` | ID of the topic the event belongs to. The value `0` means no parent topic appears in the response. |
| `data.event_list[].cover_url` | Cover image URL for the event. It is an empty string for topics. |
| `data.topic_list[].hot_title` | Title of a larger topic or campaign that groups events. |
| `data.topic_list[].event_ids` | List of event IDs that belong to this topic. |
| `data.topic_list[].level_code` | Level marker of the entry. Topics show `1` and events show `2` in this response. |
| `data.event_list[].city_name / data.event_list[].event_status / data.event_list[].publish_cnt` | City name, status code and publish count of the event. In the sample they are empty, `-1` and `0`. |

### Notes

- Send `start_date` and `end_date` as 10-digit Unix timestamps in seconds.
- Leave `city_code` and `category_code` empty to get all cities and all categories.
- Get `city_code` values from [Douyin Billboard City List](/apis/douyin/billboard/city-list) and `category_code` values from [Douyin Billboard Hot Category List](/apis/douyin/billboard/hot-category-list).
- To read one calendar entry in detail, call [Douyin Billboard Hot Calendar Detail](/apis/douyin/billboard/hot-calendar-detail).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-calendar-list.json`](../../../../catalog/models/douyin/billboard/hot-calendar-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-calendar-list

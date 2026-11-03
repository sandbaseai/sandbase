# Douyin Creator Mission Task List API: pricing, parameters and code examples

`douyin/creator/mission-task-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns creator mission tasks from Douyin with filtering options. Supports filters for industry classification, search keywords, mission type, and release timeframes.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/mission-task-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/mission-task-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/mission-task-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/mission-task-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/creator/mission-task-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Number of tasks per page, recommended 24 range 1–100 |
| `cursor` | integer |  | Cursor for pagination, 0 for first page range 0– |
| `keyword` |  |  | Keyword search (optional, supports task name or task ID)  |
| `pay_type` |  |  | Payment type (optional)  |
| `tab_scene` | integer |  | Scene type  |
| `industry_lv1` | integer |  | Primary industry (-1=All).  |
| `industry_lv2` | integer |  | Secondary industry (-1=All).  |
| `mission_type` | integer |  | Mission type, usually 1  |
| `platform_channel` |  |  | Platform channel (optional)  |
| `publish_time_start` |  |  | Publish start time filter (optional, timestamp format)  |
| `quick_selector_scene` |  |  | Quick filter scene (optional)  |
| `greater_than_cost_progress` |  |  | Cost progress filter (optional)  |

## Details

Returns a paged list of Douyin creator mission tasks, with each task's name, ID, industry IDs, run dates and commission settings. All inputs are optional, so you can send an empty body to get the first page, or add filters such as `keyword`, `industry_lv1` and `mission_type`.

### Use cases

- List open Douyin creator missions and read each task's start and end dates.
- Find a mission by task name or task ID with `keyword`.
- Narrow missions to one industry by setting `industry_lv1` and `industry_lv2`.
- Compare `task_commission.pay_type` values across missions to group tasks by payment model.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/mission-task-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cursor` | integer | No | Cursor for pagination, 0 for first page |
| `greater_than_cost_progress` | string | No | Cost progress filter (optional) |
| `industry_lv1` | integer | No | Primary industry (-1=All). |
| `industry_lv2` | integer | No | Secondary industry (-1=All). |
| `keyword` | string | No | Keyword search (optional, supports task name or task ID) |
| `limit` | integer | No | Number of tasks per page, recommended 24 |
| `mission_type` | integer | No | Mission type, usually 1 |
| `pay_type` | string | No | Payment type (optional) |
| `platform_channel` | string | No | Platform channel (optional) |
| `publish_time_start` | string | No | Publish start time filter (optional, timestamp format) |
| `quick_selector_scene` | string | No | Quick filter scene (optional) |
| `tab_scene` | integer | No | Scene type |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "has_more": true,
  "mission_cards": [
    {
      "brand_logo": "",
      "brand_name": "",
      "content_type": 2,
      "end_time": 1801238399,
      "first_industry_id": 1913,
      "icon": "https://p26-star-fe-sign.byteimg.com/tos-cn-i-9hvokabxw2/ad3ea81874524f6d8c67bb5…",
      "id_str": "7600738522332905512",
      "name": "孤勇无双直播任务",
      "second_industry_id": 191311,
      "start_time": 1769738400,
      "task_commission": {
        "budget": 0,
        "commission_rate": 0,
        "convert_unit_amount": 0,
        "cpm_vv_price": 0,
        "max_settled_price": 0,
        "min_settled_price": 0,
        "pay_type": 17,
        "remain_reward_amount": 0
      }
    }
  ],
  "next_cursor": 24,
  "status_code": 0,
  "status_msg": "",
  "total_num": 8209
}
```

### Response fields

| Field | Meaning |
|---|---|
| `total_num` | Total number of tasks that match the request. |
| `has_more` | Shows whether another page of tasks is available. |
| `next_cursor` | Value to send as `cursor` to get the next page. |
| `mission_cards[].id_str` | Task ID as a string. Keep it as a string because the number is long. |
| `mission_cards[].name` | Task name, in Chinese in the sample response. |
| `mission_cards[].start_time / mission_cards[].end_time` | Start and end of the task as Unix timestamps in seconds. |
| `mission_cards[].first_industry_id / mission_cards[].second_industry_id` | IDs of the primary and secondary industry the task belongs to. |
| `mission_cards[].content_type` | Numeric content type of the task. The sample tasks all return `2`. |
| `mission_cards[].brand_name / mission_cards[].brand_logo` | Brand name and logo of the task. Both can be empty strings. |
| `mission_cards[].task_commission.pay_type` | Numeric payment type of the task. Related fields in the same object are `budget`, `commission_rate`, `min_settled_price` and `max_settled_price`. |

### Notes

- Start with `cursor` set to `0`. Pass `next_cursor` from the response as `cursor` for the next page, and stop when `has_more` is false.
- Set `limit` between 1 and 100 to change the page size. The parameter description recommends 24.
- Set `industry_lv1` and `industry_lv2` to `-1` to include all industries. Use [Douyin Creator Industry Category Config](/apis/douyin/creator/industry-category-config) to look up industry IDs.
- `start_time` and `end_time` are Unix timestamps in seconds.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/mission-task-list.json`](../../../../catalog/models/douyin/creator/mission-task-list.json) · Store page: https://www.sandbase.ai/model/douyin/creator/mission-task-list

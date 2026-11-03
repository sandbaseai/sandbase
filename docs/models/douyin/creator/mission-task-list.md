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

Retrieve available creator mission tasks on Douyin using query parameters like `keyword`, `mission_type`, and `cursor`.

### Use cases

- Search Douyin mission tasks by task name or ID.
- Filter missions across primary and secondary industry tiers.
- Track task opportunities matching specific channel criteria.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/mission-task-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `limit` | integer | No | Number of tasks per page, recommended 24 |
| `cursor` | integer | No | Cursor for pagination, 0 for first page |
| `keyword` | string | No | Keyword search (optional, supports task name or task ID) |
| `pay_type` | string | No | Payment type (optional) |
| `tab_scene` | integer | No | Scene type |
| `industry_lv1` | integer | No | Primary industry (-1=All). |
| `industry_lv2` | integer | No | Secondary industry (-1=All). |
| `mission_type` | integer | No | Mission type, usually 1 |
| `platform_channel` | string | No | Platform channel (optional) |
| `publish_time_start` | string | No | Publish start time filter (optional, timestamp format) |
| `quick_selector_scene` | string | No | Quick filter scene (optional) |
| `greater_than_cost_progress` | string | No | Cost progress filter (optional) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "status_code": 0,
  "total_num": 0
}
```

### Notes

- Use `cursor` starting at 0 for pagination and `limit` to set items per page (default recommended is 24).
- Set `industry_lv1` and `industry_lv2` to -1 to query all industry categories.
- Filter tasks by release timestamp using `publish_time_start`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/mission-task-list.json`](../../../../catalog/models/douyin/creator/mission-task-list.json) · Store page: https://www.sandbase.ai/model/douyin/creator/mission-task-list

# Douyin Xingtu IP Activity List API: pricing, parameters and code examples

`douyin/xingtu-v2/ip-activity-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Returns Xingtu IP calendar activities across designated time windows, with optional filters for activity status, categories, and industries.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/ip-activity-list", "query_end_time": "1774972799", "query_start_time": "1767196800"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/ip-activity-list', {'query_end_time': '1774972799', 'query_start_time': '1767196800'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/ip-activity-list", {
  "query_end_time": "1774972799",
  "query_start_time": "1767196800"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/ip-activity-list", sandbase.Params{
	"query_end_time": "1774972799",
	"query_start_time": "1767196800",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/ip-activity-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `status_list` |  |  | IP status list  |
| `category_list` |  |  | IP category list  |
| `query_end_time` | string | yes | Query end timestamp, e.g. `1774972799`  |
| `industry_id_list` |  |  | Industry ID list  |
| `query_start_time` | string | yes | Query start timestamp, e.g. `1767196800`  |

## Details

Retrieve a list of Xingtu IP calendar activities for a given timeframe using `query_start_time` and `query_end_time`.

### Use cases

- Look up upcoming Douyin Xingtu IP activities within a scheduled time range.
- Filter marketing campaign calendars by activity category and industry IDs.
- Monitor investment and campaign schedules for brand collaboration planning.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/ip-activity-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query_end_time": "1774972799", "query_start_time": "1767196800"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query_end_time` | string | Yes | Query end timestamp, e.g. |
| `query_start_time` | string | Yes | Query start timestamp, e.g. |
| `status_list` | string | No | IP status list |
| `category_list` | string | No | IP category list |
| `industry_id_list` | string | No | Industry ID list |

### Notes

- `query_start_time` and `query_end_time` require Unix timestamps.
- Refine queries using `status_list`, `category_list`, and `industry_id_list`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/ip-activity-list.json`](../../../../catalog/models/douyin/xingtu-v2/ip-activity-list.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/ip-activity-list

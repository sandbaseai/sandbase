# Douyin Total Hot Billboard API: pricing, parameters and code examples

`douyin/billboard/hot-total-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Douyin total hot list billboard entries across specified time ranges. Supports filtering by snapshot type, keyword, category tags, and date range with pagination controls.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-total-list", "page": 1, "page_size": 10, "type": "snapshot"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-total-list', {'page': 1, 'page_size': 10, 'type': 'snapshot'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-total-list", {
  "page": 1,
  "page_size": 10,
  "type": "snapshot"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-total-list", sandbase.Params{
	"page": 1,
	"page_size": 10,
	"type": "snapshot",
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-total-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer | yes | Page number  |
| `type` | string | yes | Snapshot type snapshot view by time range view by time range.  |
| `keyword` | string |  | Hot search term  |
| `end_date` | string |  | Snapshot end time format yyyyMMdd  |
| `page_size` | integer | yes | Number of items per page  |
| `start_date` | string |  | Snapshot start time format yyyyMMdd  |
| `sentence_tag` | string |  | Hot category tag, get from hot list category, multiple categories separated by commas, empty for all  |
| `snapshot_time` | string |  | Snapshot time format yyyyMMddHHmmss  |

## Details

Look up overall trending search rankings on Douyin using `type`, `page`, and `page_size`. Filter results by `keyword`, `sentence_tag`, or snapshot date ranges.

### Use cases

- Track overall trending search rankings on Douyin across specific dates.
- Filter trending billboard topics by category tag or keyword.
- Monitor historical hot search snapshots over designated time ranges.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-total-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"page": 1, "page_size": 10, "type": "snapshot"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | integer | Yes | Page number |
| `type` | string | Yes | Snapshot type snapshot view by time range view by time range. |
| `page_size` | integer | Yes | Number of items per page |
| `keyword` | string | No | Hot search term |
| `end_date` | string | No | Snapshot end time format yyyyMMdd |
| `start_date` | string | No | Snapshot start time format yyyyMMdd |
| `sentence_tag` | string | No | Hot category tag, get from hot list category, multiple categories separated by commas, empty for all |
| `snapshot_time` | string | No | Snapshot time format yyyyMMddHHmmss |

### Notes

- Format `start_date` and `end_date` as `yyyyMMdd`, and `snapshot_time` as `yyyyMMddHHmmss`.
- Supply comma-separated category tags in `sentence_tag`, or leave it empty to return all categories.
- Paging requires both `page` and `page_size`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-total-list.json`](../../../../catalog/models/douyin/billboard/hot-total-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-total-list

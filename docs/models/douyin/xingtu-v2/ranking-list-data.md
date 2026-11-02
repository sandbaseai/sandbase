# Douyin XingTu Ranking List Data API: pricing, parameters and code examples

`douyin/xingtu-v2/ranking-list-data` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Returns Douyin XingTu author business ranking records by type, date, and category qualifier. It provides author rankings, performance scores, and order metrics.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/ranking-list-data", "code": 1, "date": "20260131", "period": 30, "qualifier": "1901", "version": "flow_split"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/ranking-list-data', {'code': 1, 'date': '20260131', 'period': 30, 'qualifier': '1901', 'version': 'flow_split'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/ranking-list-data", {
  "code": 1,
  "date": "20260131",
  "period": 30,
  "qualifier": "1901",
  "version": "flow_split"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/ranking-list-data", sandbase.Params{
	"code": 1,
	"date": "20260131",
	"period": 30,
	"qualifier": "1901",
	"version": "flow_split",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/ranking-list-data` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `code` | integer |  | Ranking type code default `1` |
| `date` | string |  | Date, format YYYYMMDD default `"20260131"` |
| `period` | integer |  | 7=weekly, 30=monthly default `30` |
| `version` | string |  | `flow_split`=default for video rankings, `base`=commonly used for live rankings default `"flow_split"` |
| `qualifier` | string |  | Category qualifier_id from `get_ranking_list_catalog` default `"1901"` |

## Details

Retrieve Douyin XingTu influencer leaderboard records using parameters like `code`, `qualifier`, `date`, and `period`.

### Use cases

- Track top-performing Douyin XingTu influencers across weekly or monthly cycles.
- Analyze author ranking shifts and commercial order fulfillment rates.
- Compare talent scores across different category qualifiers and video formats.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/ranking-list-data" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `code` | integer | No | Ranking type code |
| `date` | string | No | Date, format YYYYMMDD |
| `period` | integer | No | 7=weekly, 30=monthly |
| `version` | string | No | `flow_split`=default for video rankings, `base`=commonly used for live rankings |
| `qualifier` | string | No | Category qualifier_id from `get_ranking_list_catalog` |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "authors": [
    {
      "old_rank": "1",
      "rank": "1",
      "score": 0.58994708994709,
      "star_id": "7146074596666507300",
      "attribute_datas": {
        "author_id": "7146074596666507300",
        "author_status": "1",
        "core_user_id": "3777519688105684",
        "finish_order_cnt": "> 20",
        "item_order_rate": "0.0546",
        "modify_time": "1769932545"
      }
    }
  ]
}
```

### Notes

- Set `period` to 7 for weekly rankings or 30 for monthly rankings.
- Set `version` to `flow_split` for video rankings or `base` for live stream rankings.
- Obtain category `qualifier` values from the ranking list catalog endpoint.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/ranking-list-data.json`](../../../../catalog/models/douyin/xingtu-v2/ranking-list-data.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/ranking-list-data

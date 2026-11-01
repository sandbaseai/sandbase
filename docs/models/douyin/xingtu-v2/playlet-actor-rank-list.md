# Douyin Xingtu Playlet Actor Ranking List

`douyin/xingtu-v2/playlet-actor-rank-list` · api · Douyin

Returns Xingtu ranking lists for Douyin playlet actors based on specified dates and evaluation periods. Filter rankings by actor category and ranking types.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/xingtu-v2/playlet-actor-rank-list", "category": "playlet_actor_list", "date": "20251130", "name": "playlet_actor_composite_list", "period": 30, "qualifier": ""}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/xingtu-v2/playlet-actor-rank-list', {'category': 'playlet_actor_list', 'date': '20251130', 'name': 'playlet_actor_composite_list', 'period': 30, 'qualifier': ''})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/xingtu-v2/playlet-actor-rank-list", {
  "category": "playlet_actor_list",
  "date": "20251130",
  "name": "playlet_actor_composite_list",
  "period": 30,
  "qualifier": ""
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/xingtu-v2/playlet-actor-rank-list", sandbase.Params{
	"category": "playlet_actor_list",
	"date": "20251130",
	"name": "playlet_actor_composite_list",
	"period": 30,
	"qualifier": "",
})
```

Same call via the path form: `POST /v1/api/douyin/xingtu-v2/playlet-actor-rank-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `date` | string |  | Date, format YYYYMMDD default `"20251130"` |
| `name` | string |  | Ranking name, `playlet_actor_composite_list`=composite list default `"playlet_actor_composite_list"` |
| `period` | integer |  | 7=weekly, 30=monthly default `30` |
| `category` | string |  | Category, default `playlet_actor_list` default `"playlet_actor_list"` |
| `qualifier` | string |  | Actor type, empty=all default `""` |

## Details

Retrieve Douyin Xingtu playlet actor rankings by specifying evaluation parameters such as `date`, `period`, and list `name`.

### Use cases

- Track top-performing Douyin playlet actors over weekly or monthly intervals.
- Evaluate talent options for upcoming playlet productions.
- Monitor composite performance metrics across playlet creator categories.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/xingtu-v2/playlet-actor-rank-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date` | string | No | Date, format YYYYMMDD |
| `name` | string | No | Ranking name, `playlet_actor_composite_list`=composite list |
| `period` | integer | No | 7=weekly, 30=monthly |
| `category` | string | No | Category, default `playlet_actor_list` |
| `qualifier` | string | No | Actor type, empty=all |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "author_rank_list": [
    {
      "core_user_id": "59187082550",
      "id": "59187082550",
      "name": "傅汉源"
    }
  ]
}
```

### Notes

- Set `period` to 7 for weekly lists or 30 for monthly lists.
- Provide `date` in YYYYMMDD format to inspect historical rankings.
- Set `name` to `playlet_actor_composite_list` for composite rankings.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Xingtu Author Audience Distribution](/model/douyin/xingtu-v2/author-audience-distribution): Returns audience profile distribution metrics for a specified Xingtu creator based on creator ID and link type, with selectable platform source and channel opt…
- [Douyin Xingtu Author Base Info](/model/douyin/xingtu-v2/author-base-info): Returns basic creator profile data from Douyin Xingtu by author identifier, with options to include recommendation details and linkage information.
- [Douyin Xingtu Author Business Card Info](/model/douyin/xingtu-v2/author-business-card-info): Returns business card details for a Douyin Xingtu creator based on the specified author ID.

---
Machine-readable: [`catalog/models/douyin/xingtu-v2/playlet-actor-rank-list.json`](../../../../catalog/models/douyin/xingtu-v2/playlet-actor-rank-list.json) · Store page: https://www.sandbase.ai/model/douyin/xingtu-v2/playlet-actor-rank-list

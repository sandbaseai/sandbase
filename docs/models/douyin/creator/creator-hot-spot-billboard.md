# Douyin Creator Hot Spot Billboard

`douyin/creator/creator-hot-spot-billboard` · api · Douyin

Returns trending hot spot billboard rankings for Douyin creators, including hot scores and query identifiers filtered by search type, tag, or city code.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-hot-spot-billboard", "billboard_tag": "0", "hot_search_type": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-hot-spot-billboard', {'billboard_tag': '0', 'hot_search_type': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-hot-spot-billboard", {
  "billboard_tag": "0",
  "hot_search_type": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-hot-spot-billboard", sandbase.Params{
	"billboard_tag": "0",
	"hot_search_type": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-hot-spot-billboard` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `city_code` |  |  | City code - required when hot_search_type=2  |
| `billboard_tag` | string |  | Hot spot tag - multiple tags separated by comma default `"0"` |
| `hot_search_type` | integer |  | Hot search type default `1` |

## Details

Access current Douyin creator hot spot rankings using `hot_search_type`, optional `billboard_tag`, and `city_code` filters.

### Use cases

- Track rising search topics and rankings across Douyin.
- Analyze trending creator themes filtered by category tags.
- Monitor city-level hot spot rankings using local city codes.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-hot-spot-billboard" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `city_code` | string | No | City code - required when hot_search_type=2 |
| `billboard_tag` | string | No | Hot spot tag - multiple tags separated by comma |
| `hot_search_type` | integer | No | Hot search type |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "item_list": [
    {
      "category": "体育",
      "hot_score": 12087333,
      "query_id": "2682945",
      "rank": 1,
      "rank_diff": 0,
      "title": "国足vs塔吉克斯坦"
    }
  ]
}
```

### Notes

- `city_code` is required when `hot_search_type` is set to 2.
- Pass multiple tags in `billboard_tag` separated by commas.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Creator Activity Details](/model/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/model/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/model/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/creator-hot-spot-billboard.json`](../../../../catalog/models/douyin/creator/creator-hot-spot-billboard.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-hot-spot-billboard

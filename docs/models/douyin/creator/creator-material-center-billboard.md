# Douyin Creator Material Center Billboard API: pricing, parameters and code examples

`douyin/creator/creator-material-center-billboard` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns trending billboard items from the Douyin Creator Material Center with interaction metrics. Supports filtering by time, billboard tag, and sorting order.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-material-center-billboard", "billboard_tag": 0, "order_key": 1, "time_filter": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-material-center-billboard', {'billboard_tag': 0, 'order_key': 1, 'time_filter': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-material-center-billboard", {
  "billboard_tag": 0,
  "order_key": 1,
  "time_filter": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-material-center-billboard", sandbase.Params{
	"billboard_tag": 0,
	"order_key": 1,
	"time_filter": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-material-center-billboard` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `order_key` | integer |  | Order key default `1` |
| `time_filter` | integer |  | Time filter default `1` |
| `billboard_tag` | integer |  | Billboard tag, 0=all, other values can be obtained through config interface default `0` |

## Details

Retrieve creator material billboard items along with engagement statistics using `order_key`, `time_filter`, and `billboard_tag`.

### Use cases

- Track top-performing creator video materials across Douyin.
- Analyze engagement metrics such as play counts, likes, and hot scores.
- Discover trending content categories filtered by specific billboard tags.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-material-center-billboard" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `order_key` | integer | No | Order key |
| `time_filter` | integer | No | Time filter |
| `billboard_tag` | integer | No | Billboard tag, 0=all, other values can be obtained through config interface |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "item_list": [
    {
      "author_link": "https://www.iesdouyin.com/share/user/70563022822?sec_uid=MS4wLjABAAAAQeIjx1d53Cg…",
      "author_name": "<user>",
      "collection_count": 0,
      "comment_count": 102759,
      "duration": 133313,
      "hot_onboard_time": 0,
      "hot_score": 660013,
      "item_id": "7692811973934927590",
      "like_count": 3286609,
      "play_count": 49355670
    }
  ]
}
```

### Notes

- Set `billboard_tag` to 0 for all categories, or pass values obtained from the configuration interface.
- Refine rankings by passing `order_key` for sorting and `time_filter` for time frames.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Creator Activity Details](/model/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/model/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/model/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/creator-material-center-billboard.json`](../../../../catalog/models/douyin/creator/creator-material-center-billboard.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-material-center-billboard

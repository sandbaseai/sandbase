# Douyin Creator Hot Music Billboard API: pricing, parameters and code examples

`douyin/creator/creator-hot-music-billboard` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending music rankings from the Douyin creator platform. Filters allow sorting by view metrics, like counts, popularity, or submission volumes across customizable time ranges.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-hot-music-billboard", "billboard_tag": 0, "order_key": 1, "time_filter": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-hot-music-billboard', {'billboard_tag': 0, 'order_key': 1, 'time_filter': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-hot-music-billboard", {
  "billboard_tag": 0,
  "order_key": 1,
  "time_filter": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-hot-music-billboard", sandbase.Params{
	"billboard_tag": 0,
	"order_key": 1,
	"time_filter": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-hot-music-billboard` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `order_key` | integer |  | Order key (1=highest views, 2=most likes, 4=highest popularity, 5=most submissions) default `1` |
| `time_filter` | integer |  | Time filter (1=24 hours, 2=7 days, 3=30 days) default `1` |
| `billboard_tag` | integer |  | Billboard tag, 0=all, other values can be obtained through config interface default `0` |

## Details

Access Douyin trending audio charts by querying with optional filters such as `order_key`, `time_filter`, and `billboard_tag`.

### Use cases

- Identify trending audio tracks on Douyin for content planning.
- Track audio performance metrics including play counts and like numbers.
- Analyze music popularity shifts across 24-hour, 7-day, or 30-day windows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-hot-music-billboard" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `order_key` | integer | No | Order key (1=highest views, 2=most likes, 4=highest popularity, 5=most submissions) |
| `time_filter` | integer | No | Time filter (1=24 hours, 2=7 days, 3=30 days) |
| `billboard_tag` | integer | No | Billboard tag, 0=all, other values can be obtained through config interface |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "item_list": [
    {
      "collection_count": 0,
      "comment_count": 102759,
      "hot_onboard_time": 0,
      "hot_score": 660013,
      "item_id": "7692811983661746980",
      "like_count": 2621660,
      "play_count": 49355670,
      "publish_count": 244,
      "query_id": "285104519",
      "share_count": 262924
    }
  ]
}
```

### Notes

- `order_key` accepts 1 for highest views, 2 for most likes, 4 for highest popularity, and 5 for most submissions.
- `time_filter` accepts 1 for 24 hours, 2 for 7 days, and 3 for 30 days.
- `billboard_tag` defaults to 0 for all categories, with additional category values obtainable from the config endpoint.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Creator Activity Details](/apis/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/apis/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/apis/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/creator-hot-music-billboard.json`](../../../../catalog/models/douyin/creator/creator-hot-music-billboard.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-hot-music-billboard

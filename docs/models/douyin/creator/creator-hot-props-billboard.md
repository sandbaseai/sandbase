# Douyin Creator Hot Props Billboard API: pricing, parameters and code examples

`douyin/creator/creator-hot-props-billboard` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns trending creator prop rankings and performance metrics on Douyin. Supports filtering by sorting sequence, time interval, and prop category tag.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/creator/creator-hot-props-billboard", "billboard_tag": 0, "order_key": 1, "time_filter": 1}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/creator/creator-hot-props-billboard', {'billboard_tag': 0, 'order_key': 1, 'time_filter': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/creator/creator-hot-props-billboard", {
  "billboard_tag": 0,
  "order_key": 1,
  "time_filter": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/creator/creator-hot-props-billboard", sandbase.Params{
	"billboard_tag": 0,
	"order_key": 1,
	"time_filter": 1,
})
```

Same call via the path form: `POST /v1/api/douyin/creator/creator-hot-props-billboard` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `order_key` | integer |  | Order key default `1` |
| `time_filter` | integer |  | Time filter default `1` |
| `billboard_tag` | integer |  | Billboard tag, 0=all, other values can be obtained through config interface default `0` |

## Details

Access Douyin creator hot props rankings filtered by `billboard_tag`, `time_filter`, and `order_key`.

### Use cases

- Identify trending props and visual effects across Douyin video creators.
- Monitor engagement metrics such as play count and collection count for viral props.
- Analyze popular creative tools to guide content strategy and production.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/creator/creator-hot-props-billboard" \
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
      "collection_count": 43141,
      "comment_count": 0,
      "hot_onboard_time": 0,
      "hot_score": 0,
      "item_id": "271554030",
      "like_count": 192,
      "play_count": 45800949,
      "publish_count": 68811,
      "query_id": "391777092",
      "share_count": 0
    }
  ]
}
```

### Notes

- Set `billboard_tag` to 0 for all props, or use values obtained from the configuration endpoint.
- Sort and filter results using `order_key` and `time_filter`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Creator Activity Details](/model/douyin/creator/creator-activity-detail): Returns detailed information for a specific Douyin creator activity.
- [Douyin Activity List](/model/douyin/creator/creator-activity-list): Returns activity and campaign records for Douyin accounts within a specified timestamp window between start_time and end_time.
- [Douyin Content Categories](/model/douyin/creator/creator-content-category): Returns the list of content categories available on Douyin.

---
Machine-readable: [`catalog/models/douyin/creator/creator-hot-props-billboard.json`](../../../../catalog/models/douyin/creator/creator-hot-props-billboard.json) · Store page: https://www.sandbase.ai/model/douyin/creator/creator-hot-props-billboard

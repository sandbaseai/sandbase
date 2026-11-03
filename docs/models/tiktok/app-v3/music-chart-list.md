# TikTok Music Chart List API: pricing, parameters and code examples

`tiktok/app-v3/music-chart-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns TikTok music chart rankings and track details. Supports filtering by chart type scene alongside cursor-based pagination.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/music-chart-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/music-chart-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/music-chart-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/music-chart-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/music-chart-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number per page, default 50, max 50 default `50` |
| `scene` | integer |  | Chart type default `0` |
| `cursor` | integer |  | Pagination cursor, default 0 default `0` |

## Details

Retrieve trending music chart tracks on TikTok by specifying the chart type using `scene`. Paginate through chart entries using `cursor` and `count`.

### Use cases

- Monitor popular and trending audio tracks across TikTok music charts.
- Analyze artist appearances and track metadata from ranked audio lists.
- Integrate real-time TikTok chart data into music discovery platforms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/music-chart-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Number per page, default 50, max 50 |
| `scene` | integer | No | Chart type |
| `cursor` | integer | No | Pagination cursor, default 0 |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "music_list": [
    {
      "id": 7245341979050396417,
      "music_info": {
        "audition_duration": 60,
        "author": "Taylor Swift",
        "author_deleted": false,
        "binded_challenge_id": 0,
        "commercial_right_type": 3,
        "create_time": 1790303820
      }
    }
  ]
}
```

### Notes

- Control results per page using `count`, with a default and maximum limit of 50.
- Filter charts by passing a specific chart type integer into `scene`.
- Paginate results by supplying `cursor`, which defaults to 0.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Room Online Status Batch](/apis/tiktok/app-v3/check-live-room-online-batch): Returns the online availability status for multiple TikTok broadcast rooms in a single request.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.

---
Machine-readable: [`catalog/models/tiktok/app-v3/music-chart-list.json`](../../../../catalog/models/tiktok/app-v3/music-chart-list.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/music-chart-list

# TikTok Room Online Status Batch

`tiktok/app-v3/check-live-room-online-batch` · api · TikTok

Returns the online availability status for multiple TikTok broadcast rooms in a single request. Accepts a list of up to 50 room IDs.

## Pricing

- **$0.015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/app-v3/check-live-room-online-batch"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/app-v3/check-live-room-online-batch', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/app-v3/check-live-room-online-batch", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/app-v3/check-live-room-online-batch", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/app-v3/check-live-room-online-batch` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_ids` | array |  | List of TikTok live room IDs default `["7494491933781003054", "7494514925034113835", "7494520590523517739"]` |

## Details

Checks whether multiple TikTok broadcast rooms are currently active by passing a list of room identifiers in `room_ids`.

### Use cases

- Check the active status of multiple broadcast rooms simultaneously.
- Filter out inactive broadcasts before querying detailed room metrics.
- Track stream availability across a roster of monitored accounts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/check-live-room-online-batch" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_ids` | array | No | List of TikTok live room IDs |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "alive": false,
      "room_id": 7494491933781003054,
      "room_id_str": "7494491933781003054"
    }
  ]
}
```

### Notes

- Supports checking up to 50 identifiers in `room_ids` per call.
- Room identifiers can be obtained from `/api/v1/tiktok/web/get_live_room_id`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok LIVE Status](/model/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Content Translation](/model/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.
- [TikTok Creator Search Insights](/model/tiktok/app-v3/creator-search-insights): Get TikTok Creator Search Insights: trending search queries with popularity scores, trend history and video counts, including content-gap topics, by category a…

---
Machine-readable: [`catalog/models/tiktok/app-v3/check-live-room-online-batch.json`](../../../../catalog/models/tiktok/app-v3/check-live-room-online-batch.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/check-live-room-online-batch

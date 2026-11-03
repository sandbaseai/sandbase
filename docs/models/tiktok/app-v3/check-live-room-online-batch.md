# TikTok Room Online Status Batch API: pricing, parameters and code examples

`tiktok/app-v3/check-live-room-online-batch` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns the online availability status for multiple TikTok broadcast rooms in a single request. Accepts a list of up to 50 room IDs.

## Pricing

- **$0.01 per call** (USD)
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

Returns the live status of up to 50 TikTok LIVE rooms in one request. It needs a list of room IDs in `room_ids`. Each result shows whether that room is currently live.

### Use cases

- Check a list of monitored rooms in one call and keep only those that are live.
- Filter out ended rooms before you request room details.
- Poll a set of saved room IDs to see when each stream stops.
- Validate a batch of room IDs collected from earlier lookups.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/app-v3/check-live-room-online-batch" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_ids` | array | No | List of TikTok live room IDs |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "alive": false,
      "room_id": 7494491933781003054,
      "room_id_str": "7494491933781003054"
    }
  ],
  "extra": {
    "now": 1793691831215
  },
  "status_code": 0
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[]` | One result per room ID you sent. |
| `data[].room_id_str` | Room ID as a string. Use this form to match results to your input without losing digits. |
| `data[].room_id` | Room ID as a number. It has the same value as `room_id_str`. |
| `data[].alive` | `true` if the room is live now, `false` if it is not. All three sample rooms returned `false`. |
| `extra.now` | Time of the response as a 13-digit number, which looks like a Unix timestamp in milliseconds. |
| `status_code` | Status of the call. `0` in the sample response. |

### Notes

- Send up to 50 strings in `room_ids`. The sample response returned one `data` entry for each ID sent.
- Match results by `room_id_str`. The numeric `room_id` is a long integer that some JSON parsers may round.
- To check a single room, use [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online).
- To get details about a live room, call [TikTok Broadcast Room Information](/apis/tiktok/app-v3/live-room-info).

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok LIVE Status](/apis/tiktok/app-v3/check-live-room-online): Check whether a TikTok LIVE room is currently live by room ID.
- [TikTok Content Translation](/apis/tiktok/app-v3/content-translate): Translates provided text content into a designated target language.
- [TikTok Creator Search Insights](/apis/tiktok/app-v3/creator-search-insights): Get TikTok Creator Search Insights: trending search queries with popularity scores, trend history and video counts, including content-gap topics, by category a…

---
Machine-readable: [`catalog/models/tiktok/app-v3/check-live-room-online-batch.json`](../../../../catalog/models/tiktok/app-v3/check-live-room-online-batch.json) · Store page: https://www.sandbase.ai/model/tiktok/app-v3/check-live-room-online-batch

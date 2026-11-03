# TikTok Room Active Status Batch Check API: pricing, parameters and code examples

`tiktok/web/batch-check-live-alive` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.05 per call · **Modes:** sync

Checks whether multiple TikTok broadcast rooms are currently active. Accepts a comma-separated list of room identifiers to return current status details.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/batch-check-live-alive", "room_ids": "7530611486784277278,7530633767468288782,7530636465034775310,7530604930088848142"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/batch-check-live-alive', {'room_ids': '7530611486784277278,7530633767468288782,7530636465034775310,7530604930088848142'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/batch-check-live-alive", {
  "room_ids": "7530611486784277278,7530633767468288782,7530636465034775310,7530604930088848142"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/batch-check-live-alive", sandbase.Params{
	"room_ids": "7530611486784277278,7530633767468288782,7530636465034775310,7530604930088848142",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/batch-check-live-alive` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_ids` | string | yes | Live room ID list separated by commas, e.g.: 7530611486784277278,7530633767468288782  |

## Details

This API checks whether several TikTok live rooms are broadcasting right now. It takes one input, `room_ids`, a comma-separated string of live room IDs, and returns an `alive` flag for each room.

### Use cases

- Check a watchlist of live room IDs in one call and keep only the rooms that are broadcasting.
- Remove ended rooms from a monitoring dashboard before you fetch more room details.
- Poll a set of known room IDs to see when a stream goes live or ends.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/batch-check-live-alive" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_ids": "7530611486784277278,7530633767468288782,7530636465034775310,7530604930088848142"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_ids` | string | Yes | Live room ID list separated by commas, e.g.: 7530611486784277278,7530633767468288782 |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "results": {
    "cookie": "tt_chain…",
    "data": [
      {
        "alive": false,
        "room_id": 7530611486784277278,
        "room_id_str": "7530611486784277278"
      }
    ],
    "extra": {
      "now": 1793691861314
    },
    "status_code": 0,
    "tt_chain_token": "0k5cdiqY…"
  },
  "total_queried": 4
}
```

### Response fields

| Field | Meaning |
|---|---|
| `results.data[].alive` | Whether the room is currently live. `false` means the room is not active. |
| `results.data[].room_id` | The room ID as a number. |
| `results.data[].room_id_str` | The same room ID as a string. Use this one to avoid number precision loss in your code. |
| `results.extra.now` | A timestamp for when the check ran. The value looks like Unix time in milliseconds. |
| `results.status_code` | Status code for the check. `0` appears in this response. |
| `results.tt_chain_token / results.cookie` | A token and a cookie string returned with the check. The cookie contains the same token value. |
| `total_queried` | The number of room IDs sent in the request. |

### Notes

- Separate room IDs with commas and no extra fields. The example request sends 4 IDs.
- The sample response lists 3 items in `results.data` for 4 queried IDs. Compare `total_queried` with the length of `results.data` to find missing rooms.
- To check a single room, use [TikTok Stream Status Check](/apis/tiktok/web/check-live-alive).
- To get full room details for a live room, call [TikTok Stream Room Information](/apis/tiktok/web/live-data).

### Pricing

$0.05 per successful call. Failed calls are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/batch-check-live-alive.json`](../../../../catalog/models/tiktok/web/batch-check-live-alive.json) · Store page: https://www.sandbase.ai/model/tiktok/web/batch-check-live-alive

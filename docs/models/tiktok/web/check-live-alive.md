# TikTok Stream Status Check API: pricing, parameters and code examples

`tiktok/web/check-live-alive` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.002 per call (free daily quota) · **Modes:** sync

Checks the active broadcast state of a specified TikTok room. Returns room identifier data and a boolean flag indicating whether the stream is active.

## Pricing

- **$0.002 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/check-live-alive", "room_id": "7674625312902925057"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/check-live-alive', {'room_id': '7674625312902925057'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/check-live-alive", {
  "room_id": "7674625312902925057"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/check-live-alive", sandbase.Params{
	"room_id": "7674625312902925057",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/check-live-alive` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string | yes | Live room ID  |

## Details

Returns whether a single TikTok live room is broadcasting right now. It needs one input, the live `room_id`, and returns that ID with an `alive` true or false flag.

### Use cases

- Check whether a known live room is still on air before you start collecting its data.
- Poll a room ID and send an alert when `alive` changes to `true`.
- Filter out ended rooms from a saved list of room IDs, one call per room.
- Confirm a room has closed before you stop a recording or monitoring job.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/check-live-alive" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "7381444193462078214"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Live room ID |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "live_room_status": {
    "cookie": "tt_chain…",
    "data": [
      {
        "alive": false,
        "room_id": 7381444193462078214,
        "room_id_str": "7381444193462078214"
      }
    ],
    "extra": {
      "now": 1793691862008
    },
    "status_code": 0,
    "tt_chain_token": "0k5cdiqY…"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `live_room_status.data[].alive` | Boolean flag. `true` means the room is broadcasting now, `false` means it is not. The sample response shows `false`. |
| `live_room_status.data[].room_id / live_room_status.data[].room_id_str` | The room ID as a number and as a string. Use the string form, because large numbers can lose precision in some JSON parsers. |
| `live_room_status.status_code` | Status code of the check. `0` appears in the sample response for a successful lookup. |
| `live_room_status.extra.now` | Timestamp of the check, shown as a 13-digit number (`1793691862008`). It looks like Unix time in milliseconds. |
| `live_room_status.tt_chain_token / live_room_status.cookie` | A chain token value and the cookie string that carries it. These are session values, not stream data. |

### Notes

- Pass `room_id` as a string, for example `7381444193462078214`.
- The `data` list holds one item for the one room you send. To check many rooms in one call, use [TikTok Room Active Status Batch Check](/apis/tiktok/web/batch-check-live-alive).
- If you only have a user or stream link, resolve the ID first with [TikTok Room ID Resolver](/apis/tiktok/web/live-room-id).
- For details about a room that is live, call [TikTok Stream Room Information](/apis/tiktok/web/live-data).

### Pricing

$0.002 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/check-live-alive.json`](../../../../catalog/models/tiktok/web/check-live-alive.json) · Store page: https://www.sandbase.ai/model/tiktok/web/check-live-alive

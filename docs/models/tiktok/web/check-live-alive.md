# TikTok Stream Status Check API: pricing, parameters and code examples

`tiktok/web/check-live-alive` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.003 per call (free daily quota) · **Modes:** sync

Checks the active broadcast state of a specified TikTok room. Returns room identifier data and a boolean flag indicating whether the stream is active.

## Pricing

- **$0.003 per call** (USD)
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

Check whether a TikTok broadcast room is currently active by supplying `room_id`.

### Use cases

- Verify whether a specific broadcast room is currently active.
- Trigger automated alerts when a target room goes on air.
- Track broadcast availability before directing viewers to a stream.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/check-live-alive" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "7381444193462078214"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Live room ID |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "live_room_status": {
    "data": [
      {
        "alive": false,
        "room_id": 7381444193462078214,
        "room_id_str": "7381444193462078214"
      }
    ]
  }
}
```

### Notes

- Requires a valid `room_id` to look up the stream status.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/check-live-alive.json`](../../../../catalog/models/tiktok/web/check-live-alive.json) · Store page: https://www.sandbase.ai/model/tiktok/web/check-live-alive

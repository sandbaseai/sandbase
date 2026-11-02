# TikTok Room ID Resolver API: pricing, parameters and code examples

`tiktok/web/live-room-id` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Resolves a TikTok stream room ID from a given room URL. Supports both standard profile stream URLs and shortened links to obtain the unique room identifier.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/live-room-id", "live_room_url": "https://www.tiktok.com/@maksukaracun/live"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/live-room-id', {'live_room_url': 'https://www.tiktok.com/@maksukaracun/live'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/live-room-id", {
  "live_room_url": "https://www.tiktok.com/@maksukaracun/live"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/live-room-id", sandbase.Params{
	"live_room_url": "https://www.tiktok.com/@maksukaracun/live",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/live-room-id` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `live_room_url` | string | yes | Live room link  |

## Details

Extracts the room ID from a TikTok broadcast link by passing the URL to `live_room_url`. Accepts both short links and standard web stream URLs.

### Use cases

- Resolve short share URLs into direct room identifiers for downstream processing.
- Retrieve the room ID needed to query broadcast details or stream status.
- Parse stream links submitted by users into structured room identifiers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/live-room-id" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"live_room_url": "https://www.tiktok.com/@maksukaracun/live"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `live_room_url` | string | Yes | Live room link |

### Notes

- Accepts short URLs (such as `vt.tiktok.com` links) as well as standard profile broadcast links via `live_room_url`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/live-room-id.json`](../../../../catalog/models/tiktok/web/live-room-id.json) · Store page: https://www.sandbase.ai/model/tiktok/web/live-room-id

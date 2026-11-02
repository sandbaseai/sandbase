# TikTok Room Danmaku Messages API: pricing, parameters and code examples

`tiktok/web/live-im-fetch` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Retrieves real-time danmaku and chat messages from a TikTok broadcast room. Requires a room ID and supports both protobuf and JSON output formats.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/live-im-fetch", "room_id": "7693529622901705485"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/live-im-fetch', {'room_id': '7693529622901705485'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/live-im-fetch", {
  "room_id": "7693529622901705485"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/live-im-fetch", sandbase.Params{
	"room_id": "7693529622901705485",
})
```

Same call via the path form: `POST /v1/api/tiktok/web/live-im-fetch` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string | yes | Live room id  |
| `user_unique_id` | string |  | User unique ID (optional)  |
| `resp_content_type` | string |  | Response format, protobuf (default) or json  |

## Details

Access danmaku chat messages from an active TikTok broadcast using `room_id`. You can optionally supply `user_unique_id` and specify the output format.

### Use cases

- Monitor real-time audience comments during a broadcast.
- Collect stream interaction data for sentiment analysis.
- Display incoming stream chat in external moderation dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/live-im-fetch" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_id": "7693529622901705485"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | Yes | Live room id |
| `user_unique_id` | string | No | User unique ID (optional) |
| `resp_content_type` | string | No | Response format, protobuf (default) or json |

### Notes

- `resp_content_type` controls output format and accepts protobuf (default) or json.
- `user_unique_id` is an optional parameter to identify a specific user.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/live-im-fetch.json`](../../../../catalog/models/tiktok/web/live-im-fetch.json) · Store page: https://www.sandbase.ai/model/tiktok/web/live-im-fetch

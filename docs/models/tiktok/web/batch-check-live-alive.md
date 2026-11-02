# TikTok Room Active Status Batch Check API: pricing, parameters and code examples

`tiktok/web/batch-check-live-alive` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.075 per call · **Modes:** sync

Checks whether multiple TikTok broadcast rooms are currently active. Accepts a comma-separated list of room identifiers to return current status details.

## Pricing

- **$0.075 per call** (USD)

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

Inspect the active broadcast status across multiple TikTok streams using `room_ids`. Pass a comma-separated list of room identifiers to inspect stream availability.

### Use cases

- Monitor multiple TikTok broadcast rooms simultaneously for real-time stream status.
- Track when target creators begin broadcasting across a watchlist of room identifiers.
- Filter inactive broadcast rooms from automated monitoring dashboards.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/batch-check-live-alive" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"room_ids": "<room_ids>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_ids` | string | Yes | Live room ID list separated by commas, e.g.: 7530611486784277278,7530633767468288782 |

### Notes

- Pass multiple room identifiers formatted as a comma-separated string in `room_ids`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/model/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/model/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/model/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/batch-check-live-alive.json`](../../../../catalog/models/tiktok/web/batch-check-live-alive.json) · Store page: https://www.sandbase.ai/model/tiktok/web/batch-check-live-alive

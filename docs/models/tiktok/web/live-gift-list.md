# TikTok Room Gift List API: pricing, parameters and code examples

`tiktok/web/live-gift-list` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.025 per call · **Modes:** sync

Returns the catalog of gifts available in a TikTok broadcast, including gift identifiers, names, and diamond values. Accepts an optional room identifier to retrieve room-specific options.

## Pricing

- **$0.025 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/web/live-gift-list"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/web/live-gift-list', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/web/live-gift-list", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/web/live-gift-list", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/web/live-gift-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `room_id` | string |  | Live room ID (optional) default `""` |

## Details

Retrieve the catalog of virtual gifts for TikTok broadcasts by providing an optional `room_id`. This endpoint returns gift details such as gift names, IDs, duration, and diamond counts.

### Use cases

- Display available broadcast gifts and their diamond values within an analytics dashboard.
- Monitor available gift types and configurations across different broadcast rooms.
- Map gift identifiers and names to incoming broadcast event notifications.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/web/live-gift-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `room_id` | string | No | Live room ID (optional) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "gifts": [
      {
        "describe": "sent Lyric Mail",
        "diamond_count": 15,
        "duration": 1000,
        "expiration_timestamp": 0,
        "for_linkmic": true,
        "gift_label_type": 0,
        "gift_sub_type": 0,
        "id": 1329117,
        "name": "Lyric Mail",
        "primary_effect_id": 0,
        "image": {
          "image_type": 0
        },
        "lock_info": {
          "highlight_enabled": false,
          "lock_type": 0
        }
      }
    ]
  }
}
```

### Notes

- The `room_id` parameter is optional when requesting the gift catalog.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Video IDs from URLs (Batch)](/apis/tiktok/web/all-aweme-id): Resolves and extracts TikTok video IDs from a list of video URLs.
- [TikTok User Sec User ID Extractor](/apis/tiktok/web/all-sec-user-id): Returns a list of sec_user_id identifiers corresponding to TikTok user profile URLs.
- [TikTok Profile Unique IDs](/apis/tiktok/web/all-unique-id): Resolves a batch of TikTok user homepage links to retrieve their corresponding unique identifiers.

---
Machine-readable: [`catalog/models/tiktok/web/live-gift-list.json`](../../../../catalog/models/tiktok/web/live-gift-list.json) · Store page: https://www.sandbase.ai/model/tiktok/web/live-gift-list

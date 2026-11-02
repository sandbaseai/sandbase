# Bilibili App Home Feed API: pricing, parameters and code examples

`bilibili/app/home-feed` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended video items from the Bilibili app home feed. Supports pagination via timestamp index and pull-to-refresh controls.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/home-feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/home-feed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/home-feed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/home-feed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/bilibili/app/home-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `idx` | integer |  | Page index, defaults to current timestamp  |
| `pull` | boolean |  | Pull to refresh default `true` |
| `flush` | integer |  | Flush flag (0=normal load, 1=refresh) default `0` |

## Details

Retrieve recommended video items from the Bilibili mobile app feed using `idx`, `pull`, and `flush` to control pagination and refresh behavior.

### Use cases

- Display recommended video items in custom Bilibili feed displays.
- Monitor trending titles and creator metadata appearing on the home feed.
- Simulate app-style feed browsing and content discovery flows.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/home-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `idx` | integer | No | Page index, defaults to current timestamp |
| `pull` | boolean | No | Pull to refresh |
| `flush` | integer | No | Flush flag (0=normal load, 1=refresh) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "items": [
      {
        "card_type": "small_cover_v2",
        "cover_left_1_content_description": "609.7万观看",
        "cover_left_2_content_description": "1149弹幕",
        "cover_left_text_1": "609.7万",
        "cover_left_text_2": "1149",
        "cover_right_content_description": "1分钟15秒",
        "cover_right_text": "1:15",
        "title": "⚡️ 疯 狂 闪 身 步 ⚡️",
        "args": {
          "tname": "鬼畜",
          "up_id": 632887,
          "up_name": "伢伢gagako"
        },
        "desc_button": {
          "text": "伢伢gagako",
          "type": 1
        },
        "player_args": {
          "duration": 75,
          "type": "av"
        }
      }
    ]
  }
}
```

### Notes

- `idx` sets the page index and defaults to the current timestamp.
- `flush` controls the load type, accepting 0 for normal load and 1 for refresh.
- `pull` indicates whether the request acts as a pull-to-refresh operation.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili App Bangumi Tab](/model/bilibili/app/bangumi-tab): Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.
- [Bilibili App Cinema Tab](/model/bilibili/app/cinema-tab): Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query para…
- [Bilibili App Single Video Details](/model/bilibili/app/one-video): Returns detailed video metadata for a specific Bilibili video.

---
Machine-readable: [`catalog/models/bilibili/app/home-feed.json`](../../../../catalog/models/bilibili/app/home-feed.json) · Store page: https://www.sandbase.ai/model/bilibili/app/home-feed

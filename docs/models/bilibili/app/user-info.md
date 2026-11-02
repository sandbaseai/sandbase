# Bilibili App User Info API: pricing, parameters and code examples

`bilibili/app/user-info` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns account profile details and uploaded video archives for a specified Bilibili creator using their unique user identifier.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/user-info", "user_id": "203680252"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/user-info', {'user_id': '203680252'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/user-info", {
  "user_id": "203680252"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/user-info", sandbase.Params{
	"user_id": "203680252",
})
```

Same call via the path form: `POST /v1/api/bilibili/app/user-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `user_id` | string | yes | User ID (required)  |

## Details

Access Bilibili user profile and archive video data by providing a valid `user_id`. This endpoint retrieves uploaded video items along with playback counts and timestamps.

### Use cases

- Retrieve video upload history and view counts for a specific creator.
- Display recent Bilibili video items on external creator profile dashboards.
- Analyze video upload timestamps and duration metrics across accounts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/user-info" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"user_id": "203680252"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `user_id` | string | Yes | User ID (required) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": {
    "archive": {
      "item": [
        {
          "author": "AYCS2",
          "ctime": 1790748319,
          "duration": 1171,
          "publish_time_text": "9月30日",
          "title": "老Y蜜月之旅 | 马尔代夫菲诺芙",
          "tname": "出行",
          "view_content": "17万",
          "view_self_type": 0
        }
      ]
    }
  }
}
```

### Notes

- Requires a valid Bilibili `user_id` to retrieve profile and archive data.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili App Bangumi Tab](/model/bilibili/app/bangumi-tab): Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.
- [Bilibili App Cinema Tab](/model/bilibili/app/cinema-tab): Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query para…
- [Bilibili App Home Feed](/model/bilibili/app/home-feed): Returns recommended video items from the Bilibili app home feed.

---
Machine-readable: [`catalog/models/bilibili/app/user-info.json`](../../../../catalog/models/bilibili/app/user-info.json) · Store page: https://www.sandbase.ai/model/bilibili/app/user-info

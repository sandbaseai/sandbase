# Bilibili App Popular Feed API: pricing, parameters and code examples

`bilibili/app/popular-feed` · data API · Bilibili · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Retrieves popular video feed items from the Bilibili app. Supports pagination through page index and previous video identifiers.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "bilibili/app/popular-feed"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('bilibili/app/popular-feed', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("bilibili/app/popular-feed", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "bilibili/app/popular-feed", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/bilibili/app/popular-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `idx` | integer |  | Page index (starting from 1) default `1` |
| `last_param` | string |  | Last video ID from previous page (for pagination)  |

## Details

Access popular trending video items on the Bilibili app. Use `idx` to specify the page index and `last_param` to handle pagination between result sets.

### Use cases

- Track trending and high-performing videos on the Bilibili app.
- Display popular video recommendations in external dashboards.
- Paginate through top video feeds for content discovery.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/bilibili/app/popular-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `idx` | integer | No | Page index (starting from 1) |
| `last_param` | string | No | Last video ID from previous page (for pagination) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "card_type": "small_cover_v5",
      "cover_right_text_1": "23:59",
      "from_type": "recommend",
      "right_desc_1": "小潮院长 等联合创作",
      "right_desc_2": "223.2万观看 · 昨天 12:00",
      "title": "惊惊惊惊惊惊惊惊了"
    }
  ]
}
```

### Notes

- `idx` defines the page index starting from 1.
- `last_param` accepts the last video ID from the previous page for pagination.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Bilibili App Bangumi Tab](/model/bilibili/app/bangumi-tab): Returns Bilibili app bangumi tab data, providing curated anime recommendations, feed items, and category listings for mobile clients.
- [Bilibili App Cinema Tab](/model/bilibili/app/cinema-tab): Returns cinema tab content from the Bilibili app, featuring curated movies, TV shows, and entertainment recommendations without requiring additional query para…
- [Bilibili App Home Feed](/model/bilibili/app/home-feed): Returns recommended video items from the Bilibili app home feed.

---
Machine-readable: [`catalog/models/bilibili/app/popular-feed.json`](../../../../catalog/models/bilibili/app/popular-feed.json) · Store page: https://www.sandbase.ai/model/bilibili/app/popular-feed

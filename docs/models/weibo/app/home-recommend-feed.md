# Weibo Home Recommend Feed API: pricing, parameters and code examples

`weibo/app/home-recommend-feed` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/home-recommend-feed", "count": 15}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/home-recommend-feed', {'count': 15})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/home-recommend-feed", {
  "count": 15
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/home-recommend-feed", sandbase.Params{
	"count": 15,
})
```

Same call via the path form: `POST /v1/api/weibo/app/home-recommend-feed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` |  |  | Page number, don't pass for first page, pass "2" for second page, and so on  |
| `count` | integer |  | Items per page, default 15, max 50 default `15`; range 1–50 |

## Details

Retrieve the Weibo mobile app home recommendation stream using optional `page` and `count` query parameters.

### Use cases

- Analyze engagement metrics on recommended Weibo posts.
- Track recommended content trends from the mobile home stream.
- Collect recommended feed items for social media monitoring.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/home-recommend-feed" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `page` | string | No | Page number, don't pass for first page, pass "2" for second page, and so on |
| `count` | integer | No | Items per page, default 15, max 50 |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "items": [
    {
      "category": "feed",
      "data": {
        "attitudes_count": 94,
        "attitudes_status": 0,
        "comment_guide_type": 0,
        "comments_count": 12,
        "content_auth": 0,
        "favorites_count": 0
      }
    }
  ]
}
```

### Notes

- Omit `page` for the first page and pass "2" or higher for subsequent pages.
- Use `count` to set items per page from 1 to 50, defaulting to 15.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo App AI Smart Search](/apis/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Hot Search Rankings](/apis/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.
- [Weibo Hot Search Categories](/apis/weibo/app/hot-search-categories): Returns all available hot search categories from Weibo.

---
Machine-readable: [`catalog/models/weibo/app/home-recommend-feed.json`](../../../../catalog/models/weibo/app/home-recommend-feed.json) · Store page: https://www.sandbase.ai/model/weibo/app/home-recommend-feed

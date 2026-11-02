# Weibo Post Reposts API: pricing, parameters and code examples

`weibo/app/status-reposts` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns a list of reposts for a specified Weibo post or video. Output includes repost details and engagement metrics with pagination support.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/status-reposts", "max_id": null, "status_id": "5016922058656962"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/status-reposts', {'max_id': None, 'status_id': '5016922058656962'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/status-reposts", {
  "max_id": null,
  "status_id": "5016922058656962"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/status-reposts", sandbase.Params{
	"max_id": nil,
	"status_id": "5016922058656962",
})
```

Same call via the path form: `POST /v1/api/weibo/app/status-reposts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `max_id` |  |  | Pagination cursor, don't pass for first request, use returned max_id for subsequent requests  |
| `status_id` | string | yes | Post ID or Video ID (required)  |

## Details

Retrieve the repost list for a specified Weibo post or video using `status_id`. Page through additional results by passing `max_id`.

### Use cases

- Track repost activity and distribution metrics for Weibo posts.
- Analyze social sharing patterns and amplification for specific content.
- Collect repost identifiers and interaction counts for social analytics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/status-reposts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"status_id": "5016922058656962"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `status_id` | string | Yes | Post ID or Video ID (required) |
| `max_id` | string | No | Pagination cursor, don't pass for first request, use returned max_id for subsequent requests |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "items": [
    {
      "category": "detail",
      "type": "forward",
      "data": {
        "attitudes_count": 0,
        "attitudes_status": 0,
        "comments_count": 0,
        "content_auth": 0,
        "favorites_count": 0,
        "id": 5343146838068091
      }
    }
  ]
}
```

### Notes

- Pass the post or video identifier to `status_id`.
- Leave `max_id` empty for the initial request, then pass the returned cursor for subsequent pages.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo App AI Smart Search](/model/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/model/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/model/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/status-reposts.json`](../../../../catalog/models/weibo/app/status-reposts.json) · Store page: https://www.sandbase.ai/model/weibo/app/status-reposts

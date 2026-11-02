# Weibo Post Comments (App) API: pricing, parameters and code examples

`weibo/app/status-comments` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns the first-level comments for a designated post or video on Weibo. Supports sorting options and cursor-based pagination for browsing discussion threads.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/status-comments", "max_id": null, "sort_type": "0", "status_id": "5258708168476831"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/status-comments', {'max_id': None, 'sort_type': '0', 'status_id': '5258708168476831'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/status-comments", {
  "max_id": null,
  "sort_type": "0",
  "status_id": "5258708168476831"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/status-comments", sandbase.Params{
	"max_id": nil,
	"sort_type": "0",
	"status_id": "5258708168476831",
})
```

Same call via the path form: `POST /v1/api/weibo/app/status-comments` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `max_id` |  |  | Pagination cursor, don't pass for first request, use returned max_id for subsequent requests  |
| `sort_type` | string |  | Comment sort type default `"0"` |
| `status_id` | string | yes | Post ID or Video ID (required)  |

## Details

Retrieve top-level comments for a specific post or video using its `status_id`. You can paginate through responses and control comment ordering.

### Use cases

- Display top-level user comments under a Weibo post or video.
- Track audience sentiment and reactions on specific Weibo discussions.
- Extract discussion threads for social listening and community analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/status-comments" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"status_id": "5258708168476831"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `status_id` | string | Yes | Post ID or Video ID (required) |
| `max_id` | string | No | Pagination cursor, don't pass for first request, use returned max_id for subsequent requests |
| `sort_type` | string | No | Comment sort type |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "items": [
    {
      "category": "detail",
      "type": "comment_header_tip",
      "data": {
        "tip_biz_type": 0,
        "tip_type": 3
      }
    }
  ]
}
```

### Notes

- Pagination is handled via `max_id`; omit it on the initial call and pass the returned value for subsequent requests.
- Use `sort_type` to specify the ordering of the returned comments.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo App AI Smart Search](/model/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/model/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/model/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/status-comments.json`](../../../../catalog/models/weibo/app/status-comments.json) · Store page: https://www.sandbase.ai/model/weibo/app/status-comments

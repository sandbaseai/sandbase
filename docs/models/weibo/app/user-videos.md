# Weibo User Videos API: pricing, parameters and code examples

`weibo/app/user-videos` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the video feed for a specified Weibo user in a waterfall layout. Accepts a user identifier and an optional cursor for paginated results.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/app/user-videos", "uid": "8431518763"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/app/user-videos', {'uid': '8431518763'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/app/user-videos", {
  "uid": "8431518763"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/app/user-videos", sandbase.Params{
	"uid": "8431518763",
})
```

Same call via the path form: `POST /v1/api/weibo/app/user-videos` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `uid` | string | yes | User ID (required)  |
| `since_id` |  |  | Pagination cursor, don't pass for first request, use returned since_id for subsequent requests  |

## Details

Retrieve video items posted by a specific account using `uid`. Subsequent pages can be requested using the returned `since_id` cursor.

### Use cases

- Display an account video gallery inside an external application.
- Track recent video uploads from specific Weibo creators.
- Archive historical video posts for social media analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/app/user-videos" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"uid": "8431518763"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `uid` | string | Yes | User ID (required) |
| `since_id` | string | No | Pagination cursor, don't pass for first request, use returned since_id for subsequent requests |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "items": [
    {
      "category": "cell",
      "type": "span"
    }
  ]
}
```

### Notes

- Pass `uid` to specify the target user account.
- Omit `since_id` on the initial call, then pass the returned cursor value for subsequent requests.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo App AI Smart Search](/model/weibo/app/ai-smart-search): Returns AI smart search channel results and feed metadata from Weibo for a specified keyword query, with optional page-based pagination.
- [Weibo Home Recommend Feed](/model/weibo/app/home-recommend-feed): Returns recommended feed items from the Weibo app homepage, with options to paginate and specify the number of items per request.
- [Weibo Hot Search Rankings](/model/weibo/app/hot-search): Returns current Weibo hot search rankings across various categories.

---
Machine-readable: [`catalog/models/weibo/app/user-videos.json`](../../../../catalog/models/weibo/app/user-videos.json) · Store page: https://www.sandbase.ai/model/weibo/app/user-videos

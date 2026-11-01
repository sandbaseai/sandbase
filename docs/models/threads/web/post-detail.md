# Threads Post Detail

`threads/web/post-detail` · api · Threads

Returns detailed information for a specific Threads post using its numeric ID. Call this endpoint to inspect post content and metadata from the web interface.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "threads/web/post-detail", "post_id": "3349029093483693129"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('threads/web/post-detail', {'post_id': '3349029093483693129'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("threads/web/post-detail", {
  "post_id": "3349029093483693129"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "threads/web/post-detail", sandbase.Params{
	"post_id": "3349029093483693129",
})
```

Same call via the path form: `POST /v1/api/threads/web/post-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `post_id` | string | yes | Post ID (numeric only), for example: 3349029093483693129, can be obtained from other APIs. If using URL to get, call /fetch_post_detail_v2 API.  |

## Details

Retrieve detailed post data from Threads by specifying a numeric `post_id`.

### Use cases

- Retrieve content and metadata for a specific Threads post.
- Inspect Threads post information using an existing post identifier.
- Display individual Threads post details within an external dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/threads/web/post-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"post_id": "3349029093483693129"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `post_id` | string | Yes | Post ID (numeric only), for example: 3349029093483693129, can be obtained from other APIs. |

### Notes

- The `post_id` must be numeric only.
- To look up details by URL instead of `post_id`, call the /fetch_post_detail_v2 endpoint.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Threads Post Detail (V2)](/model/threads/web/post-detail-v2): Returns detailed information for a specific Threads post.
- [Threads Profile Search](/model/threads/web/search-profiles): Searches Threads user profiles based on a specified text query string.
- [Threads Recent Content Search](/model/threads/web/search-recent): Searches recent Threads content matching a specified keyword query.

---
Machine-readable: [`catalog/models/threads/web/post-detail.json`](../../../../catalog/models/threads/web/post-detail.json) · Store page: https://www.sandbase.ai/model/threads/web/post-detail

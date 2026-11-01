# Threads Post Detail (V2)

`threads/web/post-detail-v2` · api · Threads

Returns detailed information for a specific Threads post. Queries can be performed using either a full post link or a post short code as input.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "threads/web/post-detail-v2"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('threads/web/post-detail-v2', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("threads/web/post-detail-v2", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "threads/web/post-detail-v2", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/threads/web/post-detail-v2` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string |  | Full post URL (optional), for example: https://www.threads.com/@taylorswift/post/DPVUglOjOUu  |
| `post_id` | string |  | Post short code (optional), for example: DPVUglOjOUu, can be extracted from post URL, e.g., DPVUglOjOUu in https://www.threads.com/@taylorswift/post/DPVUglOjOUu  |

## Details

Retrieve Threads post information by supplying either a complete link in `url` or a post short code in `post_id`.

### Use cases

- Retrieve metadata and content for a specific Threads post.
- Extract post details using short codes from public links.
- Monitor specific Threads posts by querying their web address.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/threads/web/post-detail-v2" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | No | Full post URL (optional), for example: https://www.threads.com/@taylorswift/post/DPVUglOjOUu |
| `post_id` | string | No | Post short code (optional), for example: DPVUglOjOUu, can be extracted from post URL, e.g., DPVUglOjOUu in https://www.threads.com/@taylorswift/post/DPVUglOjOUu |

### Notes

- Provide either `url` or `post_id` to look up the post.
- The `post_id` value corresponds to the short code extracted from the Threads post link.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Threads Post Detail](/model/threads/web/post-detail): Returns detailed information for a specific Threads post using its numeric ID.
- [Threads Profile Search](/model/threads/web/search-profiles): Searches Threads user profiles based on a specified text query string.
- [Threads Recent Content Search](/model/threads/web/search-recent): Searches recent Threads content matching a specified keyword query.

---
Machine-readable: [`catalog/models/threads/web/post-detail-v2.json`](../../../../catalog/models/threads/web/post-detail-v2.json) · Store page: https://www.sandbase.ai/model/threads/web/post-detail-v2

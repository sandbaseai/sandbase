# Threads Recent Content Search

`threads/web/search-recent` · api · Threads

Searches recent Threads content matching a specified keyword query. Returns matching web posts with cursor-based pagination support.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "threads/web/search-recent", "query": "bitcoin"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('threads/web/search-recent', {'query': 'bitcoin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("threads/web/search-recent", {
  "query": "bitcoin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "threads/web/search-recent", sandbase.Params{
	"query": "bitcoin",
})
```

Same call via the path form: `POST /v1/api/threads/web/search-recent` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search query, for example: bitcoin  |
| `end_cursor` | string |  | Pagination cursor (optional), used to get next page data  |

## Details

Search recent posts on Threads by providing a search keyword in `query`. For multi-page results, pass `end_cursor` to retrieve subsequent batches.

### Use cases

- Track recent Threads discussions around specific topics or brands.
- Monitor breaking news and emerging trends across the platform.
- Collect search result feeds for analytical and monitoring tools.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/threads/web/search-recent" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "<query>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search query, for example: bitcoin |
| `end_cursor` | string | No | Pagination cursor (optional), used to get next page data |

### Notes

- Use `end_cursor` to paginate through subsequent pages of search results.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Threads Post Detail](/model/threads/web/post-detail): Returns detailed information for a specific Threads post using its numeric ID.
- [Threads Post Detail (V2)](/model/threads/web/post-detail-v2): Returns detailed information for a specific Threads post.
- [Threads Profile Search](/model/threads/web/search-profiles): Searches Threads user profiles based on a specified text query string.

---
Machine-readable: [`catalog/models/threads/web/search-recent.json`](../../../../catalog/models/threads/web/search-recent.json) · Store page: https://www.sandbase.ai/model/threads/web/search-recent

# Threads Profile Search

`threads/web/search-profiles` · api · Threads

Searches Threads user profiles based on a specified text query string. Returns matching user accounts and profile information from the platform.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "threads/web/search-profiles", "query": "mark"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('threads/web/search-profiles', {'query': 'mark'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("threads/web/search-profiles", {
  "query": "mark"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "threads/web/search-profiles", sandbase.Params{
	"query": "mark",
})
```

Same call via the path form: `POST /v1/api/threads/web/search-profiles` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search query, for example: mark  |

## Details

Look up Threads user profiles by supplying a text search term via the `query` parameter.

### Use cases

- Find relevant Threads accounts matching brand or organization names.
- Discover user profiles based on specific keywords or handles.
- Locate public figures and creators across the Threads network.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/threads/web/search-profiles" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search query, for example: mark |

### Notes

- The `query` parameter specifies the text search term, such as a name or handle.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Threads Post Detail](/model/threads/web/post-detail): Returns detailed information for a specific Threads post using its numeric ID.
- [Threads Post Detail (V2)](/model/threads/web/post-detail-v2): Returns detailed information for a specific Threads post.
- [Threads Recent Content Search](/model/threads/web/search-recent): Searches recent Threads content matching a specified keyword query.

---
Machine-readable: [`catalog/models/threads/web/search-profiles.json`](../../../../catalog/models/threads/web/search-profiles.json) · Store page: https://www.sandbase.ai/model/threads/web/search-profiles

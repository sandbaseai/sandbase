# Reddit Subreddit Posts

`reddit/subreddit-posts` · api · Reddit

Fetch posts from a subreddit listing (hot, new, or top).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00038**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/subreddit-posts", "subreddit": "programming"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/subreddit-posts', {'subreddit': 'programming'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/subreddit-posts", {
  "subreddit": "programming"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/subreddit-posts", sandbase.Params{
	"subreddit": "programming",
})
```

Same call via the path form: `POST /v1/api/reddit/subreddit-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Listing sort order. one of: `hot`, `new`, `top`; default `"hot"` |
| `after` | string |  | Legacy pagination alias. Prefer `cursor`; omit both fields for the first page.  |
| `limit` | integer |  | Page size to ask for (up to 100). Some sources honor it; others always return their whole page of about 25 posts. A page is never trimmed after the call, so pass nextCursor back as cursor to continue exactly where this… default `25`; range 1–100 |
| `cursor` | string |  | Opaque pagination cursor from a previous response's `nextCursor`; omit for the first page.  |
| `subreddit` | string | yes | Subreddit name without the leading r/ (e.g. "golang").  |
| `timeframe` | string |  | Time window, applied when sort is "top" (e.g. "year" for the year's top posts). Ignored for hot/new. Omit to default to the current day for top. one of: `all`, `year`, `month`, `week`, `day`, `hour` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `isArchived` or `selftext`, and it is served only by a source that…  |

## Details

Fetch posts from a subreddit listing (hot, new, or top).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/subreddit-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 5, "subreddit": "programming"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subreddit` | string | Yes | Subreddit name without the leading r/ (e.g. "golang"). |
| `after` | string | No | Legacy pagination alias. Prefer `cursor`; omit both fields for the first page. |
| `cursor` | string | No | Opaque pagination cursor from a previous response's `nextCursor`; omit for the first page. |
| `limit` | integer | No | Page size to ask for (up to 100). Some sources honor it; others always return their whole page of about 25 posts. A page is never trimmed after the call, so pass nextCursor back as cursor to continue exactly where this r |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `isArchived` or `selftext`, and it is served only by a source that ret |
| `sort` | string | No | Listing sort order. One of: `hot`, `new`, `top`. Default `"hot"`. |
| `timeframe` | string | No | Time window, applied when sort is "top" (e.g. "year" for the year's top posts). Ignored for hot/new. Omit to default to the current day for top. One of: `all`, `year`, `month`, `week`, `day`, `hour`. |

### Pricing

Billed at the actual cost of each call, usually $0.00038 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/reddit/subreddit-posts.json`](../../../catalog/models/reddit/subreddit-posts.json) · Store page: https://www.sandbase.ai/model/reddit/subreddit-posts

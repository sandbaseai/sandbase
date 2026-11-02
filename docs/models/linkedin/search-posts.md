# LinkedIn Post Search API: pricing, parameters and code examples

`linkedin/search-posts` · data API · LinkedIn · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0012 per call · **Modes:** sync

Search public LinkedIn posts by keyword (text, link, publish date). Results come from search-engine matches over public LinkedIn posts and work best with English keywords.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "linkedin/search-posts", "query": "hiring"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('linkedin/search-posts', {'query': 'hiring'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("linkedin/search-posts", {
  "query": "hiring"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "linkedin/search-posts", sandbase.Params{
	"query": "hiring",
})
```

Same call via the path form: `POST /v1/api/linkedin/search-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | The post search query.  |
| `cursor` | string |  | Pagination cursor from a previous response.  |
| `datePosted` | string |  | Filter by recency. One of last-hour, last-day, last-week, last-month, last-year. one of: `last-hour`, `last-day`, `last-week`, `last-month`, `last-year` |
| `requireCursor` | boolean |  | Deprecated. Every source for this search returns a nextCursor, so this changes nothing about the price or which source serves you; it stays accepted so callers that already send it keep working.  |

## Details

Search public LinkedIn posts by keyword (text, link, publish date). Results come from search-engine matches over public LinkedIn posts and work best with English keywords.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/linkedin/search-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "hiring", "datePosted": "last-week"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The post search query. |
| `cursor` | string | No | Pagination cursor from a previous response. |
| `datePosted` | string | No | Filter by recency. One of last-hour, last-day, last-week, last-month, last-year. One of: `last-hour`, `last-day`, `last-week`, `last-month`, `last-year`. |
| `requireCursor` | boolean | No | Deprecated. Every source for this search returns a nextCursor, so this changes nothing about the price or which source serves you; it stays accepted so callers that already send it keep working. |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/linkedin/search-posts.json`](../../../catalog/models/linkedin/search-posts.json) · Store page: https://www.sandbase.ai/model/linkedin/search-posts

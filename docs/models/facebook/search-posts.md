# Facebook Post Search API: pricing, parameters and code examples

`facebook/search-posts` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.03 per call · **Modes:** sync

Search public Facebook posts by keyword, optionally filtered by location, and get structured post records (text, author, engagement).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.03**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/search-posts", "query": "nike"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/search-posts', {'query': 'nike'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/search-posts", {
  "query": "nike"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/search-posts", sandbase.Params{
	"query": "nike",
})
```

Same call via the path form: `POST /v1/api/facebook/search-posts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results to return (1-20, default 20). range 1–20 |
| `query` | string | yes | Keyword or phrase to search Facebook posts for (e.g. 'product launch').  |
| `endDate` | string |  | Only return posts published on or before this date, format YYYY-MM-DD (e.g. 2024-12-31).  |
| `location` | string |  | Optional place name; include both city and country for best matches (e.g. 'Paris, France'). Uses Facebook's place filter, which favors posts tagged at that place rather than every post by people who live there, and can…  |
| `startDate` | string |  | Only return posts published on or after this date, format YYYY-MM-DD (e.g. 2024-01-01).  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `imagesCount` or `albumPreview`, and it is served only by a source…  |

## Details

Search public Facebook posts by keyword, optionally filtered by location, and get structured post records (text, author, engagement).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/search-posts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "query": "nike"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword or phrase to search Facebook posts for (e.g. 'product launch'). |
| `endDate` | string | No | Only return posts published on or before this date, format YYYY-MM-DD (e.g. 2024-12-31). |
| `limit` | integer | No | Maximum number of results to return (1-20, default 20). |
| `location` | string | No | Optional place name; include both city and country for best matches (e.g. 'Paris, France'). Uses Facebook's place filter, which favors posts tagged at that place rather than every post by people who live there, and can s |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `imagesCount` or `albumPreview`, and it is served only by a source tha |
| `startDate` | string | No | Only return posts published on or after this date, format YYYY-MM-DD (e.g. 2024-01-01). |

### Pricing

Billed at the actual cost of each call, usually $0.03 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/facebook/search-posts.json`](../../../catalog/models/facebook/search-posts.json) · Store page: https://www.sandbase.ai/model/facebook/search-posts

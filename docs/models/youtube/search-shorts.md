# YouTube Shorts Search

`youtube/search-shorts` · api · YouTube

Search YouTube Shorts by keyword and get matching Shorts (title, views, URL) with cursor pagination as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/search-shorts", "query": "cats"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/search-shorts', {'query': 'cats'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/search-shorts", {
  "query": "cats"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/search-shorts", sandbase.Params{
	"query": "cats",
})
```

Same call via the path form: `POST /v1/api/youtube/search-shorts` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | The keyword to search Shorts for.  |
| `cursor` | string |  | Continuation token from a previous response for pagination.  |
| `sortBy` | string |  | Sort order: "relevance" (default) or "popular" (most-viewed). one of: `relevance`, `popular`; default `"relevance"` |
| `uploadDate` | string |  | Filter by upload recency. Omit for any time. one of: `today`, `this_week`, `this_month`, `this_year` |

## Details

Search YouTube Shorts by keyword and get matching Shorts (title, views, URL) with cursor pagination as normalized JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/search-shorts" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "cats"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The keyword to search Shorts for. |
| `cursor` | string | No | Continuation token from a previous response for pagination. |
| `sortBy` | string | No | Sort order: "relevance" (default) or "popular" (most-viewed). One of: `relevance`, `popular`. |
| `uploadDate` | string | No | Filter by upload recency. Omit for any time. One of: `today`, `this_week`, `this_month`, `this_year`. |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/youtube/search-shorts.json`](../../../catalog/models/youtube/search-shorts.json) · Store page: https://www.sandbase.ai/model/youtube/search-shorts

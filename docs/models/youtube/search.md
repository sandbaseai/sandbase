# YouTube Search

`youtube/search` · api · YouTube

Search YouTube and get matching videos (title, channel, views, length, publish time) as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0005**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "youtube/search", "query": "how to cook rice"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('youtube/search', {'query': 'how to cook rice'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("youtube/search", {
  "query": "how to cook rice"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "youtube/search", sandbase.Params{
	"query": "how to cook rice",
})
```

Same call via the path form: `POST /v1/api/youtube/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | The YouTube search query.  |
| `cursor` | string |  | Continuation token from a previous response for pagination.  |
| `sortBy` | string |  | Sort order: "relevance" (default) or "popular" (most-viewed). one of: `relevance`, `popular`; default `"relevance"` |
| `uploadDate` | string |  | Filter by upload recency. Omit for any time. one of: `today`, `this_week`, `this_month`, `this_year` |
| `requireCursor` | boolean |  | Deprecated; send `requireFields: ["nextCursor"]` instead, which does exactly the same thing. Set true if you intend to page through results, so the request is only served by a source that can return a nextCursor. Omit…  |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `nextCursor`, and it is served only by a source that returns every…  |

## Details

Search YouTube and get matching videos (title, channel, views, length, publish time) as normalized JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/youtube/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "how to cook rice"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The YouTube search query. |
| `cursor` | string | No | Continuation token from a previous response for pagination. |
| `requireCursor` | boolean | No | Deprecated; send `requireFields: ["nextCursor"]` instead, which does exactly the same thing. Set true if you intend to page through results, so the request is only served by a source that can return a nextCursor. Omit it |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `nextCursor`, and it is served only by a source that returns every one |
| `sortBy` | string | No | Sort order: "relevance" (default) or "popular" (most-viewed). One of: `relevance`, `popular`. |
| `uploadDate` | string | No | Filter by upload recency. Omit for any time. One of: `today`, `this_week`, `this_month`, `this_year`. |

### Pricing

Billed at the actual cost of each call, usually $0.0005 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/youtube/search.json`](../../../catalog/models/youtube/search.json) · Store page: https://www.sandbase.ai/model/youtube/search

# Reddit Subreddit Search

`reddit/subreddit-search` · api · Reddit

Search posts within a single subreddit by query, sort, and timeframe.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00035**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "reddit/subreddit-search", "subreddit": "Fitness"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('reddit/subreddit-search', {'subreddit': 'Fitness'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("reddit/subreddit-search", {
  "subreddit": "Fitness"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "reddit/subreddit-search", sandbase.Params{
	"subreddit": "Fitness",
})
```

Same call via the path form: `POST /v1/api/reddit/subreddit-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Optional sort order: relevance, hot, top, new, comments. one of: `relevance`, `hot`, `top`, `new`, `comments` |
| `query` | string |  | Optional search query to match posts (e.g. 'push ups').  |
| `cursor` | string |  | Optional pagination token from a previous response. Include `nextCursor` in requireFields on the first request to make sure a source that supports pagination serves it.  |
| `subreddit` | string | yes | Subreddit name without the r/ prefix (e.g. 'Fitness').  |
| `timeframe` | string |  | Optional time filter: all, year, month, week, day, hour. one of: `all`, `year`, `month`, `week`, `day`, `hour` |
| `requireFields` | array |  | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `nextCursor` or `selftext`, and it is served only by a source that…  |

## Details

Search posts within a single subreddit by query, sort, and timeframe.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/reddit/subreddit-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "push ups", "subreddit": "Fitness"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `subreddit` | string | Yes | Subreddit name without the r/ prefix (e.g. 'Fitness'). |
| `cursor` | string | No | Optional pagination token from a previous response. Include `nextCursor` in requireFields on the first request to make sure a source that supports pagination serves it. |
| `query` | string | No | Optional search query to match posts (e.g. 'push ups'). |
| `requireFields` | array | No | Optional; omit it and routing is unchanged, with the cheapest source serving. Name the output fields this request must be able to return, for example `nextCursor` or `selftext`, and it is served only by a source that ret |
| `sort` | string | No | Optional sort order: relevance, hot, top, new, comments. One of: `relevance`, `hot`, `top`, `new`, `comments`. |
| `timeframe` | string | No | Optional time filter: all, year, month, week, day, hour. One of: `all`, `year`, `month`, `week`, `day`, `hour`. |

### Pricing

Billed at the actual cost of each call, usually $0.00035 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/reddit/subreddit-search.json`](../../../catalog/models/reddit/subreddit-search.json) · Store page: https://www.sandbase.ai/model/reddit/subreddit-search

# Hacker News Search API: pricing, parameters and code examples

`hacker-news/search` · data API · Hacker News · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0015 per call · **Modes:** sync

Search Hacker News by keyword - matching stories with title, link, author, points, and comment count as clean JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0015**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "hacker-news/search", "query": "ai"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('hacker-news/search', {'query': 'ai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("hacker-news/search", {
  "query": "ai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "hacker-news/search", sandbase.Params{
	"query": "ai",
})
```

Same call via the path form: `POST /v1/api/hacker-news/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `tags` | string |  | Optional result filter, e.g. "story" or "comment".  |
| `query` | string | yes | Search keyword, e.g. "ai".  |

## Details

Search Hacker News by keyword - matching stories with title, link, author, points, and comment count as clean JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/hacker-news/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "ai"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword, e.g. "ai". |
| `tags` | string | No | Optional result filter, e.g. "story" or "comment". |

### Pricing

Billed at the actual cost of each call, usually $0.0015 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/hacker-news/search.json`](../../../catalog/models/hacker-news/search.json) · Store page: https://www.sandbase.ai/model/hacker-news/search

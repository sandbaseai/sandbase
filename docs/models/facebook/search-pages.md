# Facebook Page Search API: pricing, parameters and code examples

`facebook/search-pages` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.123 per call · **Modes:** sync

Search Facebook Pages by keyword, optionally narrowed to a location, and get structured page profiles (name, category, followers, contact details).

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.123**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/search-pages", "query": "nike"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/search-pages', {'query': 'nike'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/search-pages", {
  "query": "nike"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/search-pages", sandbase.Params{
	"query": "nike",
})
```

Same call via the path form: `POST /v1/api/facebook/search-pages` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results to return (1-10, default 10). You are billed per result returned, so a lower limit costs less. range 1–10 |
| `query` | string | yes | Keyword to search Facebook Pages for (e.g. 'coffee roasters').  |
| `location` | string |  | Optional free-text location to narrow the search: a city, province, or country (e.g. 'Berlin').  |

## Details

Search Facebook Pages by keyword, optionally narrowed to a location, and get structured page profiles (name, category, followers, contact details).

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/search-pages" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"limit": 3, "query": "nike"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword to search Facebook Pages for (e.g. 'coffee roasters'). |
| `limit` | integer | No | Maximum number of results to return (1-10, default 10). You are billed per result returned, so a lower limit costs less. |
| `location` | string | No | Optional free-text location to narrow the search: a city, province, or country (e.g. 'Berlin'). |

### Pricing

Billed at the actual cost of each call, usually $0.123 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/facebook/search-pages.json`](../../../catalog/models/facebook/search-pages.json) · Store page: https://www.sandbase.ai/model/facebook/search-pages

# Facebook Company Search API: pricing, parameters and code examples

`facebook/search-companies` · data API · Facebook · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0011 per call · **Modes:** sync

Search the Meta Ad Library for advertisers by keyword and get matching pages: page ID, category, verification, follower counts, and linked Instagram.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0011**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/search-companies", "query": "nike"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/search-companies', {'query': 'nike'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/search-companies", {
  "query": "nike"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/search-companies", sandbase.Params{
	"query": "nike",
})
```

Same call via the path form: `POST /v1/api/facebook/search-companies` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Keyword to search advertiser pages for (e.g. "nike").  |

## Details

Search the Meta Ad Library for advertisers by keyword and get matching pages: page ID, category, verification, follower counts, and linked Instagram.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/search-companies" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "nike"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Keyword to search advertiser pages for (e.g. "nike"). |

### Pricing

Billed at the actual cost of each call, usually $0.0011 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/facebook/search-companies.json`](../../../catalog/models/facebook/search-companies.json) · Store page: https://www.sandbase.ai/model/facebook/search-companies

# Facebook Marketplace Location Search

`facebook/marketplace-location-search` · api · Facebook

Resolve a place name to Facebook Marketplace locations with coordinates and metadata as normalized JSON.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0012**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "facebook/marketplace-location-search", "query": "Austin"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('facebook/marketplace-location-search', {'query': 'Austin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("facebook/marketplace-location-search", {
  "query": "Austin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "facebook/marketplace-location-search", sandbase.Params{
	"query": "Austin",
})
```

Same call via the path form: `POST /v1/api/facebook/marketplace-location-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Location search query (e.g. a city name).  |

## Details

Resolve a place name to Facebook Marketplace locations with coordinates and metadata as normalized JSON.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/facebook/marketplace-location-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "Austin"}'
```

The result is returned in `outputs[0].data`. A lookup that finds nothing still succeeds and returns `found: false`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Location search query (e.g. a city name). |

### Pricing

Billed at the actual cost of each call, usually $0.0012 per request. A call can cost more when the first data source fails and another one answers. Failed calls are not charged. Lookups that find nothing and searches with no results are billed at their actual cost, which is often lower and can be $0.

---
Machine-readable: [`catalog/models/facebook/marketplace-location-search.json`](../../../catalog/models/facebook/marketplace-location-search.json) · Store page: https://www.sandbase.ai/model/facebook/marketplace-location-search

# Yellow Pages Search Filters API: pricing, parameters and code examples

`yellowpages/search-filters` · data API · Yellow Pages · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Get available search filters for a query and location. Returns quick filter options (e.g., 'OPEN 24 Hours') and nearby location refinements when available. Useful for discovering refinement options before narrowing a search.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yellowpages/search-filters", "query": "plumber", "location": "new york ny"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yellowpages/search-filters', {'query': 'plumber', 'location': 'new york ny'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yellowpages/search-filters", {
  "query": "plumber",
  "location": "new york ny"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yellowpages/search-filters", sandbase.Params{
	"query": "plumber",
	"location": "new york ny",
})
```

Same call via the path form: `POST /v1/api/yellowpages/search-filters` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword (e.g., 'plumber', 'restaurant')  |
| `location` | string | yes | Location (e.g., 'new york ny', 'los angeles ca')  |

## Details

Get available search filters for a query and location. Returns quick filter options (e.g., 'OPEN 24 Hours') and nearby location refinements when available. Useful for discovering refinement options before narrowing a search.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "yellowpages/search-filters", "query": "plumber", "location": "new york ny"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `location` | string | Yes | Location (e.g., 'new york ny', 'los angeles ca') |
| `query` | string | Yes | Search keyword (e.g., 'plumber', 'restaurant') |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yellowpages/search-filters.json`](../../../catalog/models/yellowpages/search-filters.json) · Store page: https://www.sandbase.ai/model/yellowpages/search-filters

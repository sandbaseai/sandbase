# Yellow Pages Search Businesses API: pricing, parameters and code examples

`yellowpages/search-businesses` · data API · Yellow Pages · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Full-text search for businesses by keyword and location on YellowPages.com.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "yellowpages/search-businesses", "query": "plumber", "location": "new york ny"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('yellowpages/search-businesses', {'query': 'plumber', 'location': 'new york ny'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("yellowpages/search-businesses", {
  "query": "plumber",
  "location": "new york ny"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "yellowpages/search-businesses", sandbase.Params{
	"query": "plumber",
	"location": "new york ny",
})
```

Same call via the path form: `POST /v1/api/yellowpages/search-businesses` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Starting page number for pagination default `1` |
| `limit` | integer |  | Maximum number of results to return across all pages default `500` |
| `query` | string | yes | Search keyword (e.g., 'plumber', 'restaurant', 'dentist')  |
| `location` | string | yes | Location to search in (e.g., 'new york ny', 'los angeles ca')  |

## Details

Full-text search for businesses by keyword and location on YellowPages.com.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "yellowpages/search-businesses", "page": 1, "limit": 5, "query": "plumber", "location": "new york ny"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `location` | string | Yes | Location to search in (e.g., 'new york ny', 'los angeles ca') |
| `query` | string | Yes | Search keyword (e.g., 'plumber', 'restaurant', 'dentist') |
| `limit` | integer | No | Maximum number of results to return across all pages |
| `page` | integer | No | Starting page number for pagination |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/yellowpages/search-businesses.json`](../../../catalog/models/yellowpages/search-businesses.json) · Store page: https://www.sandbase.ai/model/yellowpages/search-businesses

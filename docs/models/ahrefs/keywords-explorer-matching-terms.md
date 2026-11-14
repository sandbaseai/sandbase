# Ahrefs Keywords Explorer Matching Terms API: pricing, parameters and code examples

`ahrefs/keywords-explorer-matching-terms` · data API · Ahrefs · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.01419 per call · **Modes:** async

Find keyword ideas containing seed terms, with volume and difficulty.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.01419**

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ahrefs/keywords-explorer-matching-terms", "country": "us", "keywords": ["coffee grinder"]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ahrefs/keywords-explorer-matching-terms', {'country': 'us', 'keywords': ['coffee grinder']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ahrefs/keywords-explorer-matching-terms", {
  "country": "us",
  "keywords": [
    "coffee grinder"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ahrefs/keywords-explorer-matching-terms", sandbase.Params{
	"country": "us",
	"keywords": []any{"coffee grinder"},
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ahrefs/keywords-explorer-matching-terms` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of rows to return (1-50, default 10). Each returned row is charged, so this caps the cost of one call. default `10`; range 1–50 |
| `where` | string |  | JSON filter expression (see the Ahrefs filter syntax docs). Filterable fields: keyword, volume, difficulty, cpc.  |
| `country` | string | yes | Two-letter country code (ISO 3166-1 alpha-2), e.g. 'us'.  |
| `keywords` | array | yes | Keywords to analyze (up to 100). Each returned keyword is one charged row.  |
| `order_by` | string |  | Sort order: 'field' or 'field:desc', comma-separated. Sortable fields: keyword, volume, difficulty, cpc.  |

## Details

Find keyword ideas containing seed terms, with volume and difficulty.

### Pricing

- Inspect reference unit price: $0.01419 USD per result.
- Final settlement uses the provider-reported actual cost after strict validation; the reference price is not used to infer the final charge.

---
Machine-readable: [`catalog/models/ahrefs/keywords-explorer-matching-terms.json`](../../../catalog/models/ahrefs/keywords-explorer-matching-terms.json) · Store page: https://www.sandbase.ai/model/ahrefs/keywords-explorer-matching-terms

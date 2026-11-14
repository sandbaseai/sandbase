# Ahrefs Serp Overview Serp Overview API: pricing, parameters and code examples

`ahrefs/serp-overview-serp-overview` · data API · Ahrefs · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0129 per call · **Modes:** async

Get the top organic results for a keyword with ratings, backlinks, and traffic.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0129**

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ahrefs/serp-overview-serp-overview", "country": "us", "keyword": "coffee grinder"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ahrefs/serp-overview-serp-overview', {'country': 'us', 'keyword': 'coffee grinder'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ahrefs/serp-overview-serp-overview", {
  "country": "us",
  "keyword": "coffee grinder"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ahrefs/serp-overview-serp-overview", sandbase.Params{
	"country": "us",
	"keyword": "coffee grinder",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ahrefs/serp-overview-serp-overview` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `date` | string |  | Report date in YYYY-MM-DD format. Use today's date for current values.  |
| `country` | string | yes | Two-letter country code (ISO 3166-1 alpha-2), e.g. 'us'.  |
| `keyword` | string | yes | The keyword to analyze.  |
| `top_positions` | integer |  | Return organic results ranked at positions 1..N — at most N charged rows, fewer when some of those positions hold SERP features (which are never returned). Defaults to 100 (the maximum). default `100`; range 1–100 |

## Details

Get the top organic results for a keyword with ratings, backlinks, and traffic.

### Pricing

- Inspect reference unit price: $0.0129 USD per result.
- Final settlement uses the provider-reported actual cost after strict validation; the reference price is not used to infer the final charge.

---
Machine-readable: [`catalog/models/ahrefs/serp-overview-serp-overview.json`](../../../catalog/models/ahrefs/serp-overview-serp-overview.json) · Store page: https://www.sandbase.ai/model/ahrefs/serp-overview-serp-overview

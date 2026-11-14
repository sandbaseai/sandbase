# Ahrefs Site Explorer Domain Rating API: pricing, parameters and code examples

`ahrefs/site-explorer-domain-rating` · data API · Ahrefs · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00129 per call · **Modes:** async

Get a target's Domain Rating (0-100 link authority) and its global rank.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00129**

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ahrefs/site-explorer-domain-rating", "date": "2026-11-01", "target": "ahrefs.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ahrefs/site-explorer-domain-rating', {'date': '2026-11-01', 'target': 'ahrefs.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ahrefs/site-explorer-domain-rating", {
  "date": "2026-11-01",
  "target": "ahrefs.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ahrefs/site-explorer-domain-rating", sandbase.Params{
	"date": "2026-11-01",
	"target": "ahrefs.com",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ahrefs/site-explorer-domain-rating` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `date` | string | yes | Report date in YYYY-MM-DD format. Use today's date for current values.  |
| `target` | string | yes | The target of the report: a domain ('example.com') or a URL ('https://example.com/page').  |

## Details

Get a target's Domain Rating (0-100 link authority) and its global rank.

### Pricing

- Inspect reference unit price: $0.00129 USD per result.
- Final settlement uses the provider-reported actual cost after strict validation; the reference price is not used to infer the final charge.

---
Machine-readable: [`catalog/models/ahrefs/site-explorer-domain-rating.json`](../../../catalog/models/ahrefs/site-explorer-domain-rating.json) · Store page: https://www.sandbase.ai/model/ahrefs/site-explorer-domain-rating

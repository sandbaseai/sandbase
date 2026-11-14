# Ahrefs Site Explorer Total Search Volume History API: pricing, parameters and code examples

`ahrefs/site-explorer-total-search-volume-history` · data API · Ahrefs · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.007095 per call · **Modes:** async

Track total search volume of keywords a target ranks for over time.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.007095**

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ahrefs/site-explorer-total-search-volume-history", "date_from": "2026-08-01", "target": "ahrefs.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ahrefs/site-explorer-total-search-volume-history', {'date_from': '2026-08-01', 'target': 'ahrefs.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ahrefs/site-explorer-total-search-volume-history", {
  "date_from": "2026-08-01",
  "target": "ahrefs.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ahrefs/site-explorer-total-search-volume-history", sandbase.Params{
	"date_from": "2026-08-01",
	"target": "ahrefs.com",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ahrefs/site-explorer-total-search-volume-history` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `scope` | string |  | Scope of the target: exact (this URL only), prefix (URLs starting with the target), domain (the domain without subdomains), or subdomains (default — the domain and all its subdomains). one of: `exact`, `prefix`, `domain`, `subdomains`; default `"subdomains"` |
| `target` | string | yes | The target of the report: a domain ('example.com') or a URL ('https://example.com/page').  |
| `country` | string |  | Two-letter country code (ISO 3166-1 alpha-2), e.g. 'us'.  |
| `date_to` | string |  | End date of the historical period in YYYY-MM-DD format. Defaults to today.  |
| `protocol` | string |  | Protocol of the target: both (default), http, or https. one of: `both`, `http`, `https`; default `"both"` |
| `date_from` | string | yes | Start date of the historical period in YYYY-MM-DD format.  |
| `history_grouping` | string |  | Time bucket size for history rows: daily, weekly, or monthly (default). Each bucket is one charged row. one of: `daily`, `weekly`, `monthly`; default `"monthly"` |

## Details

Track total search volume of keywords a target ranks for over time.

### Pricing

- Inspect reference unit price: $0.007095 USD per result.
- Final settlement uses the provider-reported actual cost after strict validation; the reference price is not used to infer the final charge.

---
Machine-readable: [`catalog/models/ahrefs/site-explorer-total-search-volume-history.json`](../../../catalog/models/ahrefs/site-explorer-total-search-volume-history.json) · Store page: https://www.sandbase.ai/model/ahrefs/site-explorer-total-search-volume-history

# Ahrefs Site Explorer Pages By Internal Links API: pricing, parameters and code examples

`ahrefs/site-explorer-pages-by-internal-links` · data API · Ahrefs · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.001935 per call · **Modes:** async

List a target's pages ordered by incoming internal link counts.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.001935**

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ahrefs/site-explorer-pages-by-internal-links", "target": "ahrefs.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ahrefs/site-explorer-pages-by-internal-links', {'target': 'ahrefs.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ahrefs/site-explorer-pages-by-internal-links", {
  "target": "ahrefs.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ahrefs/site-explorer-pages-by-internal-links", sandbase.Params{
	"target": "ahrefs.com",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ahrefs/site-explorer-pages-by-internal-links` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of rows to return (1-50, default 10). Each returned row is charged, so this caps the cost of one call. default `10`; range 1–50 |
| `scope` | string |  | Scope of the target: exact (this URL only), prefix (URLs starting with the target), domain (the domain without subdomains), or subdomains (default — the domain and all its subdomains). one of: `exact`, `prefix`, `domain`, `subdomains`; default `"subdomains"` |
| `where` | string |  | JSON filter expression (see the Ahrefs filter syntax docs). Filterable fields: url_to, title_target, links_to_target.  |
| `target` | string | yes | The target of the report: a domain ('example.com') or a URL ('https://example.com/page').  |
| `order_by` | string |  | Sort order: 'field' or 'field:desc', comma-separated. Sortable fields: url_to, links_to_target.  |
| `protocol` | string |  | Protocol of the target: both (default), http, or https. one of: `both`, `http`, `https`; default `"both"` |

## Details

List a target's pages ordered by incoming internal link counts.

### Pricing

- Inspect reference unit price: $0.001935 USD per result.
- Final settlement uses the provider-reported actual cost after strict validation; the reference price is not used to infer the final charge.

---
Machine-readable: [`catalog/models/ahrefs/site-explorer-pages-by-internal-links.json`](../../../catalog/models/ahrefs/site-explorer-pages-by-internal-links.json) · Store page: https://www.sandbase.ai/model/ahrefs/site-explorer-pages-by-internal-links

# Ahrefs Site Explorer Ai Responses Count API: pricing, parameters and code examples

`ahrefs/site-explorer-ai-responses-count` · data API · Ahrefs · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.087075 per call · **Modes:** async

Count how often eight AI assistants cite a target in generated answers.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.087075**

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ahrefs/site-explorer-ai-responses-count", "target": "ahrefs.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ahrefs/site-explorer-ai-responses-count', {'target': 'ahrefs.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ahrefs/site-explorer-ai-responses-count", {
  "target": "ahrefs.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ahrefs/site-explorer-ai-responses-count", sandbase.Params{
	"target": "ahrefs.com",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ahrefs/site-explorer-ai-responses-count` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `date` | string |  | Report date in YYYY-MM-DD format. Use today's date for current values.  |
| `scope` | string |  | Scope of the target: exact (this URL only), prefix (URLs starting with the target), domain (the domain without subdomains), or subdomains (default — the domain and all its subdomains). one of: `exact`, `prefix`, `domain`, `subdomains`; default `"subdomains"` |
| `target` | string | yes | The target of the report: a domain ('example.com') or a URL ('https://example.com/page').  |
| `country` | string |  | Two-letter country code (ISO 3166-1 alpha-2), e.g. 'us'.  |
| `protocol` | string |  | Protocol of the target: both (default), http, or https. one of: `both`, `http`, `https`; default `"both"` |

## Details

Count how often eight AI assistants cite a target in generated answers.

### Pricing

- Inspect reference unit price: $0.087075 USD per result.
- Final settlement uses the provider-reported actual cost after strict validation; the reference price is not used to infer the final charge.

---
Machine-readable: [`catalog/models/ahrefs/site-explorer-ai-responses-count.json`](../../../catalog/models/ahrefs/site-explorer-ai-responses-count.json) · Store page: https://www.sandbase.ai/model/ahrefs/site-explorer-ai-responses-count

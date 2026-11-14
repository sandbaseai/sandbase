# Ahrefs Keywords Explorer Volume History API: pricing, parameters and code examples

`ahrefs/keywords-explorer-volume-history` · data API · Ahrefs · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00129 per call · **Modes:** async

Track a keyword's monthly search volume over time in one country.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00129**

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ahrefs/keywords-explorer-volume-history", "country": "us", "date_from": "2026-08-01", "keyword": "coffee grinder"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ahrefs/keywords-explorer-volume-history', {'country': 'us', 'date_from': '2026-08-01', 'keyword': 'coffee grinder'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ahrefs/keywords-explorer-volume-history", {
  "country": "us",
  "date_from": "2026-08-01",
  "keyword": "coffee grinder"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ahrefs/keywords-explorer-volume-history", sandbase.Params{
	"country": "us",
	"date_from": "2026-08-01",
	"keyword": "coffee grinder",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ahrefs/keywords-explorer-volume-history` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `country` | string | yes | Two-letter country code (ISO 3166-1 alpha-2), e.g. 'us'.  |
| `date_to` | string |  | End date of the historical period in YYYY-MM-DD format. Defaults to today.  |
| `keyword` | string | yes | The keyword to analyze.  |
| `date_from` | string | yes | Start date of the historical period in YYYY-MM-DD format.  |

## Details

Track a keyword's monthly search volume over time in one country.

### Pricing

- Inspect reference unit price: $0.00129 USD per result.
- Final settlement uses the provider-reported actual cost after strict validation; the reference price is not used to infer the final charge.

---
Machine-readable: [`catalog/models/ahrefs/keywords-explorer-volume-history.json`](../../../catalog/models/ahrefs/keywords-explorer-volume-history.json) · Store page: https://www.sandbase.ai/model/ahrefs/keywords-explorer-volume-history

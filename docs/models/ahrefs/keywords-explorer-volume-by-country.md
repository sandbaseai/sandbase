# Ahrefs Keywords Explorer Volume By Country API: pricing, parameters and code examples

`ahrefs/keywords-explorer-volume-by-country` · data API · Ahrefs · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.007095 per call · **Modes:** async

Split a keyword's search volume across countries.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.007095**

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ahrefs/keywords-explorer-volume-by-country", "keyword": "coffee grinder"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ahrefs/keywords-explorer-volume-by-country', {'keyword': 'coffee grinder'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ahrefs/keywords-explorer-volume-by-country", {
  "keyword": "coffee grinder"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ahrefs/keywords-explorer-volume-by-country", sandbase.Params{
	"keyword": "coffee grinder",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ahrefs/keywords-explorer-volume-by-country` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of rows to return (1-50, default 10). Each returned row is charged, so this caps the cost of one call. default `10`; range 1–50 |
| `keyword` | string | yes | The keyword to analyze.  |

## Details

Split a keyword's search volume across countries.

### Pricing

- Inspect reference unit price: $0.007095 USD per result.
- Final settlement uses the provider-reported actual cost after strict validation; the reference price is not used to infer the final charge.

---
Machine-readable: [`catalog/models/ahrefs/keywords-explorer-volume-by-country.json`](../../../catalog/models/ahrefs/keywords-explorer-volume-by-country.json) · Store page: https://www.sandbase.ai/model/ahrefs/keywords-explorer-volume-by-country

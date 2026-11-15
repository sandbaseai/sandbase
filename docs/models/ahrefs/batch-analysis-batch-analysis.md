# Ahrefs Batch Analysis Batch Analysis API: pricing, parameters and code examples

`ahrefs/batch-analysis-batch-analysis` · data API · Ahrefs · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.013545 per call · **Modes:** async

Get Domain Rating, backlinks, and traffic metrics for up to 100 targets at once.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.013545**

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "ahrefs/batch-analysis-batch-analysis", "targets": [{"url": "ahrefs.com"}]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('ahrefs/batch-analysis-batch-analysis', {'targets': [{'url': 'ahrefs.com'}]})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("ahrefs/batch-analysis-batch-analysis", {
  "targets": [
    {
      "url": "ahrefs.com"
    }
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "ahrefs/batch-analysis-batch-analysis", sandbase.Params{
	"targets": []any{map[string]any{
		"url": "ahrefs.com",
	}},
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/ahrefs/batch-analysis-batch-analysis` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `country` | string |  | Two-letter country code (ISO 3166-1 alpha-2), e.g. 'us'.  |
| `targets` | array | yes | Targets to analyze (up to 50; one charged row per target).  |

## Details

Get Domain Rating, backlinks, and traffic metrics for up to 100 targets at once.

### Pricing

- Inspect reference unit price: $0.013545 USD per result.
- Final settlement uses the provider-reported actual cost after strict validation; the reference price is not used to infer the final charge.

---
Machine-readable: [`catalog/models/ahrefs/batch-analysis-batch-analysis.json`](../../../catalog/models/ahrefs/batch-analysis-batch-analysis.json) · Store page: https://www.sandbase.ai/model/ahrefs/batch-analysis-batch-analysis

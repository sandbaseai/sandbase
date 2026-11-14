# Akta Markdown API: pricing, parameters and code examples

`akta/markdown` · data API · Akta · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.025 per call · **Modes:** async

Get selected company profile sections as one Markdown document.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.025**

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "akta/markdown", "company": "https://canva.com", "sections": ["firmographic"]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('akta/markdown', {'company': 'https://canva.com', 'sections': ['firmographic']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("akta/markdown", {
  "company": "https://canva.com",
  "sections": [
    "firmographic"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "akta/markdown", sandbase.Params{
	"company": "https://canva.com",
	"sections": []any{"firmographic"},
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/akta/markdown` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `company` | string | yes | Company website (e.g. 'https://canva.com') or the company uuid returned by the akta Company Search endpoint. A bare company name is NOT accepted here — resolve it via company-search first.  |
| `sections` | array | yes | Sections to return (comma-separated query param). Required — to get every section, list all of them. Available: firmographic, business_model, company_assessment, trust_signal, company_hierarchy, digital_presence,…  |

## Details

Get selected company profile sections as one Markdown document.

### Pricing

- Inspect reference unit price: $0.025 USD per result.
- Final settlement uses the provider-reported actual cost after strict validation; the reference price is not used to infer the final charge.

---
Machine-readable: [`catalog/models/akta/markdown.json`](../../../catalog/models/akta/markdown.json) · Store page: https://www.sandbase.ai/model/akta/markdown

# Akta Company Website Traffic API: pricing, parameters and code examples

`akta/company-website-traffic` · data API · Akta · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.075 per call · **Modes:** async

Get a company website's monthly visits, engagement and traffic sources.

## Pricing

- **$0.075 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "akta/company-website-traffic", "company": "https://canva.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('akta/company-website-traffic', {'company': 'https://canva.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("akta/company-website-traffic", {
  "company": "https://canva.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "akta/company-website-traffic", sandbase.Params{
	"company": "https://canva.com",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/akta/company-website-traffic` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `company` | string | yes | Company website (e.g. 'https://canva.com') or the company uuid returned by the akta Company Search endpoint. A bare company name is NOT accepted here — resolve it via company-search first.  |

## Details

Get a company website's monthly visits, engagement and traffic sources.

---
Machine-readable: [`catalog/models/akta/company-website-traffic.json`](../../../catalog/models/akta/company-website-traffic.json) · Store page: https://www.sandbase.ai/model/akta/company-website-traffic

# Apollo Organization Enrichment

`apollo/company-enrich` · api · Apollo

Enrich one company by domain. `domain` is the only parameter and it must be the bare domain (apple.com), not a full URL.

## Pricing

- **$0.01975 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apollo/company-enrich", "domain": "stripe.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('apollo/company-enrich', {'domain': 'stripe.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("apollo/company-enrich", {
  "domain": "stripe.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "apollo/company-enrich", sandbase.Params{
	"domain": "stripe.com",
})
```

Same call via the path form: `POST /v1/api/apollo/company-enrich` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domain` | string | yes | The domain of the company that you want to enrich. Do not include www., the @ symbol, or similar. Example: apollo.io or microsoft.com  |

## Details

Enrich one company by domain. `domain` is the only parameter and it must be the bare domain (apple.com), not a full URL.

The response is the official Apollo API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/apollo/company-enrich" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domain": "stripe.com"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domain` | string | Yes | The domain of the company that you want to enrich. Do not include www., the @ symbol, or similar. Example: apollo.io or microsoft.com |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/apollo/company-enrich.json`](../../../catalog/models/apollo/company-enrich.json) · Store page: https://www.sandbase.ai/model/apollo/company-enrich

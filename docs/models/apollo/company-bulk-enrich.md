# Apollo Bulk Organization Enrichment API: pricing, parameters and code examples

`apollo/company-bulk-enrich` · data API · Apollo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.01975 per run, depending on parameters · **Modes:** sync

Enrich up to 10 companies in one call. Body takes `domains`, an array of bare domains.

## Pricing

- Depends on parameters ().

| parameters | USD |
|---|---|
| defaults | 0.01975 |

Formula: `0.01975 * Math.max(1.0, Math.min(10.0, len(params["domains[]"] ?? []) * 1.0))`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "apollo/company-bulk-enrich", "domains[]": ["stripe.com", "notion.so"]}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('apollo/company-bulk-enrich', {'domains[]': ['stripe.com', 'notion.so']})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("apollo/company-bulk-enrich", {
  "domains[]": [
    "stripe.com",
    "notion.so"
  ]
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "apollo/company-bulk-enrich", sandbase.Params{
	"domains[]": []any{"stripe.com", "notion.so"},
})
```

Same call via the path form: `POST /v1/api/apollo/company-bulk-enrich` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `domains[]` | array | yes | The domain of each company that you want to enrich. Do not include www., the @ symbol, or similar. Example: apollo.io and microsoft.com  |

## Details

Enrich up to 10 companies in one call. Body takes `domains`, an array of bare domains.

The response is the official Apollo API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/apollo/company-bulk-enrich" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"domains[]": ["stripe.com", "notion.so"]}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `domains[]` | array | Yes | The domain of each company that you want to enrich. Do not include www., the @ symbol, or similar. Example: apollo.io and microsoft.com |

### Pricing

$0.01975 per domain, up to 10 domains per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/apollo/company-bulk-enrich.json`](../../../catalog/models/apollo/company-bulk-enrich.json) · Store page: https://www.sandbase.ai/model/apollo/company-bulk-enrich

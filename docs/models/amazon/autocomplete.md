# Amazon Search Suggestions API: pricing, parameters and code examples

`amazon/autocomplete` · data API · Amazon · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call · **Modes:** async

Get Amazon search box suggestions for a partial keyword, optionally for a specific Amazon domain and department.

## Pricing

- **$0.00015 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "amazon/autocomplete", "k": "iphone ca"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('amazon/autocomplete', {'k': 'iphone ca'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("amazon/autocomplete", {
  "k": "iphone ca"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "amazon/autocomplete", sandbase.Params{
	"k": "iphone ca",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/amazon/autocomplete` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `k` | string | yes | Partial search text to complete.  |
| `timeout` | number |  | Seconds the data source may spend before giving up (max 50, default 50). A timed-out call is not billed. default `50`; range –50 |
| `amazon_domain` | string |  | Amazon storefront hostname.  |
| `amazon_department` | string |  | Department alias used to narrow suggestions; aps searches all departments.  |

## Details

Get Amazon search box suggestions for a partial keyword, optionally for a specific Amazon domain and department.

---
Machine-readable: [`catalog/models/amazon/autocomplete.json`](../../../catalog/models/amazon/autocomplete.json) · Store page: https://www.sandbase.ai/model/amazon/autocomplete

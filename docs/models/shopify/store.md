# Shopify Store Profile API: pricing, parameters and code examples

`shopify/store` · data API · Shopify · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

Look up any public Shopify store by its domain and get its name, description, currency, country and city, the countries it ships to, its published product and collection counts and its social links in one normalized response. A domain that is not a public Shopify store comes back not found.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "shopify/store", "store": "allbirds.com"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('shopify/store', {'store': 'allbirds.com'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("shopify/store", {
  "store": "allbirds.com"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "shopify/store", sandbase.Params{
	"store": "allbirds.com",
})
```

Same call via the path form: `POST /v1/api/shopify/store` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `store` | string | yes | Domain or URL of a public Shopify store, e.g. allbirds.com or https://kith.com. A store on its own domain is addressed by that domain.  |

## Details

Look up any public Shopify store by its domain and get its name, description, currency, country and city, the countries it ships to, its published product and collection counts and its social links in one normalized response. A domain that is not a public Shopify store comes back not found.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "shopify/store", "store": "allbirds.com"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `store` | string | Yes | Domain or URL of a public Shopify store, e.g. allbirds.com or https://kith.com. A store on its own domain is addressed by that domain. |

### Pricing

Billed at the actual cost of each call, about $0.00085 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/shopify/store.json`](../../../catalog/models/shopify/store.json) · Store page: https://www.sandbase.ai/model/shopify/store

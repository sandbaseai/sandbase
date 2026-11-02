# App Store Product API: pricing, parameters and code examples

`app-store/product` · data API · App Store · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** async

Read an iOS or Mac app's details, version history, ratings, privacy, and related apps.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "app-store/product", "product_id": "570060128"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('app-store/product', {'product_id': '570060128'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("app-store/product", {
  "product_id": "570060128"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "app-store/product", sandbase.Params{
	"product_id": "570060128",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/app-store/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `type` | string |  | App product type; only 'app' is supported. one of: `app` |
| `country` | string |  | Two-letter Apple storefront country, such as 'us' or 'gb' ('uk' is accepted). Default 'us'.  |
| `product_id` | string | yes | Positive decimal Apple app identifier, such as '570060128'.  |

## Details

Read an iOS or Mac app's details, version history, ratings, privacy, and related apps.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/app-store/product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "570060128", "country": "us", "type": "app"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Positive decimal Apple app identifier, such as '570060128'. |
| `country` | string | No | Two-letter Apple storefront country, such as 'us' or 'gb' ('uk' is accepted). Default 'us'. |
| `type` | string | No | App product type; only 'app' is supported. One of: `app`. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/app-store/product.json`](../../../catalog/models/app-store/product.json) · Store page: https://www.sandbase.ai/model/app-store/product

# Shop List Categories API: pricing, parameters and code examples

`shop-app/categories` · data API · Shop · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Returns all top-level shopping categories available on shop.app. Categories include a Shopify GID, display name, and whether they have subcategories. No parameters needed.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "shop-app/categories"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('shop-app/categories', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("shop-app/categories", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "shop-app/categories", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/shop-app/categories` with the body above minus `model`.

## Details

Returns all top-level shopping categories available on shop.app. Categories include a Shopify GID, display name, and whether they have subcategories. No parameters needed.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "shop-app/categories"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/shop-app/categories.json`](../../../catalog/models/shop-app/categories.json) · Store page: https://www.sandbase.ai/model/shop-app/categories

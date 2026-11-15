# Shop Merchant Info API: pricing, parameters and code examples

`shop-app/merchant-info` · data API · Shop · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.03 per call · **Modes:** sync

Retrieves merchant profile information including name, website, reviews, contacts, store sections, and visual theme. Returns the full shop object with all available metadata. Use the handle from get_search_autocomplete or get_product_details results.

## Pricing

- **$0.03 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "shop-app/merchant-info", "handle": "05a2xwjtkr"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('shop-app/merchant-info', {'handle': '05a2xwjtkr'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("shop-app/merchant-info", {
  "handle": "05a2xwjtkr"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "shop-app/merchant-info", sandbase.Params{
	"handle": "05a2xwjtkr",
})
```

Same call via the path form: `POST /v1/api/shop-app/merchant-info` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `handle` | string | yes | Merchant handle/slug from get_search_autocomplete or get_product_details results.  |

## Details

Retrieves merchant profile information including name, website, reviews, contacts, store sections, and visual theme. Returns the full shop object with all available metadata. Use the handle from get_search_autocomplete or get_product_details results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "shop-app/merchant-info", "handle": "05a2xwjtkr"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `handle` | string | Yes | Merchant handle/slug from get_search_autocomplete or get_product_details results. |

### Pricing

Flat $0.03 per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/shop-app/merchant-info.json`](../../../catalog/models/shop-app/merchant-info.json) · Store page: https://www.sandbase.ai/model/shop-app/merchant-info

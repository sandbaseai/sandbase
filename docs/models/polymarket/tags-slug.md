# Polymarket Get tag by slug

`polymarket/tags-slug` · api · Polymarket

Get tag by slug from Polymarket. Returns the official Polymarket API response unchanged.

## Pricing

- **$0.00044 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "polymarket/tags-slug", "slug": "product-marekt-fit"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('polymarket/tags-slug', {'slug': 'product-marekt-fit'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("polymarket/tags-slug", {
  "slug": "product-marekt-fit"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "polymarket/tags-slug", sandbase.Params{
	"slug": "product-marekt-fit",
})
```

Same call via the path form: `POST /v1/api/polymarket/tags-slug` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `slug` | string | yes | slug  |
| `include_template` | boolean |  | include_template  |

## Details

Get tag by slug from Polymarket. Returns the official Polymarket API response unchanged.

The response is the official Polymarket API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/polymarket/tags-slug" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"slug": "product-marekt-fit"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `slug` | string | Yes | slug |
| `include_template` | boolean | No | include_template |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/polymarket/tags-slug.json`](../../../catalog/models/polymarket/tags-slug.json) · Store page: https://www.sandbase.ai/model/polymarket/tags-slug

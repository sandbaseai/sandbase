# 1688 Product Description Images API: pricing, parameters and code examples

`1688/item/description-images` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.014286 per call (free daily quota) · **Modes:** sync

Get the description images of a 1688 product listing by item ID, for catalog preparation and product research.

## Pricing

- **$0.014286 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/item/description-images", "itemId": "857511694718"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/item/description-images', {'itemId': '857511694718'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/item/description-images", {
  "itemId": "857511694718"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/item/description-images", sandbase.Params{
	"itemId": "857511694718",
})
```

Same call via the path form: `POST /v1/api/1688/item/description-images` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `itemId` | string | yes | 1688 product ID.  |

## Details

Get the description images of a 1688 product listing by item ID, for catalog preparation and product research.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/item/description-images" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"itemId": "857511694718"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `itemId` | string | Yes | 1688 product ID. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/1688/item/description-images.json`](../../../../catalog/models/1688/item/description-images.json) · Store page: https://www.sandbase.ai/model/1688/item/description-images

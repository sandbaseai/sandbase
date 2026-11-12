# Xiaohongshu Shop Product Detail API: pricing, parameters and code examples

`xiaohongshu/ec/product-detail` · data API · Xiaohongshu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.028571 per call · **Modes:** sync

Get a Xiaohongshu (RedNote) shop product by SKU ID, with title, price, images, specifications, seller and sales information.

## Pricing

- **$0.028571 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "xiaohongshu/ec/product-detail", "skuId": "699c2a9a1dbf92000109a517"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('xiaohongshu/ec/product-detail', {'skuId': '699c2a9a1dbf92000109a517'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("xiaohongshu/ec/product-detail", {
  "skuId": "699c2a9a1dbf92000109a517"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "xiaohongshu/ec/product-detail", sandbase.Params{
	"skuId": "699c2a9a1dbf92000109a517",
})
```

Same call via the path form: `POST /v1/api/xiaohongshu/ec/product-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `skuId` | string | yes | Product SKU ID.  |

## Details

Get a Xiaohongshu (RedNote) shop product by SKU ID, with title, price, images, specifications, seller and sales information.

The result is returned in `outputs[0].data` in the platform's original structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/xiaohongshu/ec/product-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"skuId": "699c2a9a1dbf92000109a517"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `skuId` | string | Yes | Product SKU ID. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/xiaohongshu/ec/product-detail.json`](../../../../catalog/models/xiaohongshu/ec/product-detail.json) · Store page: https://www.sandbase.ai/model/xiaohongshu/ec/product-detail

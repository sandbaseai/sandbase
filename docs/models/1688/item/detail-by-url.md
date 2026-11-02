# 1688 Product Details by URL API: pricing, parameters and code examples

`1688/item/detail-by-url` · data API · 1688 · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.013889 per call (free daily quota) · **Modes:** sync

Get 1688 product details from a product URL: prices by quantity, SKUs, MOQ and supplier, in the chosen language.

## Pricing

- **$0.013889 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "1688/item/detail-by-url", "url": "https://detail.1688.com/offer/857511694718.html"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('1688/item/detail-by-url', {'url': 'https://detail.1688.com/offer/857511694718.html'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("1688/item/detail-by-url", {
  "url": "https://detail.1688.com/offer/857511694718.html"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "1688/item/detail-by-url", sandbase.Params{
	"url": "https://detail.1688.com/offer/857511694718.html",
})
```

Same call via the path form: `POST /v1/api/1688/item/detail-by-url` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string | yes | 1688 product URL.  |
| `scene` | string |  | Optional dropshipping pricing scene. one of: `drop_shipping` |
| `language` | string |  | Output language. one of: `en`, `zh`, `ru`, `th`, `pt`, `es`, `tr`, `vi`, `ja`, `ko`; default `"zh"` |
| `optimizeTitle` | boolean |  | Optimize Chinese titles by removing non-core words. default `false` |

## Details

Get 1688 product details from a product URL: prices by quantity, SKUs, MOQ and supplier, in the chosen language.

The response is the platform's original data structure.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/1688/item/detail-by-url" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://detail.1688.com/offer/857511694718.html"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `url` | string | Yes | 1688 product URL. |
| `scene` | string | No | Optional dropshipping pricing scene. |
| `optimizeTitle` | boolean | No | Optimize Chinese titles by removing non-core words. |
| `language` | string | No | Output language. |

### Pricing

Flat price per call. Failed calls and empty results are not charged.

---
Machine-readable: [`catalog/models/1688/item/detail-by-url.json`](../../../../catalog/models/1688/item/detail-by-url.json) · Store page: https://www.sandbase.ai/model/1688/item/detail-by-url

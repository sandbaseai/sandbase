# Google Play Product Details API: pricing, parameters and code examples

`google-play/product` · data API · Google Play · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** sync

Details of a Google Play app, game, ebook, audiobook or movie by product ID: rating, downloads, price, developer and description.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-play/product", "product_id": "com.duolingo"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-play/product', {'product_id': 'com.duolingo'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-play/product", {
  "product_id": "com.duolingo"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-play/product", sandbase.Params{
	"product_id": "com.duolingo",
})
```

Same call via the path form: `POST /v1/api/google-play/product` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gl` | string |  | Two-letter country code. default `"us"` |
| `hl` | string |  | Storefront language, such as en, de, or zh-TW. Maximum 32 characters. default `"en"` |
| `store` | string |  | Product catalog containing this identifier. one of: `apps`, `books`, `audiobooks`, `movies`, `tv`; default `"apps"` |
| `timeout` | number |  | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater than 0 and at most 90. On expiry, the…  |
| `season_id` | string |  | Native season identifier, such as tvseason-OVPad1njPzI.P. Requires store=tv.  |
| `product_id` | string | yes | Native Google Play product identifier, with 1 to 512 letters, digits, underscores, dots, or hyphens.  |

## Details

Details of a Google Play app, game, ebook, audiobook or movie by product ID: rating, downloads, price, developer and description.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-play/product" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"product_id": "com.duolingo"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `product_id` | string | Yes | Native Google Play product identifier, with 1 to 512 letters, digits, underscores, dots, or hyphens. |
| `gl` | string | No | Two-letter country code. |
| `hl` | string | No | Storefront language, such as en, de, or zh-TW. Maximum 32 characters. |
| `season_id` | string | No | Native season identifier, such as tvseason-OVPad1njPzI.P. Requires store=tv. |
| `store` | string | No | Product catalog containing this identifier. |
| `timeout` | number | No | Optional budget for the entire request in seconds, measured from gateway receipt until the response is ready to send. Includes admission, queueing and settlement. Must be greater t |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-play/product.json`](../../../catalog/models/google-play/product.json) · Store page: https://www.sandbase.ai/model/google-play/product

# DataForSEO Merchant Amazon ASIN

`dataforseo/v3/merchant/amazon/asin/live/advanced` · api · DataForSEO

Returns real-time Amazon product details for a single ASIN: title, brand, price, availability, rating and review count, images, bullet points, specifications, variants and buy-box seller.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/merchant/amazon/asin/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/merchant/amazon/asin/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/merchant/amazon/asin/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/merchant/amazon/asin/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/merchant/amazon/asin/live/advanced` with the body above minus `model`.

## Details

Retrieves live Amazon product details for one ASIN in a chosen marketplace location.

### Use cases

- Enrich a product catalogue with Amazon titles, images, specs and variants.
- Track price, availability and buy-box seller for specific ASINs.
- Pull rating and review counts for competitor products.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/merchant/amazon/asin/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"asin": "B0CP9YB3Q4", "location_code": 2840, "language_code": "en_US"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `asin` | Amazon product ASIN. |
| `location_code` | Location code, e.g. 2840 for the United States. |
| `language_code` | Language code, e.g. "en". |

### Pricing

Flat price per call. Failed calls are not charged.

### Related APIs

- [DataForSEO Merchant Amazon Products](/model/dataforseo/v3/merchant/amazon/products/live/advanced): Returns Amazon search results for a keyword with ratings, sellers and positions.
- [DataForSEO Merchant Amazon Sellers](/model/dataforseo/v3/merchant/amazon/sellers/live/advanced): Returns sellers and offers for an Amazon product.

---
Machine-readable: [`catalog/models/dataforseo/v3/merchant/amazon/asin/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/merchant/amazon/asin/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/merchant/amazon/asin/live/advanced

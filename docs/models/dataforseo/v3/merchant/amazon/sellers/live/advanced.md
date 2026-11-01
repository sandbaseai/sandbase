# DataForSEO Merchant Amazon Sellers

`dataforseo/v3/merchant/amazon/sellers/live/advanced` · api · DataForSEO

Retrieves real-time Amazon seller information and merchant data across e-commerce listings. Returns merchant profiles, ratings, and seller metrics for competitive analysis.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/merchant/amazon/sellers/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/merchant/amazon/sellers/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/merchant/amazon/sellers/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/merchant/amazon/sellers/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/merchant/amazon/sellers/live/advanced` with the body above minus `model`.

## Details

Access live Amazon seller data to inspect merchant details and listing status for specific products.

### Use cases

- Track competitor seller ratings and storefront performance on Amazon.
- Monitor multiple merchants competing for the Amazon Buy Box on target products.
- Audit seller profiles and fulfillment options across active listings.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/merchant/amazon/sellers/live/advanced" \
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

- [DataForSEO Backlinks Anchors](/model/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/model/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/model/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/merchant/amazon/sellers/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/merchant/amazon/sellers/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/merchant/amazon/sellers/live/advanced

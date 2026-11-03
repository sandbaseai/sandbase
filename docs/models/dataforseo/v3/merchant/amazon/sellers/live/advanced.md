# DataForSEO Merchant Amazon Sellers API: pricing, parameters and code examples

`dataforseo/v3/merchant/amazon/sellers/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0033 per call · **Modes:** sync

Retrieves real-time Amazon seller information and merchant data across e-commerce listings. Returns merchant profiles, ratings, and seller metrics for competitive analysis.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0033**

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

## Parameters

| name | type | required | description |
|---|---|---|---|
| `asin` | string |  | Amazon product ASIN.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

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

Billed at the actual cost of each call, about $0.0033 for the request above. The cost grows with the number of rows, targets or pages a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/merchant/amazon/sellers/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/merchant/amazon/sellers/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/merchant/amazon/sellers/live/advanced

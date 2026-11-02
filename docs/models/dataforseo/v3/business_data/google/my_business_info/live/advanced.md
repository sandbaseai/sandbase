# DataForSEO Google Business Listing Info API: pricing, parameters and code examples

`dataforseo/v3/business_data/google/my_business_info/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.0054 per call · **Modes:** sync

Returns comprehensive Google Business Profile data, including local listing details, customer reviews, ratings, and business attributes for targeted locations.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.0054**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/business_data/google/my_business_info/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/business_data/google/my_business_info/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/business_data/google/my_business_info/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/business_data/google/my_business_info/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/business_data/google/my_business_info/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Retrieves Google Business Profile listing data directly from Google local results. Call this endpoint to inspect localized merchant profiles and business attributes.

### Use cases

- Audit local Google Business Profile listings across target geographic locations.
- Extract business hours, addresses, contact details, and category classifications.
- Monitor local merchant profile attributes and customer rating metrics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/business_data/google/my_business_info/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "The Metropolitan Museum of Art", "location_code": 2840, "language_code": "en"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `keyword` | Search query. |
| `location_code` | Location code, e.g. 2840 for the United States. |
| `language_code` | Language code, e.g. "en". |

### Pricing

Billed at the actual cost of each call, about $0.0054 for the request above. The cost grows with the number of rows, targets or pages a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

### Related APIs

- [DataForSEO Backlinks Anchors](/model/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/model/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/model/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/business_data/google/my_business_info/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/business_data/google/my_business_info/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/business_data/google/my_business_info/live/advanced

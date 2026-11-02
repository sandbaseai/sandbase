# DataForSEO Google Hotel Search Advanced API: pricing, parameters and code examples

`dataforseo/v3/business_data/google/hotel_searches/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.004 per call · **Modes:** sync

Returns detailed Google Hotel search results and business data for target locations. Provides hotel listings, guest ratings, and business attributes directly from Google.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.004**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/business_data/google/hotel_searches/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/business_data/google/hotel_searches/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/business_data/google/hotel_searches/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/business_data/google/hotel_searches/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/business_data/google/hotel_searches/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |

## Details

Retrieves real-time Google Hotel search results and hotel metadata using query criteria.

### Use cases

- Retrieve live Google Hotel listings for target travel destinations.
- Inspect hotel business attributes, amenities, and guest ratings.
- Monitor competitor hotel visibility in Google search results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/business_data/google/hotel_searches/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "hotels in new york", "location_code": 2840, "language_code": "en"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `keyword` | Search query. |
| `location_code` | Location code, e.g. 2840 for the United States. |
| `language_code` | Language code, e.g. "en". |

### Pricing

Billed at the actual cost of each call, about $0.004 for the request above. The cost grows with the number of rows, targets or pages a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

### Related APIs

- [DataForSEO Backlinks Anchors](/model/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/model/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/model/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/business_data/google/hotel_searches/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/business_data/google/hotel_searches/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/business_data/google/hotel_searches/live/advanced

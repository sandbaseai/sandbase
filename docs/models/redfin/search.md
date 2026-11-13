# Redfin Search API: pricing, parameters and code examples

`redfin/search` · data API · Redfin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call · **Modes:** async

Search Redfin home listings by region, map bounds or search URL with price, beds, baths, size, status and property type filters, returning address, price and listing details.

## Pricing

- **$0.00015 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "redfin/search"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('redfin/search', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("redfin/search", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "redfin/search", sandbase.Params{})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/redfin/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `url` | string |  | Redfin city, ZIP, county or neighborhood search URL. Existing URL filters are retained unless overridden. Supply one location: a region URL, region_id with region_type, or map_bounds.  |
| `sort` | string |  | Result ordering. Defaults to recommended when no URL is supplied. one of: `newest`, `price_asc`, `price_desc`, `recommended`, `sqft` |
| `limit` | integer |  | Maximum listings returned. Narrow the region or map bounds when results reach this limit. The response does not advertise pagination or a total count. If search_information.possibly_truncated is true, narrow the… range 1–350 |
| `status` | string |  | Listing status. Defaults to for_sale when no URL is supplied. one of: `for_sale`, `sold` |
| `timeout` | number |  | Seconds the data source may spend before giving up (max 50, default 50). A timed-out call is not billed. default `50`; range –50 |
| `max_beds` | integer |  | Maximum number of bedrooms. range 0–20 |
| `max_sqft` | integer |  | Maximum interior area in square feet. range 0–9007199254740991 |
| `min_beds` | integer |  | Minimum number of bedrooms. range 0–20 |
| `min_sqft` | integer |  | Minimum interior area in square feet. range 0–9007199254740991 |
| `max_price` | integer |  | Maximum listing price in US dollars. range 0–9007199254740991 |
| `min_baths` | number |  | Minimum number of bathrooms. range 0–20 |
| `min_price` | integer |  | Minimum listing price in US dollars. range 0–9007199254740991 |
| `region_id` | integer |  | Redfin region identifier; requires region_type. range -9007199254740991–9007199254740991 |
| `map_bounds` | string |  | Map rectangle as north,east,south,west.  |
| `region_type` |  |  | Region kind: 1 neighborhood, 2 ZIP region, 5 county, 6 city, 11 state. A ZIP region identifier differs from the ZIP code. Use a Redfin ZIP search URL if the region identifier is unknown.  |
| `property_type` | string |  | Restrict results to one property type. one of: `co_op`, `condo`, `house`, `land`, `manufactured`, `multi_family`, `other`, `townhouse` |
| `sold_within_days` | integer |  | Sold listings from the last N days; requires status=sold. Defaults to 180 for sold searches. range 1–365 |

## Details

Search Redfin home listings by region, map bounds or search URL with price, beds, baths, size, status and property type filters, returning address, price and listing details.

---
Machine-readable: [`catalog/models/redfin/search.json`](../../../catalog/models/redfin/search.json) · Store page: https://www.sandbase.ai/model/redfin/search

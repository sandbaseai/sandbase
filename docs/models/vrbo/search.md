# Vrbo Search API: pricing, parameters and code examples

`vrbo/search` · data API · Vrbo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

Search Vrbo vacation rentals by destination and dates, with guest, bedroom, bed, bathroom and price filters, and get up to 50 listings per call: Vrbo property ID and link, name, summary line, property type, bedrooms, beds, guest rating and review count, nightly and total stay price with the original nightly price before any discount, and photos as normalized JSON. Page with offset; the price is the same whatever the limit.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "vrbo/search", "location": "Lake Tahoe", "checkIn": "2026-12-13", "checkOut": "2026-12-16"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('vrbo/search', {'location': 'Lake Tahoe', 'checkIn': '2026-12-13', 'checkOut': '2026-12-16'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("vrbo/search", {
  "location": "Lake Tahoe",
  "checkIn": "2026-12-13",
  "checkOut": "2026-12-16"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "vrbo/search", sandbase.Params{
	"location": "Lake Tahoe",
	"checkIn": "2026-12-13",
	"checkOut": "2026-12-16",
})
```

Same call via the path form: `POST /v1/api/vrbo/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `sort` | string |  | Result order: recommended (Vrbo's default), price_low_to_high, price_high_to_low, review (highest rated first) or review_count (most reviewed first). one of: `recommended`, `price_low_to_high`, `price_high_to_low`, `review`, `review_count` |
| `limit` | integer |  | Maximum number of listings to return (1-50, default 20). The price is the same whatever the limit. default `20`; range 1–50 |
| `adults` | integer |  | Number of adult guests (e.g. 2). range 1–20 |
| `offset` | integer |  | Number of listings to skip, for paging: send offset 20 with limit 20 for the second page. default `0`; range 0–1000 |
| `checkIn` | string | yes | Check-in date in YYYY-MM-DD format (e.g. 2027-01-15). Today or later.  |
| `minBeds` | integer |  | Minimum number of beds (e.g. 4). range 1–20 |
| `checkOut` | string | yes | Check-out date in YYYY-MM-DD format (e.g. 2027-01-18). After the check-in date.  |
| `location` | string | yes | Destination to search rentals in: a city, region or area (e.g. Lake Tahoe, Lisbon, Outer Banks, North Carolina).  |
| `priceMax` | integer |  | Maximum price in the currency results are priced in (each listing's currency), per night or for the whole stay as priceType says (e.g. 400). With a price filter, only listings Vrbo prices for your dates are returned. range 1–1000000 |
| `priceMin` | integer |  | Minimum price in the currency results are priced in (each listing's currency), per night or for the whole stay as priceType says (e.g. 100). range 0–1000000 |
| `priceType` | string |  | Whether priceMin and priceMax are a nightly price (default) or the total for the stay. one of: `nightly`, `total`; default `"nightly"` |
| `minBedrooms` | integer |  | Minimum number of bedrooms (e.g. 3). range 0–50 |
| `childrenAges` | array |  | Age of each child guest, one entry per child (e.g. [5, 8] for two children aged 5 and 8). Omit it when no children are staying.  |
| `minBathrooms` | integer |  | Minimum number of bathrooms (e.g. 2). range 1–50 |

## Details

Search Vrbo vacation rentals by destination and dates, with guest, bedroom, bed, bathroom and price filters, and get up to 50 listings per call: Vrbo property ID and link, name, summary line, property type, bedrooms, beds, guest rating and review count, nightly and total stay price with the original nightly price before any discount, and photos as normalized JSON. Page with offset; the price is the same whatever the limit.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "vrbo/search", "limit": 5, "adults": 2, "checkIn": "2026-12-13", "checkOut": "2026-12-16", "location": "Lake Tahoe"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `checkIn` | string | Yes | Check-in date in YYYY-MM-DD format (e.g. 2027-01-15). Today or later. |
| `checkOut` | string | Yes | Check-out date in YYYY-MM-DD format (e.g. 2027-01-18). After the check-in date. |
| `location` | string | Yes | Destination to search rentals in: a city, region or area (e.g. Lake Tahoe, Lisbon, Outer Banks, North Carolina). |
| `adults` | integer | No | Number of adult guests (e.g. 2). |
| `childrenAges` | array | No | Age of each child guest, one entry per child (e.g. [5, 8] for two children aged 5 and 8). Omit it when no children are staying. |
| `limit` | integer | No | Maximum number of listings to return (1-50, default 20). The price is the same whatever the limit. |
| `minBathrooms` | integer | No | Minimum number of bathrooms (e.g. 2). |
| `minBedrooms` | integer | No | Minimum number of bedrooms (e.g. 3). |
| `minBeds` | integer | No | Minimum number of beds (e.g. 4). |
| `offset` | integer | No | Number of listings to skip, for paging: send offset 20 with limit 20 for the second page. Default `0`. |
| `priceMax` | integer | No | Maximum price in the currency results are priced in (each listing's currency), per night or for the whole stay as priceType says (e.g. 400). With a price filter, only listings Vrbo prices for your dates are returned. |
| `priceMin` | integer | No | Minimum price in the currency results are priced in (each listing's currency), per night or for the whole stay as priceType says (e.g. 100). |
| `priceType` | string | No | Whether priceMin and priceMax are a nightly price (default) or the total for the stay. One of: `nightly`, `total`. |
| `sort` | string | No | Result order: recommended (Vrbo's default), price_low_to_high, price_high_to_low, review (highest rated first) or review_count (most reviewed first). One of: `recommended`, `price_low_to_high`, `price_high_to_low`, `revi |

### Pricing

Billed at the actual cost of each call, about $0.00085 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/vrbo/search.json`](../../../catalog/models/vrbo/search.json) · Store page: https://www.sandbase.ai/model/vrbo/search

# Vrbo Listing API: pricing, parameters and code examples

`vrbo/listing` · data API · Vrbo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.00085 per call · **Modes:** sync

Get one Vrbo vacation rental by its property ID: name, link, address, coordinates, bedrooms, bathrooms, beds and guest capacity, guest rating with category scores and review count, amenities by group, full description, house rules, important information, availability and price for your dates (total and average per night, fees included), every photo with its caption and the latest guest reviews, as normalized JSON. Takes the id vrbo.search returns.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.00085**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "vrbo/listing", "propertyId": "69764328"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('vrbo/listing', {'propertyId': '69764328'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("vrbo/listing", {
  "propertyId": "69764328"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "vrbo/listing", sandbase.Params{
	"propertyId": "69764328",
})
```

Same call via the path form: `POST /v1/api/vrbo/listing` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `adults` | integer |  | Number of adult guests to price for (1-20, default 2). default `2`; range 1–20 |
| `checkIn` | string |  | Check-in date to price and check availability for, in YYYY-MM-DD format (e.g. 2027-01-15). Today or later. Without dates, a 3-night stay about a month ahead is priced; the dates used are in stay.  |
| `checkOut` | string |  | Check-out date in YYYY-MM-DD format (e.g. 2027-01-18). After the check-in date. With a check-in date alone, the stay is 3 nights.  |
| `propertyId` | string | yes | Vrbo property ID: the id vrbo.search returns for a listing (e.g. 69764328).  |
| `childrenAges` | array |  | Age of each child guest, one entry per child (e.g. [5, 8] for two children aged 5 and 8). Omit it when no children are staying.  |

## Details

Get one Vrbo vacation rental by its property ID: name, link, address, coordinates, bedrooms, bathrooms, beds and guest capacity, guest rating with category scores and review count, amenities by group, full description, house rules, important information, availability and price for your dates (total and average per night, fees included), every photo with its caption and the latest guest reviews, as normalized JSON. Takes the id vrbo.search returns.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/run" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "vrbo/listing", "adults": 2, "checkIn": "2026-12-13", "checkOut": "2026-12-16", "propertyId": "69764328"}'
```

The result is returned in `outputs[0].data`. Lookups that find nothing fail with a not-found error.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `propertyId` | string | Yes | Vrbo property ID: the id vrbo.search returns for a listing (e.g. 69764328). |
| `adults` | integer | No | Number of adult guests to price for (1-20, default 2). |
| `checkIn` | string | No | Check-in date to price and check availability for, in YYYY-MM-DD format (e.g. 2027-01-15). Today or later. Without dates, a 3-night stay about a month ahead is priced; the dates used are in stay. |
| `checkOut` | string | No | Check-out date in YYYY-MM-DD format (e.g. 2027-01-18). After the check-in date. With a check-in date alone, the stay is 3 nights. |
| `childrenAges` | array | No | Age of each child guest, one entry per child (e.g. [5, 8] for two children aged 5 and 8). Omit it when no children are staying. |

### Pricing

Billed at the actual cost of each call, about $0.00085 per request. A call can cost more when the first data source fails and another one answers. Failed calls and lookups that find nothing are not charged.

---
Machine-readable: [`catalog/models/vrbo/listing.json`](../../../catalog/models/vrbo/listing.json) · Store page: https://www.sandbase.ai/model/vrbo/listing

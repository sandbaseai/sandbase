# Booking.com Search API: pricing, parameters and code examples

`booking/search` · data API · Booking.com · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Search Booking.com properties by destination and dates, with property name, price, rating, review score, address and photos.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "booking/search", "q": "Austin"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('booking/search', {'q': 'Austin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("booking/search", {
  "q": "Austin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "booking/search", sandbase.Params{
	"q": "Austin",
})
```

Same call via the path form: `POST /v1/api/booking/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Parameter defines the destination to search for: a city, a region, a district, a landmark, or an airport (e.g., `Paris`, `Tuscany`, `Manhattan`, or `Eiffel Tower`). Booking.com doesn't return results for most street…  |
| `hl` | string |  | Parameter defines the language to use for the Booking.com search (e.g., `en-us` (default) for English (US), `fr` for French, or `pt-br` for Portuguese (Brazil)). Head to the Booking.com languages page for a full list…  |
| `nflt` | string |  | Parameter defines any other Booking.com filters, like amenities, meals, districts, brands, or distance from the center. It's the value of the `nflt` parameter of Booking.com search URLs: a semicolon-separated list of…  |
| `limit` | string |  | Parameter defines the maximum number of results to return, from `1` to `100`. It defaults to `25`, like on Booking.com. Booking.com sometimes returns a few more properties: sponsored ones, or the searched property.  |
| `rooms` | string |  | Parameter defines the number of rooms, from `1` (default) to `30`. It can't be greater than the number of `adults`.  |
| `adults` | string |  | Parameter defines the number of adults, from `1` to `30`. It defaults to `2`.  |
| `device` | string |  | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser.  |
| `offset` | string |  | Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `0` (default) is the first page of results, `25` is the 2nd page of results with the default `limit`, etc.).…  |
| `rating` | string |  | Parameter defines the minimum review score of the properties. Available options: `9` - Wonderful: 9+ `8` - Very Good: 8+ `7` - Good: 7+ `6` - Pleasant: 6+  |
| `sort_by` | string |  | Parameter defines the sorting of the results. It defaults to `popularity` (Our top picks). Available options: `popularity` - Our top picks `upsort_bh` - Homes & apartments first `price` - Price (lowest first)…  |
| `children` | string |  | Parameter defines the number of children, from `0` (default) to `10`. Their ages must be set with `children_ages`.  |
| `currency` | string |  | Parameter defines the currency of the returned prices. It defaults to `hotel_currency`, the currency of each property (e.g., `EUR` in Paris), returned in `currency` of each property. Head to the Booking.com currencies…  |
| `max_price` | string |  | Parameter defines the maximum price per night, in the currency of the results (e.g., `300`). It must be used together with a `currency` code.  |
| `min_price` | string |  | Parameter defines the minimum price per night, in the currency of the results (e.g., `100`). It must be used together with a `currency` code.  |
| `flex_window` | string |  | Parameter defines how many days the check-in and check-out dates can move, earlier or later, for the best price of each property. Each property then has the dates of its price in `check_in_date` and `check_out_date`.…  |
| `hotel_class` | string |  | Parameter defines the property ratings to show: stars for hotels, or Booking.com's own rating for homes and apartments. It's a comma-separated list of ratings from `1` to `5` (e.g., `4,5` for 4 and 5-star properties).  |
| `check_in_date` | string |  | Parameter defines the check-in date. The format is **YYYY-MM-DD** (e.g., `2026-12-12`). It must be used together with `check_out_date`. When dates aren't set, Booking.com returns properties without prices.  |
| `children_ages` | string |  | Parameter defines the age of each child at check-out, from `0` to `17`. It's a comma-separated list of ages (e.g., `5` for one child, or `5,9` for two children). When `children` isn't set, it's the number of ages.  |
| `session_token` | string |  | Parameter defines the token that keeps the same Booking.com visitor between searches. Booking.com ranks properties differently for each visitor, so without it, the next pages can repeat properties of the previous ones.…  |
| `check_out_date` | string |  | Parameter defines the check-out date. The format is **YYYY-MM-DD** (e.g., `2026-12-15`). It must be used together with `check_in_date`, and be up to 90 nights later than it.  |
| `property_types` | string |  | Parameter defines the property types to show. It's a comma-separated list of property type IDs (e.g., `204` for hotels, or `201,220` for apartments and vacation homes). Head to the Booking.com property types page for a…  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `free_cancellation` | string |  | Parameter defines whether to only show properties with free cancellation. It can be set to `true` or `false` (default).  |

## Details

Search Booking.com properties by destination and dates, with property name, price, rating, review score, address and photos.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/booking/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "Austin"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Parameter defines the destination to search for: a city, a region, a district, a landmark, or an airport (e.g., `Paris`, `Tuscany`, `Manhattan`, or `Eiffel Tower`). Booking.com doesn't return results for most street addresses. |
| `hl` | string | No | Parameter defines the language to use for the Booking.com search (e.g., `en-us` (default) for English (US), `fr` for French, or `pt-br` for Portuguese (Brazil)). Head to the Booking.com languages page for a full list of supported languages. |
| `currency` | string | No | Parameter defines the currency of the returned prices. It defaults to `hotel_currency`, the currency of each property (e.g., `EUR` in Paris), returned in `currency` of each property. Head to the Booking.com currencies page for a full list o |
| `check_in_date` | string | No | Parameter defines the check-in date. The format is **YYYY-MM-DD** (e.g., `2026-12-12`). It must be used together with `check_out_date`. When dates aren't set, Booking.com returns properties without prices. |
| `check_out_date` | string | No | Parameter defines the check-out date. The format is **YYYY-MM-DD** (e.g., `2026-12-15`). It must be used together with `check_in_date`, and be up to 90 nights later than it. |
| `flex_window` | string | No | Parameter defines how many days the check-in and check-out dates can move, earlier or later, for the best price of each property. Each property then has the dates of its price in `check_in_date` and `check_out_date`. It must be used togethe |
| `adults` | string | No | Parameter defines the number of adults, from `1` to `30`. It defaults to `2`. |
| `children` | string | No | Parameter defines the number of children, from `0` (default) to `10`. Their ages must be set with `children_ages`. |
| `children_ages` | string | No | Parameter defines the age of each child at check-out, from `0` to `17`. It's a comma-separated list of ages (e.g., `5` for one child, or `5,9` for two children). When `children` isn't set, it's the number of ages. |
| `rooms` | string | No | Parameter defines the number of rooms, from `1` (default) to `30`. It can't be greater than the number of `adults`. |
| `sort_by` | string | No | Parameter defines the sorting of the results. It defaults to `popularity` (Our top picks). Available options: `popularity` - Our top picks `upsort_bh` - Homes & apartments first `price` - Price (lowest first) `price_from_high_to_low` - Pric |
| `min_price` | string | No | Parameter defines the minimum price per night, in the currency of the results (e.g., `100`). It must be used together with a `currency` code. |
| `max_price` | string | No | Parameter defines the maximum price per night, in the currency of the results (e.g., `300`). It must be used together with a `currency` code. |
| `hotel_class` | string | No | Parameter defines the property ratings to show: stars for hotels, or Booking.com's own rating for homes and apartments. It's a comma-separated list of ratings from `1` to `5` (e.g., `4,5` for 4 and 5-star properties). |
| `rating` | string | No | Parameter defines the minimum review score of the properties. Available options: `9` - Wonderful: 9+ `8` - Very Good: 8+ `7` - Good: 7+ `6` - Pleasant: 6+ |
| `free_cancellation` | string | No | Parameter defines whether to only show properties with free cancellation. It can be set to `true` or `false` (default). |
| `property_types` | string | No | Parameter defines the property types to show. It's a comma-separated list of property type IDs (e.g., `204` for hotels, or `201,220` for apartments and vacation homes). Head to the Booking.com property types page for a full list of supporte |
| `nflt` | string | No | Parameter defines any other Booking.com filters, like amenities, meals, districts, brands, or distance from the center. It's the value of the `nflt` parameter of Booking.com search URLs: a semicolon-separated list of filters (e.g., `hotelfa |
| `offset` | string | No | Parameter defines the result offset. It skips the given number of results. It's used for pagination. (e.g., `0` (default) is the first page of results, `25` is the 2nd page of results with the default `limit`, etc.). It can be up to `1000`: |
| `limit` | string | No | Parameter defines the maximum number of results to return, from `1` to `100`. It defaults to `25`, like on Booking.com. Booking.com sometimes returns a few more properties: sponsored ones, or the searched property. |
| `session_token` | string | No | Parameter defines the token that keeps the same Booking.com visitor between searches. Booking.com ranks properties differently for each visitor, so without it, the next pages can repeat properties of the previous ones. It's returned in `the |
| `device` | string | No | Parameter defines the device to use to get the results. It can be set to `desktop` (default) to use a regular browser, `tablet` to use a tablet browser (currently using iPads), or `mobile` to use a mobile browser. |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/booking/search.json`](../../../catalog/models/booking/search.json) · Store page: https://www.sandbase.ai/model/booking/search

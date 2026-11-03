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

Returns a list of hotels that Google Hotels shows for a search query in a given location and language. Each hotel has a title, star class, coordinates, a nightly price and a guest rating. You send a `keyword`, a `location_code` and a `language_code`.

### Use cases

- Build a price list of hotels in a city for one check-in date.
- Find hotels with a discount label such as "17% less than usual".
- Map hotel locations with their `latitude` and `longitude` and compare ratings by area.
- Rank hotels in a destination by guest rating and review count.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/business_data/google/hotel_searches/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "hotels in new york", "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search query. |
| `language_code` | string | No | Language code, e.g. "en". |
| `location_code` | integer | No | Location code, e.g. 2840 for the United States. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "status_code": 20000,
  "status_message": "Ok.",
  "tasks": [
    {
      "data": {
        "api": "business_data",
        "device": "desktop",
        "function": "hotel_searches",
        "keyword": "hotels in new york",
        "language_code": "en",
        "location_code": 2840,
        "os": "windows",
        "se": "google"
      },
      "id": "11030828-2190-0293-0000-c13ead85f48b",
      "path": [
        "v3"
      ],
      "result": [
        {
          "check_url": "https://www.google.com/travel/search?q=hotels+in+new+york%2c+United+States&hl=en…",
          "datetime": "2026-11-03 08:28:51 +00:00",
          "items": [
            {
              "hotel_identifier": "ChoImOTyzeuCzrykARoNL2cvMTF2cGw0bnIzYhAB",
              "is_paid": false,
              "location": {
                "latitude": 40.7835127,
                "longitude": -73.8408876
              },
              "overview_images": [
                "https://lh3.googleusercontent.com/grass-cs/AABkmLf8BlMpA-fjlDIOeCxbGUyJzy_nQ51AE…"
              ],
              "prices": {
                "check_in": "2026-11-04 00:00:00 +00:00",
                "check_out": "2026-11-05 00:00:00 +00:00",
                "currency": "USD",
                "discount_text": "17% less than usual",
                "items": null,
                "price": 125,
                "price_without_discount": null,
                "prices_by_dates": null
              },
              "reviews": {
                "mentions": null,
                "other_sites_reviews": null,
                "rating_distribution": null,
                "value": 4.3,
                "votes_count": 615
              },
              "stars": 2,
              "title": "LY New York Hotel"
            }
          ],
          "items_count": 18,
          "keyword": "hotels in new york, United States",
          "language_code": "en",
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "5.0342 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "5.0432 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].items[].title` | Hotel name as shown in Google Hotels. |
| `tasks[].result[].items[].hotel_identifier` | Google's ID for the hotel. Use it to look up one hotel in detail. |
| `tasks[].result[].items[].stars` | Star class of the hotel. |
| `tasks[].result[].items[].prices.price / tasks[].result[].items[].prices.currency` | Listed price for the stay and its currency code, such as `USD`. |
| `tasks[].result[].items[].prices.check_in / tasks[].result[].items[].prices.check_out` | Dates the price applies to. They use the format `YYYY-MM-DD HH:MM:SS +00:00`. |
| `tasks[].result[].items[].prices.discount_text` | Discount label such as "17% less than usual". It is `null` when Google shows none. |
| `tasks[].result[].items[].reviews.value / tasks[].result[].items[].reviews.votes_count` | Average guest rating and the number of ratings behind it. |
| `tasks[].result[].items[].location.latitude / tasks[].result[].items[].location.longitude` | Coordinates of the hotel. |
| `tasks[].result[].items[].overview_images[]` | URLs of hotel photos. |
| `tasks[].result[].items_count` | Number of hotels in the result. |

### Notes

- Set `location_code` from the DataForSEO location list. The example uses `2840` for the United States.
- The response echoes the search as `keyword` with the country added, for example `hotels in new york, United States`. `check_url` links to the matching Google Hotels page.
- Fields such as `prices.items`, `prices.prices_by_dates` and `reviews.rating_distribution` were `null` in this response.
- To get more detail on one hotel, pass its `hotel_identifier` to [DataForSEO Google Hotel Details](/apis/dataforseo/v3/business_data/google/hotel_info/live/advanced).

### Pricing

Billed at the actual cost of each call, about $0.004 for the request above. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/apis/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/apis/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/apis/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/business_data/google/hotel_searches/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/business_data/google/hotel_searches/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/business_data/google/hotel_searches/live/advanced

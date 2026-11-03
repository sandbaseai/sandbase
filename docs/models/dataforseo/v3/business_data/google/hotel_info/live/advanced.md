# DataForSEO Google Hotel Details API: pricing, parameters and code examples

`dataforseo/v3/business_data/google/hotel_info/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.004 per call (free daily quota) · **Modes:** sync

Fetch a Google Hotels page: rates by provider, amenities, reviews. Google Hotels details for a hotel_identifier.

## Pricing

- **$0.004 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/business_data/google/hotel_info/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/business_data/google/hotel_info/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/business_data/google/hotel_info/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/business_data/google/hotel_info/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/business_data/google/hotel_info/live/advanced` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `language_code` | string |  | Language code, e.g. "en".  |
| `location_code` | integer |  | Location code, e.g. 2840 for the United States.  |
| `hotel_identifier` | string |  | Google hotel identifier from hotel search results.  |

## Details

Returns the Google Hotels details page for one hotel: address, description, amenities, check-in and check-out times, and location data. It needs a `hotel_identifier` from hotel search results, plus a `location_code` and `language_code`.

### Use cases

- Build a hotel profile with address, description and map coordinates for a travel site.
- Compare amenities such as free Wi-Fi, pool and restaurant across competing hotels.
- Show check-in and check-out times in a booking or itinerary tool.
- Find the Google Hotels page URL for a property and open it for a rate check.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/business_data/google/hotel_info/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"hotel_identifier": "ChYIq6SB--i6p6cpGgovbS8wN2s5ODZfEAE", "location_code": 2840, "language_code": "en"}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `hotel_identifier` | string | No | Google hotel identifier from hotel search results. |
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
        "function": "hotel_info",
        "hotel_identifier": "ChYIq6SB--i6p6cpGgovbS8wN2s5ODZfEAE",
        "language_code": "en",
        "location_code": 2840,
        "os": "windows",
        "se": "google"
      },
      "id": "11030828-2190-0285-0000-3fdb3f54e6b9",
      "path": [
        "v3"
      ],
      "result": [
        {
          "about": {
            "amenities": [
              {
                "category": "internet",
                "category_label": "Internet",
                "items": [
                  {
                    "amenity": "wifi",
                    "amenity_label": "Wi-Fi",
                    "hint": "free",
                    "hint_label": "Free",
                    "is_available": true
                  }
                ]
              }
            ],
            "check_in_time": {
              "hour": 15,
              "minute": 0
            },
            "check_out_time": {
              "hour": 11,
              "minute": 0
            },
            "description": "Sophisticated quarters in an upmarket hotel offering an elegant restaurant, an o…",
            "domain": "president.gr",
            "full_address": "President Hotel Athens, Leof. Kifisias 43, Athina 115 23, Greece",
            "popular_amenities": [
              {
                "amenity": "pool",
                "amenity_label": "Pool",
                "hint": null,
                "hint_label": null,
                "is_available": true
              }
            ],
            "sub_descriptions": [
              "An 8-minute walk from a metro stop, this upscale hotel is 5 km from the Temple o…"
            ]
          },
          "address": "Leof. Kifisias 43, Athina 115 23, Greece",
          "check_url": "https://www.google.com/travel/hotels/entity/ChYIq6SB--i6p6cpGgovbS8wN2s5ODZfEAE?…",
          "datetime": "2026-11-03 08:28:58 +00:00",
          "hotel_identifier": "ChYIq6SB--i6p6cpGgovbS8wN2s5ODZfEAE",
          "language_code": "en",
          "location": {
            "latitude": 37.989081399999996,
            "location_chain": [
              {
                "card_id": "/m/0b76ryf",
                "cid": "10046976553708580665",
                "feature_id": "0x14a1c7bf3d8ca3e3:0x8b6e07f1c67a6f39",
                "title": "Decentralized Administration of Attica"
              }
            ],
            "longitude": 23.7638777,
            "maps_url": "https://maps.google.com/maps?hl=en&gl=US&um=1&ie=UTF-8&fb=1&sa=X&ll=37.9890814,2…",
            "neighborhood": "Central Athens Regional Unit",
            "neighborhood_description": "Busy Central Athens is known for classical landmarks, including the Temple of Ol…",
            "overall_score": null,
            "score_by_categories": {
              "airport_access": 0,
              "overall": 0,
              "restaurants": 0,
              "things_to_do": 0,
              "transit": 0
            }
          },
          "location_code": 2840
        }
      ],
      "result_count": 1,
      "status_code": 20000,
      "status_message": "Ok.",
      "time": "3.0197 sec."
    }
  ],
  "tasks_count": 1,
  "tasks_error": 0,
  "time": "3.0296 sec.",
  "version": "0.1.20261022"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `tasks[].result[].about.description` | Short text description of the hotel. |
| `tasks[].result[].about.sub_descriptions[]` | Longer description paragraphs covering distance to landmarks, rooms and on-site facilities. |
| `tasks[].result[].about.full_address / tasks[].result[].address` | Street address of the hotel. `full_address` includes the hotel name. |
| `tasks[].result[].about.check_in_time / tasks[].result[].about.check_out_time` | Check-in and check-out times as `hour` and `minute`. |
| `tasks[].result[].about.popular_amenities[]` | Main amenities Google highlights. Each row has `amenity_label`, an optional `hint_label` such as Free, and `is_available`. |
| `tasks[].result[].about.amenities[].items[]` | Full amenity list grouped by `category_label`, such as Internet or Food & drink. Each item has `amenity`, `hint` and `is_available`. |
| `tasks[].result[].about.domain` | Website domain of the hotel. |
| `tasks[].result[].location.latitude / tasks[].result[].location.longitude` | Coordinates of the hotel. |
| `tasks[].result[].location.location_chain[].title` | Place names from the wider region down to the city, for example Attica and Athens. |
| `tasks[].result[].check_url` | Google Hotels URL for this hotel in the requested language and location. |

### Notes

- Get `hotel_identifier` from hotel search results, for example from [DataForSEO Google Hotel Search Advanced](/apis/dataforseo/v3/business_data/google/hotel_searches/live/advanced).
- `datetime` uses the format `2026-11-03 08:28:58 +00:00`.
- `location.score_by_categories` values and `location.overall_score` can be `0` or `null` when no score is present, so check them before use.
- The `hint` field on amenities is `null` when there is no extra detail.

### Pricing

$0.004 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/dataforseo/v3/business_data/google/hotel_info/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/business_data/google/hotel_info/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/business_data/google/hotel_info/live/advanced

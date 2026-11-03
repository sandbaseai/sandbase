# Google Hotels Search API: pricing, parameters and code examples

`google-hotels/search` · data API · Google Hotels · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Google Hotels results for a destination and stay dates: hotels, nightly rates, ratings, amenities and offers.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-hotels/search", "q": "Bali Resorts", "check_in_date": "2026-12-15", "check_out_date": "2026-12-16", "adults": 2}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-hotels/search', {'q': 'Bali Resorts', 'check_in_date': '2026-12-15', 'check_out_date': '2026-12-16', 'adults': 2})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-hotels/search", {
  "q": "Bali Resorts",
  "check_in_date": "2026-12-15",
  "check_out_date": "2026-12-16",
  "adults": 2
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-hotels/search", sandbase.Params{
	"q": "Bali Resorts",
	"check_in_date": "2026-12-15",
	"check_out_date": "2026-12-16",
	"adults": 2,
})
```

Same call via the path form: `POST /v1/api/google-hotels/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | q  |
| `adults` | integer | yes | adults  |
| `check_in_date` | string | yes | YYYY-MM-DD  |
| `check_out_date` | string | yes | YYYY-MM-DD  |

## Details

Returns Google Hotels results for a search phrase and stay dates. Send a destination or query in `q`, the `check_in_date` and `check_out_date`, and the number of `adults`. The response lists matching hotels with nightly rates, ratings, amenities and review data, plus a list of sponsored offers.

### Use cases

- Compare nightly rates for resorts in one destination on a given pair of dates.
- Build a shortlist of top-rated 5-star hotels near an airport or beach using ratings and nearby places.
- Track deals by reading the `deal` and `deal_description` fields for properties priced below their usual rate.
- Map hotel locations from `gps_coordinates` to show options on a travel planning page.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-hotels/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "Bali Resorts", "check_in_date": "2026-12-15", "check_out_date": "2026-12-16", "adults": 2}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `adults` | integer | Yes | adults |
| `check_in_date` | string | Yes | YYYY-MM-DD |
| `check_out_date` | string | Yes | YYYY-MM-DD |
| `q` | string | Yes | q |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "ads": [
    {
      "amenities": [
        "Hot tub"
      ],
      "extracted_price": 31,
      "gps_coordinates": {
        "latitude": -8.545097,
        "longitude": 115.48575900000002
      },
      "link": "https://www.google.com/aclk?sa=l&ai=DChsSEwi48L3VpOuXAxUtakcBHU6xNy0YACICCAEQERo…",
      "name": "Bhalance Hotel Retreat",
      "overall_rating": 4.7,
      "price": "$31",
      "property_token": "CgsI1eid…",
      "reviews": 167,
      "source": "Booking.com",
      "source_icon": "https://www.gstatic.com/travel-hotels/branding/icon_184.png",
      "thumbnail": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTvjG2IR0PzonYXe8V7wELVznFu…"
    }
  ],
  "brands": [
    {
      "children": [
        {
          "id": 67,
          "name": "Banyan Tree"
        }
      ],
      "id": 33,
      "name": "Accor Live Limitless"
    }
  ],
  "properties": [
    {
      "amenities": [
        "Breakfast"
      ],
      "check_in_time": "3:00 PM",
      "check_out_time": "12:00 PM",
      "deal": "46% less than usual",
      "deal_description": "Great Deal",
      "description": "Upscale oceanfront retreat with elegant rooms, suites & villas, plus 9 restauran…",
      "extracted_hotel_class": 5,
      "gps_coordinates": {
        "latitude": -8.786196799999999,
        "longitude": 115.1392512
      },
      "hotel_class": "5-star hotel",
      "images": [
        {
          "original_image": "https://lh3.googleusercontent.com/grass-cs/AABkmLc314DkNzZrU8uGbTczw8WfncDhg6d2S…",
          "thumbnail": "https://lh3.googleusercontent.com/grass-cs/AABkmLc314DkNzZrU8uGbTczw8WfncDhg6d2S…"
        }
      ],
      "link": "https://www.ayana.com/",
      "location_rating": 4.1
    }
  ],
  "search_information": {
    "total_results": 15000
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `properties[].name` | Name of the hotel or resort. |
| `properties[].overall_rating / properties[].reviews` | Average guest rating and the total number of reviews for the property. |
| `properties[].rate_per_night.extracted_display_price / properties[].rate_per_night.extracted_lowest` | Nightly price as a number. The first is the displayed price before taxes and fees. The second is the lowest figure, which matches the `after_taxes_fees` value in the sample. |
| `properties[].total_rate` | Same structure as `rate_per_night`, with price strings such as `display_price` and numeric `extracted_` versions. |
| `properties[].deal / properties[].deal_description` | Text such as `46% less than usual` and a label such as `Great Deal`. Present only on some properties. |
| `properties[].hotel_class / properties[].extracted_hotel_class` | Star class as text (`5-star hotel`) and as a number (`5`). |
| `properties[].amenities[] / properties[].check_in_time / properties[].check_out_time` | Listed amenities and the check-in and check-out times of the property. |
| `properties[].reviews_breakdown[]` | Per-category review counts (`positive`, `neutral`, `negative`, `total_mentioned`) for topics such as Property, Service and Nature. |
| `properties[].nearby_places[]` | Nearby landmarks, each with a travel `type` (for example Taxi or Walking) and a `duration`. |
| `ads[].name / ads[].extracted_price / ads[].source` | Sponsored listings with the hotel name, a numeric price and the booking site shown for the offer. `free_cancellation` appears on some. |
| `properties[].property_token / ads[].property_token` | Identifier for a single property. |

### Notes

- All four parameters are required. Dates use the format `YYYY-MM-DD`.
- The `brands` array lists hotel brand groups with an `id`, a `name` and `children` sub-brands.
- Prices in the sample are strings with a `$` sign, and each has a matching `extracted_` number you can use directly.
- The result is returned in `outputs[0].data`.

### Pricing

$0.015 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-hotels/search.json`](../../../catalog/models/google-hotels/search.json) · Store page: https://www.sandbase.ai/model/google-hotels/search

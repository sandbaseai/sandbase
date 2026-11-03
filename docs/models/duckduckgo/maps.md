# DuckDuckGo Maps API: pricing, parameters and code examples

`duckduckgo/maps` · data API · DuckDuckGo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.00015 per call (free daily quota) · **Modes:** async

Search DuckDuckGo Maps for places inside a viewport rectangle or around a center.

## Pricing

- **$0.00015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "duckduckgo/maps", "q": "coffee"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('duckduckgo/maps', {'q': 'coffee'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("duckduckgo/maps", {
  "q": "coffee"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "duckduckgo/maps", sandbase.Params{
	"q": "coffee",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/duckduckgo/maps` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `q` | string | yes | Place or category query, up to 500 characters.  |
| `lat` | number |  | Viewport center latitude. Requires lon. range -90–90 |
| `lon` | number |  | Viewport center longitude. Requires lat. range -180–180 |
| `bbox` | string |  | Viewport rectangle as 'top,left,bottom,right'. Required unless lat and lon are supplied.  |
| `strict_bbox` | boolean |  | Exclude results outside the requested bounds. Default true.  |

## Details

Returns a list of places that match a text query inside a map viewport. Each place has an address, coordinates, rating, opening hours, contact details and a few reviews. You pass `q` plus either `lat` and `lon` for a center point or `bbox` for a rectangle.

### Use cases

- Build a list of coffee shops near a given point with their addresses and phone numbers.
- Compare `rating` and `reviews` counts across businesses in one neighborhood.
- Plot places on a map using `gps_coordinates`.
- Check which nearby places are open now and what hours they keep.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/duckduckgo/maps" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"q": "coffee", "lat": 40.7128, "lon": -74.006}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `q` | string | Yes | Place or category query, up to 500 characters. |
| `bbox` | string | No | Viewport rectangle as 'top,left,bottom,right'. Required unless lat and lon are supplied. |
| `lat` | number | No | Viewport center latitude. Requires lon. |
| `lon` | number | No | Viewport center longitude. Requires lat. |
| `strict_bbox` | boolean | No | Exclude results outside the requested bounds. Default true. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "local_results": [
    {
      "address": "38 Park Row, New York, NY 10038",
      "address_lines": [
        "38 Park Row"
      ],
      "city": "New York",
      "country_code": "US",
      "gps_coordinates": {
        "latitude": 40.7116156,
        "longitude": -74.0066955
      },
      "images": [
        "https://s3-media0.fl.yelpcdn.com/bphoto/kIWhmJh35yANG7qeEZsdvg/o.jpg"
      ],
      "link": "https://www.yelp.com/biz/starbucks-new-york-395?adjust_creative=duckduckgo&utm_c…",
      "menu": "https://www.starbucks.com/menu",
      "open_state": "Closed",
      "operating_hours": {
        "fri": "05:00:00 - 20:00:00",
        "mon": "05:00:00 - 20:00:00",
        "sat": "05:00:00 - 20:00:00",
        "sun": "05:00:00 - 20:00:00",
        "thu": "05:00:00 - 20:00:00",
        "tue": "05:00:00 - 20:00:00",
        "wed": "05:00:00 - 20:00:00"
      },
      "phone": "+12126088073",
      "phone_formatted": "+1 212 608 8073"
    }
  ],
  "search_metadata": {
    "created_at": "2026-11-03 07:33:07 UTC",
    "id": "581ba2bb9f7abc1700bb0841",
    "processed_at": "2026-11-03 07:33:07 UTC",
    "status": "Success",
    "total_time_taken": 1.348
  },
  "search_parameters": {
    "lat": 40.7128,
    "lon": -74.006,
    "q": "coffee",
    "strict_bbox": true
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `local_results[].title` | Name of the place. |
| `local_results[].type` | Category label for the place, such as `Coffee & tea`. |
| `local_results[].address / local_results[].city / local_results[].country_code` | Full street address, city and country code of the place. |
| `local_results[].gps_coordinates.latitude / local_results[].gps_coordinates.longitude` | Coordinates of the place. |
| `local_results[].rating / local_results[].reviews` | Average rating and the number of reviews behind it. |
| `local_results[].price / local_results[].price_score` | Price level shown as dollar signs and as a number. |
| `local_results[].open_state` | Whether the place is open or closed at the time of the call, for example `Closed`. |
| `local_results[].operating_hours` | Opening and closing times for each weekday, keyed by `mon` to `sun`. |
| `local_results[].phone / local_results[].phone_formatted / local_results[].website` | Phone number in raw and display form, and the place's website. |
| `local_results[].review_details[]` | A few sample reviews with `date`, `rating`, `snippet` and the reviewer in `user`. |
| `local_results[].source[]` | Map services that list this place, each with its own `place_id`. |

### Notes

- Send either `lat` and `lon` together, or `bbox` as `top,left,bottom,right`. The `search_parameters` object in the response echoes the values used.
- `strict_bbox` defaults to `true`, so results outside the requested bounds are dropped.
- `position` gives the rank of each place in `local_results`.
- Check `search_metadata.status` for `Success` before reading the results.

### Pricing

$0.00015 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/duckduckgo/maps.json`](../../../catalog/models/duckduckgo/maps.json) · Store page: https://www.sandbase.ai/model/duckduckgo/maps

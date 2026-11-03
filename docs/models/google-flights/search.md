# Google Flights Search API: pricing, parameters and code examples

`google-flights/search` · data API · Google Flights · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Google Flights itineraries for a route and date: airlines, times, stops, durations, prices and price insights.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-flights/search", "departure_id": "CDG", "arrival_id": "AUS", "outbound_date": "2026-12-15"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-flights/search', {'departure_id': 'CDG', 'arrival_id': 'AUS', 'outbound_date': '2026-12-15'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-flights/search", {
  "departure_id": "CDG",
  "arrival_id": "AUS",
  "outbound_date": "2026-12-15"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-flights/search", sandbase.Params{
	"departure_id": "CDG",
	"arrival_id": "AUS",
	"outbound_date": "2026-12-15",
})
```

Same call via the path form: `POST /v1/api/google-flights/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `type` | string |  | 1 round trip (default) \| 2 one way \| 3 multi-city  |
| `currency` | string |  | currency  |
| `arrival_id` | string | yes | destination airport/location code  |
| `return_date` | string |  | YYYY-MM-DD, required when type=1  |
| `departure_id` | string | yes | origin airport/location code  |
| `outbound_date` | string | yes | YYYY-MM-DD  |

## Details

Returns Google Flights itineraries for one route and date. Each itinerary lists the flight legs, layovers, total duration, price and carbon emissions. You send an origin code, a destination code and an outbound date.

### Use cases

- Compare the cheapest one-way fares from Paris (`CDG`) to Austin (`AUS`) on a given day.
- Build a flight picker that shows each leg, its airline, aircraft and departure and arrival times.
- Filter itineraries by number of stops or layover length to find short connections.
- Rank options by carbon emissions against the typical figure for the route.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-flights/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"departure_id": "CDG", "arrival_id": "AUS", "outbound_date": "2026-12-15", "type": "2"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `arrival_id` | string | Yes | destination airport/location code |
| `departure_id` | string | Yes | origin airport/location code |
| `outbound_date` | string | Yes | YYYY-MM-DD |
| `currency` | string | No | currency |
| `return_date` | string | No | YYYY-MM-DD, required when type=1 |
| `type` | string | No | 1 round trip (default) / 2 one way / 3 multi-city |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "airports": [
    {
      "arrival": [
        {
          "airport": {
            "id": "AUS",
            "name": "Austin-Bergstrom International Airport"
          },
          "city": "Austin",
          "country": "United States",
          "country_code": "US",
          "image": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcRKdjkMcBZuGRD1MjnuLQvdGtpT…",
          "thumbnail": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSQ73FSj9E8pKaNvjWKyEDQGfLV…"
        }
      ],
      "departure": [
        {
          "airport": {
            "id": "CDG",
            "name": "Aéroport de Paris-Charles de Gaulle"
          },
          "city": "Paris",
          "country": "France",
          "country_code": "FR",
          "image": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcQGx8ii2KbSDdbdzfKye5oDN2bw…",
          "thumbnail": "https://encrypted-tbn3.gstatic.com/images?q=tbn:ANd9GcSyQJ-woNs0iO22mPSkmRUM5gcs…"
        }
      ]
    }
  ],
  "best_flights": [
    {
      "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/DL.png",
      "booking_token": "WyJDalJJ…",
      "carbon_emissions": {
        "difference_percent": 16,
        "this_flight": 598000,
        "typical_for_this_route": 517000
      },
      "extensions": [
        "Checked baggage for a fee"
      ],
      "flights": [
        {
          "airline": "Delta",
          "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/DL.png",
          "airplane": "Airbus A330",
          "arrival_airport": {
            "id": "MSP",
            "name": "Minneapolis-Saint Paul International Airport",
            "time": "2026-12-15 13:10"
          },
          "departure_airport": {
            "id": "CDG",
            "name": "Aéroport de Paris-Charles de Gaulle",
            "time": "2026-12-15 10:30"
          },
          "duration": 580,
          "extensions": [
            "Average legroom (31 in)"
          ],
          "flight_number": "DL 153"
        }
      ],
      "layovers": [
        {
          "duration": 95,
          "id": "MSP",
          "name": "Minneapolis-Saint Paul International Airport"
        }
      ],
      "price": 949,
      "total_duration": 847,
      "type": "One way"
    }
  ],
  "other_flights": [
    {
      "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/multi.png",
      "booking_token": "WyJDalJJ…",
      "carbon_emissions": {
        "difference_percent": 38,
        "this_flight": 712000,
        "typical_for_this_route": 517000
      },
      "extensions": [
        "1 checked bag up to 23 kg included"
      ],
      "flights": [
        {
          "airline": "Air Tahiti Nui",
          "airline_logo": "https://www.gstatic.com/flights/airline_logos/70px/TN.png",
          "airplane": "Boeing 787",
          "arrival_airport": {
            "id": "LAX",
            "name": "Los Angeles International Airport",
            "time": "2026-12-15 14:00"
          },
          "departure_airport": {
            "id": "CDG",
            "name": "Aéroport de Paris-Charles de Gaulle",
            "time": "2026-12-15 11:35"
          },
          "duration": 685,
          "extensions": [
            "Average legroom (31 in)"
          ],
          "flight_number": "TN 7"
        }
      ],
      "layovers": [
        {
          "duration": 288,
          "id": "LAX",
          "name": "Los Angeles International Airport"
        }
      ],
      "price": 766,
      "total_duration": 1156,
      "type": "One way"
    }
  ],
  "price_insights": {
    "lowest_price": 766,
    "price_history": [
      [
        1788386400
      ]
    ],
    "price_level": "typical",
    "typical_price_range": [
      630
    ]
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `best_flights[] / other_flights[]` | Lists of itineraries. `best_flights` holds the top-ranked options and `other_flights` holds the rest. Both use the same structure. |
| `best_flights[].price` | Total fare for the itinerary as a number. The response does not show the currency, so set `currency` in the request if you need a specific one. |
| `best_flights[].total_duration` | Total travel time of the itinerary, including layovers. The 847 value for a trip with 580 and 172 minute legs and a 95 minute layover suggests minutes. |
| `best_flights[].flights[]` | The individual legs of the itinerary, in order. A one-stop itinerary has two legs. |
| `best_flights[].flights[].departure_airport.id / best_flights[].flights[].arrival_airport.id` | Airport code for the start and end of a leg. Each object also has `name` and `time` in `YYYY-MM-DD HH:MM` format. |
| `best_flights[].flights[].airline / best_flights[].flights[].flight_number / best_flights[].flights[].airplane` | Operating airline, flight number such as `DL 153`, and aircraft type for the leg. |
| `best_flights[].flights[].duration` | Duration of a single leg. Values like 580 and 172 are consistent with minutes. |
| `best_flights[].layovers[]` | One entry per connection, with the airport `id`, `name` and layover `duration`. |
| `best_flights[].carbon_emissions.this_flight / best_flights[].carbon_emissions.typical_for_this_route / best_flights[].carbon_emissions.difference_percent` | Emissions for this itinerary, the typical value for the route, and the percent difference between them. Negative values mean lower than typical. |
| `best_flights[].booking_token` | Token string for the itinerary. Keep it if you need to refer to a specific option later. |

### Notes

- Use airport codes such as `CDG` and `AUS` for `departure_id` and `arrival_id`.
- `type` is `1` for round trip (default), `2` for one way or `3` for multi-city. `return_date` is required when `type` is `1`.
- Leg times are local-looking strings in `YYYY-MM-DD HH:MM` format. A leg can arrive on the next date, as the Istanbul connection shows.
- The `airports` array describes the departure and arrival airports with city, country and country code.

### Pricing

$0.015 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-flights/search.json`](../../../catalog/models/google-flights/search.json) · Store page: https://www.sandbase.ai/model/google-flights/search

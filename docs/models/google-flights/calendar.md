# Google Flights Calendar API: pricing, parameters and code examples

`google-flights/calendar` · data API · Google Flights · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get the lowest Google Flights fare for each departure date in a range between two airports, for one-way or round trips.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-flights/calendar", "departure_id": "AUS", "arrival_id": "JFK"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-flights/calendar', {'departure_id': 'AUS', 'arrival_id': 'JFK'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-flights/calendar", {
  "departure_id": "AUS",
  "arrival_id": "JFK"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-flights/calendar", sandbase.Params{
	"departure_id": "AUS",
	"arrival_id": "JFK",
})
```

Same call via the path form: `POST /v1/api/google-flights/calendar` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gl` | string |  | Parameter defines the country to use for the Google Flights search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google countries page for…  |
| `hl` | string |  | Parameter defines the language to use for the Google Flights search. It's a two-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French). Head to the Google languages page for a full list of…  |
| `type` | string |  | Parameter defines the type of the flights. Available options: `1` - Round trip (default) `2` - One way  |
| `stops` | string |  | Parameter defines the number of stops during the flight. Available options: `0` - Any number of stops (default) `1` - Nonstop only `2` - 1 stop or fewer `3` - 2 stops or fewer  |
| `adults` | string |  | Parameter defines the number of adults. Default to 1.  |
| `children` | string |  | Parameter defines the number of children. Default to 0.  |
| `currency` | string |  | Parameter defines the currency of the returned prices. Default to `USD`. Head to the Google Travel Currencies page for a full list of supported currency codes.  |
| `arrival_id` | string | yes | Parameter defines the arrival airport code or location kgmid. An airport code is an uppercase 3-letter code. You can search for it on Google Flights or IATA. For example, `CDG` is Paris Charles de Gaulle Airport and…  |
| `departure_id` | string | yes | Parameter defines the departure airport code or location kgmid. An airport code is an uppercase 3-letter code. You can search for it on Google Flights or IATA. For example, `CDG` is Paris Charles de Gaulle Airport and…  |
| `return_times` | string |  | Parameter defines the return times range. It's a string containing two (for departure only) or four (for departure and arrival) comma-separated numbers. Each number represents the beginning of an hour. For example:…  |
| `travel_class` | string |  | Parameter defines the travel class. Available options: `1` - Economy (default) `2` - Premium economy `3` - Business `4` - First  |
| `date_range_end` | string |  | Parameter defines the end date of the date range. The format is YYYY-MM-DD. e.g. `2026-12-31` Default to end of next month.  |
| `infants_on_lap` | string |  | Parameter defines the number of infants on lap. Default to 0.  |
| `outbound_times` | string |  | Parameter defines the outbound times range. It's a string containing two (for departure only) or four (for departure and arrival) comma-separated numbers. Each number represents the beginning of an hour. For example:…  |
| `infants_in_seat` | string |  | Parameter defines the number of infants in seat. Default to 0.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `round_trip_days` | string |  | Parameter defines the number of days for the round trip. Default to 7. It can only be used in combination with `type` parameter set to `1` (Round trip). Parameter cannot be used with `fixed_outbound_date` parameter.  |
| `date_range_start` | string |  | Parameter defines the start date of the date range. The format is YYYY-MM-DD. e.g. `2026-11-12` Default to today's date. When `fixed_outbound_date` is set to `true`, this date is also used as the outbound date.  |
| `exclude_airlines` | string |  | Parameter defines the airline codes to be excluded. Split multiple airlines with comma. It can't be used together with `include_airlines`. Each airline code should be a 2-character IATA code consisting of either two…  |
| `include_airlines` | string |  | Parameter defines the airline codes to be included. Split multiple airlines with comma. It can't be used together with `exclude_airlines`. Each airline code should be a 2-character IATA code consisting of either two…  |
| `fixed_outbound_date` | string |  | Parameter defines whether the outbound date is fixed. It can be set to `true` to depart on `date_range_start` and get a price for each return date in the date range, or `false` (default) to get a price for each…  |

## Details

Get the lowest Google Flights fare for each departure date in a range between two airports, for one-way or round trips.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-flights/calendar" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"departure_id": "AUS", "arrival_id": "JFK"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `departure_id` | string | Yes | Parameter defines the departure airport code or location kgmid. An airport code is an uppercase 3-letter code. You can search for it on Google Flights or IATA. For example, `CDG` is Paris Charles de Gaulle Airport and `AUS` is Austin-Bergst |
| `arrival_id` | string | Yes | Parameter defines the arrival airport code or location kgmid. An airport code is an uppercase 3-letter code. You can search for it on Google Flights or IATA. For example, `CDG` is Paris Charles de Gaulle Airport and `AUS` is Austin-Bergstro |
| `gl` | string | No | Parameter defines the country to use for the Google Flights search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google countries page for a full list of support |
| `hl` | string | No | Parameter defines the language to use for the Google Flights search. It's a two-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French). Head to the Google languages page for a full list of supported Google lang |
| `currency` | string | No | Parameter defines the currency of the returned prices. Default to `USD`. Head to the Google Travel Currencies page for a full list of supported currency codes. |
| `type` | string | No | Parameter defines the type of the flights. Available options: `1` - Round trip (default) `2` - One way |
| `date_range_start` | string | No | Parameter defines the start date of the date range. The format is YYYY-MM-DD. e.g. `2026-11-12` Default to today's date. When `fixed_outbound_date` is set to `true`, this date is also used as the outbound date. |
| `date_range_end` | string | No | Parameter defines the end date of the date range. The format is YYYY-MM-DD. e.g. `2026-12-31` Default to end of next month. |
| `round_trip_days` | string | No | Parameter defines the number of days for the round trip. Default to 7. It can only be used in combination with `type` parameter set to `1` (Round trip). Parameter cannot be used with `fixed_outbound_date` parameter. |
| `fixed_outbound_date` | string | No | Parameter defines whether the outbound date is fixed. It can be set to `true` to depart on `date_range_start` and get a price for each return date in the date range, or `false` (default) to get a price for each outbound date in the date ran |
| `travel_class` | string | No | Parameter defines the travel class. Available options: `1` - Economy (default) `2` - Premium economy `3` - Business `4` - First |
| `adults` | string | No | Parameter defines the number of adults. Default to 1. |
| `children` | string | No | Parameter defines the number of children. Default to 0. |
| `infants_in_seat` | string | No | Parameter defines the number of infants in seat. Default to 0. |
| `infants_on_lap` | string | No | Parameter defines the number of infants on lap. Default to 0. |
| `stops` | string | No | Parameter defines the number of stops during the flight. Available options: `0` - Any number of stops (default) `1` - Nonstop only `2` - 1 stop or fewer `3` - 2 stops or fewer |
| `exclude_airlines` | string | No | Parameter defines the airline codes to be excluded. Split multiple airlines with comma. It can't be used together with `include_airlines`. Each airline code should be a 2-character IATA code consisting of either two uppercase letters or one |
| `include_airlines` | string | No | Parameter defines the airline codes to be included. Split multiple airlines with comma. It can't be used together with `exclude_airlines`. Each airline code should be a 2-character IATA code consisting of either two uppercase letters or one |
| `outbound_times` | string | No | Parameter defines the outbound times range. It's a string containing two (for departure only) or four (for departure and arrival) comma-separated numbers. Each number represents the beginning of an hour. For example: `4,18`: 4:00 AM - 7:00  |
| `return_times` | string | No | Parameter defines the return times range. It's a string containing two (for departure only) or four (for departure and arrival) comma-separated numbers. Each number represents the beginning of an hour. For example: `4,18`: 4:00 AM - 7:00 PM |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-flights/calendar.json`](../../../catalog/models/google-flights/calendar.json) · Store page: https://www.sandbase.ai/model/google-flights/calendar

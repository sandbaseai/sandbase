# Google Flights Deals API: pricing, parameters and code examples

`google-flights/deals` · data API · Google Flights · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Find discounted Google Flights fares from a departure airport, with destination, price, discount, dates and airline.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-flights/deals"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-flights/deals', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-flights/deals", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-flights/deals", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/google-flights/deals` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gl` | string |  | Parameter defines the country to use for the Google Flights Deals search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google countries…  |
| `hl` | string |  | Parameter defines the language to use for the Google Flights Deals search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter…  |
| `type` | string |  | Parameter defines the type of the flights. Available options: `1` - Round trip (default) `2` - One way  |
| `query` | string |  | Parameter defines the natural language query for Google Flights Deals. e.g. `High rises`, `beach vacation next month`. Cannot be combined with `travel_duration` or `trip_length`. Describe the trip duration in `query`…  |
| `stops` | string |  | Parameter defines the number of stops during the flight. Available options: `0` - Any number of stops (default) `1` - Nonstop only `2` - 1 stop or fewer `3` - 2 stops or fewer  |
| `adults` | string |  | Parameter defines the number of adults. Default to 1.  |
| `children` | string |  | Parameter defines the number of children. Default to 0.  |
| `currency` | string |  | Parameter defines the currency of the returned prices. Default to `USD`. Head to the Google Travel Currencies page for a full list of supported currency codes.  |
| `max_price` | string |  | Parameter defines the maximum ticket price. Default to unlimited.  |
| `return_date` | string |  | Parameter defines when you want to return. Use a single YYYY-MM-DD date for an exact return date, or two comma-separated dates for a flexible return window. Examples: `2026-11-19` — return on this exact date (use with…  |
| `trip_length` | string |  | Parameter defines a custom trip length in days when searching with flexible dates. Provide a single number for an exact duration, or two comma-separated numbers for a min/max range. Examples: `7` — exactly 7 days…  |
| `departure_id` | string |  | Parameter defines the departure airport code or location kgmid. An airport code is an uppercase 3-letter code. You can search for it using our Google Flights Autocomplete API or IATA. For example, `CDG` is Paris…  |
| `max_duration` | string |  | Parameter defines the maximum flight duration, in minutes. For example, specify `1500` for 25 hours. If your search returns no results, try increasing your `max_duration` by up to `200` minutes to account for…  |
| `travel_class` | string |  | Parameter defines the travel class. Available options: `1` - Economy (default) `2` - Premium economy `3` - Business `4` - First  |
| `outbound_date` | string |  | Parameter defines when you want to depart. Use a single YYYY-MM-DD date for an exact departure date, or two comma-separated dates for a flexible departure window. Examples: `2026-11-13` — depart on this exact date…  |
| `infants_on_lap` | string |  | Parameter defines the number of infants on lap. Default to 0.  |
| `infants_in_seat` | string |  | Parameter defines the number of infants in seat. Default to 0.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `travel_duration` | string |  | Parameter defines a preset trip duration when searching with flexible dates. Available options: `1` - 1 week (default) `2` - Weekend `3` - 2 weeks Can be used alone (deals of this duration, any departure date) or with…  |
| `exclude_airlines` | string |  | Parameter defines the airline codes to be excluded. Split multiple airlines with comma. It can't be used together with `include_airlines`. Each airline code should be a 2-character IATA code consisting of either two…  |
| `include_airlines` | string |  | Parameter defines the airline codes to be included. Split multiple airlines with comma. It can't be used together with `exclude_airlines`. Each airline code should be a 2-character IATA code consisting of either two…  |

## Details

Find discounted Google Flights fares from a departure airport, with destination, price, discount, dates and airline.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-flights/deals" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"departure_id": "AUS"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `departure_id` | string | No | Parameter defines the departure airport code or location kgmid. An airport code is an uppercase 3-letter code. You can search for it using our Google Flights Autocomplete API or IATA. For example, `CDG` is Paris Charles de Gaulle Airport an |
| `gl` | string | No | Parameter defines the country to use for the Google Flights Deals search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google countries page for a full list of s |
| `hl` | string | No | Parameter defines the language to use for the Google Flights Deals search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit region c |
| `currency` | string | No | Parameter defines the currency of the returned prices. Default to `USD`. Head to the Google Travel Currencies page for a full list of supported currency codes. |
| `query` | string | No | Parameter defines the natural language query for Google Flights Deals. e.g. `High rises`, `beach vacation next month`. Cannot be combined with `travel_duration` or `trip_length`. Describe the trip duration in `query` instead. |
| `type` | string | No | Parameter defines the type of the flights. Available options: `1` - Round trip (default) `2` - One way |
| `travel_class` | string | No | Parameter defines the travel class. Available options: `1` - Economy (default) `2` - Premium economy `3` - Business `4` - First |
| `outbound_date` | string | No | Parameter defines when you want to depart. Use a single YYYY-MM-DD date for an exact departure date, or two comma-separated dates for a flexible departure window. Examples: `2026-11-13` — depart on this exact date `2026-11-13,2026-12-12` —  |
| `return_date` | string | No | Parameter defines when you want to return. Use a single YYYY-MM-DD date for an exact return date, or two comma-separated dates for a flexible return window. Examples: `2026-11-19` — return on this exact date (use with a single `outbound_dat |
| `travel_duration` | string | No | Parameter defines a preset trip duration when searching with flexible dates. Available options: `1` - 1 week (default) `2` - Weekend `3` - 2 weeks Can be used alone (deals of this duration, any departure date) or with `outbound_date` as a d |
| `trip_length` | string | No | Parameter defines a custom trip length in days when searching with flexible dates. Provide a single number for an exact duration, or two comma-separated numbers for a min/max range. Examples: `7` — exactly 7 days `5,10` — between 5 and 10 d |
| `adults` | string | No | Parameter defines the number of adults. Default to 1. |
| `children` | string | No | Parameter defines the number of children. Default to 0. |
| `infants_in_seat` | string | No | Parameter defines the number of infants in seat. Default to 0. |
| `infants_on_lap` | string | No | Parameter defines the number of infants on lap. Default to 0. |
| `stops` | string | No | Parameter defines the number of stops during the flight. Available options: `0` - Any number of stops (default) `1` - Nonstop only `2` - 1 stop or fewer `3` - 2 stops or fewer |
| `exclude_airlines` | string | No | Parameter defines the airline codes to be excluded. Split multiple airlines with comma. It can't be used together with `include_airlines`. Each airline code should be a 2-character IATA code consisting of either two uppercase letters or one |
| `include_airlines` | string | No | Parameter defines the airline codes to be included. Split multiple airlines with comma. It can't be used together with `exclude_airlines`. Each airline code should be a 2-character IATA code consisting of either two uppercase letters or one |
| `max_price` | string | No | Parameter defines the maximum ticket price. Default to unlimited. |
| `max_duration` | string | No | Parameter defines the maximum flight duration, in minutes. For example, specify `1500` for 25 hours. If your search returns no results, try increasing your `max_duration` by up to `200` minutes to account for route-specific scheduling varia |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-flights/deals.json`](../../../catalog/models/google-flights/deals.json) · Store page: https://www.sandbase.ai/model/google-flights/deals

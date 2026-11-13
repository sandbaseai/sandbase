# Google Travel Explore API: pricing, parameters and code examples

`google/travel-explore` · data API · Google · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Explore destinations from a departure airport on Google Travel, with cheapest flight and hotel prices, dates and travel time for each destination.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google/travel-explore", "departure_id": "AUS"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google/travel-explore', {'departure_id': 'AUS'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google/travel-explore", {
  "departure_id": "AUS"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google/travel-explore", sandbase.Params{
	"departure_id": "AUS",
})
```

Same call via the path form: `POST /v1/api/google/travel-explore` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gl` | string |  | Parameter defines the country to use for the Google Travel Explore search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google countries…  |
| `hl` | string |  | Parameter defines the language to use for the Google Travel Explore search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter…  |
| `bags` | string |  | Parameter defines the number of carry-on bags. Default to `0`. Parameter should not exceed the total number of passengers with carry-on bag allowance (`adults`, `children` and `infants_in_seat`).  |
| `type` | string |  | Parameter defines the type of the flights. Available options: `1` - Round trip (default) `2` - One way When this parameter is set to `3`, use `multi_city_json` to set the flight information.  |
| `month` | string |  | Parameter defines the month of the trip with flexible travel dates. The value must be a number from `1` to `12`, where `1` = January, `2` = February, …, `12` = December. `0` (default) means all months within the next 6…  |
| `stops` | string |  | Parameter defines the number of stops during the flight. Available options: `0` - Any number of stops (default) `1` - Nonstop only `2` - 1 stop or fewer `3` - 2 stops or fewer  |
| `adults` | string |  | Parameter defines the number of adults. Default to 1.  |
| `children` | string |  | Parameter defines the number of children. Default to 0.  |
| `currency` | string |  | Parameter defines the currency of the returned prices. Default to `USD`. Head to the Google Travel Currencies page for a full list of supported currency codes.  |
| `interest` | string |  | Parameter defines the interest of the destination. Available options: `0` - Popular (default) `/g/11bc58l13w` - Outdoors `/m/0b3yr` - Beaches `/m/09cmq` - Museum `/m/03g3w` - History `/m/071k0` - Skiing `travel_mode`…  |
| `max_price` | string |  | Parameter defines the maximum ticket price. Default to unlimited.  |
| `arrival_id` | string |  | Parameter defines the arrival airport code or city location kgmid. An airport code is an uppercase 3-letter code. You can search for it on Google Flights or IATA. For example, `CDG` is Paris Charles de Gaulle Airport…  |
| `return_date` | string |  | Parameter defines the return date. The format is YYYY-MM-DD. e.g. `2026-11-19` Parameter is required if `type` parameter is set to: `1` (Round trip)  |
| `travel_mode` | string |  | Parameter defines the travel mode. Available options: `0` - All (default) `1` - Flight only `travel_mode` and `interest` parameters can't be used together.  |
| `departure_id` | string | yes | Parameter defines the departure airport code or city location kgmid. An airport code is an uppercase 3-letter code. You can search for it on Google Flights or IATA. For example, `CDG` is Paris Charles de Gaulle Airport…  |
| `max_duration` | string |  | Parameter defines the maximum flight duration, in minutes. For example, specify `1500` for 25 hours. If your search returns no results, try increasing your `max_duration` by up to `200` minutes to account for…  |
| `travel_class` | string |  | Parameter defines the travel class. Available options: `1` - Economy (default) `2` - Premium economy `3` - Business `4` - First  |
| `outbound_date` | string |  | Parameter defines the outbound date. The format is YYYY-MM-DD. e.g. `2026-11-13`  |
| `infants_on_lap` | string |  | Parameter defines the number of infants on lap. Default to 0.  |
| `arrival_area_id` | string |  | Parameter defines the arrival region or country as a location kgmid. A location kgmid is a string that starts with `/m/` or `/g/`. You can search for a region or country on Wikidata and use its "Freebase ID" as the…  |
| `infants_in_seat` | string |  | Parameter defines the number of infants in seat. Default to 0.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |
| `travel_duration` | string |  | Parameter defines the duration of the trip with flexible travel dates. Available options: `1` - Weekend `2` - 1 week (default) `3` - 2 weeks  |
| `exclude_airlines` | string |  | Parameter defines the airline codes to be excluded. Split multiple airlines with a comma. Each airline code should be a 2-character IATA code consisting of either two uppercase letters or one uppercase letter and one…  |
| `include_airlines` | string |  | Parameter defines the airline codes to be included. Split multiple airlines with a comma. Each airline code should be a 2-character IATA code consisting of either two uppercase letters or one uppercase letter and one…  |

## Details

Explore destinations from a departure airport on Google Travel, with cheapest flight and hotel prices, dates and travel time for each destination.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google/travel-explore" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"departure_id": "AUS"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `departure_id` | string | Yes | Parameter defines the departure airport code or city location kgmid. An airport code is an uppercase 3-letter code. You can search for it on Google Flights or IATA. For example, `CDG` is Paris Charles de Gaulle Airport and `AUS` is Austin-B |
| `gl` | string | No | Parameter defines the country to use for the Google Travel Explore search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google countries page for a full list of  |
| `hl` | string | No | Parameter defines the language to use for the Google Travel Explore search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit region  |
| `currency` | string | No | Parameter defines the currency of the returned prices. Default to `USD`. Head to the Google Travel Currencies page for a full list of supported currency codes. |
| `arrival_area_id` | string | No | Parameter defines the arrival region or country as a location kgmid. A location kgmid is a string that starts with `/m/` or `/g/`. You can search for a region or country on Wikidata and use its "Freebase ID" as the location kgmid. For examp |
| `arrival_id` | string | No | Parameter defines the arrival airport code or city location kgmid. An airport code is an uppercase 3-letter code. You can search for it on Google Flights or IATA. For example, `CDG` is Paris Charles de Gaulle Airport and `AUS` is Austin-Ber |
| `type` | string | No | Parameter defines the type of the flights. Available options: `1` - Round trip (default) `2` - One way When this parameter is set to `3`, use `multi_city_json` to set the flight information. |
| `outbound_date` | string | No | Parameter defines the outbound date. The format is YYYY-MM-DD. e.g. `2026-11-13` |
| `return_date` | string | No | Parameter defines the return date. The format is YYYY-MM-DD. e.g. `2026-11-19` Parameter is required if `type` parameter is set to: `1` (Round trip) |
| `month` | string | No | Parameter defines the month of the trip with flexible travel dates. The value must be a number from `1` to `12`, where `1` = January, `2` = February, …, `12` = December. `0` (default) means all months within the next 6 months are considered |
| `travel_duration` | string | No | Parameter defines the duration of the trip with flexible travel dates. Available options: `1` - Weekend `2` - 1 week (default) `3` - 2 weeks |
| `travel_class` | string | No | Parameter defines the travel class. Available options: `1` - Economy (default) `2` - Premium economy `3` - Business `4` - First |
| `adults` | string | No | Parameter defines the number of adults. Default to 1. |
| `children` | string | No | Parameter defines the number of children. Default to 0. |
| `infants_in_seat` | string | No | Parameter defines the number of infants in seat. Default to 0. |
| `infants_on_lap` | string | No | Parameter defines the number of infants on lap. Default to 0. |
| `stops` | string | No | Parameter defines the number of stops during the flight. Available options: `0` - Any number of stops (default) `1` - Nonstop only `2` - 1 stop or fewer `3` - 2 stops or fewer |
| `travel_mode` | string | No | Parameter defines the travel mode. Available options: `0` - All (default) `1` - Flight only `travel_mode` and `interest` parameters can't be used together. |
| `interest` | string | No | Parameter defines the interest of the destination. Available options: `0` - Popular (default) `/g/11bc58l13w` - Outdoors `/m/0b3yr` - Beaches `/m/09cmq` - Museum `/m/03g3w` - History `/m/071k0` - Skiing `travel_mode` and `interest` paramete |
| `include_airlines` | string | No | Parameter defines the airline codes to be included. Split multiple airlines with a comma. Each airline code should be a 2-character IATA code consisting of either two uppercase letters or one uppercase letter and one digit. You can search f |
| `exclude_airlines` | string | No | Parameter defines the airline codes to be excluded. Split multiple airlines with a comma. Each airline code should be a 2-character IATA code consisting of either two uppercase letters or one uppercase letter and one digit. You can search f |
| `bags` | string | No | Parameter defines the number of carry-on bags. Default to `0`. Parameter should not exceed the total number of passengers with carry-on bag allowance (`adults`, `children` and `infants_in_seat`). |
| `max_price` | string | No | Parameter defines the maximum ticket price. Default to unlimited. |
| `max_duration` | string | No | Parameter defines the maximum flight duration, in minutes. For example, specify `1500` for 25 hours. If your search returns no results, try increasing your `max_duration` by up to `200` minutes to account for route-specific scheduling varia |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google/travel-explore.json`](../../../catalog/models/google/travel-explore.json) · Store page: https://www.sandbase.ai/model/google/travel-explore

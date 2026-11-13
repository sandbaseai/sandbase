# Google Maps Directions API: pricing, parameters and code examples

`google-maps/directions` · data API · Google Maps · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call · **Modes:** sync

Get Google Maps directions between two places by car, transit, walking, cycling or flight, with routes, distance, duration and step-by-step instructions.

## Pricing

- **$0.01 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "google-maps/directions"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('google-maps/directions', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("google-maps/directions", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "google-maps/directions", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/google-maps/directions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `gl` | string |  | Parameter defines the country to use for the Google search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google countries page for a full…  |
| `hl` | string |  | Parameter defines the language to use for the Google Maps Directions search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter…  |
| `time` | string |  | Parameter defines the time to travel. Available options: `depart_at:xxxxxx` - Specifies the departure time, where `xxxxxx` is the timestamp. E.g. `depart_at:1698229538` specifies the departure time to 2023-10-25…  |
| `avoid` | string |  | Parameter defines avoid options. Available options: `highways` - Highways `tolls` - Tolls `ferries` - Ferries You can also combine multiple options by joining them with a comma (e.g.: `highways,tolls`).  |
| `route` | string |  | Parameter defines route options. Available options: `2` - Fewer transfers `3` - Less walking `4` - Wheelchair accessible Parameter works only if `travel_mode` parameter is set to: `3` (Transit)  |
| `prefer` | string |  | Parameter defines preferred transit options. Available options: `bus` - Bus `subway` - Subway `train` - Train `tram_light_rail` - Tram and light rail You can also combine multiple options by joining them with a comma…  |
| `end_addr` | string |  | Parameter defines the address of the ending point for the direction you want to search. You can use anything that you would use in a regular Google Maps Directions search. Alternatively, you can use `end_data_id` or…  |
| `end_coords` | string |  | Parameter defines the GPS coordinates of the ending point for the direction you want to search. The format is `latitude,longitude`. E.g. `30.197471099,-97.66635289`. Alternatively, you can use `end_addr` or…  |
| `start_addr` | string |  | Parameter defines the address of the starting point for the direction you want to search. You can use anything that you would use in a regular Google Maps Directions search. Alternatively, you can use `start_data_id`…  |
| `end_data_id` | string |  | Parameter defines the data ID of the ending point for the direction you want to search. Find the data ID of a place using our Google Maps API. Alternatively, you can use `end_addr` or `end_coords`.  |
| `travel_mode` | string |  | Parameter defines the travel mode. Available options: `6` - Best (Default) `0` - Driving `9` - Two-wheeler `3` - Transit `2` - Walking `1` - Cycling `4` - Flight  |
| `start_coords` | string |  | Parameter defines the GPS coordinates of the starting point for the direction you want to search. The format is `latitude,longitude`. E.g. `30.197471099,-97.66635289`. Alternatively, you can use `start_addr` or…  |
| `distance_unit` | string |  | Parameter defines the displayed distance unit. Available options: `1` - miles `0` - km  |
| `start_data_id` | string |  | Parameter defines the data ID of the starting point for the direction you want to search. Find the data ID of a place using our Google Maps API. Alternatively, you can use `start_addr` or `start_coords`.  |
| `json_restrictor` | string |  | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details.  |

## Details

Get Google Maps directions between two places by car, transit, walking, cycling or flight, with routes, distance, duration and step-by-step instructions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/google-maps/directions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"start_addr": "Austin-Bergstrom International Airport", "end_addr": "Texas State Capitol"}'
```

The result is returned in `outputs[0].data` as structured JSON.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `start_addr` | string | No | Parameter defines the address of the starting point for the direction you want to search. You can use anything that you would use in a regular Google Maps Directions search. Alternatively, you can use `start_data_id` or `start_coords`. |
| `end_addr` | string | No | Parameter defines the address of the ending point for the direction you want to search. You can use anything that you would use in a regular Google Maps Directions search. Alternatively, you can use `end_data_id` or `end_coords`. |
| `gl` | string | No | Parameter defines the country to use for the Google search. It's a two-letter country code. (e.g., `us` for the United States, `uk` for United Kingdom, or `fr` for France) Head to the Google countries page for a full list of supported Googl |
| `hl` | string | No | Parameter defines the language to use for the Google Maps Directions search. It's a two or three-letter language code. (e.g., `en` for English, `es` for Spanish, or `fr` for French), optionally followed by a two-letter or three-digit region |
| `travel_mode` | string | No | Parameter defines the travel mode. Available options: `6` - Best (Default) `0` - Driving `9` - Two-wheeler `3` - Transit `2` - Walking `1` - Cycling `4` - Flight |
| `start_data_id` | string | No | Parameter defines the data ID of the starting point for the direction you want to search. Find the data ID of a place using our Google Maps API. Alternatively, you can use `start_addr` or `start_coords`. |
| `end_data_id` | string | No | Parameter defines the data ID of the ending point for the direction you want to search. Find the data ID of a place using our Google Maps API. Alternatively, you can use `end_addr` or `end_coords`. |
| `start_coords` | string | No | Parameter defines the GPS coordinates of the starting point for the direction you want to search. The format is `latitude,longitude`. E.g. `30.197471099,-97.66635289`. Alternatively, you can use `start_addr` or `start_data_id`. |
| `end_coords` | string | No | Parameter defines the GPS coordinates of the ending point for the direction you want to search. The format is `latitude,longitude`. E.g. `30.197471099,-97.66635289`. Alternatively, you can use `end_addr` or `end_data_id`. |
| `distance_unit` | string | No | Parameter defines the displayed distance unit. Available options: `1` - miles `0` - km |
| `avoid` | string | No | Parameter defines avoid options. Available options: `highways` - Highways `tolls` - Tolls `ferries` - Ferries You can also combine multiple options by joining them with a comma (e.g.: `highways,tolls`). |
| `prefer` | string | No | Parameter defines preferred transit options. Available options: `bus` - Bus `subway` - Subway `train` - Train `tram_light_rail` - Tram and light rail You can also combine multiple options by joining them with a comma (e.g.: `subway,train`). |
| `route` | string | No | Parameter defines route options. Available options: `2` - Fewer transfers `3` - Less walking `4` - Wheelchair accessible Parameter works only if `travel_mode` parameter is set to: `3` (Transit) |
| `time` | string | No | Parameter defines the time to travel. Available options: `depart_at:xxxxxx` - Specifies the departure time, where `xxxxxx` is the timestamp. E.g. `depart_at:1698229538` specifies the departure time to 2023-10-25 10:25:38 GMT+0000 `arrive_by |
| `json_restrictor` | string | No | Parameter defines the fields you want to include in the output, reducing payload size for faster response. See the JSON Restrictor documentation for more details. |

### Pricing

$0.010 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/google-maps/directions.json`](../../../catalog/models/google-maps/directions.json) · Store page: https://www.sandbase.ai/model/google-maps/directions

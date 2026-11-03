# AccuWeather Weather API: pricing, parameters and code examples

`accuweather/weather` · data API · AccuWeather · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.05 per call · **Modes:** async

Get comprehensive weather data for a city including current conditions, daily and hourly forecasts, alerts, allergens, and radar metadata. Resolves city name to a location key internally, then fetches multiple data.

## Pricing

- **$0.05 per call** (USD)

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "accuweather/weather", "city": "Seattle"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('accuweather/weather', {'city': 'Seattle'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("accuweather/weather", {
  "city": "Seattle"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "accuweather/weather", sandbase.Params{
	"city": "Seattle",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/accuweather/weather` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `city` | string | yes | City name to get weather for (e.g., 'Istanbul', 'New York', 'London')  |

## Details

Returns current conditions, daily and hourly forecasts, alerts, allergen levels, and radar tile metadata for one city on AccuWeather. It needs a `city` name as input and looks up the matching location key for you.

### Use cases

- Show a current weather card for a city in a travel or local news app.
- Send a morning message with the day's high, low, and chance of rain.
- Warn hay fever users when pollen or mold levels are not low.
- Build a map view that loads radar tiles for a city.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/accuweather/weather" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"city": "Seattle"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `city` | string | Yes | City name to get weather for (e.g., 'Istanbul', 'New York', 'London') |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "alerts": "none",
    "allergens": [
      {
        "level": "Low",
        "type": "Tree Pollen"
      }
    ],
    "current_conditions": {
      "condition": "Cloudy",
      "humidity": 88,
      "is_day_time": false,
      "observation_time": "2026-11-02T23:17:00-08:00",
      "temperature": 47,
      "wind_speed": 1.1
    },
    "forecast": {
      "daily": [
        {
          "condition": "Cloudy with a shower in the area",
          "date": "Mon11/2",
          "high": 51,
          "low": 44,
          "precipitation_probability": 55
        }
      ],
      "hourly": [
        {
          "condition": "Showers",
          "precipitation_probability": 48,
          "temperature": 45,
          "time": "12 AM"
        }
      ]
    },
    "location": {
      "admin_area": "Washington",
      "country": "us",
      "key": "351409",
      "localized_name": "Seattle",
      "name": "Seattle"
    },
    "radar": {
      "params": [
        "zoom"
      ],
      "radar_base_url": "https://api.accuweather.com/maps/v1/radar/static/globalSIR/tile"
    }
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.location.name / data.location.localized_name` | The city name that the lookup matched. |
| `data.location.key` | The AccuWeather location key for the matched city, for example `351409`. |
| `data.location.admin_area / data.location.country` | The state or region name and the country code of the matched city. |
| `data.current_conditions.temperature / data.current_conditions.humidity / data.current_conditions.wind_speed` | Current temperature, humidity, and wind speed. The response does not state units. |
| `data.current_conditions.condition / data.current_conditions.is_day_time` | A text description of the sky and a flag that is `true` during daytime. |
| `data.current_conditions.observation_time` | When the reading was taken, as an ISO 8601 timestamp with a UTC offset. |
| `data.forecast.daily[].date / data.forecast.daily[].high / data.forecast.daily[].low` | The day label and its high and low temperature. |
| `data.forecast.daily[].condition / data.forecast.daily[].precipitation_probability` | A text summary for the day and the chance of precipitation. |
| `data.forecast.hourly[].time / data.forecast.hourly[].temperature / data.forecast.hourly[].precipitation_probability` | The hour label, the temperature, and the chance of precipitation for that hour. |
| `data.allergens[].type / data.allergens[].level` | The allergen name, such as `Tree Pollen`, and its level, such as `Low`. |
| `data.radar.radar_base_url / data.radar.params` | The base URL for radar tiles and the parameter names (`zoom`, `lon`, `lat`) listed for it. |

### Notes

- Pass a plain city name in `city`, such as `Seattle`. To check which place a name resolves to, use [AccuWeather Search Locations](/apis/accuweather/search-locations).
- `data.alerts` is the string `none` when no alerts are active.
- Daily `date` values are short labels like `Mon11/2`, and hourly `time` values are labels like `12 AM`. Neither includes a year or time zone.
- The call runs asynchronously. Poll the run endpoint and read the result from `outputs[0].data`.

### Pricing

$0.05 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/accuweather/weather.json`](../../../catalog/models/accuweather/weather.json) · Store page: https://www.sandbase.ai/model/accuweather/weather

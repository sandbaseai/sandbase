# IQAir City Air Quality API: pricing, parameters and code examples

`iqair/city-air-quality` · data API · IQAir · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Full air quality details for a specific city including current conditions, pollutant breakdown with concentrations, hourly and daily forecasts, weather data, pollen indices, and health recommendations. City, state,.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "iqair/city-air-quality", "city": "new-york-city", "country": "usa", "state": "new-york"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('iqair/city-air-quality', {'city': 'new-york-city', 'country': 'usa', 'state': 'new-york'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("iqair/city-air-quality", {
  "city": "new-york-city",
  "country": "usa",
  "state": "new-york"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "iqair/city-air-quality", sandbase.Params{
	"city": "new-york-city",
	"country": "usa",
	"state": "new-york",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/iqair/city-air-quality` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `city` | string | yes | City URL slug (e.g. 'new-york-city', 'beijing', 'santiago'). Obtainable from the url field of get_live_city_ranking or get_world_air_quality results.  |
| `state` | string | yes | State/region URL slug (e.g. 'new-york', 'beijing', 'santiago-metropolitan').  |
| `country` | string | yes | Country URL slug (e.g. 'usa', 'china', 'chile').  |

## Details

Returns air quality details for one city: current AQI, pollutant concentrations, hourly and daily forecasts, pollen levels, and health recommendations. It needs the `city`, `state` and `country` URL slugs, such as `new-york-city`, `new-york` and `usa`.

### Use cases

- Show the current AQI and main pollutant for a city on a dashboard or widget.
- Build a 3-day air quality and weather outlook from the daily and hourly forecasts.
- Show pollen levels by type (grass, weed, tree) for allergy planning.
- Display advice on exercise, windows, masks and air purifiers based on current pollution.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/iqair/city-air-quality" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"city": "new-york-city", "country": "usa", "state": "new-york"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `city` | string | Yes | City URL slug (e.g. 'new-york-city', 'beijing', 'santiago'). Obtainable from the url field of get_live_city_ranking or get_world_air_quality results. |
| `country` | string | Yes | Country URL slug (e.g. 'usa', 'china', 'chile'). |
| `state` | string | Yes | State/region URL slug (e.g. 'new-york', 'beijing', 'santiago-metropolitan'). |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "details": {
      "activeStationsCount": 67,
      "analysis": "<script type=\"application/ld+json\">{\"@context\":\"https://schema.org\",\"@type\":\"FAQ…",
      "anonymousContributorsCount": 47,
      "breadcrumbs": [
        {
          "label": "USA",
          "url": "/usa"
        }
      ],
      "coordinates": {
        "latitude": 40.6627117,
        "longitude": -73.9386769
      },
      "country": "USA",
      "countryID": "7KEznm2wS6Zk3chh2",
      "current": {
        "WHOExposure": {
          "WHOExposure": 1.3,
          "WHOExposureColor": "red"
        },
        "aqi": 35,
        "aqiDescription": "Air quality index",
        "concentration": 6.4,
        "condition": "Clear sky",
        "estimated": false,
        "humidity": 83,
        "icon": "01n"
      },
      "featuredStation": {
        "aqi": 39,
        "contributorProfile": {
          "name": "HeWhoIsBecomingWhoHeIs",
          "pictureURL": "https://lh3.googleusercontent.com/a/AAcHTtd--bVO6WCoAzFAnzh_-M_aZVyoF6FgkPYOcBkl…",
          "url": "profile/-1-jlihbc"
        },
        "flagURL": "https://cdn.airvisual.net/flags/usa.jpg",
        "gallery": {
          "pictures": [
            "https://cdn.airvisual.net/assets/stations/c1f7f6b1-2336-41a0-bf1b-a19ce2bb284f.c…"
          ]
        },
        "id": "68947965c212f4cae27ec7da",
        "name": "South Slope",
        "url": "/usa/new-york/new-york/south-slope"
      },
      "followers": {
        "count": 2559921,
        "pictures": [
          "https://cdn.airvisual.net/tiny/default.png"
        ]
      },
      "forecasts": {
        "daily": [
          {
            "aqi": 42,
            "condition": "Clear sky",
            "humidity": 75,
            "icon": "01d",
            "pollen": {
              "globalIndexLevel": 1,
              "pollens": [
                {
                  "level": 0,
                  "type": "grass"
                }
              ]
            },
            "pressure": 1025,
            "temperature": {
              "max": 19,
              "min": 10
            },
            "ts": "2026-11-03T08:00:00.000Z"
          }
        ],
        "hourly": [
          {
            "aqi": 35,
            "condition": "Clear sky",
            "humidity": 83,
            "icon": "01n",
            "pressure": 1026,
            "temperature": 11,
            "ts": "2026-11-03T07:00:00.000Z",
            "wind": {
              "direction": 231,
              "speed": 8
            }
          }
        ]
      },
      "hasLowCostSensor": true
    },
    "pollutants": [
      {
        "aqi": 35,
        "concentration": 6.4,
        "description": "Fine particles (≤ 2.5 µm)",
        "pollutantName": "pm25",
        "unit": "µg/m³"
      }
    ],
    "recommendations": {
      "pollution": {
        "airPurifier": {
          "value": "hidden"
        },
        "exercise": {
          "text": "Enjoy outdoor activities",
          "value": "green"
        },
        "mask": {
          "value": "hidden"
        },
        "windows": {
          "product": {
            "name": "AirVisual Series",
            "text": "Get a monitor",
            "url": "/commercial-air-quality-monitors"
          },
          "text": "Open your windows to bring clean, fresh air indoors",
          "value": "green"
        }
      }
    }
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.details.current.aqi` | Current air quality index for the city. `aqiDescription` names the index. |
| `data.details.current.concentration` | Current pollutant concentration behind the AQI value. The `pollutants` list gives the unit. |
| `data.details.current.condition / humidity` | Current weather condition text and humidity value. |
| `data.pollutants[].pollutantName / description` | Short code and plain name of each measured pollutant, such as `pm25` for fine particles. |
| `data.pollutants[].aqi / concentration / unit` | AQI for that pollutant, its measured concentration, and the unit of the concentration. |
| `data.details.forecasts.daily[].aqi / temperature.max / temperature.min` | Forecast AQI and the high and low temperature for each day. `ts` gives the date and time. |
| `data.details.forecasts.daily[].pollen.pollens[]` | Pollen `level` for each `type` (grass, weed, tree). `globalIndexLevel` gives an overall pollen level. |
| `data.details.forecasts.hourly[].aqi / temperature / wind.speed / wind.direction` | Hourly forecast for AQI, temperature and wind. `ts` gives the hour. |
| `data.recommendations.pollution` | Advice for `exercise`, `windows`, `mask` and `airPurifier`. Each has a `value` such as `green` or `hidden`, and some have a `text`. |
| `data.details.coordinates / timezone / activeStationsCount` | Latitude and longitude of the city, its time zone name, and the number of active monitoring stations. |

### Notes

- Get the `city`, `state` and `country` slugs from the `url` of a result in [IQAir Live City Ranking](/apis/iqair/live-city-ranking) or [IQAir World Air Quality](/apis/iqair/world-air-quality).
- Timestamps in `ts` use ISO 8601 UTC format, for example `2026-11-03T08:00:00.000Z`.
- `data.details.recommendations` is repeated in `data.recommendations`, so you can read either one.
- Station `url` values and breadcrumb `url` values are relative paths, such as `/usa/new-york/new-york`.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/iqair/city-air-quality.json`](../../../catalog/models/iqair/city-air-quality.json) · Store page: https://www.sandbase.ai/model/iqair/city-air-quality

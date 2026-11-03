# AccuWeather Search Locations API: pricing, parameters and code examples

`accuweather/search-locations` · data API · AccuWeather · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

Search for location keys and metadata by query string. Returns matching cities with their AccuWeather location keys, geographic coordinates, timezone information, and available datasets.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "accuweather/search-locations", "query": "London"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('accuweather/search-locations', {'query': 'London'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("accuweather/search-locations", {
  "query": "London"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "accuweather/search-locations", sandbase.Params{
	"query": "London",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/accuweather/search-locations` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Location name or query to search for (e.g., 'Istanbul', 'London', 'New York')  |

## Details

This API searches AccuWeather locations by name and returns matching places. Each match includes its location `Key`, coordinates, time zone, and the data sets available for it. It needs one input: a `query` string such as `London`.

### Use cases

- Convert a city name typed by a user into the location `Key` needed for other weather calls.
- Tell apart places with the same name, such as London in the United Kingdom, Canada and the United States.
- Get latitude, longitude and elevation for a city to place it on a map.
- Check which data sets, such as air quality or alerts, exist for a location before you request them.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/accuweather/search-locations" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "London"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Location name or query to search for (e.g., 'Istanbul', 'London', 'New York') |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "AdministrativeArea": {
          "CountryID": "GB",
          "EnglishName": "London",
          "EnglishType": "London Borough",
          "ID": "LND",
          "Level": 1,
          "LocalizedName": "London",
          "LocalizedType": "London Borough"
        },
        "Country": {
          "EnglishName": "United Kingdom",
          "ID": "GB",
          "LocalizedName": "United Kingdom"
        },
        "DataSets": [
          "AirQualityCurrentConditions"
        ],
        "EnglishName": "London",
        "GeoPosition": {
          "Elevation": {
            "Imperial": {
              "Unit": "ft",
              "UnitType": 0,
              "Value": 59
            },
            "Metric": {
              "Unit": "m",
              "UnitType": 5,
              "Value": 18
            }
          },
          "Latitude": 51.514,
          "Longitude": -0.107
        },
        "IsAlias": false,
        "Key": "328328",
        "LocalizedName": "London",
        "PrimaryPostalCode": "EC4A 2",
        "Rank": 10,
        "Region": {
          "EnglishName": "Europe",
          "ID": "EUR",
          "LocalizedName": "Europe"
        },
        "SupplementalAdminAreas": [
          {
            "EnglishName": "England",
            "Level": 0,
            "LocalizedName": "England"
          }
        ]
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[].Key` | The location key for the match. Use this value to identify the place in other weather calls. |
| `data.items[].EnglishName / data.items[].LocalizedName` | The name of the place in English and in the local form. |
| `data.items[].Type` | The kind of place. In this response the value is `City`. |
| `data.items[].Country.ID / data.items[].Country.EnglishName` | The country code and country name for the match. |
| `data.items[].AdministrativeArea.EnglishName / data.items[].AdministrativeArea.ID` | The state, province or similar region that contains the place, with its short ID. |
| `data.items[].GeoPosition.Latitude / data.items[].GeoPosition.Longitude` | The coordinates of the location. |
| `data.items[].GeoPosition.Elevation.Metric.Value / data.items[].GeoPosition.Elevation.Imperial.Value` | The elevation of the location. The metric value is in `m` and the imperial value is in `ft`, as given by the `Unit` field next to each. |
| `data.items[].TimeZone.Name / data.items[].TimeZone.GmtOffset` | The IANA time zone name and the offset from GMT. `IsDaylightSaving` shows if daylight saving time is active. |
| `data.items[].DataSets` | A list of data sets available for the location, such as `AirQualityCurrentConditions` or `Alerts`. |
| `data.items[].Rank / data.items[].PrimaryPostalCode` | `Rank` is a numeric rank for the match. `PrimaryPostalCode` is the main postal code of the place. |

### Notes

- Pass the place name in `query`. The response can hold several places with the same name, so check `Country` and `AdministrativeArea` to pick the right one.
- Location keys are strings, for example `328328`. Keep them as strings.
- Call [AccuWeather Weather](/apis/accuweather/weather) next to get weather for a location. Use [AccuWeather List Cities](/apis/accuweather/list-cities) to browse cities instead of searching by name.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/accuweather/search-locations.json`](../../../catalog/models/accuweather/search-locations.json) · Store page: https://www.sandbase.ai/model/accuweather/search-locations

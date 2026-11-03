# Open-Meteo Geocoding API: pricing, parameters and code examples

`open-meteo/geocoding` · data API · Open-Meteo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0001 per call (free daily quota) · **Modes:** sync

Look up places by name and get coordinates, country, timezone, population and elevation for use with the weather APIs.

## Pricing

- **$0.0001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "open-meteo/geocoding", "name": "Berlin"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('open-meteo/geocoding', {'name': 'Berlin'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("open-meteo/geocoding", {
  "name": "Berlin"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "open-meteo/geocoding", sandbase.Params{
	"name": "Berlin",
})
```

Same call via the path form: `POST /v1/api/open-meteo/geocoding` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `name` | string | yes | Location name or postal code. Append `, ` or `, ` to narrow results.  |
| `count` | integer |  | Maximum number of results (1-100). Default 10. default `10` |
| `format` | string |  | Response format. Default `json`. one of: `json`, `protobuf`; default `"json"` |
| `language` | string |  | Two-letter language code for translated names. Default `en`. default `"en"` |
| `countryCode` | string |  | ISO-3166-1 alpha-2 country code to filter results.  |

## Details

Returns a list of places that match a name or postal code, with coordinates, country, timezone, population and elevation for each match. The only required input is `name`, for example `Berlin`.

### Use cases

- Convert a city name typed by a user into `latitude` and `longitude` for a weather request.
- Find the `timezone` of a place before you format forecast times.
- Separate places that share a name, such as Berlin in Germany and Berlin in New Hampshire, by country and region.
- Look up the place for a postal code and read its administrative areas.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/open-meteo/geocoding" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name": "Berlin"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `name` | string | Yes | Location name or postal code. Append `, ` or `, ` to narrow results. |
| `count` | integer | No | Maximum number of results (1-100). Default 10. |
| `countryCode` | string | No | ISO-3166-1 alpha-2 country code to filter results. |
| `format` | string | No | Response format. Default `json`. |
| `language` | string | No | Two-letter language code for translated names. Default `en`. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "generationtime_ms": 0.23376942,
  "results": [
    {
      "admin1": "State of Berlin",
      "admin1_id": 2950157,
      "admin3": "Berlin, Stadt",
      "admin3_id": 6547383,
      "admin4": "Berlin",
      "admin4_id": 6547539,
      "country": "Germany",
      "country_code": "DE",
      "country_id": 2921044,
      "elevation": 74.0,
      "feature_code": "PPLC",
      "id": 2950159
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `results[]` | List of matching places. The first entries are the best matches for `name`. |
| `results[].name` | Name of the place, translated to the `language` you request. |
| `results[].latitude / results[].longitude` | Coordinates of the place in decimal degrees. Pass these to the weather APIs. |
| `results[].timezone` | IANA timezone name of the place, such as `Europe/Berlin`. |
| `results[].elevation` | Elevation of the place. Open-Meteo Elevation can return the same kind of value for any coordinate. |
| `results[].population` | Number of inhabitants listed for the place. Use it to rank places that share a name. |
| `results[].country / results[].country_code` | Country name and its two-letter ISO country code. |
| `results[].admin1 / results[].admin2 / results[].admin3 / results[].admin4` | Names of the administrative areas that contain the place, from the largest (such as state) to smaller ones. Not every level appears for every place. |
| `results[].id` | Numeric ID of the place. The `admin1_id`, `admin2_id`, `admin3_id`, `admin4_id` and `country_id` fields hold the IDs of the matching areas. |
| `results[].postcodes[]` | Postal codes that belong to the place. |

### Notes

- Use `countryCode`, for example `DE`, to keep only results from one country.
- Use `count` (1-100) to change how many results come back. The default is 10.
- Pass `latitude` and `longitude` from a result to [Open-Meteo Weather Forecast](/apis/open-meteo/forecast), and add `timezone` to get local times.
- `feature_code` describes the type of place. For example, `PPLC` marks the capital in the Berlin, Germany result.

### Pricing

$0.0001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/open-meteo/geocoding.json`](../../../catalog/models/open-meteo/geocoding.json) · Store page: https://www.sandbase.ai/model/open-meteo/geocoding

# AccuWeather List Cities API: pricing, parameters and code examples

`accuweather/list-cities` · data API · AccuWeather · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** async

List all provinces or major administrative divisions within a country by its ISO 2-letter code. Searches across regional browse pages to find the country.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: async (default `async`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "accuweather/list-cities", "country_code": "US"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('accuweather/list-cities', {'country_code': 'US'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("accuweather/list-cities", {
  "country_code": "US"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "accuweather/list-cities", sandbase.Params{
	"country_code": "US",
})
```

With plain HTTP, async runs return `{"id", "status": "pending"}`. Poll until `completed` or `failed`:

```bash
curl https://api.sandbase.ai/v1/run/$RUN_ID -H "Authorization: Bearer $SANDBASE_API_KEY"
```

Same call via the path form: `POST /v1/api/accuweather/list-cities` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `country_code` | string | yes | ISO 2-letter country code, case-insensitive (e.g., 'tr', 'us', 'gb')  |

## Details

Returns the provinces or major administrative divisions of a country on AccuWeather. You send an ISO 2-letter country code in `country_code`, and each result has a name, a type, and an AccuWeather browse-page URL.

### Use cases

- List all US states to build a region picker for a weather app.
- Collect the browse-page URLs for a country to map its administrative divisions on AccuWeather.
- Check which divisions AccuWeather lists for a country before you search for a specific place.
- Seed a location database with division names for a given country.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/accuweather/list-cities" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"country_code": "US"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `country_code` | string | Yes | ISO 2-letter country code, case-insensitive (e.g., 'tr', 'us', 'gb') |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "items": [
      {
        "name": "Alabama",
        "type": "Province/City",
        "url": "https://www.accuweather.com/en/browse-locations/eur/us/al"
      }
    ]
  },
  "status": "success"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.items[]` | One province or major administrative division in the country. |
| `data.items[].name` | Name of the division, for example `Alabama`. |
| `data.items[].type` | Kind of division. The sample shows `Province/City` for US states. |
| `data.items[].url` | AccuWeather browse-locations page for the division. The path ends with a short division code such as `al` or `ak`. |
| `status` | Result of the call. The sample shows `success`. |

### Notes

- `country_code` is case-insensitive, so `US` and `us` give the same request.
- The `url` values include the country code and a short division code in the path, for example `/us/al`.
- To find a specific place, call [AccuWeather Search Locations](/apis/accuweather/search-locations). To get conditions for a place, call [AccuWeather Weather](/apis/accuweather/weather).
- The request has no pagination parameters. The only input is `country_code`.

### Pricing

$0.01 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/accuweather/list-cities.json`](../../../catalog/models/accuweather/list-cities.json) · Store page: https://www.sandbase.ai/model/accuweather/list-cities

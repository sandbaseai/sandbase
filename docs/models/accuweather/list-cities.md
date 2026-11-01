# AccuWeather List Cities

`accuweather/list-cities` · api · AccuWeather

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

List all provinces or major administrative divisions within a country by its ISO 2-letter code. Searches across regional browse pages to find the country.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/accuweather/list-cities" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"country_code": "US"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `country_code` | string | Yes | ISO 2-letter country code, case-insensitive (e.g., 'tr', 'us', 'gb') |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/accuweather/list-cities.json`](../../../catalog/models/accuweather/list-cities.json) · Store page: https://www.sandbase.ai/model/accuweather/list-cities

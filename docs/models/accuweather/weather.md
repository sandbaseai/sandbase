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

Get comprehensive weather data for a city including current conditions, daily and hourly forecasts, alerts, allergens, and radar metadata. Resolves city name to a location key internally, then fetches multiple data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/accuweather/weather" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"city": "Seattle"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `city` | string | Yes | City name to get weather for (e.g., 'Istanbul', 'New York', 'London') |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/accuweather/weather.json`](../../../catalog/models/accuweather/weather.json) · Store page: https://www.sandbase.ai/model/accuweather/weather

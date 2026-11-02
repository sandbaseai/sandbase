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

Full air quality details for a specific city including current conditions, pollutant breakdown with concentrations, hourly and daily forecasts, weather data, pollen indices, and health recommendations. City, state,.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/iqair/city-air-quality" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"city": "new-york-city", "country": "usa", "state": "new-york"}'
```

This API runs asynchronously. The call returns a task `id` with status `pending`; poll `GET https://api.sandbase.ai/v1/run/{id}` until `status` is `completed` and read the result from `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `city` | string | Yes | City URL slug (e.g. 'new-york-city', 'beijing', 'santiago'). Obtainable from the url field of get_live_city_ranking or get_world_air_quality results. |
| `country` | string | Yes | Country URL slug (e.g. 'usa', 'china', 'chile'). |
| `state` | string | Yes | State/region URL slug (e.g. 'new-york', 'beijing', 'santiago-metropolitan'). |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/iqair/city-air-quality.json`](../../../catalog/models/iqair/city-air-quality.json) · Store page: https://www.sandbase.ai/model/iqair/city-air-quality

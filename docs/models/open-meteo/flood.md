# Open-Meteo Flood Forecast API: pricing, parameters and code examples

`open-meteo/flood` · data API · Open-Meteo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0001 per call (free daily quota) · **Modes:** sync

Daily river discharge forecast and history for any coordinates from the GloFAS flood model.

## Pricing

- **$0.0001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "open-meteo/flood", "latitude": "52.52", "longitude": "13.41"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('open-meteo/flood', {'latitude': '52.52', 'longitude': '13.41'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("open-meteo/flood", {
  "latitude": "52.52",
  "longitude": "13.41"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "open-meteo/flood", sandbase.Params{
	"latitude": "52.52",
	"longitude": "13.41",
})
```

Same call via the path form: `POST /v1/api/open-meteo/flood` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `daily` | string |  | Comma-separated list of daily aggregation variables to return. Requires `timezone`. Common values: `river_discharge`, `river_discharge_mean`, `river_discharge_median`, `river_discharge_max`, `river_discharge_min`,…  |
| `models` | string |  | Comma-separated GloFAS models. Default best match.  |
| `end_date` | string |  | End of the interval, `yyyy-mm-dd` (ISO 8601).  |
| `ensemble` | boolean |  | Return all ensemble members instead of the aggregate. Default `false`. default `false` |
| `latitude` | string | yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated.  |
| `longitude` | string | yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated.  |
| `past_days` | integer |  | Number of past days to include (0-92). Default 0. default `0` |
| `start_date` | string |  | Start of the interval, `yyyy-mm-dd` (ISO 8601).  |
| `timeformat` | string |  | Time output format. Default `iso8601`. one of: `iso8601`, `unixtime`; default `"iso8601"` |
| `forecast_days` | integer |  | Number of forecast days to return (0-210). Default 92. default `92` |
| `cell_selection` | string |  | Grid-cell preference for the coordinate. Default `nearest`. one of: `land`, `sea`, `nearest`; default `"nearest"` |

## Details

Daily river discharge forecast and history for any coordinates from the GloFAS flood model.

The result is returned in `outputs[0].data` as the official Open-Meteo API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/open-meteo/flood" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"latitude": "52.52", "longitude": "13.41", "daily": "river_discharge"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cell_selection` | string | No | Grid-cell preference for the coordinate. Default `nearest`. |
| `daily` | string | No | Comma-separated list of daily aggregation variables to return. Requires `timezone`. Common values: `river_discharge`, `river_discharge_mean`, `river_discharge_m |
| `end_date` | string | No | End of the interval, `yyyy-mm-dd` (ISO 8601). |
| `ensemble` | boolean | No | Return all ensemble members instead of the aggregate. Default `false`. |
| `forecast_days` | integer | No | Number of forecast days to return (0-210). Default 92. |
| `latitude` | string | Yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated. |
| `longitude` | string | Yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated. |
| `models` | string | No | Comma-separated GloFAS models. Default best match. |
| `past_days` | integer | No | Number of past days to include (0-92). Default 0. |
| `start_date` | string | No | Start of the interval, `yyyy-mm-dd` (ISO 8601). |
| `timeformat` | string | No | Time output format. Default `iso8601`. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/open-meteo/flood.json`](../../../catalog/models/open-meteo/flood.json) · Store page: https://www.sandbase.ai/model/open-meteo/flood

# Open-Meteo Climate Projections API: pricing, parameters and code examples

`open-meteo/climate` · data API · Open-Meteo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0001 per call (free daily quota) · **Modes:** sync

Daily climate model projections to 2050 for any coordinates, from CMIP6 high-resolution models.

## Pricing

- **$0.0001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "open-meteo/climate", "end_date": "2024-01-07", "latitude": "52.52", "longitude": "13.41", "models": "MRI_AGCM3_2_S,EC_Earth3P_HR", "start_date": "2024-01-01"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('open-meteo/climate', {'end_date': '2024-01-07', 'latitude': '52.52', 'longitude': '13.41', 'models': 'MRI_AGCM3_2_S,EC_Earth3P_HR', 'start_date': '2024-01-01'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("open-meteo/climate", {
  "end_date": "2024-01-07",
  "latitude": "52.52",
  "longitude": "13.41",
  "models": "MRI_AGCM3_2_S,EC_Earth3P_HR",
  "start_date": "2024-01-01"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "open-meteo/climate", sandbase.Params{
	"end_date": "2024-01-07",
	"latitude": "52.52",
	"longitude": "13.41",
	"models": "MRI_AGCM3_2_S,EC_Earth3P_HR",
	"start_date": "2024-01-01",
})
```

Same call via the path form: `POST /v1/api/open-meteo/climate` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `daily` | string |  | Comma-separated list of daily aggregation variables to return. Requires `timezone`. Common values: `temperature_2m_max`, `temperature_2m_min`, `temperature_2m_mean`, `precipitation_sum`, `rain_sum`, `snowfall_sum`,…  |
| `models` | string | yes | Required. Comma-separated climate models: `CMCC_CM2_VHR4`, `FGOALS_f3_H`, `HiRAM_SIT_HR`, `MRI_AGCM3_2_S`, `EC_Earth3P_HR`, `MPI_ESM1_2_XR`, `NICAM16_8S`.  |
| `end_date` | string | yes | End of the interval, `yyyy-mm-dd` (ISO 8601).  |
| `latitude` | string | yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated.  |
| `longitude` | string | yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated.  |
| `start_date` | string | yes | Start of the interval, `yyyy-mm-dd` (ISO 8601).  |
| `timeformat` | string |  | Time output format. Default `iso8601`. one of: `iso8601`, `unixtime`; default `"iso8601"` |
| `cell_selection` | string |  | Grid-cell preference for the coordinate. Default `land`. one of: `land`, `sea`, `nearest`; default `"land"` |
| `wind_speed_unit` | string |  | Wind speed unit. Default `kmh`. one of: `kmh`, `ms`, `mph`, `kn`; default `"kmh"` |
| `temperature_unit` | string |  | Temperature unit. Default `celsius`. one of: `celsius`, `fahrenheit`; default `"celsius"` |
| `precipitation_unit` | string |  | Precipitation unit. Default `mm`. one of: `mm`, `inch`; default `"mm"` |
| `disable_bias_correction` | boolean |  | Return raw model output without statistical bias correction. Default `false`. default `false` |

## Details

Daily climate model projections to 2050 for any coordinates, from CMIP6 high-resolution models.

The result is returned in `outputs[0].data` as the official Open-Meteo API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/open-meteo/climate" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "2024-01-07", "latitude": "52.52", "longitude": "13.41", "models": "MRI_AGCM3_2_S,EC_Earth3P_HR", "start_date": "2024-01-01", "daily": "temperature_2m_max"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `cell_selection` | string | No | Grid-cell preference for the coordinate. Default `land`. |
| `daily` | string | No | Comma-separated list of daily aggregation variables to return. Requires `timezone`. Common values: `temperature_2m_max`, `temperature_2m_min`, `temperature_2m_m |
| `disable_bias_correction` | boolean | No | Return raw model output without statistical bias correction. Default `false`. |
| `end_date` | string | Yes | End of the interval, `yyyy-mm-dd` (ISO 8601). |
| `latitude` | string | Yes | WGS84 latitude of the location. Multiple coordinates can be comma-separated. |
| `longitude` | string | Yes | WGS84 longitude of the location (negative for the Americas). Multiple coordinates can be comma-separated. |
| `models` | string | Yes | Required. Comma-separated climate models: `CMCC_CM2_VHR4`, `FGOALS_f3_H`, `HiRAM_SIT_HR`, `MRI_AGCM3_2_S`, `EC_Earth3P_HR`, `MPI_ESM1_2_XR`, `NICAM16_8S`. |
| `precipitation_unit` | string | No | Precipitation unit. Default `mm`. |
| `start_date` | string | Yes | Start of the interval, `yyyy-mm-dd` (ISO 8601). |
| `temperature_unit` | string | No | Temperature unit. Default `celsius`. |
| `timeformat` | string | No | Time output format. Default `iso8601`. |
| `wind_speed_unit` | string | No | Wind speed unit. Default `kmh`. |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/open-meteo/climate.json`](../../../catalog/models/open-meteo/climate.json) · Store page: https://www.sandbase.ai/model/open-meteo/climate

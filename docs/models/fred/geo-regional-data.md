# FRED GeoFRED Regional Data

`fred/geo-regional-data` · api · FRED

GeoFRED Regional Data from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/geo-regional-data", "date": "2023-01-01", "frequency": "a", "region_type": "state", "season": "NSA", "series_group": "882", "units": "Dollars"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/geo-regional-data', {'date': '2023-01-01', 'frequency': 'a', 'region_type': 'state', 'season': 'NSA', 'series_group': '882', 'units': 'Dollars'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/geo-regional-data", {
  "date": "2023-01-01",
  "frequency": "a",
  "region_type": "state",
  "season": "NSA",
  "series_group": "882",
  "units": "Dollars"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/geo-regional-data", sandbase.Params{
	"date": "2023-01-01",
	"frequency": "a",
	"region_type": "state",
	"season": "NSA",
	"series_group": "882",
	"units": "Dollars",
})
```

Same call via the path form: `POST /v1/api/fred/geo-regional-data` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `date` | string | yes | The date you want to pull a series group data from. YYYY-MM-DD formatted string, required  |
| `units` | string | yes | The units of the series you want to pull. string, required  |
| `season` | string | yes | The seasonality of the series group. string, required, five possible SA (Seasonally Adjusted), NSA (Not Seasonally Adjusted), SSA (Smoothed Seasonally Adjusted), SAAR (Seasonally Adjusted Annual Rate), or NSAAR (Not…  |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `frequency` | string | yes | Frequency automatically assigns the default frequency of the map when using the Request Wizard above. The parameter can be used as a frequency aggregation feature. The maps frequency aggregation feature converts higher… one of: `d`, `w`, `bw`, `m`, `q`, `sa`, `a`, `wef`, `weth`, `wew`, `wetu`, `wem` … |
| `start_date` | string |  | The start date you want to request series group data from. This allows you to pull a range of data YYYY-MM-DD formatted string, optional  |
| `region_type` | string | yes | The region you want to pull data for. string, required One of the following values: bea msa frb necta state country county censusregion bea msa frb necta state country county censusregion one of: `bea`, `msa`, `frb`, `necta`, `state`, `country`, `county`, `censusregion` |
| `series_group` | string | yes | The ID for a group of series found in FRED. string, required  |
| `transformation` | string |  | A key that indicates a data value transformation. string, optional, default: lin (No transformation) One of the following values: 'lin', 'chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log' lin = Levels (No… one of: `lin`, `chg`, `ch1`, `pch`, `pc1`, `pca`, `cch`, `cca`, `log`; default `"lin"` |
| `aggregation_method` | string |  | string, optional, default: avg One of the following values: 'avg', 'sum', 'eop' avg = Average sum = Sum eop = End of Period avg = Average sum = Sum eop = End of Period one of: `avg`, `sum`, `eop`; default `"avg"` |

## Details

GeoFRED Regional Data from FRED. Returns the official FRED API response unchanged.

The response is the official FRED API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/geo-regional-data" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"date": "2023-01-01", "frequency": "a", "region_type": "state", "season": "NSA", "series_group": "882", "units": "Dollars", "file_type": "json"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aggregation_method` | string | No | string, optional, default: avg One of the following values: 'avg', 'sum', 'eop' avg = Average sum = Sum eop = End of Period avg = Average sum = Sum eop = End of |
| `date` | string | Yes | The date you want to pull a series group data from. YYYY-MM-DD formatted string, required |
| `file_type` | string | No | Response format. Only json is supported. |
| `frequency` | string | Yes | Frequency automatically assigns the default frequency of the map when using the Request Wizard above. The parameter can be used as a frequency aggregation featu |
| `region_type` | string | Yes | The region you want to pull data for. string, required One of the following values: bea msa frb necta state country county censusregion bea msa frb necta state  |
| `season` | string | Yes | The seasonality of the series group. string, required, five possible SA (Seasonally Adjusted), NSA (Not Seasonally Adjusted), SSA (Smoothed Seasonally Adjusted) |
| `series_group` | string | Yes | The ID for a group of series found in FRED. string, required |
| `start_date` | string | No | The start date you want to request series group data from. This allows you to pull a range of data YYYY-MM-DD formatted string, optional |
| `transformation` | string | No | A key that indicates a data value transformation. string, optional, default: lin (No transformation) One of the following values: 'lin', 'chg', 'ch1', 'pch', 'p |
| `units` | string | Yes | The units of the series you want to pull. string, required |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/fred/geo-regional-data.json`](../../../catalog/models/fred/geo-regional-data.json) · Store page: https://www.sandbase.ai/model/fred/geo-regional-data

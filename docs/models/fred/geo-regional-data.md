# FRED GeoFRED Regional Data API: pricing, parameters and code examples

`fred/geo-regional-data` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

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

Returns one value per region for a FRED GeoFRED series group on a single date. You pass a `series_group` ID, a `region_type`, a `date`, a `frequency`, a `season` and `units`.

### Use cases

- Compare per capita personal income across all US states for one year.
- Build a state-level choropleth map from the `value` for each `code`.
- Rank regions by a series group value on a given date.
- Join regional values to other datasets using the `code` and `series_id` of each region.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/geo-regional-data" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"date": "2023-01-01", "frequency": "a", "region_type": "state", "season": "NSA", "series_group": "882", "units": "Dollars", "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `date` | string | Yes | The date you want to pull a series group data from. YYYY-MM-DD formatted string, required |
| `frequency` | string | Yes | Frequency automatically assigns the default frequency of the map when using the Request Wizard above. The parameter can be used as a frequency aggregation feature. The maps frequency aggregation feature converts higher f |
| `region_type` | string | Yes | The region you want to pull data for. string, required One of the following values: bea msa frb necta state country county censusregion bea msa frb necta state country county censusregion |
| `season` | string | Yes | The seasonality of the series group. string, required, five possible SA (Seasonally Adjusted), NSA (Not Seasonally Adjusted), SSA (Smoothed Seasonally Adjusted), SAAR (Seasonally Adjusted Annual Rate), or NSAAR (Not Seas |
| `series_group` | string | Yes | The ID for a group of series found in FRED. string, required |
| `units` | string | Yes | The units of the series you want to pull. string, required |
| `aggregation_method` | string | No | string, optional, default: avg One of the following values: 'avg', 'sum', 'eop' avg = Average sum = Sum eop = End of Period avg = Average sum = Sum eop = End of Period |
| `file_type` | string | No | Response format. Only json is supported. |
| `start_date` | string | No | The start date you want to request series group data from. This allows you to pull a range of data YYYY-MM-DD formatted string, optional |
| `transformation` | string | No | A key that indicates a data value transformation. string, optional, default: lin (No transformation) One of the following values: 'lin', 'chg', 'ch1', 'pch', 'pc1', 'pca', 'cch', 'cca', 'log' lin = Levels (No transformat |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "meta": {
    "data": {
      "2023-01-01": [
        {
          "code": "01",
          "region": "Alabama",
          "series_id": "ALPCPI",
          "value": 54760
        }
      ]
    },
    "frequency": "Annual",
    "region": "state",
    "seasonality": "Not Seasonally Adjusted",
    "title": "2025 Per Capita Personal Income by State (Dollars)",
    "units": "Dollars"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `meta.title` | Title of the map. It names the measure, the region level and the units. |
| `meta.data` | Object keyed by date in `YYYY-MM-DD` format. Each key holds a list of regional values for that date. |
| `meta.data.*[].region` | Name of the region, for example `Alabama`. |
| `meta.data.*[].code` | Short code for the region. In this response it is a two-digit string for each state. |
| `meta.data.*[].series_id` | FRED series ID for this region, for example `ALPCPI`. You can use it with other FRED APIs. |
| `meta.data.*[].value` | Value of the series for the region on that date, in the units named in `meta.units`. |
| `meta.frequency / meta.seasonality` | Frequency and seasonal adjustment of the data, written out in full, such as `Annual` and `Not Seasonally Adjusted`. |
| `meta.region / meta.units` | Region type and units that were applied to the request. |

### Notes

- The key under `meta.data` is the requested `date`. The `*` in a path stands for that date key.
- Use [FRED GeoFRED Series Group](/apis/fred/geo-series-group) to look up valid `series_group` values and their details.
- Use the `series_id` from a row with [FRED Get Series Observations](/apis/fred/series-observations) to get the full history for one region.
- Set `start_date` to request a range of dates instead of a single date.

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/geo-regional-data.json`](../../../catalog/models/fred/geo-regional-data.json) · Store page: https://www.sandbase.ai/model/fred/geo-regional-data

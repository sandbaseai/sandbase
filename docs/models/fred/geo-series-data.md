# FRED GeoFRED Series Data API: pricing, parameters and code examples

`fred/geo-series-data` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

GeoFRED Series Data from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/geo-series-data", "series_id": "WIPCPI"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/geo-series-data', {'series_id': 'WIPCPI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/geo-series-data", {
  "series_id": "WIPCPI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/geo-series-data", sandbase.Params{
	"series_id": "WIPCPI",
})
```

Same call via the path form: `POST /v1/api/fred/geo-series-data` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `date` | string |  | The date you want to request series group data from. YYYY-MM-DD formatted string, optional  |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `series_id` | string | yes | The FRED series_id you want to request maps data for. Not all series that are in FRED have geographical data. string, required  |
| `start_date` | string |  | The start date you want to request series group data from. This allows you to pull a range of data YYYY-MM-DD formatted string, optional  |

## Details

Returns map data for a FRED series that has geographic values, such as per-state figures for one date. You pass a `series_id` like `WIPCPI`, and you can add `date` or `start_date` to pick the time period.

### Use cases

- Build a state-level choropleth map of per capita personal income.
- Rank US states by a single indicator for one year.
- Pull the regional series IDs for each state, then fetch their full histories.
- Compare a state's value against the national spread in a dashboard.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/geo-series-data" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"series_id": "WIPCPI", "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `series_id` | string | Yes | The FRED series_id you want to request maps data for. Not all series that are in FRED have geographical data. string, required |
| `date` | string | No | The date you want to request series group data from. YYYY-MM-DD formatted string, optional |
| `file_type` | string | No | Response format. Only json is supported. |
| `start_date` | string | No | The start date you want to request series group data from. This allows you to pull a range of data YYYY-MM-DD formatted string, optional |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "meta": {
    "data": {
      "2025-01-01": [
        {
          "code": "01",
          "region": "Alabama",
          "series_id": "ALPCPI",
          "value": 59754
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
| `meta.title` | Name of the data set, including the year, the measure and the region type. |
| `meta.units` | Unit of the values, such as `Dollars`. |
| `meta.frequency / meta.seasonality` | How often the series is published (for example `Annual`) and whether it is seasonally adjusted. |
| `meta.region` | Type of geographic region the values cover, such as `state`. |
| `meta.data` | Object keyed by date in YYYY-MM-DD format. Each key holds a list of regional values for that date. |
| `meta.data.*[].region` | Name of the region, such as `Alabama`. |
| `meta.data.*[].code` | Short region code. For states it looks like a two-digit string such as `01`. |
| `meta.data.*[].series_id` | FRED series ID for that region's own series, such as `ALPCPI`. |
| `meta.data.*[].value` | Value for that region on that date, in the units given by `meta.units`. |

### Notes

- `series_id` is required. Not every FRED series has geographic data.
- Use `date` to request one date, or `start_date` to pull a range. Both use YYYY-MM-DD format.
- Each region row has its own `series_id`. Pass it to [FRED Get Series Observations](/apis/fred/series-observations) to get that region's history.
- To find other series that share a group, try [FRED GeoFRED Series Group](/apis/fred/geo-series-group).

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/geo-series-data.json`](../../../catalog/models/fred/geo-series-data.json) · Store page: https://www.sandbase.ai/model/fred/geo-series-data

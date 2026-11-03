# FRED GeoFRED Series Group API: pricing, parameters and code examples

`fred/geo-series-group` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

GeoFRED Series Group from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/geo-series-group", "series_id": "WIPCPI"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/geo-series-group', {'series_id': 'WIPCPI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/geo-series-group", {
  "series_id": "WIPCPI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/geo-series-group", sandbase.Params{
	"series_id": "WIPCPI",
})
```

Same call via the path form: `POST /v1/api/fred/geo-series-group` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `series_id` | string | yes | The FRED series id you want to request maps meta information for. Not all series that are in FRED have geographical data. string, required  |

## Details

This API returns GeoFRED map metadata for one FRED series. It tells you the series group, region type, frequency, date range and units. It needs a FRED `series_id` that has geographic data, such as `WIPCPI`.

### Use cases

- Check whether a FRED series can be mapped by state before you request regional data.
- Read the `series_group` id and `region_type` that you need for GeoFRED map requests.
- Find the first and last date of a regional series to set a valid date range.
- Show the title, units and frequency of a map series in a dashboard label.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/geo-series-group" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"series_id": "WIPCPI", "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `series_id` | string | Yes | The FRED series id you want to request maps meta information for. Not all series that are in FRED have geographical data. string, required |
| `file_type` | string | No | Response format. Only json is supported. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "series_group": {
    "frequency": "Annual",
    "max_date": "2025-01-01",
    "min_date": "1929-01-01",
    "region_type": "state",
    "season": "NSA",
    "series_group": "882",
    "title": "Per Capita Personal Income",
    "units": "Dollars"
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `series_group.series_group` | The id of the series group, for example `882`. Use it to identify the group in GeoFRED requests. |
| `series_group.title` | The name of the series group, for example `Per Capita Personal Income`. |
| `series_group.region_type` | The type of region the data covers, for example `state`. |
| `series_group.frequency` | How often the series reports values, for example `Annual`. |
| `series_group.units` | The units of the values, for example `Dollars`. |
| `series_group.season` | The seasonal adjustment label, for example `NSA`. |
| `series_group.min_date / series_group.max_date` | The first and last dates with data, in `YYYY-MM-DD` format. |

### Notes

- Not every FRED series has geographic data. Use a `series_id` that is part of GeoFRED.
- Call [FRED GeoFRED Series Data](/apis/fred/geo-series-data) to get the values for a series.
- Call [FRED GeoFRED Regional Data](/apis/fred/geo-regional-data) to get values across regions, and [FRED GeoFRED Shape Files](/apis/fred/geo-shapes-file) to get map shapes.

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/geo-series-group.json`](../../../catalog/models/fred/geo-series-group.json) · Store page: https://www.sandbase.ai/model/fred/geo-series-group

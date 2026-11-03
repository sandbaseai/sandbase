# FRED Get Series API: pricing, parameters and code examples

`fred/series` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Series from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/series", "series_id": "GDP"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/series', {'series_id': 'GDP'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/series", {
  "series_id": "GDP"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/series", sandbase.Params{
	"series_id": "GDP",
})
```

Same call via the path form: `POST /v1/api/fred/series` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `series_id` | string | yes | The id for a series. string, required  |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |

## Details

Returns metadata for one FRED economic data series, such as its title, units, frequency and date range. It needs a `series_id`, for example `GDP`.

### Use cases

- Show the title, units and update frequency of a series before you chart it.
- Check the `observation_start` and `observation_end` dates to see how much history a series covers.
- Read `seasonal_adjustment` to tell adjusted series from unadjusted ones.
- Sort candidate series by `popularity` when you build a series picker.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/series" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"series_id": "GDP"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `series_id` | string | Yes | The id for a series. string, required |
| `file_type` | string | No | Response format. Only json is supported. |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "realtime_end": "2026-10-29",
  "realtime_start": "2026-10-29",
  "seriess": [
    {
      "frequency": "Quarterly",
      "frequency_short": "Q",
      "id": "GDP",
      "last_updated": "2026-10-29 08:03:33-05",
      "notes": "BEA Account Code: A191RC\n\nGross domestic product (GDP), the featured measure of …",
      "observation_end": "2026-07-01",
      "observation_start": "1947-01-01",
      "popularity": 92,
      "realtime_end": "2026-10-29",
      "realtime_start": "2026-10-29",
      "seasonal_adjustment": "Seasonally Adjusted Annual Rate",
      "seasonal_adjustment_short": "SAAR"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `seriess[]` | List of matching series. A request for one `series_id` returns one item. |
| `seriess[].id` | The series ID, such as `GDP`. Use it in other FRED calls. |
| `seriess[].title` | Full name of the series, such as `Gross Domestic Product`. |
| `seriess[].frequency / seriess[].frequency_short` | How often the series reports data, as a full word (`Quarterly`) and a short code (`Q`). |
| `seriess[].units / seriess[].units_short` | Unit of the values, in long form (`Billions of Dollars`) and short form (`Bil. of $`). |
| `seriess[].seasonal_adjustment / seriess[].seasonal_adjustment_short` | Seasonal adjustment of the series, in long form (`Seasonally Adjusted Annual Rate`) and short form (`SAAR`). |
| `seriess[].observation_start / seriess[].observation_end` | Dates of the first and last observation in the series, in `YYYY-MM-DD` format. |
| `seriess[].last_updated` | Timestamp of the last update to the series, with a time zone offset. |
| `seriess[].popularity` | Popularity score of the series. The value is `92` for `GDP`. |
| `seriess[].notes` | Free-text description of the series, including the source account code and a definition. |
| `realtime_start / realtime_end` | The real-time period the response applies to. Both are also repeated on each series. |

### Notes

- Use `realtime_start` and `realtime_end` in `YYYY-MM-DD` format to set the real-time period. Both default to today's date.
- This call returns metadata only. To get the data points, call [FRED Get Series Observations](/apis/fred/series-observations).
- To find a `series_id` when you do not have one, call [FRED Search Series](/apis/fred/series-search).
- To see which release a series belongs to, call [FRED Get Series Release](/apis/fred/series-release).

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/series.json`](../../../catalog/models/fred/series.json) · Store page: https://www.sandbase.ai/model/fred/series

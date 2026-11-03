# FRED Get Series Release API: pricing, parameters and code examples

`fred/series-release` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Series Release from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/series-release", "series_id": "GNPCA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/series-release', {'series_id': 'GNPCA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/series-release", {
  "series_id": "GNPCA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/series-release", sandbase.Params{
	"series_id": "GNPCA",
})
```

Same call via the path form: `POST /v1/api/fred/series-release` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `series_id` | string | yes | The id for a series. string, required  |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |

## Details

Returns the FRED data release that a series belongs to, such as the release name, ID and link to the source page. It needs a `series_id` such as `GNPCA`.

### Use cases

- Find which release publishes a given series, for example to label a chart with its source.
- Get the release `id` for a series, then pull all other series in that release.
- Check whether a series comes from a press release before you build an update schedule around it.
- Link a series to the publisher's page using the `link` value.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/series-release" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"series_id": "GNPCA", "file_type": "json"}'
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
  "realtime_end": "2026-11-03",
  "realtime_start": "2026-11-03",
  "releases": [
    {
      "id": 53,
      "link": "https://www.bea.gov/data/gdp/gross-domestic-product",
      "name": "Gross Domestic Product",
      "press_release": true,
      "realtime_end": "2026-11-03",
      "realtime_start": "2026-11-03"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `releases[].id` | Numeric ID of the release that contains the series. Use it with other FRED release APIs. |
| `releases[].name` | Name of the release, for example `Gross Domestic Product`. |
| `releases[].link` | URL of the web page for the release. |
| `releases[].press_release` | `true` if the release is a press release, `false` otherwise. |
| `releases[].realtime_start / releases[].realtime_end` | Real-time period for this release record, as YYYY-MM-DD dates. |
| `realtime_start / realtime_end` | Real-time period applied to the whole request, as YYYY-MM-DD dates. Both default to today's date. |

### Notes

- `series_id` is required. Use [FRED Search Series](/apis/fred/series-search) to find an ID if you do not have one.
- Pass `realtime_start` and `realtime_end` as YYYY-MM-DD strings to set the real-time period.
- Pass the returned `releases[].id` to [FRED Get Release](/apis/fred/release) for details, or to [FRED Get Release Series](/apis/fred/release-series) to list the other series in the release.

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/series-release.json`](../../../catalog/models/fred/series-release.json) · Store page: https://www.sandbase.ai/model/fred/series-release

# FRED Get Release API: pricing, parameters and code examples

`fred/release` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Release from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/release", "release_id": 53}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/release', {'release_id': 53})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/release", {
  "release_id": 53
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/release", sandbase.Params{
	"release_id": 53,
})
```

Same call via the path form: `POST /v1/api/fred/release` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `release_id` | integer | yes | The id for a release. integer, required  |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |

## Details

Returns details for one FRED data release, such as its name, its public link, and whether it has a press release. It needs a `release_id`, for example `53` for Gross Domestic Product.

### Use cases

- Show the name and source link of a release when you display a FRED series.
- Check whether a release is published with a press release before you build a news alert.
- Turn a stored `release_id` into a readable release name for a dashboard or report.
- Send users from a release ID to the publisher's page for the full data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/release" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"release_id": 53, "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `release_id` | integer | Yes | The id for a release. integer, required |
| `file_type` | string | No | Response format. Only json is supported. |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "realtime_end": "2026-11-02",
  "realtime_start": "2026-11-02",
  "releases": [
    {
      "id": 53,
      "link": "https://www.bea.gov/data/gdp/gross-domestic-product",
      "name": "Gross Domestic Product",
      "press_release": true,
      "realtime_end": "2026-11-02",
      "realtime_start": "2026-11-02"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `releases[]` | List of matching releases. A request for one `release_id` returns one item. |
| `releases[].id` | Numeric ID of the release. It matches the `release_id` you sent. |
| `releases[].name` | Name of the release, for example `Gross Domestic Product`. |
| `releases[].link` | URL of the release page on the publisher's website. |
| `releases[].press_release` | `true` if the release is a press release, `false` if not. |
| `releases[].realtime_start / releases[].realtime_end` | Start and end dates of the real-time period for this release, in `YYYY-MM-DD` format. |
| `realtime_start / realtime_end` | Start and end dates of the real-time period used for the request. Both default to today's date. |

### Notes

- Set `release_id` as an integer. To find IDs, call [FRED Get Releases](/apis/fred/releases), or call [FRED Series Release](/apis/fred/series-release) to get the release for a series.
- Use [FRED Get Release Dates](/apis/fred/release-dates) to see the dates on which this release is published.
- Use [FRED Get Release Series](/apis/fred/release-series) to list the series that belong to this release.
- Dates use the `YYYY-MM-DD` format. `file_type` accepts only `json`.

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/release.json`](../../../catalog/models/fred/release.json) · Store page: https://www.sandbase.ai/model/fred/release

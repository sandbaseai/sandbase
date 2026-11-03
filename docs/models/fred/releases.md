# FRED Get Releases API: pricing, parameters and code examples

`fred/releases` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Releases from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/releases"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/releases', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/releases", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/releases", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/fred/releases` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `order_by` | string |  | Order results by values of the specified attribute. One of the following strings: 'release_id', 'name', 'press_release', 'realtime_start', 'realtime_end'. optional, default: release_id one of: `release_id`, `name`, `press_release`, `realtime_start`, `realtime_end`; default `"release_id"` |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `sort_order` | string |  | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc one of: `asc`, `desc`; default `"asc"` |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |

## Details

Returns the list of all data releases published on FRED, with each release's ID, name, source link and press release flag. It needs no required input. You can page through results with `limit` and `offset` and sort them with `order_by` and `sort_order`.

### Use cases

- List every FRED release to build a browsable index of data publications.
- Find the `id` of a release by name, then use it to pull that release's series or dates.
- Filter for releases with `press_release` set to `true` to track headline economic reports.
- Collect the `link` values to send users to the original publisher page for each release.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/releases" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `file_type` | string | No | Response format. Only json is supported. |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'release_id', 'name', 'press_release', 'realtime_start', 'realtime_end'. optional, default: release_id |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `sort_order` | string | No | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 335,
  "limit": 1000,
  "offset": 0,
  "order_by": "release_id",
  "realtime_end": "2026-11-02",
  "realtime_start": "2026-11-02",
  "releases": [
    {
      "id": 1,
      "link": "https://www.fedsmallbusiness.org/about",
      "name": "Small Business Credit Survey",
      "notes": "The annual Small Business Credit Survey (SBCS) provides timely insights on small…",
      "press_release": true,
      "realtime_end": "2026-11-02",
      "realtime_start": "2026-11-02"
    }
  ],
  "sort_order": "asc"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count` | Total number of releases that match the request. Compare it with `limit` and `offset` to know how many pages exist. |
| `releases[].id` | Numeric ID of the release. Use it as the release identifier in other release APIs. |
| `releases[].name` | Name of the release, for example `Small Business Credit Survey`. |
| `releases[].link` | URL of the publisher page for the release. Some releases may not include it. |
| `releases[].notes` | Short text describing the release. Some releases have no `notes` field. |
| `releases[].press_release` | `true` if the release is a press release, `false` if not. |
| `releases[].realtime_start / releases[].realtime_end` | Start and end dates of the real-time period for this release entry, in YYYY-MM-DD format. |
| `limit / offset / order_by / sort_order` | Echo of the paging and sorting settings applied to this response. |

### Notes

- Use `limit` (1 to 1000) and `offset` to page through the list. Compare `count` with `offset` plus `limit` to see if more results remain.
- `realtime_start` and `realtime_end` take YYYY-MM-DD dates and both default to today's date.
- Pass a release `id` to [FRED Get Release](/apis/fred/release) for one release, or to [FRED Get Release Series](/apis/fred/release-series) to list its series.
- For publication dates of releases, call [FRED Get Releases Dates](/apis/fred/releases-dates).

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/releases.json`](../../../catalog/models/fred/releases.json) · Store page: https://www.sandbase.ai/model/fred/releases

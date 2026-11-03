# FRED Get Source Releases API: pricing, parameters and code examples

`fred/source-releases` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Source Releases from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/source-releases", "source_id": 1}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/source-releases', {'source_id': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/source-releases", {
  "source_id": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/source-releases", sandbase.Params{
	"source_id": 1,
})
```

Same call via the path form: `POST /v1/api/fred/source-releases` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `order_by` | string |  | Order results by values of the specified attribute. One of the following strings: 'release_id', 'name', 'press_release', 'realtime_start', 'realtime_end'. optional, default: release_id one of: `release_id`, `name`, `press_release`, `realtime_start`, `realtime_end`; default `"release_id"` |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `source_id` | integer | yes | The id for a source. integer, required  |
| `sort_order` | string |  | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc one of: `asc`, `desc`; default `"asc"` |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |

## Details

Returns the list of FRED data releases that come from one source, such as a government agency or central bank. It needs a `source_id` and returns each release with its ID, name, link, and press release flag.

### Use cases

- List every release published by one source, for example all releases tied to `source_id` 1.
- Build a catalog of release names and links for a single data publisher.
- Find which releases of a source are press releases by checking the `press_release` flag.
- Collect release IDs to pass to other release endpoints that look up series, dates, or tags.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/source-releases" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"source_id": 1, "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `source_id` | integer | Yes | The id for a source. integer, required |
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
  "count": 37,
  "limit": 1000,
  "offset": 0,
  "order_by": "release_id",
  "realtime_end": "2026-11-02",
  "realtime_start": "2026-11-02",
  "releases": [
    {
      "id": 3,
      "link": "https://home.treasury.gov/data/treasury-international-capital-tic-system",
      "name": "Treasury International Capital: Continuous Securities Long Term (CSLT)",
      "press_release": false,
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
| `count` | Total number of releases found for the source. Compare it with `limit` and `offset` to see if more pages remain. |
| `releases[].id` | Numeric ID of the release. Use it as the release ID in other FRED release APIs. |
| `releases[].name` | Name of the release, for example `G.17 Industrial Production and Capacity Utilization`. |
| `releases[].link` | URL of the release page on the publisher's website. |
| `releases[].press_release` | `true` if the release is a press release, `false` if not. |
| `releases[].notes` | Free text notes about the release, such as contact details for questions about the data. This key is missing on some releases. |
| `releases[].realtime_start / releases[].realtime_end` | Start and end dates of the real-time period for this release record. Format is `YYYY-MM-DD`. |
| `limit / offset` | Page size and starting position used for this response. |
| `order_by / sort_order` | Sort field and direction applied to the list. The response shows `release_id` and `asc` by default. |

### Notes

- `source_id` is required. Get valid IDs from [FRED Get Sources](/apis/fred/sources), or check one source with [FRED Get Source](/apis/fred/source).
- Page through results with `limit` (1 to 1000) and `offset`. Compare `count` to the number of rows already fetched.
- Pass a `releases[].id` value to [FRED Get Release](/apis/fred/release) to see more about a single release.
- `realtime_start` and `realtime_end` take `YYYY-MM-DD` dates and both default to today.

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/source-releases.json`](../../../catalog/models/fred/source-releases.json) · Store page: https://www.sandbase.ai/model/fred/source-releases

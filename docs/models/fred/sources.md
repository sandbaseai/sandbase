# FRED Get Sources API: pricing, parameters and code examples

`fred/sources` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Sources from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/sources"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/sources', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/sources", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/sources", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/fred/sources` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `order_by` | string |  | Order results by values of the specified attribute. One of the following strings: 'source_id', 'name', 'realtime_start', 'realtime_end'. optional, default: source_id one of: `source_id`, `name`, `realtime_start`, `realtime_end`; default `"source_id"` |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `sort_order` | string |  | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc one of: `asc`, `desc`; default `"asc"` |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |

## Details

Returns the list of data sources that FRED tracks, such as the Board of Governors of the Federal Reserve System. Each source has an ID, a name, and a website link. No input is required, and you can page, sort, and set a real-time period with optional parameters.

### Use cases

- Build a directory of the organizations that publish data in FRED.
- Look up the numeric `id` of a source before you request its details or releases.
- Show a source name and website link next to a FRED series in a dashboard.
- Sort sources by `name` to build an A to Z picker.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/sources" \
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
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'source_id', 'name', 'realtime_start', 'realtime_end'. optional, default: source_id |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `sort_order` | string | No | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 127,
  "limit": 1000,
  "offset": 0,
  "order_by": "source_id",
  "realtime_end": "2026-11-03",
  "realtime_start": "2026-11-03",
  "sort_order": "asc",
  "sources": [
    {
      "id": 1,
      "link": "https://www.federalreserve.gov",
      "name": "Board of Governors of the Federal Reserve System (US)",
      "realtime_end": "2026-11-03",
      "realtime_start": "2026-11-03"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count` | Total number of sources that match the request. In this response it is 127. |
| `limit / offset` | Page size and starting position used for this response. Use them to page through the list. |
| `order_by / sort_order` | The attribute and direction used to sort the sources. |
| `realtime_start / realtime_end` | The real-time period the request covers, as `YYYY-MM-DD` dates. Each source also carries its own pair of these fields. |
| `sources[].id` | Numeric ID of the source. Use it to identify the source in related FRED calls. |
| `sources[].name` | Full name of the organization, for example `Federal Reserve Bank of Philadelphia`. |
| `sources[].link` | Website URL of the source. This field is not present for every source in every case, so check before you use it. |

### Notes

- All parameters are optional. A call with only `file_type` set to `json` returns up to 1000 sources, starting at `offset` 0.
- To page through results, raise `offset` by the value of `limit` until you pass `count`.
- Use `order_by` with `source_id`, `name`, `realtime_start`, or `realtime_end`, and set `sort_order` to `asc` or `desc`.
- To get one source by its `id`, call [FRED Get Source](/apis/fred/source). To see the releases a source publishes, call [FRED Get Source Releases](/apis/fred/source-releases).

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/sources.json`](../../../catalog/models/fred/sources.json) · Store page: https://www.sandbase.ai/model/fred/sources

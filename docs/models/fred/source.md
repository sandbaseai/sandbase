# FRED Get Source API: pricing, parameters and code examples

`fred/source` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Source from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/source", "source_id": 1}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/source', {'source_id': 1})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/source", {
  "source_id": 1
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/source", sandbase.Params{
	"source_id": 1,
})
```

Same call via the path form: `POST /v1/api/fred/source` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `source_id` | integer | yes | The id for a source. integer, required  |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |

## Details

Returns details for one data source in FRED, such as the Federal Reserve Board. It needs a numeric `source_id` and returns the source name, website link, and the real-time period used for the lookup.

### Use cases

- Show the full name and website of the organization behind a FRED data set.
- Turn a `source_id` from a release or series lookup into a readable source name.
- Add a source credit and link to a chart or report built on FRED data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/source" \
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
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "realtime_end": "2026-11-02",
  "realtime_start": "2026-11-02",
  "sources": [
    {
      "id": 1,
      "link": "https://www.federalreserve.gov",
      "name": "Board of Governors of the Federal Reserve System (US)",
      "realtime_end": "2026-11-02",
      "realtime_start": "2026-11-02"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `sources[]` | List of matching sources. A request with one `source_id` returns one item. |
| `sources[].id` | Numeric ID of the source. It matches the `source_id` you sent. |
| `sources[].name` | Full name of the organization that publishes the data, for example `Board of Governors of the Federal Reserve System (US)`. |
| `sources[].link` | Website URL of the source. |
| `realtime_start / realtime_end` | Start and end dates of the real-time period for the response, in `YYYY-MM-DD` format. |
| `sources[].realtime_start / sources[].realtime_end` | Real-time period applied to this source record, in `YYYY-MM-DD` format. |

### Notes

- Find `source_id` values with [FRED Get Sources](/apis/fred/sources) or [FRED Get Release Sources](/apis/fred/release-sources).
- To list the releases that come from this source, call [FRED Get Source Releases](/apis/fred/source-releases) with the same `source_id`.
- `realtime_start` and `realtime_end` are optional and take `YYYY-MM-DD` dates. Both default to today's date.

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/source.json`](../../../catalog/models/fred/source.json) · Store page: https://www.sandbase.ai/model/fred/source

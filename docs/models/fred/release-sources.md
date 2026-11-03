# FRED Get Release Sources API: pricing, parameters and code examples

`fred/release-sources` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Release Sources from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/release-sources", "release_id": 53}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/release-sources', {'release_id': 53})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/release-sources", {
  "release_id": 53
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/release-sources", sandbase.Params{
	"release_id": 53,
})
```

Same call via the path form: `POST /v1/api/fred/release-sources` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `release_id` | integer | yes | The id for a release. integer, required  |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |

## Details

Returns the data sources behind one FRED release. Each source has an id, a name, and a link to the publisher's website. You pass a `release_id`, for example `53`.

### Use cases

- Show which agency publishes a given FRED release on a data page or citation.
- Build source attribution for charts that use series from a specific release.
- Map a release to its source id, then list every release from that source.
- Check the real-time period that applies to a source record before you cite it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/release-sources" \
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
  "sources": [
    {
      "id": 18,
      "link": "http://www.bea.gov/",
      "name": "U.S. Bureau of Economic Analysis",
      "realtime_end": "2026-11-02",
      "realtime_start": "2026-11-02"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `sources[]` | List of sources for the release. The sample returns one source. |
| `sources[].id` | Numeric id of the source. Use it with the source APIs. |
| `sources[].name` | Name of the source, such as `U.S. Bureau of Economic Analysis`. |
| `sources[].link` | Website URL of the source. |
| `sources[].realtime_start / sources[].realtime_end` | Real-time period for this source record, as `YYYY-MM-DD` dates. |
| `realtime_start / realtime_end` | Real-time period applied to the whole request. Both default to today's date when you leave them out. |

### Notes

- Get a `release_id` from [FRED Get Releases](/apis/fred/releases) or from [FRED Get Series Release](/apis/fred/series-release).
- Use the returned `sources[].id` with [FRED Get Source](/apis/fred/source) for details about the source.
- Set `realtime_start` and `realtime_end` as `YYYY-MM-DD` strings. `file_type` accepts only `json`.

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/release-sources.json`](../../../catalog/models/fred/release-sources.json) · Store page: https://www.sandbase.ai/model/fred/release-sources

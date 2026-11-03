# FRED Get Series Tags API: pricing, parameters and code examples

`fred/series-tags` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Series Tags from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/series-tags", "series_id": "GNPCA"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/series-tags', {'series_id': 'GNPCA'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/series-tags", {
  "series_id": "GNPCA"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/series-tags", sandbase.Params{
	"series_id": "GNPCA",
})
```

Same call via the path form: `POST /v1/api/fred/series-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `order_by` | string |  | Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default: series_count one of: `series_count`, `popularity`, `created`, `name`, `group_id`; default `"series_count"` |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `series_id` | string | yes | The id for a series. string, required  |
| `sort_order` | string |  | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc one of: `asc`, `desc`; default `"asc"` |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |

## Details

Returns the FRED tags attached to one economic data series. Each tag includes its group, a short description, a popularity score, and the number of series that use it. The only required input is `series_id`, such as `GNPCA`.

### Use cases

- List the tags on a series such as `GNPCA` to see how FRED classifies it, for example `gnp` or `nipa`.
- Sort a series' tags by `popularity` to pick the best tag for finding similar series.
- Build a tag filter or label display for a series page using `name` and `notes`.
- Find broad tags with a high `series_count` and use them to browse related data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/series-tags" \
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
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default: series_count |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `sort_order` | string | No | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 10,
  "limit": 1000,
  "offset": 0,
  "order_by": "series_count",
  "realtime_end": "2026-11-03",
  "realtime_start": "2026-11-03",
  "sort_order": "asc",
  "tags": [
    {
      "created": "2012-02-27 10:18:19-06",
      "group_id": "gen",
      "name": "gnp",
      "notes": "Gross National Product",
      "popularity": 28,
      "series_count": 268
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count` | Total number of tags attached to the series. |
| `limit / offset` | Page size and starting position of the returned tag list. The sample shows `limit` 1000 and `offset` 0. |
| `order_by / sort_order` | Sort attribute and direction applied to the tags. The sample shows `series_count` and `asc`. |
| `realtime_start / realtime_end` | Real-time period applied to the request, as YYYY-MM-DD dates. |
| `tags[].name` | Tag name, for example `gnp` or `nipa`. Use it as a tag value in other FRED calls. |
| `tags[].notes` | Short description of the tag. It can be an empty string. |
| `tags[].group_id` | Group the tag belongs to, for example `gen` or `rls`. |
| `tags[].popularity` | Popularity score of the tag. Higher values mean a more popular tag. |
| `tags[].series_count` | Number of series that carry this tag. |
| `tags[].created` | Timestamp when the tag was created, with a UTC offset, such as `2012-02-27 10:18:19-06`. |

### Notes

- `series_id` is the FRED series ID. You can find one with [FRED Search Series](/apis/fred/series-search).
- Use `order_by` (`series_count`, `popularity`, `created`, `name`, `group_id`) and `sort_order` (`asc`, `desc`) to change the tag order.
- To find other series that carry a tag, pass its `name` to [FRED Get Tags Series](/apis/fred/tags-series).
- To see tags that often appear with a given tag, call [FRED Get Related Tags](/apis/fred/related-tags).

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/series-tags.json`](../../../catalog/models/fred/series-tags.json) · Store page: https://www.sandbase.ai/model/fred/series-tags

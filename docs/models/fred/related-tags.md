# FRED Get Related Tags API: pricing, parameters and code examples

`fred/related-tags` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Related Tags from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/related-tags", "tag_names": "usa"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/related-tags', {'tag_names': 'usa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/related-tags", {
  "tag_names": "usa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/related-tags", sandbase.Params{
	"tag_names": "usa",
})
```

Same call via the path form: `POST /v1/api/fred/related-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `order_by` | string |  | Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default: series_count one of: `series_count`, `popularity`, `created`, `name`, `group_id`; default `"series_count"` |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `tag_names` | string | yes | A semicolon delimited list of tag names that series match all of. See the related request fred/tags . String, required, no default value. Example value: 'monetary+aggregates;weekly'. Find the related tags for series…  |
| `sort_order` | string |  | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc one of: `asc`, `desc`; default `"asc"` |
| `search_text` | string |  | The words to find matching tags with. String, optional, no filtering by search words by default.  |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `tag_group_id` | string |  | A tag group id to filter tags by type. String, optional, no filtering by tag group by default. One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'. freq = Frequency gen = General or Concept geo =…  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `exclude_tag_names` | string |  | A semicolon delimited list of tag names that series match none of. String, optional, no default value. Example value: 'discontinued;currency'. Find the related tags for series having neither tag 'discontinued' nor tag…  |

## Details

Returns FRED tags that appear on the same series as the tags you give. You pass one or more tag names in `tag_names`, and each result includes the tag's group, popularity and number of series.

### Use cases

- List the tags that co-occur with `usa` to find narrower topics for a US data search.
- Filter by `tag_group_id` to see only related geography, frequency or source tags for a tag set.
- Sort by `popularity` to find the most used tags linked to a topic.
- Build a tag browser that lets users refine a FRED series search step by step.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/related-tags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"tag_names": "usa", "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `tag_names` | string | Yes | A semicolon delimited list of tag names that series match all of. See the related request fred/tags . String, required, no default value. Example value: 'monetary+aggregates;weekly'. Find the related tags for series havi |
| `exclude_tag_names` | string | No | A semicolon delimited list of tag names that series match none of. String, optional, no default value. Example value: 'discontinued;currency'. Find the related tags for series having neither tag 'discontinued' nor tag 'c |
| `file_type` | string | No | Response format. Only json is supported. |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default: series_count |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `search_text` | string | No | The words to find matching tags with. String, optional, no filtering by search words by default. |
| `sort_order` | string | No | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc |
| `tag_group_id` | string | No | A tag group id to filter tags by type. String, optional, no filtering by tag group by default. One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'. freq = Frequency gen = General or Concept geo = Geo |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 5956,
  "limit": 1000,
  "offset": 0,
  "order_by": "series_count",
  "realtime_end": "2026-11-02",
  "realtime_start": "2026-11-02",
  "sort_order": "asc",
  "tags": [
    {
      "created": "2015-04-01 08:44:27-05",
      "group_id": "gen",
      "name": "0 to 14 years",
      "notes": "",
      "popularity": 16,
      "series_count": 2
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count` | Total number of related tags that match the request, across all pages. |
| `limit / offset` | Page size and starting position used for this response. |
| `order_by / sort_order` | The attribute and direction used to sort the tags. In this response they are `series_count` and `asc`. |
| `realtime_start / realtime_end` | The real-time period applied to the request, as YYYY-MM-DD dates. |
| `tags[].name` | The tag name. Use it in `tag_names` for other FRED calls. |
| `tags[].group_id` | The tag group the tag belongs to, such as `gen` for General or Concept. |
| `tags[].series_count` | Number of series that carry this tag in the matched set. |
| `tags[].popularity` | Popularity score of the tag. Values can be negative. |
| `tags[].created` | Timestamp of when the tag was created, with a UTC offset. |
| `tags[].notes` | Free-text note on the tag. It is often an empty string. |

### Notes

- `tag_names` is required. Separate several names with semicolons, for example `monetary+aggregates;weekly`. Use [FRED Get Tags](/apis/fred/tags) to find valid tag names.
- Page through results with `limit` (1 to 1000, default 1000) and `offset`. Compare `count` with `offset` plus `limit` to see if more pages remain.
- Results default to `order_by` `series_count` in ascending order. Set `sort_order` to `desc` to see the most used tags first.
- To get the series that carry a tag set, call [FRED Get Tags Series](/apis/fred/tags-series).

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/related-tags.json`](../../../catalog/models/fred/related-tags.json) · Store page: https://www.sandbase.ai/model/fred/related-tags

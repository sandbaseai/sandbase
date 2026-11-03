# FRED Search Series Tags API: pricing, parameters and code examples

`fred/series-search-tags` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Search Series Tags from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/series-search-tags", "series_search_text": "unemployment"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/series-search-tags', {'series_search_text': 'unemployment'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/series-search-tags", {
  "series_search_text": "unemployment"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/series-search-tags", sandbase.Params{
	"series_search_text": "unemployment",
})
```

Same call via the path form: `POST /v1/api/fred/series-search-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `order_by` | string |  | Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default: series_count one of: `series_count`, `popularity`, `created`, `name`, `group_id`; default `"series_count"` |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `tag_names` | string |  | A semicolon delimited list of tag names to only include in the response. See the related request fred/series/search/related_tags . String, optional, no filtering by tag names by default Example value: 'm1;m2'. This…  |
| `sort_order` | string |  | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc one of: `asc`, `desc`; default `"asc"` |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `tag_group_id` | string |  | A tag group id to filter tags by type. String, optional, no filtering by tag group by default. One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'. freq = Frequency gen = General or Concept geo =…  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `tag_search_text` | string |  | The words to find matching tags with. String, optional, no filtering by search words by default.  |
| `series_search_text` | string | yes | The words to match against economic data series. string, required  |

## Details

Returns the FRED tags attached to economic data series that match a search phrase. You pass the search words in `series_search_text`, and each tag comes back with its group, popularity and the number of matching series.

### Use cases

- List the tags that describe series matching "unemployment" to build a filter menu for a search page.
- Find which geography or frequency tags apply to a topic before you narrow a series search.
- Rank tags by `popularity` or `series_count` to see which concepts dominate a topic.
- Look up a tag by name with `tag_search_text` to check how many matching series carry it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/series-search-tags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"series_search_text": "unemployment", "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `series_search_text` | string | Yes | The words to match against economic data series. string, required |
| `file_type` | string | No | Response format. Only json is supported. |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default: series_count |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `sort_order` | string | No | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc |
| `tag_group_id` | string | No | A tag group id to filter tags by type. String, optional, no filtering by tag group by default. One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'. freq = Frequency gen = General or Concept geo = Geo |
| `tag_names` | string | No | A semicolon delimited list of tag names to only include in the response. See the related request fred/series/search/related_tags . String, optional, no filtering by tag names by default Example value: 'm1;m2'. This value |
| `tag_search_text` | string | No | The words to find matching tags with. String, optional, no filtering by search words by default. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 4342,
  "limit": 1000,
  "offset": 0,
  "order_by": "series_count",
  "realtime_end": "2026-11-02",
  "realtime_start": "2026-11-02",
  "sort_order": "asc",
  "tags": [
    {
      "created": "2012-02-27 10:18:19-06",
      "group_id": "gen",
      "name": "1-month",
      "notes": "",
      "popularity": 37,
      "series_count": 2
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count` | Total number of tags that match the request. Use it with `limit` and `offset` to page through results. |
| `limit / offset` | The page size and starting position used for this response. |
| `order_by / sort_order` | The attribute and direction used to sort the tags in this response. |
| `realtime_start / realtime_end` | The real-time period applied to the request, as `YYYY-MM-DD` dates. |
| `tags[].name` | The tag name. Pass it in `tag_names` to filter on this tag. |
| `tags[].group_id` | The tag group this tag belongs to, such as `gen` for General or Concept. It matches the values accepted by `tag_group_id`. |
| `tags[].series_count` | Number of series that carry this tag within the matched results. |
| `tags[].popularity` | A popularity score for the tag. Values can be negative. |
| `tags[].created` | Timestamp when the tag was created, with a UTC offset, for example `2012-02-27 10:18:19-06`. |
| `tags[].notes` | Free text note about the tag. It is often an empty string. |

### Notes

- `series_search_text` is the only required parameter.
- Page through results with `limit` (1 to 1000) and `offset`. Compare `offset` plus the number of returned tags with `count` to see if more remain.
- The default sort is `series_count` in ascending order. Set `sort_order` to `desc` to see the most used tags first.
- To search series themselves, use [FRED Search Series](/apis/fred/series-search). For tags related to a search plus chosen tags, use [FRED Search Series Related Tags](/apis/fred/series-search-related-tags).

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/series-search-tags.json`](../../../catalog/models/fred/series-search-tags.json) · Store page: https://www.sandbase.ai/model/fred/series-search-tags

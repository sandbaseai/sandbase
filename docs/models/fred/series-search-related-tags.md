# FRED Search Series Related Tags API: pricing, parameters and code examples

`fred/series-search-related-tags` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Search Series Related Tags from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/series-search-related-tags", "series_search_text": "unemployment", "tag_names": "usa"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/series-search-related-tags', {'series_search_text': 'unemployment', 'tag_names': 'usa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/series-search-related-tags", {
  "series_search_text": "unemployment",
  "tag_names": "usa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/series-search-related-tags", sandbase.Params{
	"series_search_text": "unemployment",
	"tag_names": "usa",
})
```

Same call via the path form: `POST /v1/api/fred/series-search-related-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `order_by` | string |  | Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default: series_count one of: `series_count`, `popularity`, `created`, `name`, `group_id`; default `"series_count"` |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `tag_names` | string | yes | A semicolon delimited list of tag names that series match all of. See the related request fred/series/search/tags . String, required, no default value. Example value: '30-year;frb'. Find the related tags for series…  |
| `sort_order` | string |  | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc one of: `asc`, `desc`; default `"asc"` |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `tag_group_id` | string |  | A tag group id to filter tags by type. String, optional, no filtering by tag group by default. One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'. freq = Frequency gen = General or Concept geo =…  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `tag_search_text` | string |  | The words to find matching tags with. String, optional, no filtering by search words by default.  |
| `exclude_tag_names` | string |  | A semicolon delimited list of tag names that series match none of. String, optional, no default value. Example value: 'discontinued;monthly'. Find the related tags for series having neither tag 'discontinued' nor tag…  |
| `series_search_text` | string | yes | The words to match against economic data series. string, required  |

## Details

Returns tags related to FRED economic data series that match a search text and carry all of the given tags. It needs `series_search_text` and `tag_names` (a semicolon delimited list). Each tag has a group, a name, a popularity score and a series count.

### Use cases

- Find which frequency, geography or concept tags apply to series matching `unemployment` and tagged `usa`.
- Build a filter menu that narrows a FRED series search one tag at a time.
- Rank related tags by `popularity` to suggest common search refinements.
- Exclude tags such as `discontinued` with `exclude_tag_names` to see tags for active series only.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/series-search-related-tags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"series_search_text": "unemployment", "tag_names": "usa", "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `series_search_text` | string | Yes | The words to match against economic data series. string, required |
| `tag_names` | string | Yes | A semicolon delimited list of tag names that series match all of. See the related request fred/series/search/tags . String, required, no default value. Example value: '30-year;frb'. Find the related tags for series havin |
| `exclude_tag_names` | string | No | A semicolon delimited list of tag names that series match none of. String, optional, no default value. Example value: 'discontinued;monthly'. Find the related tags for series having neither tag 'discontinued' nor tag 'mo |
| `file_type` | string | No | Response format. Only json is supported. |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default: series_count |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `sort_order` | string | No | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc |
| `tag_group_id` | string | No | A tag group id to filter tags by type. String, optional, no filtering by tag group by default. One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'. freq = Frequency gen = General or Concept geo = Geo |
| `tag_search_text` | string | No | The words to find matching tags with. String, optional, no filtering by search words by default. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 4127,
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
| `count` | Total number of related tags found for the request. Use it with `limit` and `offset` to page through results. |
| `limit / offset` | The page size and starting position used for this response. |
| `order_by / sort_order` | The attribute and direction used to sort the tags. This response used `series_count` in `asc` order. |
| `realtime_start / realtime_end` | The real-time period applied to the request, as YYYY-MM-DD dates. |
| `tags[].name` | The tag name. Pass it in `tag_names` or `exclude_tag_names` in later calls. |
| `tags[].group_id` | The tag group the tag belongs to, such as `gen` for general or concept tags. |
| `tags[].series_count` | Number of matching series that carry this tag. |
| `tags[].popularity` | Popularity score of the tag. Values can be negative, as in `-5`. |
| `tags[].created` | Timestamp when the tag was created, in `YYYY-MM-DD HH:MM:SS` form with a UTC offset. |
| `tags[].notes` | Free text note about the tag. It is often an empty string. |

### Notes

- Set `tag_group_id` to one of `freq`, `gen`, `geo`, `geot`, `rls`, `seas` or `src` to return only one type of tag.
- Page through results with `limit` (1 to 1000) and `offset`, and compare against `count` to know when to stop.
- Results sort by `series_count` ascending by default. Set `order_by` to `popularity` and `sort_order` to `desc` to see the most popular tags first.
- Use [FRED Search Series](/apis/fred/series-search) to list the series that match the tags you choose.

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/series-search-related-tags.json`](../../../catalog/models/fred/series-search-related-tags.json) · Store page: https://www.sandbase.ai/model/fred/series-search-related-tags

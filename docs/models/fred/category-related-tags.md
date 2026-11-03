# FRED Get Category Related Tags API: pricing, parameters and code examples

`fred/category-related-tags` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Category Related Tags from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/category-related-tags", "category_id": 125, "tag_names": "usa"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/category-related-tags', {'category_id': 125, 'tag_names': 'usa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/category-related-tags", {
  "category_id": 125,
  "tag_names": "usa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/category-related-tags", sandbase.Params{
	"category_id": 125,
	"tag_names": "usa",
})
```

Same call via the path form: `POST /v1/api/fred/category-related-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `order_by` | string |  | Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default: series_count one of: `series_count`, `popularity`, `created`, `name`, `group_id`; default `"series_count"` |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `tag_names` | string | yes | A semicolon delimited list of tag names that series match all of. See the related request fred/category/tags . String, required, no default value. Example value: 'services;quarterly'. Find the related tags for series…  |
| `sort_order` | string |  | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc one of: `asc`, `desc`; default `"asc"` |
| `category_id` | integer | yes | The id for a category. integer, required  |
| `search_text` | string |  | The words to find matching tags with. String, optional, no filtering by search words by default.  |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `tag_group_id` | string |  | A tag group id to filter tags by type. String, optional, no filtering by tag group by default. One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'. freq = Frequency gen = General or Concept geo =…  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `exclude_tag_names` | string |  | A semicolon delimited list of tag names that series match none of. String, optional, no default value. Example value: 'goods;sa'. Find the related tags for series having neither tag 'goods' nor tag 'sa'.  |

## Details

Returns FRED tags that appear on series in one category and that also share series with the tags you name. It needs a `category_id` and a semicolon delimited list of `tag_names`, and it returns each related tag with its group, popularity and series count.

### Use cases

- Suggest the next filter to offer in a search UI after a user picks the `usa` tag inside category 125.
- Find which general concept tags, such as `payments`, co-occur with a chosen tag in one category.
- Rank related tags by `popularity` or `series_count` to see which topics have the most series in a category.
- Narrow a tag list to one tag group, such as geography or frequency, before building a series query.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/category-related-tags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_id": 125, "tag_names": "usa", "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_id` | integer | Yes | The id for a category. integer, required |
| `tag_names` | string | Yes | A semicolon delimited list of tag names that series match all of. See the related request fred/category/tags . String, required, no default value. Example value: 'services;quarterly'. Find the related tags for series hav |
| `exclude_tag_names` | string | No | A semicolon delimited list of tag names that series match none of. String, optional, no default value. Example value: 'goods;sa'. Find the related tags for series having neither tag 'goods' nor tag 'sa'. |
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
  "count": 24,
  "limit": 1000,
  "offset": 0,
  "order_by": "series_count",
  "realtime_end": "2026-11-03",
  "realtime_start": "2026-11-03",
  "sort_order": "asc",
  "tags": [
    {
      "created": "2013-11-19 13:55:53-06",
      "group_id": "gen",
      "name": "headline figure",
      "notes": "",
      "popularity": 50,
      "series_count": 2
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count` | Total number of related tags that match the request. Use it with `limit` and `offset` to page through results. |
| `tags[].name` | The tag name. Use this value in `tag_names` or `exclude_tag_names` in later calls. |
| `tags[].group_id` | The tag group the tag belongs to, for example `gen`. It matches the `tag_group_id` filter. |
| `tags[].series_count` | Number of series that carry this tag within the request filters. |
| `tags[].popularity` | A popularity score for the tag. Higher values mean a more popular tag. |
| `tags[].created` | Timestamp for when the tag was created, in `YYYY-MM-DD HH:MM:SS` format with a UTC offset. |
| `tags[].notes` | Free text note about the tag. It can be an empty string. |
| `order_by / sort_order` | The sort attribute and direction applied to the `tags` list. The response shows `series_count` and `asc` by default. |
| `realtime_start / realtime_end` | The real-time period applied to the request, in `YYYY-MM-DD` format. |

### Notes

- Set `limit` and `offset` to page through results. `count` gives the total number of matching tags.
- Use [FRED Get Category Tags](/apis/fred/category-tags) to list all tags in a category before you pick `tag_names`.
- Use [FRED Get Tags Series](/apis/fred/tags-series) to fetch the series that match a set of tags.
- Separate several tag names with a semicolon, for example `services;quarterly`.

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/category-related-tags.json`](../../../catalog/models/fred/category-related-tags.json) · Store page: https://www.sandbase.ai/model/fred/category-related-tags

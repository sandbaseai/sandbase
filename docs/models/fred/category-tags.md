# FRED Get Category Tags API: pricing, parameters and code examples

`fred/category-tags` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Category Tags from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/category-tags", "category_id": 125}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/category-tags', {'category_id': 125})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/category-tags", {
  "category_id": 125
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/category-tags", sandbase.Params{
	"category_id": 125,
})
```

Same call via the path form: `POST /v1/api/fred/category-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `order_by` | string |  | Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default: series_count one of: `series_count`, `popularity`, `created`, `name`, `group_id`; default `"series_count"` |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `tag_names` | string |  | A semicolon delimited list of tag names to only include in the response. See the related request fred/category/related_tags . String, optional, no filtering by tag names by default Example value: 'trade;goods'. This…  |
| `sort_order` | string |  | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc one of: `asc`, `desc`; default `"asc"` |
| `category_id` | integer | yes | The id for a category. integer, required  |
| `search_text` | string |  | The words to find matching tags with. String, optional, no filtering by search words by default.  |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `tag_group_id` | string |  | A tag group id to filter tags by type. String, optional, no filtering by tag group by default. One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'. freq = Frequency gen = General or Concept geo =…  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |

## Details

Returns the FRED tags attached to one data category, along with how many series use each tag and how popular each tag is. It needs a `category_id`. You can filter and sort the tags by group, name, search text, popularity and more.

### Use cases

- List the tags that describe a FRED category so you can build a filter menu for its series.
- Find the most popular tags in a category by sorting on `popularity` in descending order.
- Narrow a category to one tag type, such as geography or frequency, with `tag_group_id`.
- Collect tag names for a category and pass them to a series lookup to find matching data.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/category-tags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"category_id": 125, "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `category_id` | integer | Yes | The id for a category. integer, required |
| `file_type` | string | No | Response format. Only json is supported. |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default: series_count |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `search_text` | string | No | The words to find matching tags with. String, optional, no filtering by search words by default. |
| `sort_order` | string | No | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc |
| `tag_group_id` | string | No | A tag group id to filter tags by type. String, optional, no filtering by tag group by default. One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'. freq = Frequency gen = General or Concept geo = Geo |
| `tag_names` | string | No | A semicolon delimited list of tag names to only include in the response. See the related request fred/category/related_tags . String, optional, no filtering by tag names by default Example value: 'trade;goods'. This valu |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 26,
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
      "name": "investment",
      "notes": "",
      "popularity": 58,
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
| `tags[].name` | The tag name, such as `investment`. You can pass it in `tag_names` on related calls. |
| `tags[].group_id` | The tag group the tag belongs to, such as `gen` for general or concept tags. |
| `tags[].series_count` | Number of series that carry this tag. |
| `tags[].popularity` | A popularity score for the tag. Higher values mean a more popular tag. |
| `tags[].created` | Timestamp for when the tag was created, with a UTC offset, for example `2012-02-27 10:18:19-06`. |
| `tags[].notes` | Free text note about the tag. It is often an empty string. |

### Notes

- Find a `category_id` with [FRED category](/apis/fred/category) or [FRED Get Category Children](/apis/fred/category-children).
- The default sort is `series_count` ascending. Set `sort_order` to `desc` to see the most used tags first.
- Page through large results with `limit` (1 to 1000) and `offset`, and compare against `count`.
- To see tags that co-occur with chosen tags in a category, call [FRED Get Category Related Tags](/apis/fred/category-related-tags).

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/category-tags.json`](../../../catalog/models/fred/category-tags.json) · Store page: https://www.sandbase.ai/model/fred/category-tags

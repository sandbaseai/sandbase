# FRED Get Tags API: pricing, parameters and code examples

`fred/tags` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Tags from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/tags"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/tags', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/tags", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/tags", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/fred/tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `order_by` | string |  | Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default: series_count one of: `series_count`, `popularity`, `created`, `name`, `group_id`; default `"series_count"` |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `tag_names` | string |  | A semicolon delimited list of tag names to only include in the response. See the related request fred/related_tags . String, optional, no filtering by tag names by default Example value: 'gdp;oecd'. This value filters…  |
| `sort_order` | string |  | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc one of: `asc`, `desc`; default `"asc"` |
| `search_text` | string |  | The words to find matching tags with. String, optional, no filtering by search words by default.  |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `tag_group_id` | string |  | A tag group id to filter tags by type. String, optional, no filtering by tag group by default. One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src', 'cc'. freq = Frequency gen = General or Concept…  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |

## Details

Returns a list of FRED tags with their group, creation time, popularity and number of series. All inputs are optional, so an empty call returns the first 1000 tags sorted by series count.

### Use cases

- List every FRED tag in a given group, such as geography or frequency, with `tag_group_id`.
- Find tags that match a word like `inflation` using `search_text`.
- Rank tags by `popularity` or `series_count` to see which topics have the most data.
- Check whether specific tags such as `gdp;oecd` exist using `tag_names`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/tags" \
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
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default: series_count |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `search_text` | string | No | The words to find matching tags with. String, optional, no filtering by search words by default. |
| `sort_order` | string | No | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc |
| `tag_group_id` | string | No | A tag group id to filter tags by type. String, optional, no filtering by tag group by default. One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src', 'cc'. freq = Frequency gen = General or Concept geo |
| `tag_names` | string | No | A semicolon delimited list of tag names to only include in the response. See the related request fred/related_tags . String, optional, no filtering by tag names by default Example value: 'gdp;oecd'. This value filters re |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 6035,
  "limit": 1000,
  "offset": 0,
  "order_by": "series_count",
  "realtime_end": "2026-11-02",
  "realtime_start": "2026-11-02",
  "sort_order": "asc",
  "tags": [
    {
      "created": "2013-04-08 13:14:37-05",
      "group_id": "gen",
      "name": "10 to 15 years",
      "notes": "",
      "popularity": 10,
      "series_count": 2
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count` | Total number of tags that match the request. Use it with `limit` and `offset` to page through all results. |
| `limit / offset` | The page size and starting position used for this response. |
| `order_by / sort_order` | The attribute and direction used to sort the tags. |
| `realtime_start / realtime_end` | The real-time period used for the request, as `YYYY-MM-DD` dates. |
| `tags[].name` | The tag name. Pass it to other FRED APIs that take tag names. |
| `tags[].group_id` | The tag group the tag belongs to, such as `gen`. It matches the values of the `tag_group_id` parameter. |
| `tags[].series_count` | Number of series that carry this tag. |
| `tags[].popularity` | Popularity score of the tag. Values can be negative. |
| `tags[].created` | Date and time the tag was created, in the format `2013-04-08 13:14:37-05`. |
| `tags[].notes` | Free-text note about the tag. Often an empty string. |

### Notes

- Page through results with `limit` (1 to 1000) and `offset`. Compare `offset` plus the number of returned tags against `count` to know when to stop.
- Set `order_by` to one of `series_count`, `popularity`, `created`, `name` or `group_id`. The default order is `series_count` ascending, so use `sort_order` set to `desc` to see the largest tags first.
- Separate several values in `tag_names` with semicolons, for example `gdp;oecd`.
- To find the series behind a tag, call [FRED Get Tags Series](/apis/fred/tags-series). To find tags that go with a given tag, call [FRED Get Related Tags](/apis/fred/related-tags).

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/tags.json`](../../../catalog/models/fred/tags.json) · Store page: https://www.sandbase.ai/model/fred/tags

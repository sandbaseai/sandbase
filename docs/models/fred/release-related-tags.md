# FRED Get Release Related Tags API: pricing, parameters and code examples

`fred/release-related-tags` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Release Related Tags from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/release-related-tags", "release_id": 53, "tag_names": "usa"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/release-related-tags', {'release_id': 53, 'tag_names': 'usa'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/release-related-tags", {
  "release_id": 53,
  "tag_names": "usa"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/release-related-tags", sandbase.Params{
	"release_id": 53,
	"tag_names": "usa",
})
```

Same call via the path form: `POST /v1/api/fred/release-related-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `order_by` | string |  | Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default: series_count one of: `series_count`, `popularity`, `created`, `name`, `group_id`; default `"series_count"` |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `tag_names` | string | yes | A semicolon delimited list of tag names that series match all of. See the related request fred/release/tags . String, required, no default value. Example value: 'defense;investment'. Find the related tags for series…  |
| `release_id` | integer | yes | The id for a release. integer, required  |
| `sort_order` | string |  | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc one of: `asc`, `desc`; default `"asc"` |
| `search_text` | string |  | The words to find matching tags with. String, optional, no filtering by search words by default.  |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `tag_group_id` | string |  | A tag group id to filter tags by type. String, optional, no filtering by tag group by default. One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'. freq = Frequency gen = General or Concept geo =…  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `exclude_tag_names` | string |  | A semicolon delimited list of tag names that series match none of. String, optional, no default value. Example value: 'monthly;financial'. Find the related tags for series having neither tag 'monthly' nor tag…  |

## Details

Returns FRED tags that are related to a set of tags within one data release. It needs a `release_id` and a semicolon delimited `tag_names` list, and it lists tags on the release's series that also carry all of those tags.

### Use cases

- List the other tags on series in release 53 that carry the tag `usa`, to see what topics the release covers.
- Narrow a series search by picking a related tag with a high `series_count`.
- Filter the tag list by `tag_group_id`, for example `freq` or `geo`, to build a frequency or geography picker.
- Rank related tags by `popularity` to show the most used tags first.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/release-related-tags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"release_id": 53, "tag_names": "usa", "file_type": "json"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `release_id` | integer | Yes | The id for a release. integer, required |
| `tag_names` | string | Yes | A semicolon delimited list of tag names that series match all of. See the related request fred/release/tags . String, required, no default value. Example value: 'defense;investment'. Find the related tags for series havi |
| `exclude_tag_names` | string | No | A semicolon delimited list of tag names that series match none of. String, optional, no default value. Example value: 'monthly;financial'. Find the related tags for series having neither tag 'monthly' nor tag 'financial' |
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
  "count": 429,
  "limit": 1000,
  "offset": 0,
  "order_by": "series_count",
  "realtime_end": "2026-11-02",
  "realtime_start": "2026-11-02",
  "sort_order": "asc",
  "tags": [
    {
      "created": "2013-10-17 10:30:51-05",
      "group_id": "gen",
      "name": "advocacy",
      "notes": "",
      "popularity": -27,
      "series_count": 2
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count` | Total number of related tags that match the request. Use it with `limit` and `offset` to page through results. |
| `limit / offset` | The page size and starting position the response used. |
| `order_by / sort_order` | The attribute and direction used to sort the `tags` list. The default sort is `series_count` ascending. |
| `realtime_start / realtime_end` | The real-time period applied to the request, as YYYY-MM-DD dates. |
| `tags[].name` | The tag name. Pass it in `tag_names` or `exclude_tag_names` on other FRED calls. |
| `tags[].group_id` | The tag group the tag belongs to, such as `gen` for general or concept tags. |
| `tags[].series_count` | Number of series that carry this tag within the matched set. |
| `tags[].popularity` | Popularity score of the tag. Values can be negative. |
| `tags[].created` | Date and time the tag was created, with a UTC offset. |
| `tags[].notes` | Free text note about the tag. It is often an empty string. |

### Notes

- Get `release_id` from [FRED Get Releases](/apis/fred/releases). Get valid tag names from [FRED Get Release Tags](/apis/fred/release-tags).
- Page with `limit` (1 to 1000, default 1000) and `offset`. Compare `count` with `offset` plus the number of returned tags to see if more remain.
- To list the series behind a tag combination, call [FRED Get Release Series](/apis/fred/release-series).

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/release-related-tags.json`](../../../catalog/models/fred/release-related-tags.json) · Store page: https://www.sandbase.ai/model/fred/release-related-tags

# FRED Get Release Tags API: pricing, parameters and code examples

`fred/release-tags` · data API · FRED · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $1e-05 per call (free daily quota) · **Modes:** sync

Get Release Tags from FRED. Returns the official FRED API response unchanged.

## Pricing

- **$1e-05 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "fred/release-tags", "release_id": 53}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('fred/release-tags', {'release_id': 53})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("fred/release-tags", {
  "release_id": 53
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "fred/release-tags", sandbase.Params{
	"release_id": 53,
})
```

Same call via the path form: `POST /v1/api/fred/release-tags` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 default `1000`; range 1–1000 |
| `offset` | integer |  | non-negative integer, optional, default: 0 default `0`; range 0– |
| `order_by` | string |  | Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default: series_count one of: `series_count`, `popularity`, `created`, `name`, `group_id`; default `"series_count"` |
| `file_type` | string |  | Response format. Only json is supported. one of: `json`; default `"json"` |
| `tag_names` | string |  | A semicolon delimited list of tag names to only include in the response. See the related request fred/release/related_tags . String, optional, no filtering by tag names by default Example value: 'gnp;quarterly'. This…  |
| `release_id` | integer | yes | The id for a release. integer, required  |
| `sort_order` | string |  | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc one of: `asc`, `desc`; default `"asc"` |
| `search_text` | string |  | The words to find matching tags with. String, optional, no filtering by search words by default.  |
| `realtime_end` | string |  | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |
| `tag_group_id` | string |  | A tag group id to filter tags by type. String, optional, no filtering by tag group by default. One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'. freq = Frequency gen = General or Concept geo =…  |
| `realtime_start` | string |  | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date  |

## Details

Returns the FRED tags attached to one data release. You pass a `release_id`, and each tag comes back with its group, popularity, series count and creation time. You can filter and sort the list with optional parameters.

### Use cases

- List every tag for a FRED release to see which topics, geographies or frequencies its series cover.
- Find the tags with the most series in a release, then use them to narrow a series search.
- Filter a release's tags by `tag_group_id` to get only the general concept tags or only the geography tags.
- Search a release's tags with `search_text` to check whether a topic such as crops is tagged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/release-tags" \
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
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default: series_count |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `search_text` | string | No | The words to find matching tags with. String, optional, no filtering by search words by default. |
| `sort_order` | string | No | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc |
| `tag_group_id` | string | No | A tag group id to filter tags by type. String, optional, no filtering by tag group by default. One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas', 'src'. freq = Frequency gen = General or Concept geo = Geo |
| `tag_names` | string | No | A semicolon delimited list of tag names to only include in the response. See the related request fred/release/related_tags . String, optional, no filtering by tag names by default Example value: 'gnp;quarterly'. This val |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "count": 428,
  "limit": 1000,
  "offset": 0,
  "order_by": "series_count",
  "realtime_end": "2026-11-02",
  "realtime_start": "2026-11-02",
  "sort_order": "asc",
  "tags": [
    {
      "created": "2020-05-11 13:13:02-05",
      "group_id": "gen",
      "name": "change",
      "notes": null,
      "popularity": 25,
      "series_count": 2
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `count` | Total number of tags that match the request. Use it with `limit` and `offset` to page through results. |
| `limit / offset` | The page size and starting position applied to this response. |
| `order_by / sort_order` | The attribute and direction used to sort the tags in this response. |
| `realtime_start / realtime_end` | The real-time period the response applies to, as `YYYY-MM-DD` dates. |
| `tags[].name` | The tag name. Pass it in `tag_names` on FRED calls to filter by this tag. |
| `tags[].group_id` | The tag group the tag belongs to, such as `gen` for general or concept tags. |
| `tags[].series_count` | Number of series in this release that carry the tag. |
| `tags[].popularity` | A popularity score for the tag. Higher values mean a more popular tag. |
| `tags[].created` | Date and time the tag was created, in `YYYY-MM-DD HH:MM:SS` format with a UTC offset. |
| `tags[].notes` | Free-text note about the tag. It is often `null` or an empty string. |

### Notes

- Get the `release_id` from [FRED Get Releases](/apis/fred/releases). The example request uses `53`.
- Page through long lists with `limit` (1 to 1000) and `offset`. Compare `offset` plus the number of returned tags against `count` to know when to stop.
- The default sort is `series_count` in ascending order, so the least used tags come first. Set `sort_order` to `desc` to see the most used tags first.
- To see tags related to a set of tag names within the release, call [FRED Get Release Related Tags](/apis/fred/release-related-tags).

### Pricing

$0.00001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/fred/release-tags.json`](../../../catalog/models/fred/release-tags.json) · Store page: https://www.sandbase.ai/model/fred/release-tags

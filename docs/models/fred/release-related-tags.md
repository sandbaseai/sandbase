# FRED Get Release Related Tags

`fred/release-related-tags` · api · FRED

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

Get Release Related Tags from FRED. Returns the official FRED API response unchanged.

The response is the official FRED API response, unchanged.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/fred/release-related-tags" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"release_id": 53, "tag_names": "usa", "file_type": "json"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `exclude_tag_names` | string | No | A semicolon delimited list of tag names that series match none of. String, optional, no default value. Example value: 'monthly;financial'. Find the related tags |
| `file_type` | string | No | Response format. Only json is supported. |
| `limit` | integer | No | The maximum number of results to return. integer between 1 and 1000, optional, default: 1000 |
| `offset` | integer | No | non-negative integer, optional, default: 0 |
| `order_by` | string | No | Order results by values of the specified attribute. One of the following strings: 'series_count', 'popularity', 'created', 'name', 'group_id'. optional, default |
| `realtime_end` | string | No | The end of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `realtime_start` | string | No | The start of the real-time period. For more information, see Real-Time Periods . YYYY-MM-DD formatted string, optional, default: today's date |
| `release_id` | integer | Yes | The id for a release. integer, required |
| `search_text` | string | No | The words to find matching tags with. String, optional, no filtering by search words by default. |
| `sort_order` | string | No | Sort results is ascending or descending order for attribute values specified by order_by. One of the following strings: 'asc', 'desc'. optional, default: asc |
| `tag_group_id` | string | No | A tag group id to filter tags by type. String, optional, no filtering by tag group by default. One of the following: 'freq', 'gen', 'geo', 'geot', 'rls', 'seas' |
| `tag_names` | string | Yes | A semicolon delimited list of tag names that series match all of. See the related request fred/release/tags . String, required, no default value. Example value: |

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/fred/release-related-tags.json`](../../../catalog/models/fred/release-related-tags.json) · Store page: https://www.sandbase.ai/model/fred/release-related-tags

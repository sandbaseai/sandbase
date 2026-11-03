# Douyin Topic Search API: pricing, parameters and code examples

`douyin/index/topic-query` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Douyin topic performance metrics matching a search term over a specific date range, including item counts, like counts, and view counts.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/topic-query", "app_name": "aweme", "end_date": "20260412", "keyword": "人工智能", "start_date": "20260406"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/topic-query', {'app_name': 'aweme', 'end_date': '20260412', 'keyword': '人工智能', 'start_date': '20260406'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/topic-query", {
  "app_name": "aweme",
  "end_date": "20260412",
  "keyword": "人工智能",
  "start_date": "20260406"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/topic-query", sandbase.Params{
	"app_name": "aweme",
	"end_date": "20260412",
	"keyword": "人工智能",
	"start_date": "20260406",
})
```

Same call via the path form: `POST /v1/api/douyin/index/topic-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Topic keyword  |
| `app_name` | string |  | Platform one of: `aweme`, `toutiao`; default `"aweme"` |
| `end_date` | string | yes | End date YYYYMMDD  |
| `start_date` | string | yes | Start date YYYYMMDD  |

## Details

Returns Douyin topics that match a search keyword, with item, like, and view counts for a date range. It needs a `keyword`, a `start_date`, and an `end_date` in YYYYMMDD format.

### Use cases

- Compare how many videos and views the topic `人工智能` has against related topics such as `人工智能机器人`.
- Find the `topic_id` of a Douyin topic from its name.
- Spot topics with zero activity in a date range and drop them from a tracking list.
- Pull weekly topic totals for a keyword to build a trend report.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/topic-query" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "20260412", "keyword": "人工智能", "start_date": "20260406"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_date` | string | Yes | End date YYYYMMDD |
| `keyword` | string | Yes | Topic keyword |
| `start_date` | string | Yes | Start date YYYYMMDD |
| `app_name` | string | No | Platform |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": 0,
    "StatusMessage": ""
  },
  "topic_list": [
    {
      "datetime": "",
      "digg_cnt": "3886643",
      "item_cnt": "26313",
      "play_read_cnt": "201528869",
      "topic_id": "1576073697445901",
      "topic_index": "2729228",
      "topic_name": "人工智能"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `topic_list[]` | List of topics whose names match the keyword. Each entry is one topic. |
| `topic_list[].topic_name` | Name of the topic, for example `人工智能`. |
| `topic_list[].topic_id` | ID of the topic, returned as a string. |
| `topic_list[].item_cnt` | Number of items (videos) counted for the topic. Returned as a string. |
| `topic_list[].digg_cnt` | Like count for the topic. Returned as a string. |
| `topic_list[].play_read_cnt` | View count for the topic. Returned as a string. |
| `topic_list[].topic_index` | Index value for the topic. It is `0` for topics with no activity. |
| `topic_list[].datetime` | Date field for the entry. It is an empty string in this response. |
| `BaseResp.StatusCode / BaseResp.StatusMessage` | Status of the call. `StatusCode` is `0` and `StatusMessage` is empty in this response. |

### Notes

- All counts and IDs are returned as strings. Convert them to numbers before you sort or sum them.
- `app_name` accepts `aweme` or `toutiao`. It defaults to `aweme`.
- Use [Douyin Topic Search Suggestions](/apis/douyin/index/topic-suggest) to find topic keywords to search with.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/topic-query.json`](../../../../catalog/models/douyin/index/topic-query.json) · Store page: https://www.sandbase.ai/model/douyin/index/topic-query

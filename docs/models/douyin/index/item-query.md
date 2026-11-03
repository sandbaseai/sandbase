# Douyin Index Video Search API: pricing, parameters and code examples

`douyin/index/item-query` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Search Douyin Index videos by keyword with filters for post date, duration, category, and label type. Returns video metadata and performance metrics.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/item-query", "query": "sandbase"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/item-query', {'query': 'sandbase'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/item-query", {
  "query": "sandbase"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/item-query", sandbase.Params{
	"query": "sandbase",
})
```

Same call via the path form: `POST /v1/api/douyin/index/item-query` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword (required), e.g. "food"  |
| `date_type` | integer |  | Publish date filter, default 0=any default `0` |
| `label_type` | integer |  | Video type (quality tag), default 0=any default `0` |
| `category_id` | string |  | Category ID (string), default "0"=all default `"0"` |
| `duration_type` | integer |  | Duration filter, default 0=any default `0` |

## Details

Searches Douyin Index videos by keyword and returns a list of matching videos with creator name, follower count, like count, duration, post time and a video link. It needs one input, `query`. Optional filters narrow results by post date, duration, category and quality tag.

### Use cases

- Find recent Douyin videos about a keyword such as `美食` and open each one through its `url`.
- Spot small accounts with hot videos by checking `isLowFansButHot` next to `fans`.
- Rank videos for a topic by `index` or `likes` to see which posts perform best.
- Narrow a search to short or long videos with `duration_type` and compare the results.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/item-query" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "美食"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (required), e.g. "food" |
| `category_id` | string | No | Category ID (string), default "0"=all |
| `date_type` | integer | No | Publish date filter, default 0=any |
| `duration_type` | integer | No | Duration filter, default 0=any |
| `label_type` | integer | No | Video type (quality tag), default 0=any |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": [
    {
      "avatarUrl": "https://p3-byteindex-sign.byteimg.com/aweme-avatar/tos-cn-i-0813c000-ce_osD7MQgO…",
      "createTime": "2026-10-30 23:34:15",
      "duration": 72,
      "fans": 13248,
      "index": "657817",
      "isHighFansRiseRate": 0,
      "isHighLikeRate": 1,
      "isHighPlayOverRate": 0,
      "isLowFansButHot": 1,
      "itemId": "7702484601909857590",
      "likes": "226165",
      "nickname": "明食记"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data[].itemId` | ID of the video, as a string. It is the last part of the video `url`. |
| `data[].title` | Video caption, including its hashtags. |
| `data[].url` | Link to the video page on Douyin. |
| `data[].nickname / data[].avatarUrl` | Display name and avatar image link of the creator. |
| `data[].fans` | Follower count of the creator, as a number. |
| `data[].likes` | Like count of the video. It comes back as a string. |
| `data[].index` | Index score of the video for this search, as a string. Higher values appear for videos that do better. |
| `data[].duration` | Length of the video. Values like `72` and `274` suggest seconds, but the response does not state the unit. |
| `data[].createTime` | Post time of the video, in `YYYY-MM-DD HH:MM:SS` format. |
| `data[].isHighLikeRate / data[].isHighFansRiseRate / data[].isHighPlayOverRate / data[].isLowFansButHot` | Flags set to `1` when the video carries that tag, and `0` when it does not. The names describe a high like rate, high follower growth, high play completion, and a hot video from a low-follower account. |

### Notes

- The response shows no pagination field, and the schema has no page parameter.
- Leave `date_type`, `label_type` and `duration_type` at `0` and `category_id` at `"0"` for an unfiltered search. Pass `category_id` as a string.
- Use [Douyin Video Search Filter Options](/apis/douyin/index/item-filter-options) to look up the filter values, and [Douyin Video Search Suggestions](/apis/douyin/index/item-sug) to find keywords.
- Pass the video to [Douyin Video Index Trend](/apis/douyin/index/item-index) for more detail on its index.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/item-query.json`](../../../../catalog/models/douyin/index/item-query.json) · Store page: https://www.sandbase.ai/model/douyin/index/item-query

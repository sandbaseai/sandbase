# Douyin Content Creative Topics API: pricing, parameters and code examples

`douyin/index/content-creative-topic` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending creative topics for a specific Douyin category. Filter results by category ID, evaluation period, ranking metric, and end date.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/content-creative-topic", "end_date": "20260405", "tag_id": "601"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/content-creative-topic', {'end_date': '20260405', 'tag_id': '601'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/content-creative-topic", {
  "end_date": "20260405",
  "tag_id": "601"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/content-creative-topic", sandbase.Params{
	"end_date": "20260405",
	"tag_id": "601",
})
```

Same call via the path form: `POST /v1/api/douyin/index/content-creative-topic` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `period` | string |  | "1" / "3" / "7" one of: `1`, `3`, `7`; default `"7"` |
| `tag_id` | string | yes | Category ID (same as category_id in fetch_item_query)  |
| `end_date` | string | yes | End date YYYYMMDD. **Must be a Sunday only when period=7**; any day for period=1/3  |
| `rank_type` | string |  | "index" or "rise" one of: `index`, `rise`; default `"index"` |

## Details

Returns a list of trending creative topics (hashtags) for one Douyin content category. Each topic comes with engagement totals and a few sample videos. You send a `tag_id` and an `end_date`.

### Use cases

- Find which hashtags are leading in a content category for a given week.
- Compare topics by `index`, `digg_cnt` and `item_cnt` to pick tags for new videos.
- Pull sample videos under a topic to see what content drives it.
- Switch `rank_type` to `rise` to find topics that are growing fastest.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/content-creative-topic" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"end_date": "20260405", "tag_id": "601"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `end_date` | string | Yes | End date YYYYMMDD. **Must be a Sunday only when period=7**; any day for period=1/3 |
| `tag_id` | string | Yes | Category ID (same as category_id in fetch_item_query) |
| `period` | string | No | "1" / "3" / "7" |
| `rank_type` | string | No | "index" or "rise" |

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
      "digg_cnt": "171445435",
      "id": "1635669004810253",
      "index": "201575639",
      "item_cnt": "19739286",
      "item_list": [
        {
          "img": "https://p9-byteindex-sign.byteimg.com/tos-cn-p-0015c000-ce/oAfEB3pEBb9bEEkAFmALx…",
          "item_id": "7621900494017844389",
          "title": "仅用了0秒就接受了自己的新身份#vlog十亿流量扶持计划 #内容太过真实 #vlog日常 #搞笑 #学生时代",
          "url": "https://www.douyin.com/share/video/7621900494017844389"
        }
      ],
      "name": "搞笑",
      "vv": "9700000928"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `topic_list[].name` | Topic name, shown as a hashtag-style label such as `搞笑`. |
| `topic_list[].id` | ID of the topic. |
| `topic_list[].index` | Index score used to rank the topic. Higher values mean a higher rank under `rank_type` `index`. |
| `topic_list[].digg_cnt` | Total like count for videos under the topic. |
| `topic_list[].item_cnt` | Number of videos under the topic. |
| `topic_list[].vv` | View count for the topic. |
| `topic_list[].item_list[].title` | Caption of a sample video, including its hashtags. |
| `topic_list[].item_list[].item_id` | ID of the sample video. |
| `topic_list[].item_list[].url` | Share link to the sample video on douyin.com. |
| `topic_list[].item_list[].img` | Cover image URL of the sample video. The link is signed and carries an expiry in its query string. |

### Notes

- Numeric values such as `digg_cnt`, `index` and `vv` come back as strings.
- `end_date` uses the format `YYYYMMDD`. It must be a Sunday when `period` is `7`. Any day works for `1` or `3`.
- `tag_id` is the same value as `category_id` in the video search APIs. [Douyin Index Video Search](/apis/douyin/index/item-query) is a related call.
- Call [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date) or [Douyin Content Guide Valid Dates](/apis/douyin/index/content-valid-date) to check which dates have data.

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/content-creative-topic.json`](../../../../catalog/models/douyin/index/content-creative-topic.json) · Store page: https://www.sandbase.ai/model/douyin/index/content-creative-topic

# Douyin Current Hot Topics Leaderboard API: pricing, parameters and code examples

`douyin/index/current-hot-topic` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns Douyin real-time hot topics and the trending topics leaderboard. Use this endpoint to observe currently viral subjects and platform-wide discussions.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/current-hot-topic"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/current-hot-topic', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/current-hot-topic", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/current-hot-topic", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/index/current-hot-topic` with the body above minus `model`.

## Details

Returns two Douyin topic lists: the current hot topics and the rocketing (fast-rising) topics. The request takes no input parameters. Send an empty JSON object.

### Use cases

- Show the topics ranked highest on Douyin right now in a trend dashboard.
- Compare the `current` and `rocketing` lists to spot topics that are climbing quickly.
- Group trending topics by `category` to see which areas such as sports or finance dominate the list.
- Save each topic's `topic_index` and `vv` over time to build a history of topic ranks and view counts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/current-hot-topic" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "current": [
    {
      "category": "时政",
      "content_cnt": "6",
      "rank": "1",
      "rank_flag": "0",
      "topic_index": "12100833",
      "topic_name": "美官员称美袭击伊朗格什姆岛",
      "vv": "11053887"
    }
  ],
  "rocketing": [
    {
      "category": "社会",
      "content_cnt": "0",
      "rank": "1",
      "rank_flag": "0",
      "topic_index": "8467988",
      "topic_name": "网民编造“花费260万登顶珠峰”被罚",
      "vv": "0"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `current[]` | Ranked list of the current hot topics on Douyin. |
| `rocketing[]` | Ranked list of rocketing topics. It uses the same fields as `current[]`. |
| `current[].topic_name / rocketing[].topic_name` | Title of the topic, in Chinese. |
| `current[].rank / rocketing[].rank` | Position of the topic within its list, starting at `1`. The value is a string. |
| `current[].topic_index / rocketing[].topic_index` | Numeric ID of the topic, returned as a string. |
| `current[].category / rocketing[].category` | Topic category label in Chinese, such as `时政` (politics), `体育` (sports), `社会` (society) or `财经` (finance). |
| `current[].vv / rocketing[].vv` | View count figure for the topic, returned as a string. Some topics show `0`. |
| `current[].content_cnt / rocketing[].content_cnt` | Content count figure for the topic, returned as a string. |
| `current[].rank_flag / rocketing[].rank_flag` | Flag that goes with the rank. The response shows only `0` and `1`, and the meaning of each value is not documented. |

### Notes

- The request body is an empty object `{}`. There is no pagination parameter.
- All values, including numbers, come back as strings. Convert them before sorting or doing math.
- To dig into one topic, call [Douyin Hot Topic Detail Analysis](/apis/douyin/index/hot-detail). To find topics by keyword, use [Douyin Topic Search](/apis/douyin/index/topic-query).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/current-hot-topic.json`](../../../../catalog/models/douyin/index/current-hot-topic.json) · Store page: https://www.sandbase.ai/model/douyin/index/current-hot-topic

# Douyin Index Subscribed Keywords API: pricing, parameters and code examples

`douyin/index/get-user-sub-word` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns the list of subscribed keywords configured by the current logged-in user on Douyin Index. Useful for retrieving tracked topics without manual lookup.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/get-user-sub-word"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/get-user-sub-word', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/get-user-sub-word", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/get-user-sub-word", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/douyin/index/get-user-sub-word` with the body above minus `model`.

## Details

Returns the keywords that the current logged-in user subscribes to on Douyin Index. Each keyword comes with its latest index value, rank, and a short daily index history. The request needs no input parameters.

### Use cases

- List the topics a Douyin Index account tracks without opening the Douyin Index site.
- Read the latest `keyword_index` for each tracked keyword to feed a monitoring dashboard.
- Find keywords flagged with an unusual change by checking `ratio_status`.
- Copy the tracked keyword list into another analytics tool.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/get-user-sub-word" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": 0,
    "StatusMessage": ""
  },
  "sub_num": "0",
  "word_ratio": [
    {
      "index_style": "搜索指数",
      "keyword": "巨量算数",
      "keyword_index": "16265",
      "keyword_index_weekly": [
        {
          "datetime": "20261027",
          "index": "14195"
        }
      ],
      "rank": "1",
      "ratio": -0.06237389750389116,
      "ratio_ex": 0.1,
      "ratio_status": "有异动",
      "show": "搜索指数",
      "sub_channel": 1,
      "sub_style": "搜索指数"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `sub_num` | Number of subscriptions, returned as a string. In the sample response it is `"0"` even though one keyword is listed, so do not rely on it as a count of `word_ratio`. |
| `word_ratio[].keyword` | The subscribed keyword text, for example `巨量算数`. |
| `word_ratio[].keyword_index` | Latest index value for the keyword, returned as a string. |
| `word_ratio[].index_style / word_ratio[].show / word_ratio[].sub_style` | Name of the index type shown for the subscription. The sample value is `搜索指数` (search index). |
| `word_ratio[].keyword_index_weekly[].datetime` | Date of the data point in `YYYYMMDD` format, for example `20261028`. |
| `word_ratio[].keyword_index_weekly[].index` | Index value for that date, returned as a string. The list holds a few days of recent values. |
| `word_ratio[].rank` | Position of the keyword in the list, returned as a string. |
| `word_ratio[].ratio / word_ratio[].ratio_ex` | Numeric change values for the keyword index. `ratio` is a decimal such as `-0.0624`. The response does not state the comparison period. |
| `word_ratio[].ratio_status` | Text label for the change. The sample value `有异动` means there is an unusual movement. |
| `BaseResp.StatusCode` | Status code of the call. `0` appears in a successful response. |

### Notes

- The request body is an empty JSON object `{}`. The result depends on the account tied to the call.
- Index values and ranks arrive as strings. Convert them to numbers before you sort or chart them.
- To look at one keyword in more detail, call [Douyin Multi Keyword Hot Trend](/apis/douyin/index/multi-keyword-hot-trend) or [Douyin Index Keyword Valid Dates](/apis/douyin/index/keyword-valid-date).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/get-user-sub-word.json`](../../../../catalog/models/douyin/index/get-user-sub-word.json) · Store page: https://www.sandbase.ai/model/douyin/index/get-user-sub-word

# Douyin Topic Search Suggestions API: pricing, parameters and code examples

`douyin/index/topic-suggest` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns autocomplete topic suggestions based on a search query. Supports filtering by target platform such as Douyin or Toutiao.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/topic-suggest", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/topic-suggest', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/topic-suggest", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/topic-suggest", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/douyin/index/topic-suggest` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Topic keyword  |
| `app_name` | string |  | Platform, aweme=Douyin, toutiao=Toutiao one of: `aweme`, `toutiao`; default `"aweme"` |

## Details

Returns autocomplete topic suggestions for a search keyword. Each suggestion has a topic ID and a topic name. You send a `keyword` and can set `app_name` to choose Douyin or Toutiao.

### Use cases

- Fill a topic search box with suggestions as a user types a keyword.
- Find the `topic_id` for a topic name before you pass it to another Douyin Index call.
- Compare the topic names suggested for the same keyword on Douyin and on Toutiao.
- Build a list of related topic names around a theme such as `人工智能`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/topic-suggest" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Topic keyword |
| `app_name` | string | No | Platform, aweme=Douyin, toutiao=Toutiao |

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
      "topic_id": "1576073697445901",
      "topic_name": "人工智能"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `topic_list` | List of suggested topics for the keyword. The first item in the sample is an exact match for the keyword. |
| `topic_list[].topic_id` | ID of the suggested topic, returned as a string. |
| `topic_list[].topic_name` | Display name of the suggested topic. It can be the keyword itself or a longer related name. |
| `BaseResp.StatusCode` | Status code of the request. `0` in the sample response. |
| `BaseResp.StatusMessage` | Status text. It is an empty string in the sample response. |

### Notes

- `app_name` accepts `aweme` for Douyin or `toutiao` for Toutiao. The default is `aweme`.
- Treat `topic_id` as a string. The sample IDs have 16 to 19 digits.
- To search topics in full instead of getting suggestions, call [Douyin Topic Search](/apis/douyin/index/topic-query).
- To see what is trending now, call [Douyin Current Hot Topics Leaderboard](/apis/douyin/index/current-hot-topic).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/topic-suggest.json`](../../../../catalog/models/douyin/index/topic-suggest.json) · Store page: https://www.sandbase.ai/model/douyin/index/topic-suggest

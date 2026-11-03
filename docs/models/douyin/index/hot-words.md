# Douyin Hot Search Keywords API: pricing, parameters and code examples

`douyin/index/hot-words` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns a list of current trending search keywords and their growth rates on Douyin or Toutiao. Results can be filtered by the target platform application.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/hot-words", "app_name": "aweme"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/hot-words', {'app_name': 'aweme'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/hot-words", {
  "app_name": "aweme"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/hot-words", sandbase.Params{
	"app_name": "aweme",
})
```

Same call via the path form: `POST /v1/api/douyin/index/hot-words` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `app_name` | string |  | Platform, aweme=Douyin, toutiao=Toutiao one of: `aweme`, `toutiao`; default `"aweme"` |

## Details

Returns a list of trending search keywords on Douyin or Toutiao. Each keyword comes with an index value and growth figures. The only input is the optional `app_name` parameter, which defaults to `aweme` (Douyin).

### Use cases

- Pull the current trending Douyin search terms each day to find topics for new videos.
- Compare the `aweme` and `toutiao` lists to see which keywords trend on one platform but not the other.
- Rank keywords by `growth_rate` to spot terms that are rising fast.
- Feed the keywords into other Douyin Index APIs to study a single term in more depth.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/hot-words" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `app_name` | string | No | Platform, aweme=Douyin, toutiao=Toutiao |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "BaseResp": {
    "StatusCode": 0,
    "StatusMessage": ""
  },
  "hot_words": [
    {
      "growth": "50",
      "growth_rate": 100,
      "index": "100",
      "keyword": "美食"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `hot_words[]` | List of trending search keywords. |
| `hot_words[].keyword` | The trending search term, as text in Chinese. |
| `hot_words[].index` | Index value for the keyword, returned as a string. In the sample, all three keywords have `100`. |
| `hot_words[].growth` | Growth value for the keyword, returned as a string. |
| `hot_words[].growth_rate` | Growth rate for the keyword, returned as a number. |
| `BaseResp.StatusCode / BaseResp.StatusMessage` | Status of the call. `StatusCode` of `0` with an empty `StatusMessage` means the call succeeded. |

### Notes

- Set `app_name` to `aweme` for Douyin (the default) or `toutiao` for Toutiao.
- `index` and `growth` come back as strings, while `growth_rate` is a number. Convert the strings before you sort or compare them.
- To study one keyword further, pass it to [Douyin Hot Trend Words](/apis/douyin/index/hot-trend-word) or [Douyin Relation Word Analysis](/apis/douyin/index/relation-word).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/hot-words.json`](../../../../catalog/models/douyin/index/hot-words.json) · Store page: https://www.sandbase.ai/model/douyin/index/hot-words

# Douyin Hot Trend Words API: pricing, parameters and code examples

`douyin/index/hot-trend-word` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns trending search words suggested in the keyword index search box. Filter by platform and word type to retrieve relevant search suggestions.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/index/hot-trend-word", "app_name": "aweme", "type": 0}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/index/hot-trend-word', {'app_name': 'aweme', 'type': 0})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/index/hot-trend-word", {
  "app_name": "aweme",
  "type": 0
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/index/hot-trend-word", sandbase.Params{
	"app_name": "aweme",
	"type": 0,
})
```

Same call via the path form: `POST /v1/api/douyin/index/hot-trend-word` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `type` | integer |  | Word type, 0=search words (plain words, id is always "0"), default `0`; range 0–1 |
| `app_name` | string |  | Platform, aweme=Douyin, toutiao=Toutiao (toutiao currently returns empty) one of: `aweme`, `toutiao`; default `"aweme"` |

## Details

Returns the trending search words that Douyin suggests in the keyword index search box. Both inputs are optional: `app_name` picks the platform and `type` picks the word type.

### Use cases

- Pull the current list of suggested search words to see which terms Douyin is surfacing today.
- Seed a keyword research list with fresh terms before you check each one in the keyword index.
- Track which words appear from one day to the next by saving the list with its `update_time`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/hot-trend-word" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `app_name` | string | No | Platform, aweme=Douyin, toutiao=Toutiao (toutiao currently returns empty) |
| `type` | integer | No | Word type, 0=search words (plain words, id is always "0"), |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "trend_words": [
    {
      "id": "0",
      "word": "百乔"
    }
  ],
  "update_time": "20261102"
}
```

### Response fields

| Field | Meaning |
|---|---|
| `trend_words[]` | List of suggested trending search words. |
| `trend_words[].word` | The suggested search word as plain text. |
| `trend_words[].id` | Word ID. For `type` 0 (search words) it is always the string `"0"`. |
| `update_time` | Date of the list as a `YYYYMMDD` string, for example `20261102`. |

### Notes

- The request works with an empty body `{}`. The defaults are `app_name` set to `aweme` and `type` set to `0`.
- `app_name` accepts `aweme` (Douyin) or `toutiao`. Toutiao currently returns an empty result.
- `type` accepts `0` or `1`. Only `0` (search words) is described in the parameter documentation.
- To analyze a word you found here, pass it to [Douyin Hot Search Keywords](/apis/douyin/index/hot-words) or [Douyin Relation Word Analysis](/apis/douyin/index/relation-word).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Douyin Index Area List](/apis/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/apis/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/apis/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/hot-trend-word.json`](../../../../catalog/models/douyin/index/hot-trend-word.json) · Store page: https://www.sandbase.ai/model/douyin/index/hot-trend-word

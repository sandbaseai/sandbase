# Douyin Hot Trend Words API: pricing, parameters and code examples

`douyin/index/hot-trend-word` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns trending search words suggested in the keyword index search box. Filter by platform and word type to retrieve relevant search suggestions.

## Pricing

- **$0.0015 per call** (USD)
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

Returns hot trend words suggested in the keyword index search box using `app_name` and `type`.

### Use cases

- Retrieve trending keyword suggestions from Douyin's search box.
- Identify rising topics for keyword index analysis.
- Power autocomplete and recommendation fields for search inputs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/index/hot-trend-word" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `type` | integer | No | Word type, 0=search words (plain words, id is always "0"), |
| `app_name` | string | No | Platform, aweme=Douyin, toutiao=Toutiao (toutiao currently returns empty) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "trend_words": [
    {
      "id": "0",
      "word": "蔡康永"
    }
  ]
}
```

### Notes

- Set `app_name` to `aweme` for Douyin or `toutiao` for Toutiao (Toutiao currently returns empty).
- Set `type` to `0` for plain search words where the ID is always `0`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Index Area List](/model/douyin/index/all-area): Returns the complete list of supported geographic areas available for Douyin Index queries.
- [Douyin Index Valid Dates](/model/douyin/index/all-valid-date): Returns the latest valid dates available for each data type in Douyin Index.
- [Douyin Brand Popularity Cycles](/model/douyin/index/brand-cycles): Returns periodic brand popularity and cycle analysis data across platforms for a specified brand name and date range.

---
Machine-readable: [`catalog/models/douyin/index/hot-trend-word.json`](../../../../catalog/models/douyin/index/hot-trend-word.json) · Store page: https://www.sandbase.ai/model/douyin/index/hot-trend-word

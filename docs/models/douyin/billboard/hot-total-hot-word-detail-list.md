# Douyin Billboard Hot Word Details API: pricing, parameters and code examples

`douyin/billboard/hot-total-hot-word-detail-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns detailed billboard metrics for a specific Douyin content word. Filters include the search keyword, word identifier, and target query date.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-total-hot-word-detail-list", "keyword": "抖音音乐", "query_day": 20260928, "word_id": "pyLt6qABVdxnZYm5fRPW"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-total-hot-word-detail-list', {'keyword': '抖音音乐', 'query_day': 20260928, 'word_id': 'pyLt6qABVdxnZYm5fRPW'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-total-hot-word-detail-list", {
  "keyword": "抖音音乐",
  "query_day": 20260928,
  "word_id": "pyLt6qABVdxnZYm5fRPW"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-total-hot-word-detail-list", sandbase.Params{
	"keyword": "抖音音乐",
	"query_day": 20260928,
	"word_id": "pyLt6qABVdxnZYm5fRPW",
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-total-hot-word-detail-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword  |
| `word_id` | string | yes | Content word id  |
| `query_day` | integer | yes | Query date, format is YYYYMMDD  |

## Details

This endpoint retrieves detailed billboard statistics for a specific trending term on Douyin. Look up word metrics by supplying `keyword`, `word_id`, and `query_day`.

### Use cases

- Analyze trending content word performance on Douyin for a specific date.
- Track historical popularity metrics for targeted billboard keywords.
- Compare daily metric breakdowns across specific content word identifiers.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-total-hot-word-detail-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "<keyword>", "query_day": "<query_day>", "word_id": "<word_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword |
| `word_id` | string | Yes | Content word id |
| `query_day` | integer | Yes | Query date, format is YYYYMMDD |

### Notes

- `query_day` requires an integer date formatted as YYYYMMDD.
- Both `keyword` and `word_id` must be provided to query word details.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-total-hot-word-detail-list.json`](../../../../catalog/models/douyin/billboard/hot-total-hot-word-detail-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-total-hot-word-detail-list

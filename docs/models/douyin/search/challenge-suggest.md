# Douyin Hashtag Suggestions API: pricing, parameters and code examples

`douyin/search/challenge-suggest` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Returns a list of suggested Douyin hashtags and challenges matching a query keyword, including challenge IDs and view counts.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/challenge-suggest", "keyword": "游戏"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/challenge-suggest', {'keyword': '游戏'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/challenge-suggest", {
  "keyword": "游戏"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/challenge-suggest", sandbase.Params{
	"keyword": "游戏",
})
```

Same call via the path form: `POST /v1/api/douyin/search/challenge-suggest` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search keyword, e.g., "game" default `"游戏"` |

## Details

Retrieve autocomplete challenge and hashtag suggestions from Douyin based on a `keyword` input.

### Use cases

- Autocomplete hashtag inputs in search and tag selection tools.
- Discover related Douyin challenges and their total view counts.
- Identify popular tags matching specific topic keywords.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/challenge-suggest" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Search keyword, e.g., "game" |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "sug_list": [
    {
      "cha_name": "游戏",
      "group_id": "6596155186173973764",
      "tag": 0,
      "view_count": 739698965727
    }
  ]
}
```

### Notes

- Query related challenges by providing search text in `keyword`.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Challenge Search](/apis/douyin/search/challenge-search-v1): Returns Douyin challenge and hashtag search results matching a query.
- [Douyin Hashtag Challenge Search (V2)](/apis/douyin/search/challenge-search-v2): Returns Douyin hashtag and challenge search results matching a query keyword.
- [Douyin Discussion Search](/apis/douyin/search/discuss-search): Returns discussion and question-and-answer search results from Douyin.

---
Machine-readable: [`catalog/models/douyin/search/challenge-suggest.json`](../../../../catalog/models/douyin/search/challenge-suggest.json) · Store page: https://www.sandbase.ai/model/douyin/search/challenge-suggest

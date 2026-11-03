# Douyin Work Hot Comment Word Cloud API: pricing, parameters and code examples

`douyin/billboard/hot-comment-word-list` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns word cloud analysis data and keyword weights extracted from comments on a Douyin video. Input a target video identifier to analyze audience feedback topics.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/billboard/hot-comment-word-list", "aweme_id": "7372484719365098803"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/billboard/hot-comment-word-list', {'aweme_id': '7372484719365098803'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/billboard/hot-comment-word-list", {
  "aweme_id": "7372484719365098803"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/billboard/hot-comment-word-list", sandbase.Params{
	"aweme_id": "7372484719365098803",
})
```

Same call via the path form: `POST /v1/api/douyin/billboard/hot-comment-word-list` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `aweme_id` | string | yes | Work id  |

## Details

Retrieve keyword weights and word cloud analysis for video comments by supplying `aweme_id`. This endpoint provides audience discussion terms associated with a specific Douyin post.

### Use cases

- Analyze common terms and audience sentiment across video comments.
- Generate visual word clouds based on viewer discussion keywords.
- Extract prominent comment topics to evaluate content engagement.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/billboard/hot-comment-word-list" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"aweme_id": "7372484719365098803"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `aweme_id` | string | Yes | Work id |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "value": 61,
      "word_seg": "宝宝"
    }
  ]
}
```

### Notes

- Requires `aweme_id` representing the target work identifier.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin Billboard City List](/apis/douyin/billboard/city-list): Returns the list of Chinese cities supported by Douyin billboard rankings.
- [Douyin Billboard Vertical Content Tags](/apis/douyin/billboard/content-tag): Returns a list of vertical content tags available on the Douyin billboard platform.
- [Douyin Fan Interest Account List](/apis/douyin/billboard/hot-account-fans-interest-account-list): Returns a list of 20 accounts that followers of a target creator are interested in on Douyin.

---
Machine-readable: [`catalog/models/douyin/billboard/hot-comment-word-list.json`](../../../../catalog/models/douyin/billboard/hot-comment-word-list.json) · Store page: https://www.sandbase.ai/model/douyin/billboard/hot-comment-word-list

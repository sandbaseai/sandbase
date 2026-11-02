# Douyin Search Suggestions API: pricing, parameters and code examples

`douyin/search/search-suggest` · data API · Douyin · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.01 per call (free daily quota) · **Modes:** sync

Get Douyin search autocomplete suggestions for a keyword: the related queries users see while typing in the Douyin app.

## Pricing

- **$0.01 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "douyin/search/search-suggest", "keyword": "人工智能"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('douyin/search/search-suggest', {'keyword': '人工智能'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("douyin/search/search-suggest", {
  "keyword": "人工智能"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "douyin/search/search-suggest", sandbase.Params{
	"keyword": "人工智能",
})
```

Same call via the path form: `POST /v1/api/douyin/search/search-suggest` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Input keyword, e.g., "Artificial Intelligence" default `"人工智能"` |

## Details

Pass a keyword and get the search suggestions Douyin shows in its search box.

### Use cases

- Research long-tail keywords for Douyin SEO.
- Understand how users search for a topic.
- Generate keyword lists for content planning.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/douyin/search/search-suggest" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "人工智能"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | No | Input keyword, e.g., "Artificial Intelligence" |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "sug_list": [
    {
      "content": "人工智能",
      "word_record": {
        "group_id": "6527568579963917582",
        "words_content": "人工智能",
        "words_position": 0,
        "words_source": "sug"
      }
    }
  ]
}
```

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Douyin General Search](/model/douyin/search/general-search-v1): Search Douyin (Chinese TikTok) from the app's general search tab and get videos with descriptions, authors and play, like, comment and share counts.
- [Douyin Video Search (V1)](/model/douyin/search/video-search-v1): Search Douyin videos by keyword: descriptions, authors and play, like, comment and share counts, with sort, publish-time, duration and content-type filters.
- [Douyin Video Search](/model/douyin/search/video-search-v2): Search Douyin videos by keyword and get descriptions, authors and play, like, comment and share counts.

---
Machine-readable: [`catalog/models/douyin/search/search-suggest.json`](../../../../catalog/models/douyin/search/search-suggest.json) · Store page: https://www.sandbase.ai/model/douyin/search/search-suggest

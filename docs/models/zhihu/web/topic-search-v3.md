# Zhihu Topic Search (V3) API: pricing, parameters and code examples

`zhihu/web/topic-search-v3` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Searches Zhihu topics by keyword and returns matching topic profiles, follower metrics, and highlighted text matches with pagination support.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/topic-search-v3", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/topic-search-v3', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/topic-search-v3", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/topic-search-v3", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/topic-search-v3` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | string |  | Number of topics per page default `"25"` |
| `offset` | string |  | Offset default `"0"` |
| `keyword` | string | yes | Search Keywords  |

## Details

Query Zhihu topics matching a search term using the `keyword` parameter. It returns topic metadata including follower counts, descriptions, and topic identifiers.

### Use cases

- Discover relevant Zhihu topic identifiers for specific subject keywords.
- Inspect follower statistics and descriptions across matching Zhihu topics.
- Track topic visibility and audience interest on Zhihu.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/topic-search-v3" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keywords |
| `limit` | string | No | Number of topics per page |
| `offset` | string | No | Offset |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "data": [
    {
      "id": "20083046",
      "type": "search_result",
      "highlight": {
        "description": "由 Elon Musk, Peter Thiel, Sam Altman",
        "title": "OpenAI"
      },
      "object": {
        "agreed_count": 0,
        "description": "由 Elon Musk, Peter Thiel, Sam Altman",
        "follower_count": 6548,
        "followers_count": 6548,
        "id": "20083046",
        "name": "OpenAI"
      }
    }
  ]
}
```

### Notes

- Supports pagination via the optional `limit` and `offset` parameters.
- The `keyword` parameter is required to perform the search.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/model/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/model/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/model/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/topic-search-v3.json`](../../../../catalog/models/zhihu/web/topic-search-v3.json) · Store page: https://www.sandbase.ai/model/zhihu/web/topic-search-v3

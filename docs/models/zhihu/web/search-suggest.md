# Zhihu Search Suggestions API: pricing, parameters and code examples

`zhihu/web/search-suggest` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns search query suggestions and related topics from Zhihu based on a specified search keyword.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/search-suggest", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/search-suggest', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/search-suggest", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/search-suggest", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/zhihu/web/search-suggest` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search Keywords  |

## Details

Retrieve autocomplete suggestions from Zhihu by providing a query term in `keyword`.

### Use cases

- Populate search autocomplete menus in real time.
- Discover related topic queries based on user input.
- Enhance search input boxes with Zhihu suggestions.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/search-suggest" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search Keywords |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "suggest": [
    {
      "id": -2962146858830793432,
      "label": "activity_topic",
      "query": "OpenAI",
      "raw_id": "-2962146858830793432",
      "tab_type": "general"
    }
  ]
}
```

### Notes

- The `keyword` parameter is required.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Zhihu AI Search Stream](/model/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/model/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/model/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/search-suggest.json`](../../../../catalog/models/zhihu/web/search-suggest.json) · Store page: https://www.sandbase.ai/model/zhihu/web/search-suggest

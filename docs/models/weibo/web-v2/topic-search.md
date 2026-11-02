# Weibo Topic Search API: pricing, parameters and code examples

`weibo/web-v2/topic-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Searches Weibo topics matching a keyword and returns topic names, URLs, discussion counts, and read metrics across paginated results.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/topic-search", "query": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/topic-search', {'query': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/topic-search", {
  "query": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/topic-search", sandbase.Params{
	"query": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/topic-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `page` | integer |  | Page number (default 1) default `1` |
| `query` | string | yes | Search keyword (required)  |

## Details

Search Weibo topics by supplying a search keyword in `query`. Paginate through results using `page`.

### Use cases

- Track discussion volume and reader metrics for specific Weibo topics.
- Discover trending topic hashtags associated with a target keyword.
- Monitor audience engagement on brand or industry hashtags.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/topic-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (required) |
| `page` | integer | No | Page number (default 1) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "parsed_data": {
    "items": [
      {
        "discuss_count": 75000,
        "read_count": 110000000,
        "topic": {
          "name": "#openai#",
          "name_plain": "openai",
          "url": "https://s.weibo.com/weibo/%23openai%23"
        }
      }
    ]
  }
}
```

### Notes

- `query` is required for all searches.
- `page` defaults to 1 when omitted.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/model/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/model/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/model/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/topic-search.json`](../../../../catalog/models/weibo/web-v2/topic-search.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/topic-search

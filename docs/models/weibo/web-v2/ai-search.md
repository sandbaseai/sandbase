# Weibo AI Search API: pricing, parameters and code examples

`weibo/web-v2/ai-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/ai-search", "query": "#人工智能#"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/ai-search', {'query': '#人工智能#'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/ai-search", {
  "query": "#人工智能#"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/ai-search", sandbase.Params{
	"query": "#人工智能#",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/ai-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search keyword (required, recommend using topic format #TopicName#)  |

## Details

Use this endpoint to query Weibo AI intelligent search results by supplying a search keyword via `query`.

### Use cases

- Search Weibo content and topics using AI-assisted matching.
- Retrieve multimodal card results with relevance and hit scores.
- Monitor user engagement metrics for specific topic queries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/ai-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "#人工智能#"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search keyword (required, recommend using topic format #TopicName#) |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "card_multimodal": {
    "data": [
      {
        "click_num": 0,
        "click_rate": 0,
        "doc_score": 4467,
        "hit_score_final": 82.729683,
        "hit_score_new": 99.902344,
        "type": "p",
        "user_name": "<user>",
        "vtype": 0
      }
    ]
  }
}
```

### Notes

- The `query` parameter accepts keywords and recommends using the topic format such as #TopicName#.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [Weibo Advanced Search](/model/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/model/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo All Groups Information](/model/weibo/web-v2/all-groups): Retrieves complete group information on the Weibo platform.

---
Machine-readable: [`catalog/models/weibo/web-v2/ai-search.json`](../../../../catalog/models/weibo/web-v2/ai-search.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/ai-search

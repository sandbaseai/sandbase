# Weibo AI Related Search Content API: pricing, parameters and code examples

`weibo/web-v2/ai-related-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/ai-related-search", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/ai-related-search', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/ai-related-search", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/ai-related-search", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/ai-related-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword (required, recommend using topic format #TopicName#)  |

## Details

Returns AI-generated search extension content for a keyword on Weibo. The content comes back as one HTML string that holds related questions, recommended bloggers, and reference posts. It needs one input, `keyword`.

### Use cases

- Pull the HTML block for a topic and parse out the related questions to see what users ask about it.
- Extract the recommended bloggers for a keyword to build a list of accounts to follow or study.
- Collect the reference posts shown for a keyword to find source posts for a topic.
- Compare the AI extension block across several topic keywords to see how the content differs.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/ai-related-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword (required, recommend using topic format #TopicName#) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "code": "100000",
  "data": {
    "html": "                            <div class=\"zhisou_module_9000\">\n            <div cl…"
  },
  "msg": ""
}
```

### Response fields

| Field | Meaning |
|---|---|
| `code` | Status code of the response. The sample call returned `100000`. |
| `msg` | Message text. It was an empty string in the sample call. |
| `data.html` | HTML markup of the AI search extension module. It holds the related questions, recommended bloggers, and reference posts as page elements, so you need to parse the HTML to read them. |

### Notes

- Use the topic format `#TopicName#` for `keyword`, for example `#OpenAI#`, as the parameter description recommends.
- The response has no separate JSON fields for questions, bloggers, or posts. Parse `data.html` to get them.
- To read full posts found this way, call [Weibo Post Detail](/apis/weibo/web-v2/post-detail). For more keyword ideas, try [Weibo Similar Search Recommendations](/apis/weibo/web-v2/similar-search).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.
- [Weibo All Groups Information](/apis/weibo/web-v2/all-groups): Retrieves complete group information on the Weibo platform.

---
Machine-readable: [`catalog/models/weibo/web-v2/ai-related-search.json`](../../../../catalog/models/weibo/web-v2/ai-related-search.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/ai-related-search

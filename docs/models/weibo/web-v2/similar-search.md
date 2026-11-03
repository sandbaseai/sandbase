# Weibo Similar Search Recommendations API: pricing, parameters and code examples

`weibo/web-v2/similar-search` · data API · Weibo · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns related search keyword recommendations and hot query suggestions based on a target query. Supports topic tag formatting.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "weibo/web-v2/similar-search", "keyword": "OpenAI"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('weibo/web-v2/similar-search', {'keyword': 'OpenAI'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("weibo/web-v2/similar-search", {
  "keyword": "OpenAI"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "weibo/web-v2/similar-search", sandbase.Params{
	"keyword": "OpenAI",
})
```

Same call via the path form: `POST /v1/api/weibo/web-v2/similar-search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string | yes | Search keyword (required, supports topic tag format like #TopicName#)  |

## Details

Returns search suggestions that Weibo shows for a keyword. The main list is `hotquery`, which holds suggested query strings with a `count` value. The only input is `keyword`, which can be plain text or a topic tag like `#TopicName#`.

### Use cases

- Collect suggested search phrases around a brand name such as OpenAI for keyword research.
- Find which related phrases Weibo ranks highest for a term by comparing `count` values.
- Spot new news-style queries tied to a keyword, such as event headlines, to feed a topic monitor.
- Check whether a topic tag keyword returns suggestions before you run a full post search.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/weibo/web-v2/similar-search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `keyword` | string | Yes | Search keyword (required, supports topic tag format like #TopicName#) |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "history": [],
  "hotquery": [
    {
      "count": 500001120,
      "discuss": 0,
      "discuss_arae": 0,
      "discuss_num": 0,
      "suggestion": "openai",
      "top_flag": 2,
      "topic_flag": 0,
      "type": 2
    }
  ],
  "query_relates": [],
  "real_hot": [],
  "user": [],
  "users": []
}
```

### Response fields

| Field | Meaning |
|---|---|
| `hotquery[].suggestion` | The suggested search text, for example `openai 数学`. |
| `hotquery[].count` | A numeric score attached to the suggestion. Higher values appear first in the sample, so you can use it to compare suggestions. |
| `hotquery[].type / hotquery[].top_flag` | Numeric codes for the kind of suggestion. In the sample both fields hold the same value (`2` or `15`) for each item. The response does not explain what each code means. |
| `hotquery[].topic_flag` | Numeric flag for topic status. It is `0` for all items in the sample. |
| `hotquery[].discuss / hotquery[].discuss_num / hotquery[].discuss_arae` | Discussion counters for the suggestion. All are `0` in the sample, so they may be empty for many queries. The key `discuss_arae` is spelled this way in the response. |
| `history / query_relates / real_hot / user / users` | Other suggestion lists. All are empty arrays for this request, so check them for other keywords. |

### Notes

- Send `keyword` as plain text or wrapped in `#` for a topic tag, for example `#TopicName#`.
- The request has no pagination parameter. Each call returns one list of suggestions.
- To read the posts behind a suggestion, pass its `suggestion` text to [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search) or [Weibo Real-Time Search](/apis/weibo/web-v2/realtime-search).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Weibo Advanced Search](/apis/weibo/web-v2/advanced-search): Search Weibo posts by keyword with filters for time range, post type (hot, original, verified, media) and content type (images, video, links).
- [Weibo AI Related Search Content](/apis/weibo/web-v2/ai-related-search): Returns AI-generated content extensions for a keyword, including related questions, recommended bloggers, and reference posts.
- [Weibo AI Search](/apis/weibo/web-v2/ai-search): Returns multimodal search results and relevance scores from Weibo intelligent search for a specified keyword or topic query.

---
Machine-readable: [`catalog/models/weibo/web-v2/similar-search.json`](../../../../catalog/models/weibo/web-v2/similar-search.json) · Store page: https://www.sandbase.ai/model/weibo/web-v2/similar-search

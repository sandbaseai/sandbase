# Zhihu Search Recommendations API: pricing, parameters and code examples

`zhihu/web/search-recommend` · data API · Zhihu · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns recommended search queries and trending suggestions from Zhihu Web. Helps discover popular topics and keywords without providing input search criteria.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "zhihu/web/search-recommend"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('zhihu/web/search-recommend', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("zhihu/web/search-recommend", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "zhihu/web/search-recommend", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/zhihu/web/search-recommend` with the body above minus `model`.

## Details

Returns a list of recommended search queries from Zhihu Web. It takes no input, so you send an empty JSON object `{}`.

### Use cases

- Show the search phrases Zhihu currently recommends on its search entry page.
- Track which news topics appear as recommended queries and which carry the `new` label.
- Collect recommended phrases as seed keywords for topic or content research.
- Feed a recommended phrase into a keyword search to find the posts behind it.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/zhihu/web/search-recommend" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

The result is returned in `outputs[0].data`.

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "offset": 0,
  "recommend_queries": {
    "attached_info": "OkaCAyA2NjRhZDk1Y2E1ZWJmM2NlMjIwZGYzZjM0MjBmNjI5YfIDIDRlZDk4YjhlZTdjNDYwYjc5OTA3…",
    "queries": [
      {
        "attached_info": "OkaCAyA2NjRhZDk1Y2E1ZWJmM2NlMjIwZGYzZjM0MjBmNjI5YfIDIDRlZDk4YjhlZTdjNDYwYjc5OTA3…",
        "from_scene": "",
        "query": "将有两名中国人登陆月球",
        "query_color": "",
        "query_display": "将有两名中国人登陆月球",
        "query_id": 0,
        "real_query": "将有两名中国人登陆月球",
        "redirect_link": "",
        "request_click_id": "6488e8b0-5a28-48b1-be7c-585d8be83ef8",
        "str_query_id": "",
        "type": "normal",
        "uuid": "0da2b799-c498-4975-a2da-71a4b3e56938"
      }
    ],
    "recommend_hash_id": "664ad95ca5ebf3ce220df3f3420f629a"
  },
  "search_hash_id": "",
  "switch_off": false
}
```

### Response fields

| Field | Meaning |
|---|---|
| `recommend_queries.queries[]` | The list of recommended search queries. Each item is one suggested phrase. |
| `recommend_queries.queries[].query / query_display / real_query` | The text of the suggested query. In the sample all three hold the same phrase. |
| `recommend_queries.queries[].label` | A tag on some queries. The sample shows `new`. Items without a tag have no `label` key. |
| `recommend_queries.queries[].image_item.icon_url` | URL of a small icon shown next to the query. `image_item.width` and `image_item.height` give its size values. |
| `recommend_queries.queries[].type` | The query type. The sample value is `normal`. |
| `recommend_queries.queries[].uuid` | A unique ID string for each recommended query. |
| `recommend_queries.queries[].request_click_id` | An ID shared by all queries in the same response. |
| `recommend_queries.queries[].attached_info / recommend_queries.attached_info` | Encoded tracking strings attached to each query and to the whole list. |
| `recommend_queries.recommend_hash_id` | A hash ID for this set of recommendations. |
| `switch_off` | A boolean flag. The sample value is `false`. |

### Notes

- The request has no parameters. Send `{}` as the body.
- `query_id` is `0` and `redirect_link` is empty in the sample, so use the `query` text as the identifier for the phrase.
- To search with a returned phrase, pass its `query` text to [Zhihu Article Search](/apis/zhihu/web/article-search-v3).
- For the current trending questions, see [Zhihu Hot List](/apis/zhihu/web/hot-list).

### Pricing

$0.001 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

### Related APIs

- [Zhihu AI Search Stream](/apis/zhihu/web/ai-search-stream): Returns streaming AI search results from Zhihu based on a query prompt.
- [Zhihu Answer Details](/apis/zhihu/web/answer-detail): Retrieves detailed information for a specific Zhihu answer using its numeric ID, including answer text, timestamps, and share links.
- [Zhihu Article Search](/apis/zhihu/web/article-search-v3): Search Zhihu articles and answers by keyword and get titles, excerpts, authors, vote and comment counts, with sorting, content type and time filters plus offse…

---
Machine-readable: [`catalog/models/zhihu/web/search-recommend.json`](../../../../catalog/models/zhihu/web/search-recommend.json) · Store page: https://www.sandbase.ai/model/zhihu/web/search-recommend

# Tavily Search API: pricing, parameters and code examples

`tavily/search` · data API · Tavily · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.012 per call (free daily quota) · **Modes:** sync

AI-optimized web search for agents and RAG: ranked results with titles, URLs and relevant content, depth control, news and finance topics, domain filters and an optional generated answer.

## Pricing

- **$0.012 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tavily/search", "include_answer": true, "max_results": 8, "query": "手性钙钛矿 圆偏振拉曼 手性声子 谱学", "search_depth": "basic"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tavily/search', {'include_answer': True, 'max_results': 8, 'query': '手性钙钛矿 圆偏振拉曼 手性声子 谱学', 'search_depth': 'basic'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tavily/search", {
  "include_answer": true,
  "max_results": 8,
  "query": "手性钙钛矿 圆偏振拉曼 手性声子 谱学",
  "search_depth": "basic"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tavily/search", sandbase.Params{
	"include_answer": true,
	"max_results": 8,
	"query": "手性钙钛矿 圆偏振拉曼 手性声子 谱学",
	"search_depth": "basic",
})
```

Same call via the path form: `POST /v1/api/tavily/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | The search query.  |
| `topic` | string |  | Topic category to focus the search. one of: `general`, `news`, `finance`; default `"general"` |
| `max_results` | integer |  | Maximum number of results to return. default `5`; range 1–20 |
| `search_depth` | string |  | Depth of search. 'advanced' returns more comprehensive results. one of: `basic`, `advanced`; default `"basic"` |
| `include_answer` | boolean |  | Include an LLM-generated answer summarizing the results. default `false` |
| `exclude_domains` | array |  | Exclude results from these domains.  |
| `include_domains` | array |  | Only include results from these domains.  |
| `include_raw_content` | boolean |  | Include the full raw page content for each result. default `false` |

## Details

Tavily returns search results already cleaned for LLMs: each result has a title, URL, relevant content snippet and score. Optionally get a short generated answer or the raw page content.

### Use cases

- Give agents real-time web access.
- Build RAG pipelines on fresh sources.
- Research news or financial topics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tavily/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI Codex documentation", "max_results": 3}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The search query. |
| `topic` | string | No | Topic category to focus the search. |
| `max_results` | integer | No | Maximum number of results to return. |
| `search_depth` | string | No | Depth of search. 'advanced' returns more comprehensive results. |
| `include_answer` | boolean | No | Include an LLM-generated answer summarizing the results. |
| `exclude_domains` | array | No | Exclude results from these domains. |
| `include_domains` | array | No | Only include results from these domains. |
| `include_raw_content` | boolean | No | Include the full raw page content for each result. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "query": "OpenAI Codex documentation",
  "results": [
    {
      "title": "Documentation and implementation of Open AI's new Codex model - API -…",
      "url": "https://community.openai.com/t/documentation-and-implementation-of-op…",
      "content": "# Documentation and implementation of Open AI's new Codex model  Hi,  I am look…",
      "score": 0.8624794
    }
  ],
  "response_time": 1.18
}
```

### Notes

- `search_depth`: basic or advanced (more comprehensive).
- Set `include_answer` to `true` for an LLM-generated summary.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/tavily/search.json`](../../../catalog/models/tavily/search.json) · Store page: https://www.sandbase.ai/model/tavily/search

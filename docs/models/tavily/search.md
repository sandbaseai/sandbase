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

Web search built for LLM agents and RAG. Each result comes back with a title, URL, the most relevant content snippet and a relevance score, so you can pass results straight to a model. Optionally get a generated answer, images or the cleaned full page text.

### Use cases

- Give an agent current web results without writing a scraper.
- Collect fresh sources for retrieval-augmented generation.
- Track news or finance topics with `topic` and a time range.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tavily/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI Codex documentation", "max_results": 3}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The search query. |
| `exclude_domains` | array | No | Exclude results from these domains. |
| `include_answer` | boolean | No | Include an LLM-generated answer summarizing the results. |
| `include_domains` | array | No | Only include results from these domains. |
| `include_raw_content` | boolean | No | Include the full raw page content for each result. |
| `max_results` | integer | No | Maximum number of results to return. |
| `search_depth` | string | No | Depth of search. 'advanced' returns more comprehensive results. |
| `topic` | string | No | Topic category to focus the search. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "answer": null,
  "follow_up_questions": null,
  "images": [],
  "query": "OpenAI Codex documentation",
  "request_id": "9a4efa6f-8022-44af-a4c1-a1633319ea49",
  "response_time": 0.99,
  "results": [
    {
      "content": "[52:01] So before we wrap up, I just want to share a few additional resources. s…",
      "id": "a3a4d2-00",
      "raw_content": null,
      "score": 0.81665546,
      "title": "Getting started with Codex",
      "url": "https://www.youtube.com/watch?v=px7XlbYgk7I"
    }
  ],
  "usage": {
    "credits": 1
  }
}
```

### Response fields

| Field | Meaning |
|---|---|
| `results[]` | Ranked results: `title`, `url`, `content` (relevant excerpt), `score` (0-1 relevance) and `raw_content` when `include_raw_content` is set. |
| `answer` | Generated answer when `include_answer` is true, otherwise null. |
| `images` | Image results when `include_images` is true. |
| `response_time` | Upstream time in seconds. |

### Notes

- `search_depth: "advanced"` searches more deeply and is slower; the default `basic` fits most agent calls.
- Use `include_domains` / `exclude_domains` to restrict sources and `max_results` (up to 20) to bound the answer size.

### Pricing

$0.012 per successful call. Failed calls, including lookups whose target does not exist, are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/tavily/search.json`](../../../catalog/models/tavily/search.json) · Store page: https://www.sandbase.ai/model/tavily/search

# Cloudsway Web Search API: pricing, parameters and code examples

`cloudsway/search` · data API · Cloudsway · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.005 per call (free daily quota) · **Modes:** sync

Web search API for AI agents with topic focus (news, academic, company, finance and more), country, date range and domain filters, plus optional full text, summaries and highlights.

## Pricing

- **$0.005 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "cloudsway/search", "end_date": "2026-08-06", "include_highlights": true, "max_results": 5, "query": "Groq LPU inference funding valuation revenue 2025 2026", "search_depth": "basic", "start_date": "2024-01-01", "topic": "company"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('cloudsway/search', {'end_date': '2026-08-06', 'include_highlights': True, 'max_results': 5, 'query': 'Groq LPU inference funding valuation revenue 2025 2026', 'search_depth': 'basic', 'start_date': '2024-01-01', 'topic': 'company'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("cloudsway/search", {
  "end_date": "2026-08-06",
  "include_highlights": true,
  "max_results": 5,
  "query": "Groq LPU inference funding valuation revenue 2025 2026",
  "search_depth": "basic",
  "start_date": "2024-01-01",
  "topic": "company"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "cloudsway/search", sandbase.Params{
	"end_date": "2026-08-06",
	"include_highlights": true,
	"max_results": 5,
	"query": "Groq LPU inference funding valuation revenue 2025 2026",
	"search_depth": "basic",
	"start_date": "2024-01-01",
	"topic": "company",
})
```

Same call via the path form: `POST /v1/api/cloudsway/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | The search query string.  |
| `topic` | string |  | Content category to focus on. one of: `general`, `news`, `academic`, `company`, `people`, `finance`; default `"general"` |
| `country` | string |  | Two-letter ISO country code for localized results. one of: `US`, `GB`, `CN`, `JP`, `DE`, `FR`, `KR`, `IN`, `CA`, `AU`, `SG`, `BR` … |
| `end_date` | string |  | Only return results published before this date. Format: YYYY-MM-DD.  |
| `start_date` | string |  | Only return results published after this date. Format: YYYY-MM-DD.  |
| `max_results` | integer |  | Maximum number of results to return. default `10`; range 1–100 |
| `include_text` | boolean |  | Return full page text content for each result. default `false` |
| `search_depth` | string |  | basic: fast, low-latency search (~1s). advanced: multi-step reasoning with higher quality results (4-40s), costs more. one of: `basic`, `advanced`; default `"basic"` |
| `max_characters` | integer |  | Maximum characters for text content per result. default `3000`; range 1–10000 |
| `exclude_domains` | array |  | Exclude results from these domains.  |
| `include_domains` | array |  | Only return results from these domains.  |
| `include_summary` | boolean |  | Return a short summary of each result. default `false` |
| `include_highlights` | boolean |  | Return key excerpts relevant to the query. default `true` |

## Details

Search the web for a query and get ranked results with title, URL, publish date and relevance score. Optionally include highlights, summaries or full page text for RAG.

### Use cases

- Ground LLM answers with fresh web sources.
- Research news, companies or academic topics.
- Restrict results to trusted domains or a date window.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/cloudsway/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI Codex documentation", "max_results": 3}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The search query string. |
| `topic` | string | No | Content category to focus on. |
| `country` | string | No | Two-letter ISO country code for localized results. |
| `end_date` | string | No | Only return results published before this date. |
| `start_date` | string | No | Only return results published after this date. |
| `max_results` | integer | No | Maximum number of results to return. |
| `include_text` | boolean | No | Return full page text content for each result. |
| `search_depth` | string | No | basic: fast, low-latency search (~1s). advanced: multi-step reasoning with higher quality results (4-40s), costs more. |
| `max_characters` | integer | No | Maximum characters for text content per result. |
| `exclude_domains` | array | No | Exclude results from these domains. |
| `include_domains` | array | No | Only return results from these domains. |
| `include_summary` | boolean | No | Return a short summary of each result. |
| `include_highlights` | boolean | No | Return key excerpts relevant to the query. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "entities": [
    {
      "title": "OpenAI Codex CLI Official Documentation Guide (2026) | Codex Knowledg…",
      "url": "https://codex.danielvaughan.com/2026/04/19/openai-codex-cli-official-…",
      "content": "The official Codex CLI documentation has grown considerably since the tool’s op…",
      "published_date": "2026-04-19T07:22:32.0000000",
      "score": 0.75424725
    }
  ]
}
```

### Notes

- `search_depth`: basic (about 1 s) or advanced (multi-step, 4–40 s, higher quality).

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/cloudsway/search.json`](../../../catalog/models/cloudsway/search.json) · Store page: https://www.sandbase.ai/model/cloudsway/search

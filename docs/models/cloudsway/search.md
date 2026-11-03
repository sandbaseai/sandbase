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

Runs a web search and returns a ranked list of results, each with a title, URL, text excerpt and relevance score. It needs a `query` string. Optional parameters set the topic, country, date range, domain filters and how much text each result carries.

### Use cases

- Ground an LLM answer with web sources for a question such as a product's documentation.
- Search news, company, people, finance or academic pages by setting `topic`.
- Limit results to trusted sites with `include_domains`, or drop noisy sites with `exclude_domains`.
- Collect page text for a RAG index by setting `include_text` and `max_characters`.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/cloudsway/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI Codex documentation", "max_results": 3}'
```

The result is returned in `outputs[0]`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The search query string. |
| `country` | string | No | Two-letter ISO country code for localized results. |
| `end_date` | string | No | Only return results published before this date. Format: YYYY-MM-DD. |
| `exclude_domains` | array | No | Exclude results from these domains. |
| `include_domains` | array | No | Only return results from these domains. |
| `include_highlights` | boolean | No | Return key excerpts relevant to the query. |
| `include_summary` | boolean | No | Return a short summary of each result. |
| `include_text` | boolean | No | Return full page text content for each result. |
| `max_characters` | integer | No | Maximum characters for text content per result. |
| `max_results` | integer | No | Maximum number of results to return. |
| `search_depth` | string | No | basic: fast, low-latency search (~1s). advanced: multi-step reasoning with higher quality results (4-40s), costs more. |
| `start_date` | string | No | Only return results published after this date. Format: YYYY-MM-DD. |
| `topic` | string | No | Content category to focus on. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "entities": [
    {
      "content": "This repository is an open mirror of publicly available OpenAI documentation, de…",
      "favicon": "",
      "published_date": "",
      "score": 0.7974826,
      "text": "This repository is an open mirror of publicly available OpenAI documentation, de…",
      "title": "life-is-blue/openai-codex-docs-mirror",
      "url": "/goto?url=CAEScwHrOzAVyqJlcWCR7wj-Uo8LUhYkbGGWgWFrXninn1jsth8bPewCNJ4g0-3WaY1ZOS…"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `entities[]` | One search result. The list is ordered by the search ranking and holds up to `max_results` items. |
| `entities[].title` | Title of the result page. |
| `entities[].url` | Link to the result page. Most results hold a full `https://` URL, but some hold a relative `/goto?url=...` link. |
| `entities[].content` | Short excerpt of the page that relates to the query. |
| `entities[].text` | Longer page text. It does not appear on every result. |
| `entities[].score` | Relevance score as a decimal number. Use it to compare results within one response. |
| `entities[].published_date` | Publish time in ISO format such as `2026-03-24T00:11:38.0000000`. It is an empty string when the page has no date. |
| `entities[].favicon` | URL of the site icon. It is an empty string when none is available. |

### Notes

- Set `max_results` between 1 and 100. The default is 10.
- `search_depth` accepts `basic` or `advanced`. The `advanced` setting takes longer and costs more.
- `start_date` and `end_date` use the `YYYY-MM-DD` format.
- `topic` accepts `general`, `news`, `academic`, `company`, `people` or `finance`.

### Pricing

$0.005 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/cloudsway/search.json`](../../../catalog/models/cloudsway/search.json) · Store page: https://www.sandbase.ai/model/cloudsway/search

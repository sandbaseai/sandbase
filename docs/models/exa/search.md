# Exa Search API: pricing, parameters and code examples

`exa/search` · data API · Exa · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0105 per call (free daily quota) · **Modes:** sync

Neural web search for AI apps and agents. Ask in natural language and get the most relevant pages, with optional highlights, summaries or full text, domain filters and date ranges.

## Pricing

- **$0.0105 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "exa/search", "category": "research paper", "contents": {"highlights": true}, "numResults": 5, "query": "Ferroelectric control of chiral phonons"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('exa/search', {'category': 'research paper', 'contents': {'highlights': True}, 'numResults': 5, 'query': 'Ferroelectric control of chiral phonons'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("exa/search", {
  "category": "research paper",
  "contents": {
    "highlights": true
  },
  "numResults": 5,
  "query": "Ferroelectric control of chiral phonons"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "exa/search", sandbase.Params{
	"category": "research paper",
	"contents": map[string]any{
		"highlights": true,
	},
	"numResults": 5,
	"query": "Ferroelectric control of chiral phonons",
})
```

Same call via the path form: `POST /v1/api/exa/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `type` | string |  | Search mode. auto lets Exa choose; the deep modes trade latency for higher-quality retrieval. one of: `auto`, `fast`, `instant`, `deep-lite`, `deep`, `deep-reasoning`; default `"auto"` |
| `query` | string | yes | The natural-language search query.  |
| `category` | string |  | Optional hint about the kind of pages to prioritize. one of: `company`, `research paper`, `news`, `personal site`, `financial report`, `people` |
| `contents` | object |  | Content options to return alongside each result.  |
| `numResults` | integer |  | Number of results to return. default `10`; range 1–100 |
| `outputSchema` | object |  | JSON Schema used to synthesize a structured output from the results.  |
| `systemPrompt` | string |  | Instruction that guides how the structured output is generated.  |
| `excludeDomains` | array |  | Exclude results from these domains.  |
| `includeDomains` | array |  | Only return results from these domains.  |
| `endPublishedDate` | string |  | Only return results published on or before this ISO 8601 date.  |
| `startPublishedDate` | string |  | Only return results published on or after this ISO 8601 date.  |

## Details

Exa Search finds web pages by meaning rather than keywords. Send a natural-language query and get ranked results with titles, URLs and optional page content, ready to feed into an LLM.

### Use cases

- Ground LLM answers and agents with fresh web sources (RAG).
- Find companies, research papers or news on a topic.
- Restrict results to trusted domains or a publish-date window.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/exa/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI Codex documentation", "type": "fast", "numResults": 3, "contents": {"highlights": true}}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The natural-language search query. |
| `type` | string | No | Search mode. auto lets Exa choose; the deep modes trade latency for higher-quality retrieval. |
| `category` | string | No | Optional hint about the kind of pages to prioritize. |
| `contents` | object | No | Content options to return alongside each result. |
| `numResults` | integer | No | Number of results to return. |
| `outputSchema` | object | No | JSON Schema used to synthesize a structured output from the results. |
| `systemPrompt` | string | No | Instruction that guides how the structured output is generated. |
| `excludeDomains` | array | No | Exclude results from these domains. |
| `includeDomains` | array | No | Only return results from these domains. |
| `endPublishedDate` | string | No | Only return results published on or before this ISO 8601 date. |
| `startPublishedDate` | string | No | Only return results published on or after this ISO 8601 date. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "entities": [
    {
      "title": "Codex manual",
      "url": "https://developers.openai.com/codex/codex-manual.md",
      "highlights": [
        "Codex is OpenAI's coding agent for software development. ChatGPT Plus, Pro, Business, Edu, and Enterprise pla…"
      ]
    }
  ]
}
```

### Notes

- `type` trades speed for quality: `instant` / `fast` for low latency, `deep` modes for harder research queries.
- Use `contents` to return highlights, summaries or full text with each result.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/exa/search.json`](../../../catalog/models/exa/search.json) · Store page: https://www.sandbase.ai/model/exa/search

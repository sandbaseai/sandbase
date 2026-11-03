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

Exa Search returns web pages ranked by meaning for a natural-language query. It needs a `query` and can also return highlights, summaries or full text for each result.

### Use cases

- Feed relevant web pages into an LLM agent as sources for an answer.
- Search only `openai.com` or other chosen domains to find official documentation.
- Find news or research papers on a topic within a set publish-date window.
- Pull highlight snippets for many pages to check which ones match a topic before reading them in full.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/exa/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI Codex documentation", "type": "fast", "numResults": 3, "contents": {"highlights": true}}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The natural-language search query. |
| `category` | string | No | Optional hint about the kind of pages to prioritize. |
| `contents` | object | No | Content options to return alongside each result. |
| `endPublishedDate` | string | No | Only return results published on or before this ISO 8601 date. |
| `excludeDomains` | array | No | Exclude results from these domains. |
| `includeDomains` | array | No | Only return results from these domains. |
| `numResults` | integer | No | Number of results to return. |
| `outputSchema` | object | No | JSON Schema used to synthesize a structured output from the results. |
| `startPublishedDate` | string | No | Only return results published on or after this ISO 8601 date. |
| `systemPrompt` | string | No | Instruction that guides how the structured output is generated. |
| `type` | string | No | Search mode. auto lets Exa choose; the deep modes trade latency for higher-quality retrieval. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "requestId": "d90a84d1907c9964235784d496c7fe4b",
  "resolvedSearchType": "",
  "results": [
    {
      "highlights": [
        "# Codex — full documentation\n\n> Single-file Markdown export of ChatGPT docs for …"
      ],
      "id": "https://learn.chatgpt.com/docs/llms-full.txt",
      "title": "",
      "url": "https://learn.chatgpt.com/docs/llms-full.txt"
    }
  ],
  "searchTime": 407.6
}
```

### Response fields

| Field | Meaning |
|---|---|
| `requestId` | ID of this search request. |
| `resolvedSearchType` | Search mode that ran. It can be an empty string, as in this `fast` request. |
| `results[]` | List of matching pages, ordered by relevance. |
| `results[].url / results[].id` | Page URL. In this response `id` has the same value as `url`. |
| `results[].title` | Page title. It can be an empty string when the page has no title. |
| `results[].highlights[]` | Text snippets from the page that match the query. These appear when `contents.highlights` is `true`, and long snippets are cut. |
| `searchTime` | Time the search took. The response shows no unit, so check it against your own timing before relying on it. |

### Notes

- Set `numResults` between 1 and 100 to control how many results come back. The default is 10.
- Set `contents.text`, `contents.summary` or `contents.highlights` to `true` to get page content in each result. Without it, results hold only the basic fields.
- Use `includeDomains` or `excludeDomains` with `startPublishedDate` and `endPublishedDate` (ISO 8601) to narrow results.
- To read the full content of known URLs, call [Exa Contents](/apis/exa/contents). To get a direct answer with sources, call [Exa Question Answering](/apis/exa/answer).

### Pricing

$0.0105 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/exa/search.json`](../../../catalog/models/exa/search.json) · Store page: https://www.sandbase.ai/model/exa/search

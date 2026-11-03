# Firecrawl Web Search API: pricing, parameters and code examples

`firecrawl/search` · data API · Firecrawl · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.015 per call · **Modes:** sync

Searches the web using a text query and returns relevant pages with their titles, descriptions, and source URLs. Supports adjusting result counts.

## Pricing

- **$0.015 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "firecrawl/search", "query": "openai"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('firecrawl/search', {'query': 'openai'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("firecrawl/search", {
  "query": "openai"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "firecrawl/search", sandbase.Params{
	"query": "openai",
})
```

Same call via the path form: `POST /v1/api/firecrawl/search` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `limit` | integer |  | Maximum number of results to return. range 1–100 |
| `query` | string | yes | The search query.  |

## Details

Returns a ranked list of web pages that match a text query. Each result has a title, a description, a source URL, and its rank. The only required input is `query`, and `limit` caps the number of results.

### Use cases

- Collect source URLs and snippets for a research topic before reading the pages.
- Feed search results into an LLM pipeline as context for a question.
- Check which sites rank for a brand name such as `OpenAI`.
- Build a list of URLs to pass to a scraper or crawler.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/firecrawl/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The search query. |
| `limit` | integer | No | Maximum number of results to return. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "data": {
    "web": [
      {
        "description": "OpenAI | Research & Deployment\n\n## Latest research\n[An OpenAI model proposes a s…",
        "position": 1,
        "title": "OpenAI | Research & Deployment",
        "url": "https://openai.com/"
      }
    ]
  },
  "id": "01a1a053-d894-7766-8468-2b045150832c",
  "success": true
}
```

### Response fields

| Field | Meaning |
|---|---|
| `data.web[]` | List of search results, in ranked order. |
| `data.web[].position` | Rank of the result in the list. `1` is the first result. |
| `data.web[].title` | Title of the web page. |
| `data.web[].url` | Source URL of the page. |
| `data.web[].description` | Text taken from the page. It can be a short summary or raw page text with Markdown, links, and line breaks. |
| `success` | `true` when the search call worked. |
| `id` | Unique ID of this search response, in UUID format. |

### Notes

- `query` can be up to 500 characters. `limit` accepts whole numbers from 1 to 100.
- The `description` value can contain Markdown and image links, so clean it before showing it to users.
- To read the full content of a result, pass its `url` to [Firecrawl Page Scraper](/apis/firecrawl/scrape).
- To list other pages on the same site, pass the `url` to [Firecrawl URL Discovery](/apis/firecrawl/map).

### Pricing

$0.015 per successful call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/firecrawl/search.json`](../../../catalog/models/firecrawl/search.json) · Store page: https://www.sandbase.ai/model/firecrawl/search

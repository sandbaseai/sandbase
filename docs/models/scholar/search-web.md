# Scholar Web Search API: pricing, parameters and code examples

`scholar/search-web` · data API · Scholar · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0036 per call (free daily quota) · **Modes:** sync

Returns web search results tailored to academic and research topics. Supports filtering by publication year ranges and limiting the total result count.

## Pricing

- **$0.0036 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "scholar/search-web", "max_num_results": 10, "query": "ferroelectric control of chiral phonons"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('scholar/search-web', {'max_num_results': 10, 'query': 'ferroelectric control of chiral phonons'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("scholar/search-web", {
  "max_num_results": 10,
  "query": "ferroelectric control of chiral phonons"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "scholar/search-web", sandbase.Params{
	"max_num_results": 10,
	"query": "ferroelectric control of chiral phonons",
})
```

Same call via the path form: `POST /v1/api/scholar/search-web` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search query for scholarly materials.  |
| `as_yhi` | integer |  | Year of publication upper bound. range 1900–2030 |
| `as_ylo` | integer |  | Year of publication lower bound. range 1900–2030 |
| `max_num_results` | integer |  | Maximum number of search results to return, up to 100. range 1–100 |

## Details

Returns a list of web search results for a query about academic or research topics. Each result has a title, a link and a short text snippet. The only required input is `query`.

### Use cases

- Collect links to web pages about a research topic or organization to start a literature review.
- Limit results to a range of publication years with `as_ylo` and `as_yhi` when tracking recent work on a subject.
- Pull titles and snippets into a script to build a quick reading list for a topic.
- Cap the number of results with `max_num_results` to keep batch searches small.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/scholar/search-web" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

The result is returned in `outputs[0].data`.

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search query for scholarly materials. |
| `as_yhi` | integer | No | Year of publication upper bound. |
| `as_ylo` | integer | No | Year of publication lower bound. |
| `max_num_results` | integer | No | Maximum number of search results to return, up to 100. |

### Example response

Real response for the request above, trimmed: lists keep their first item and long strings are cut.

```json
{
  "id": "eHmhgUEw1bDSj3osRJJASw",
  "results": [
    {
      "link": "https://openai.com/",
      "snippet": "We believe our research will eventually lead to artificial general intelligence,…",
      "title": "OpenAI | Research & Deployment"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | Identifier string for this search response. |
| `results` | List of search results for the query. |
| `results[].title` | Title of the matching web page. |
| `results[].link` | Full URL of the matching web page. |
| `results[].snippet` | Short text excerpt from the page that relates to the query. |

### Notes

- Use `max_num_results` (1 to 100) to set how many results to return.
- Use `as_ylo` and `as_yhi` (each 1900 to 2030) to set the lower and upper publication year.
- Results are general web pages, so they can include company sites and encyclopedia entries. For results from Google Scholar, call [Scholar Search (Google Scholar)](/apis/scholar/search-scholar).
- For a combined search, try [Scholar Smart Search](/apis/scholar/search-mixed).

### Pricing

$0.0036 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/scholar/search-web.json`](../../../catalog/models/scholar/search-web.json) · Store page: https://www.sandbase.ai/model/scholar/search-web

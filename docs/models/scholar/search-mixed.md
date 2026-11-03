# Scholar Smart Search API: pricing, parameters and code examples

`scholar/search-mixed` · data API · Scholar · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0036 per call (free daily quota) · **Modes:** sync

Returns scholarly and academic search results matching a query. Supports filtering by publication year range and limiting the total number of returned entries.

## Pricing

- **$0.0036 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "scholar/search-mixed", "max_num_results": 15, "query": "ferroelectric control of chiral phonons"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('scholar/search-mixed', {'max_num_results': 15, 'query': 'ferroelectric control of chiral phonons'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("scholar/search-mixed", {
  "max_num_results": 15,
  "query": "ferroelectric control of chiral phonons"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "scholar/search-mixed", sandbase.Params{
	"max_num_results": 15,
	"query": "ferroelectric control of chiral phonons",
})
```

Same call via the path form: `POST /v1/api/scholar/search-mixed` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search query for scholarly materials.  |
| `as_yhi` | integer |  | Year of publication upper bound. range 1900–2030 |
| `as_ylo` | integer |  | Year of publication lower bound. range 1900–2030 |
| `max_num_results` | integer |  | Maximum number of search results to return, up to 100. range 1–100 |

## Details

Returns a list of scholarly search results for a text query. Each result has a title, a link, a snippet, the author list and a citation count. The only required input is `query`, and you can narrow results by publication year or cap the number of results.

### Use cases

- Build a reading list of papers on a topic by collecting titles and links.
- Rank papers on a subject by `number_of_citations` to find the most cited work.
- Limit a literature search to a set of years with `as_ylo` and `as_yhi`.
- Pull snippets and author names into a tool that screens papers before full review.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/scholar/search-mixed" \
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
  "id": "IIWUPXGJyZoQBlkCNCM7ew",
  "results": [
    {
      "authors": [
        "KI Roumeliotis"
      ],
      "link": "https://www.mdpi.com/1999-5903/15/6/192",
      "number_of_citations": 1215,
      "snippet": "According to numerous reports, ChatGPT represents a significant breakthrough in …",
      "title": "Chatgpt and open-ai models: A preliminary review"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `id` | Identifier of this search response. |
| `results[]` | List of matching scholarly results, one object per result. |
| `results[].title` | Title of the paper or article. |
| `results[].link` | URL of the page where the result is hosted, such as a journal site or arXiv. |
| `results[].authors[]` | Author names as shown in the result, often with first names shortened to initials. |
| `results[].number_of_citations` | Number of citations listed for the result. |
| `results[].snippet` | Short text excerpt from the result. Some results do not include it. |

### Notes

- Send `query` as free text. Optional inputs are `max_num_results` (1 to 100), `as_ylo` and `as_yhi` (years from 1900 to 2030).
- The `snippet` key is missing from some results, so check for it before reading it.
- For other search styles, see [Scholar Search (Google Scholar)](/apis/scholar/search-scholar) or [Scholar Web Search](/apis/scholar/search-web).

### Pricing

$0.0036 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/scholar/search-mixed.json`](../../../catalog/models/scholar/search-mixed.json) · Store page: https://www.sandbase.ai/model/scholar/search-mixed

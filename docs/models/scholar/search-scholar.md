# Scholar Search (Google Scholar) API: pricing, parameters and code examples

`scholar/search-scholar` · data API · Scholar · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0036 per call (free daily quota) · **Modes:** sync

Search academic papers on Google Scholar: titles, authors, links, citation counts and snippets, with publication-year filters.

## Pricing

- **$0.0036 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "scholar/search-scholar", "max_num_results": 10, "query": "chiral phonons"}'
```

**Python** ([sdk/python](../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('scholar/search-scholar', {'max_num_results': 10, 'query': 'chiral phonons'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("scholar/search-scholar", {
  "max_num_results": 10,
  "query": "chiral phonons"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "scholar/search-scholar", sandbase.Params{
	"max_num_results": 10,
	"query": "chiral phonons",
})
```

Same call via the path form: `POST /v1/api/scholar/search-scholar` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `query` | string | yes | Search query for scholarly materials.  |
| `as_yhi` | integer |  | Year of publication upper bound. range 1900–2030 |
| `as_ylo` | integer |  | Year of publication lower bound. range 1900–2030 |
| `max_num_results` | integer |  | Maximum number of search results to return, up to 100. range 1–100 |

## Details

This API searches Google Scholar and returns a list of matching papers. Each result has a title, author initials, a link, a citation count and a text snippet. It needs a `query` string and can limit results by publication year.

### Use cases

- Build a reading list on a topic by pulling the top papers for a search phrase.
- Rank candidate papers by `number_of_citations` to find widely cited work.
- Restrict a literature search to recent work with `as_ylo` and `as_yhi`.
- Feed titles, links and snippets to an AI assistant so it can cite academic sources.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/scholar/search-scholar" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "large language models", "max_num_results": 3}'
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
  "id": "J9ir6_SfmHvXRvlaVSaKOA",
  "results": [
    {
      "authors": [
        "G Bai"
      ],
      "link": "https://dl.acm.org/doi/abs/10.1145/3845797",
      "number_of_citations": 279,
      "snippet": "… Beyond Eficiency: A Systematic Survey of Resource-Eficient Large Language Mode…",
      "title": "Beyond efficiency: A systematic survey of resource-efficient large language mode…"
    }
  ]
}
```

### Response fields

| Field | Meaning |
|---|---|
| `results[]` | List of matching papers. The list holds up to `max_num_results` items. |
| `results[].title` | Title of the paper. |
| `results[].authors[]` | Authors of the paper, shown as first initials plus surname, such as `G Bai`. The list can be shortened. |
| `results[].link` | URL of the paper on the publisher's site. |
| `results[].number_of_citations` | Number of citations Google Scholar shows for the paper. |
| `results[].snippet` | Short text excerpt from the paper that matches the query. Long snippets end with `…`. |
| `id` | Identifier string for this search response. |

### Notes

- Set `max_num_results` between 1 and 100 to control how many papers come back.
- `as_ylo` is the earliest publication year and `as_yhi` is the latest. Both accept values from 1900 to 2030.
- For other search modes, see [Scholar Smart Search](/apis/scholar/search-mixed) and [Scholar Web Search](/apis/scholar/search-web).

### Pricing

$0.0036 per successful call. Failed calls are not charged. It is included in the daily free quota of each organization.

---
Machine-readable: [`catalog/models/scholar/search-scholar.json`](../../../catalog/models/scholar/search-scholar.json) · Store page: https://www.sandbase.ai/model/scholar/search-scholar

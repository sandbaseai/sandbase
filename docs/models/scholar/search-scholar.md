# Scholar Search (Google Scholar)

`scholar/search-scholar` · api · Scholar

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

Search scholarly literature for a query and get papers with authors, links, citation counts and snippets. Filter by publication year.

### Use cases

- Literature reviews and research assistants.
- Find highly cited papers on a topic.
- Ground AI answers with academic sources.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/scholar/search-scholar" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "large language models", "max_num_results": 3}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | Search query for scholarly materials. |
| `as_yhi` | integer | No | Year of publication upper bound. |
| `as_ylo` | integer | No | Year of publication lower bound. |
| `max_num_results` | integer | No | Maximum number of search results to return, up to 100. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "results": [
    {
      "title": "A comprehensive overview of large language models",
      "authors": [
        "H Naveed",
        "AU Khan",
        "S Qiu",
        "…"
      ],
      "link": "https://dl.acm.org/doi/abs/10.1145/3744746",
      "number_of_citations": 3775,
      "snippet": "… Large Language Models (LLMs) have recently demonstrated remarkable capabiliti…"
    }
  ]
}
```

### Notes

- `as_ylo` / `as_yhi` set the earliest and latest publication year.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/scholar/search-scholar.json`](../../../catalog/models/scholar/search-scholar.json) · Store page: https://www.sandbase.ai/model/scholar/search-scholar

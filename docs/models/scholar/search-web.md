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

Search for academic and research-oriented web content using a query string in `query`. You can also filter results within specific publication years.

### Use cases

- Find web resources relevant to scientific and academic research topics.
- Filter scholarly search results between specific lower and upper publication years.
- Retrieve academic search snippets and titles for automated literature discovery.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/scholar/search-web" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
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
      "link": "https://openai.com/",
      "snippet": "We believe our research will eventually lead to artificial general intelligence, a system…",
      "title": "OpenAI | Research & Deployment"
    }
  ]
}
```

### Notes

- Set `as_ylo` and `as_yhi` to constrain results by lower and upper publication years.
- `max_num_results` accepts an integer up to 100.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/scholar/search-web.json`](../../../catalog/models/scholar/search-web.json) · Store page: https://www.sandbase.ai/model/scholar/search-web

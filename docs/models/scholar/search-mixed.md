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

Search for academic and web materials using `query`. You can also filter publication dates with `as_ylo` and `as_yhi`.

### Use cases

- Find academic papers and scholarly articles by topic.
- Filter scholarly search results within specific publication years.
- Retrieve relevant research paper links and snippets for automated review.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/scholar/search-mixed" \
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
      "link": "https://www.mdpi.com/1999-5903/15/6/192",
      "snippet": "According to numerous reports, ChatGPT represents a significant breakthrough in the field…",
      "title": "Chatgpt and open-ai models: A preliminary review"
    }
  ]
}
```

### Notes

- `max_num_results` accepts a value up to 100.
- Use `as_ylo` and `as_yhi` to specify lower and upper bounds for publication years.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/scholar/search-mixed.json`](../../../catalog/models/scholar/search-mixed.json) · Store page: https://www.sandbase.ai/model/scholar/search-mixed

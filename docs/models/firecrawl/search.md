# Firecrawl Web Search

`firecrawl/search` · api · Firecrawl

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

Look up web search results using `query`. You can optionally restrict the total number of items returned using `limit`.

### Use cases

- Retrieve relevant web page URLs and snippets for research queries.
- Gather search results to feed context into automated LLM pipelines.
- Find source URLs and page metadata for specific search terms.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/firecrawl/search" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "OpenAI"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `query` | string | Yes | The search query. |
| `limit` | integer | No | Maximum number of results to return. |

### Example response

Real response for the request above, trimmed to the main fields. User names and long IDs are masked.

```json
{
  "web": [
    {
      "description": "OpenAI | Research & Deployment  ## Latest research [An OpenAI model proposes a solution t…",
      "title": "OpenAI | Research & Deployment",
      "url": "https://openai.com/"
    }
  ]
}
```

### Notes

- Specify `query` to set the search terms.
- Use `limit` to configure the maximum number of results to return.

### Pricing

Flat price per call. Failed calls are not charged.

---
Machine-readable: [`catalog/models/firecrawl/search.json`](../../../catalog/models/firecrawl/search.json) · Store page: https://www.sandbase.ai/model/firecrawl/search

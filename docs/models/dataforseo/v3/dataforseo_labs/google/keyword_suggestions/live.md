# DataForSEO Labs Google Keyword Suggestions

`dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live` · api · DataForSEO

Returns Google keyword suggestions alongside relevant search metrics from DataForSEO Labs. Enables discovery of related search terms and query opportunities.

## Pricing

- **$0.024 per call** (USD)

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live` with the body above minus `model`.

## Details

Returns Google keyword suggestions and associated metrics for search optimization workflows.

### Use cases

- Discover related Google search queries for SEO research.
- Expand search marketing keyword lists with suggested terms.
- Evaluate keyword opportunities using search volume metrics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "running shoes", "limit": 5, "location_code": 2840, "language_code": "en"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `keyword` | Search query. |
| `limit` | Maximum number of results (up to 100). |
| `location_code` | Location code, e.g. 2840 for the United States. |
| `language_code` | Language code, e.g. "en". |

### Pricing

Flat price per call. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/model/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/model/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/model/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live.json`](../../../../../../../catalog/models/dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/dataforseo_labs/google/keyword_suggestions/live

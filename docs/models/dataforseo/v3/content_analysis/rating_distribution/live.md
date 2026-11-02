# DataForSEO Content Analysis Rating Distribution API: pricing, parameters and code examples

`dataforseo/v3/content_analysis/rating_distribution/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024 per call · **Modes:** sync

Returns the distribution of ratings across analyzed web content and media sources. Helps evaluate audience sentiment and review scores across aggregated citations.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/content_analysis/rating_distribution/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/content_analysis/rating_distribution/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/content_analysis/rating_distribution/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/content_analysis/rating_distribution/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/content_analysis/rating_distribution/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |

## Details

This endpoint returns rating distribution metrics across web content sources based on the submitted search criteria.

### Use cases

- Examine review rating distributions across online content mentioning a brand or topic.
- Analyze audience satisfaction levels across multiple digital sources.
- Benchmark customer sentiment profiles against competitor coverage.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/content_analysis/rating_distribution/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "nike"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `keyword` | Search query. |

### Pricing

Billed at the actual cost of each call, about $0.024 for the request above. The cost grows with the number of rows, targets or pages a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

### Related APIs

- [DataForSEO Backlinks Anchors](/model/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/model/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/model/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/content_analysis/rating_distribution/live.json`](../../../../../../catalog/models/dataforseo/v3/content_analysis/rating_distribution/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/content_analysis/rating_distribution/live

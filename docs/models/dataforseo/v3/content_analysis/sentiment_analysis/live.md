# DataForSEO Content Sentiment Analysis API: pricing, parameters and code examples

`dataforseo/v3/content_analysis/sentiment_analysis/live` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** about $0.024036 per call · **Modes:** sync

Evaluates text content to determine sentiment scores and emotional tone. Returns sentiment classifications and polarity metrics across analyzed web content.

## Pricing

- Usage-based. Billed per call from metered usage; the reference price is typical. Reference: **$0.024036**

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/content_analysis/sentiment_analysis/live"}'
```

**Python** ([sdk/python](../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/content_analysis/sentiment_analysis/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/content_analysis/sentiment_analysis/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/content_analysis/sentiment_analysis/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/content_analysis/sentiment_analysis/live` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `keyword` | string |  | Search query.  |

## Details

This endpoint evaluates sentiment for submitted content. It returns tone analysis and polarity metrics for the provided text.

### Use cases

- Evaluate public sentiment across brand-related web content.
- Analyze emotional tone within digital articles and customer feedback.
- Score text polarity for market research and competitive analysis.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/content_analysis/sentiment_analysis/live" \
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

Billed at the actual cost of each call, about $0.024036 for the request above. The cost grows with the number of rows, targets or pages a call returns. Failed calls are not charged. Searches with no results are billed at their actual cost.

### Related APIs

- [DataForSEO Backlinks Anchors](/model/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/model/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/model/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/content_analysis/sentiment_analysis/live.json`](../../../../../../catalog/models/dataforseo/v3/content_analysis/sentiment_analysis/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/content_analysis/sentiment_analysis/live

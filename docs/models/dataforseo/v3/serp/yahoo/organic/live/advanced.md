# DataForSEO Yahoo Organic SERP

`dataforseo/v3/serp/yahoo/organic/live/advanced` · api · DataForSEO

Returns real-time organic search engine results pages from Yahoo. Delivers detailed rank positions, titles, URLs, and SERP snippet data for specified search queries.

## Pricing

- Depends on parameters (`params.depth`).

| parameters | USD |
|---|---|
| defaults | 0.003 |

Formula: `0.003 * Math.ceil(Math.max(params.depth ?? 6.0, 1.0) / 6.0)`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/yahoo/organic/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/yahoo/organic/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/yahoo/organic/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/yahoo/organic/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/yahoo/organic/live/advanced` with the body above minus `model`.

## Details

Returns real-time organic Yahoo search engine results pages (SERP) for query keywords and target locations.

### Use cases

- Track search ranking positions on Yahoo for target keywords.
- Monitor competitor visibility across Yahoo organic listings.
- Extract organic snippets and destination URLs for SEO audits.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/yahoo/organic/live/advanced" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keyword": "running shoes", "location_code": 2840, "language_code": "en"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `keyword` | Search query. |
| `location_code` | Location code, e.g. 2840 for the United States. |
| `language_code` | Language code, e.g. "en". |

### Pricing

$0.003 per page of 6 results. The default depth (6) is one page; for example depth 30 costs 5 pages. Failed calls are not charged. Extra crawled pages, pixel rankings, async AI overview, People Also Ask clicks and search operators (site:, intitle: ...) are not supported.

### Related APIs

- [DataForSEO Backlinks Anchors](/model/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/model/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/model/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/yahoo/organic/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/yahoo/organic/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/yahoo/organic/live/advanced

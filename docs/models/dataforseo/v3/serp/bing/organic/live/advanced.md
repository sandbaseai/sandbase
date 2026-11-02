# DataForSEO Bing Organic Search API: pricing, parameters and code examples

`dataforseo/v3/serp/bing/organic/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.003 per run, depending on parameters · **Modes:** sync

Returns real-time organic search engine results pages from Bing with advanced item data. Provides detailed ranking elements and structured SERP positions for organic listings.

## Pricing

- Depends on parameters (`params.depth`).

| parameters | USD |
|---|---|
| defaults | 0.003 |

Formula: `0.003 * Math.ceil(Math.max(params.depth ?? 10.0, 1.0) / 10.0)`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/bing/organic/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/bing/organic/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/bing/organic/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/bing/organic/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/bing/organic/live/advanced` with the body above minus `model`.

## Details

Retrieve advanced organic search results directly from Bing. This endpoint provides real-time SERP data and detailed ranking positions for organic listings.

### Use cases

- Analyze organic search engine rankings on Bing.
- Monitor competitor visibility across Bing search results.
- Track position changes for search terms over time.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/bing/organic/live/advanced" \
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

$0.003 per page of 10 results. The default depth (10) is one page; for example depth 50 costs 5 pages. Failed calls are not charged. Extra crawled pages, pixel rankings, async AI overview, People Also Ask clicks and search operators (site:, intitle: ...) are not supported.

### Related APIs

- [DataForSEO Backlinks Anchors](/model/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/model/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/model/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/bing/organic/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/bing/organic/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/bing/organic/live/advanced

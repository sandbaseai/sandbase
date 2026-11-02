# DataForSEO Google Images SERP API: pricing, parameters and code examples

`dataforseo/v3/serp/google/images/live/advanced` · data API · DataForSEO · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** from $0.003 per run, depending on parameters · **Modes:** sync

Returns Google Images search engine results pages with detailed image metadata. Provides real-time SERP data for visual search queries across Google Images.

## Pricing

- Depends on parameters (`params.depth`).

| parameters | USD |
|---|---|
| defaults | 0.003 |

Formula: `0.003 * Math.ceil(Math.max(params.depth ?? 100.0, 1.0) / 100.0)`

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/serp/google/images/live/advanced"}'
```

**Python** ([sdk/python](../../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/serp/google/images/live/advanced', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/serp/google/images/live/advanced", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/serp/google/images/live/advanced", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/serp/google/images/live/advanced` with the body above minus `model`.

## Details

Retrieve real-time Google Images search engine result pages. Inspect returned image ranking positions, source URLs, and visual search features.

### Use cases

- Track visual search rankings across Google Images.
- Analyze competitor imagery and source domains in image search results.
- Extract rich metadata from visual SERP layouts.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/serp/google/images/live/advanced" \
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

$0.003 per page of 100 results. The default depth (100) is one page; for example depth 500 costs 5 pages. Failed calls are not charged. Extra crawled pages, pixel rankings, async AI overview, People Also Ask clicks and search operators (site:, intitle: ...) are not supported.

### Related APIs

- [DataForSEO Backlinks Anchors](/model/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/model/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/model/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/serp/google/images/live/advanced.json`](../../../../../../../../catalog/models/dataforseo/v3/serp/google/images/live/advanced.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/serp/google/images/live/advanced

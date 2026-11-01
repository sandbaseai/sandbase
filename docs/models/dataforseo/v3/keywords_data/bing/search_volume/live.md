# DataForSEO Bing Keyword Search Volume

`dataforseo/v3/keywords_data/bing/search_volume/live` · api · DataForSEO

Returns search volume metrics from Bing for specified target keywords. Helps track search query popularity and monthly demand trends directly on the Bing search engine.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/bing/search_volume/live", "keywords": ["seo tools", "keyword research"], "language_code": "en", "location_code": 2840}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/bing/search_volume/live', {'keywords': ['seo tools', 'keyword research'], 'language_code': 'en', 'location_code': 2840})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/bing/search_volume/live", {
  "keywords": [
    "seo tools",
    "keyword research"
  ],
  "language_code": "en",
  "location_code": 2840
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/bing/search_volume/live", sandbase.Params{
	"keywords": []any{"seo tools", "keyword research"},
	"language_code": "en",
	"location_code": 2840,
})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/bing/search_volume/live` with the body above minus `model`.

## Details

Access Bing search volume metrics in real time for specified keyword lists to analyze Bing search trends.

### Use cases

- Analyze Bing search volume for targeted search terms.
- Evaluate historical query demand and keyword popularity on Bing.
- Support SEO research focused on Microsoft Bing traffic.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/bing/search_volume/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["running shoes"], "location_code": 2840, "language_code": "en"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `keywords` | List of keywords (up to 100 per call). |
| `location_code` | Location code, e.g. 2840 for the United States. |
| `language_code` | Language code, e.g. "en". |

### Pricing

Flat price per call. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/model/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/model/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/model/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/bing/search_volume/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/bing/search_volume/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/bing/search_volume/live

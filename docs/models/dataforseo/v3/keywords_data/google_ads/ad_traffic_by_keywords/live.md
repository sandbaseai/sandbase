# DataForSEO Google Ads Traffic by Keywords

`dataforseo/v3/keywords_data/google_ads/ad_traffic_by_keywords/live` · api · DataForSEO

Returns estimated Google Ads ad traffic metrics for specified search terms. It provides estimates for search volume, potential impressions, clicks, and advertising performance.

## Pricing

- **$0.003 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "dataforseo/v3/keywords_data/google_ads/ad_traffic_by_keywords/live"}'
```

**Python** ([sdk/python](../../../../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('dataforseo/v3/keywords_data/google_ads/ad_traffic_by_keywords/live', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("dataforseo/v3/keywords_data/google_ads/ad_traffic_by_keywords/live", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "dataforseo/v3/keywords_data/google_ads/ad_traffic_by_keywords/live", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/dataforseo/v3/keywords_data/google_ads/ad_traffic_by_keywords/live` with the body above minus `model`.

## Details

This endpoint returns estimated ad traffic metrics from Google Ads for specified `keywords`.

### Use cases

- Estimate Google Ads impression and click volume for target keywords.
- Compare potential advertising traffic across competing search terms.
- Evaluate paid search campaign reach prior to launching ad campaigns.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/dataforseo/v3/keywords_data/google_ads/ad_traffic_by_keywords/live" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"keywords": ["running shoes"], "bid": 10, "match": "exact", "location_code": 2840, "language_code": "en"}'
```

### Parameters

The JSON body is forwarded to the upstream endpoint (one task per call). Fields used above:

| Name | Description |
|---|---|
| `keywords` | List of keywords (up to 100 per call). |
| `bid` | Bid in USD. |
| `match` | Keyword match type: exact, phrase or broad. |
| `location_code` | Location code, e.g. 2840 for the United States. |
| `language_code` | Language code, e.g. "en". |

### Pricing

Flat price per call. Failed calls are not charged.

### Related APIs

- [DataForSEO Backlinks Anchors](/model/dataforseo/v3/backlinks/anchors/live): Returns anchor text distribution metrics for backlinks pointing to a target website or page.
- [DataForSEO Backlinks List](/model/dataforseo/v3/backlinks/backlinks/live): Returns a list of external backlinks pointing to a specified target domain or webpage.
- [DataForSEO Backlinks Bulk Ranks](/model/dataforseo/v3/backlinks/bulk_ranks/live): Returns rank metrics for multiple domains or pages in bulk.

---
Machine-readable: [`catalog/models/dataforseo/v3/keywords_data/google_ads/ad_traffic_by_keywords/live.json`](../../../../../../../catalog/models/dataforseo/v3/keywords_data/google_ads/ad_traffic_by_keywords/live.json) · Store page: https://www.sandbase.ai/model/dataforseo/v3/keywords_data/google_ads/ad_traffic_by_keywords/live

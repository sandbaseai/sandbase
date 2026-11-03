# TikTok Ad Query Suggestions API: pricing, parameters and code examples

`tiktok/ads/query-suggestions` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns popular or keyword-based ad search suggestions across TikTok. Filter results by target country code, scenario type, and an optional query string.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ads/query-suggestions"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ads/query-suggestions', {})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ads/query-suggestions", {});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ads/query-suggestions", sandbase.Params{})
```

Same call via the path form: `POST /v1/api/tiktok/ads/query-suggestions` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `count` | integer |  | Number of suggestions to return, default 50  |
| `query` | string |  | Input keyword (optional), returns suggestions based on input; popular ones if omitted  |
| `scenario` | integer |  | Scenario type, default 1  |
| `country_code` | string |  | Country code, default US  |

## Details

Retrieves search query recommendations for ad discovery, using optional filters such as `query`, `country_code`, and `scenario`.

### Use cases

- Discover trending keywords for ad campaign targeting.
- Generate keyword autocomplete suggestions for search inputs.
- Identify regional creative themes based on country-specific queries.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/query-suggestions" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `count` | integer | No | Number of suggestions to return, default 50 |
| `query` | string | No | Input keyword (optional), returns suggestions based on input; popular ones if omitted |
| `scenario` | integer | No | Scenario type, default 1 |
| `country_code` | string | No | Country code, default US |

### Notes

- If `query` is omitted, the endpoint returns general popular suggestions.
- `country_code` defaults to US.
- `count` defaults to 50 suggestions per call.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Ad Interactive Analysis](/apis/tiktok/ads/ad-interactive-analysis): Returns audience retention and interaction analytics across video timestamps for a specified ad creative.
- [TikTok Ad Keyframe Analysis](/apis/tiktok/ads/ad-keyframe-analysis): Returns keyframe performance metrics across video ad timestamps for a specified material ID, including retention and conversion figures.
- [TikTok Ad Material Percentile Rankings](/apis/tiktok/ads/ad-percentile): Returns ad performance percentile rankings within the industry for a specific ad material.

---
Machine-readable: [`catalog/models/tiktok/ads/query-suggestions.json`](../../../../catalog/models/tiktok/ads/query-suggestions.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/query-suggestions

# TikTok Recommended Ads API: pricing, parameters and code examples

`tiktok/ads/recommended-ads` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns similar recommended TikTok ads based on a specified ad material ID. Supports optional filtering by industry ID and country code.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ads/recommended-ads", "material_id": "<material_id>"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ads/recommended-ads', {'material_id': '<material_id>'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ads/recommended-ads", {
  "material_id": "<material_id>"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ads/recommended-ads", sandbase.Params{
	"material_id": "<material_id>",
})
```

Same call via the path form: `POST /v1/api/tiktok/ads/recommended-ads` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `industry` | string |  | Industry ID, e.g., Games: 25308000000  |
| `material_id` | string | yes | Reference ad material ID, required parameter  |
| `country_code` | string |  | Country code, e.g., US, UK, JP  |

## Details

Look up recommended TikTok ads matching an existing creative by providing a `material_id`. You can also filter results using `industry` and `country_code`.

### Use cases

- Discover ad examples in the same industry for creative benchmarking.
- Find similar reference ads based on an existing ad material ID.
- Explore successful ad styles tailored to specific country markets.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/recommended-ads" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"material_id": "<material_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `material_id` | string | Yes | Reference ad material ID, required parameter |
| `industry` | string | No | Industry ID, e.g., Games: 25308000000 |
| `country_code` | string | No | Country code, e.g., US, UK, JP |

### Notes

- `material_id` is required to specify the reference ad material.
- `industry` accepts numeric industry IDs, such as 25308000000 for Games.
- `country_code` filters results by standard country identifiers like US, UK, or JP.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Ad Interactive Analysis](/model/tiktok/ads/ad-interactive-analysis): Returns audience retention and interaction analytics across video timestamps for a specified ad creative.
- [TikTok Ad Keyframe Analysis](/model/tiktok/ads/ad-keyframe-analysis): Returns keyframe performance metrics across video ad timestamps for a specified material ID, including retention and conversion figures.
- [TikTok Ad Material Percentile Rankings](/model/tiktok/ads/ad-percentile): Returns ad performance percentile rankings within the industry for a specific ad material.

---
Machine-readable: [`catalog/models/tiktok/ads/recommended-ads.json`](../../../../catalog/models/tiktok/ads/recommended-ads.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/recommended-ads

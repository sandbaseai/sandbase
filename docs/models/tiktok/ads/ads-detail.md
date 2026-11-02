# TikTok Ad Detail API: pricing, parameters and code examples

`tiktok/ads/ads-detail` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.0015 per call (free daily quota) · **Modes:** sync

Returns detailed information about a single TikTok ad, including creative content, creator information, and engagement performance metrics using a specific ad identifier.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ads/ads-detail", "ads_id": "7164467399885864962"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ads/ads-detail', {'ads_id': '7164467399885864962'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ads/ads-detail", {
  "ads_id": "7164467399885864962"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ads/ads-detail", sandbase.Params{
	"ads_id": "7164467399885864962",
})
```

Same call via the path form: `POST /v1/api/tiktok/ads/ads-detail` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `ads_id` | string | yes | Ad ID, required parameter, can be obtained from ad lists or TikTok Ads Creative Center  |

## Details

Retrieve comprehensive ad details and performance metrics by providing an `ads_id`.

### Use cases

- Review creative content and creator details for a specific TikTok ad.
- Analyze engagement metrics including views, likes, and comments on an ad.
- Evaluate specific ad effectiveness and audience feedback.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/ads-detail" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"ads_id": "<ads_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `ads_id` | string | Yes | Ad ID, required parameter, can be obtained from ad lists or TikTok Ads Creative Center |

### Notes

- `ads_id` can be obtained from ad lists or the TikTok Ads Creative Center.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Ad Interactive Analysis](/model/tiktok/ads/ad-interactive-analysis): Returns audience retention and interaction analytics across video timestamps for a specified ad creative.
- [TikTok Ad Keyframe Analysis](/model/tiktok/ads/ad-keyframe-analysis): Returns keyframe performance metrics across video ad timestamps for a specified material ID, including retention and conversion figures.
- [TikTok Ad Material Percentile Rankings](/model/tiktok/ads/ad-percentile): Returns ad performance percentile rankings within the industry for a specific ad material.

---
Machine-readable: [`catalog/models/tiktok/ads/ads-detail.json`](../../../../catalog/models/tiktok/ads/ads-detail.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/ads-detail

# TikTok Ad Keyframe Analysis API: pricing, parameters and code examples

`tiktok/ads/ad-keyframe-analysis` · data API · TikTok · callable with one SandBase API key from curl, Python, TypeScript and Go.

**Price:** $0.001 per call (free daily quota) · **Modes:** sync

Returns keyframe performance metrics across video ad timestamps for a specified material ID, including retention and conversion figures.

## Pricing

- **$0.001 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ads/ad-keyframe-analysis", "material_id": "7164467399885864962"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ads/ad-keyframe-analysis', {'material_id': '7164467399885864962'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ads/ad-keyframe-analysis", {
  "material_id": "7164467399885864962"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ads/ad-keyframe-analysis", sandbase.Params{
	"material_id": "7164467399885864962",
})
```

Same call via the path form: `POST /v1/api/tiktok/ads/ad-keyframe-analysis` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `metric` | string |  | Analysis metric (retain_ctr, retain_cvr, click_cnt, convert_cnt, play_retain_cnt)  |
| `material_id` | string | yes | Ad material ID, required parameter  |

## Details

Fetch frame-by-frame audience engagement and drop-off metrics for an ad video using its `material_id`.

### Use cases

- Identify exact video timestamps where audience drop-off occurs.
- Compare retention and conversion rates across creative keyframes.
- Optimize ad pacing and hook placement based on frame-level metrics.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/ad-keyframe-analysis" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"material_id": "<material_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `material_id` | string | Yes | Ad material ID, required parameter |
| `metric` | string | No | Analysis metric (retain_ctr, retain_cvr, click_cnt, convert_cnt, play_retain_cnt) |

### Notes

- Supported `metric` values include retain_ctr, retain_cvr, click_cnt, convert_cnt, and play_retain_cnt.
- Requires a valid `material_id` representing the ad creative.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Ad Interactive Analysis](/apis/tiktok/ads/ad-interactive-analysis): Returns audience retention and interaction analytics across video timestamps for a specified ad creative.
- [TikTok Ad Material Percentile Rankings](/apis/tiktok/ads/ad-percentile): Returns ad performance percentile rankings within the industry for a specific ad material.
- [TikTok Ad Detail](/apis/tiktok/ads/ads-detail): Returns detailed information about a single TikTok ad, including creative content, creator information, and engagement performance metrics using a specific ad …

---
Machine-readable: [`catalog/models/tiktok/ads/ad-keyframe-analysis.json`](../../../../catalog/models/tiktok/ads/ad-keyframe-analysis.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/ad-keyframe-analysis

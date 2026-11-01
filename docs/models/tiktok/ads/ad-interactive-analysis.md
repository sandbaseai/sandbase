# TikTok Ad Interactive Analysis

`tiktok/ads/ad-interactive-analysis` · api · TikTok

Returns audience retention and interaction analytics across video timestamps for a specified ad creative. Supports filtering by analysis metric and time period.

## Pricing

- **$0.0015 per call** (USD)
- Free quota: 100 calls/day per organization (shared across free-quota APIs).

## Call it

Modes: sync (default `sync`). Only pass `mode` values listed here. The SDKs' `run()` waits for async results; `submit()` + `wait()` split the two steps.

**curl**

```bash
curl https://api.sandbase.ai/v1/run \
  -H "Authorization: Bearer $SANDBASE_API_KEY" -H 'Content-Type: application/json' \
  -d '{"model": "tiktok/ads/ad-interactive-analysis", "material_id": "7164467399885864962"}'
```

**Python** ([sdk/python](../../../../sdk/python))

```python
from sandbase import SandBase

result = SandBase().run('tiktok/ads/ad-interactive-analysis', {'material_id': '7164467399885864962'})
print(result["outputs"])
```

**TypeScript** ([sdk/typescript](../../../../sdk/typescript))

```ts
import { SandBase } from "@sandbaseai/sdk";

const result = await new SandBase().run("tiktok/ads/ad-interactive-analysis", {
  "material_id": "7164467399885864962"
});
console.log(result.outputs);
```

**Go** ([sdk/go](../../../../sdk/go))

```go
c, _ := sandbase.NewClient("")
run, err := c.Run(ctx, "tiktok/ads/ad-interactive-analysis", sandbase.Params{
	"material_id": "7164467399885864962",
})
```

Same call via the path form: `POST /v1/api/tiktok/ads/ad-interactive-analysis` with the body above minus `model`.

## Parameters

| name | type | required | description |
|---|---|---|---|
| `material_id` | string | yes | Ad material ID, required parameter  |
| `metric_type` | string |  | Analysis type  |
| `period_type` | integer |  | Time range, default 180 days  |

## Details

Look up audience retention and engagement data across video time points using `material_id`. Customize results with optional `metric_type` and `period_type` parameters.

### Use cases

- Inspect audience retention curves at specific video playback timestamps.
- Identify high-engagement moments within video ad creatives.
- Determine optimal ad duration based on historical interaction patterns.

### Request

```bash
curl -X POST "https://api.sandbase.ai/v1/api/tiktok/ads/ad-interactive-analysis" \
  -H "Authorization: Bearer $SANDBASE_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"material_id": "<material_id>"}'
```

### Parameters

| Name | Type | Required | Description |
|---|---|---|---|
| `material_id` | string | Yes | Ad material ID, required parameter |
| `metric_type` | string | No | Analysis type |
| `period_type` | integer | No | Time range, default 180 days |

### Notes

- `period_type` specifies the analysis time range and defaults to 180 days.
- `material_id` is required to identify the target ad material.

### Pricing

Flat price per call. Failed calls, including lookups whose target does not exist, are not charged.

### Related APIs

- [TikTok Ad Keyframe Analysis](/model/tiktok/ads/ad-keyframe-analysis): Returns keyframe performance metrics across video ad timestamps for a specified material ID, including retention and conversion figures.
- [TikTok Ad Material Percentile Rankings](/model/tiktok/ads/ad-percentile): Returns ad performance percentile rankings within the industry for a specific ad material.
- [TikTok Ad Detail](/model/tiktok/ads/ads-detail): Returns detailed information about a single TikTok ad, including creative content, creator information, and engagement performance metrics using a specific ad …

---
Machine-readable: [`catalog/models/tiktok/ads/ad-interactive-analysis.json`](../../../../catalog/models/tiktok/ads/ad-interactive-analysis.json) · Store page: https://www.sandbase.ai/model/tiktok/ads/ad-interactive-analysis
